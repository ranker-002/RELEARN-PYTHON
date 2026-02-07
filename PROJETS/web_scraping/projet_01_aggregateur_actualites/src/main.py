#!/usr/bin/env python3
"""
Agrégateur d'Actualités RSS

Un agrégateur de flux d'actualités qui rassemble les dernières nouvelles
de plusieurs sources en un seul endroit.

Usage:
    python src/main.py                    # Mode interactif
    python src/main.py --refresh         # Rafraîchir tous les flux
    python src/main.py --list            # Lister les articles
    python src/main.py --config CONFIG   # Utiliser un fichier config
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional, List
from datetime import datetime
import logging


# Import des modules du projet
try:
    from .models.article import Article, LuStatus
    from .models.feed import FluxRSS
    from .services.rss_parser import RSSParser
    from .services.fetcher import FeedFetcher
    from .services.filter import ArticleFilter
    from .services.cache import CacheManager
    from .utils.config import Config
    from .utils.date_utils import DateUtils
except ImportError:
    # Pour exécution directe
    from models.article import Article, LuStatus
    from models.feed import FluxRSS
    from services.rss_parser import RSSParser
    from services.fetcher import FeedFetcher
    from services.filter import ArticleFilter
    from services.cache import CacheManager
    from utils.config import Config
    from utils.date_utils import DateUtils


class Colors:
    """Codes couleur pour l'affichage CLI."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"


class AggregateurApp:
    """Application principale de l'agrégateur RSS."""
    
    VERSION = "1.0.0"
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialise l'application.
        
        Args:
            config_path: Chemin vers le fichier de configuration
        """
        self.config = Config.load(config_path) if config_path else Config()
        self.logger = self._setup_logging()
        self.parser = RSSParser()
        self.fetcher = FeedFetcher(timeout=self.config.get("timeout", 10))
        self.filter = ArticleFilter(self.config.get("filtres", {}))
        self.cache = CacheManager()
        self.flux: List[FluxRSS] = []
        self.page_courante = 1
        self.articles_par_page = 10
        
        self.logger.info(f"Agrégateur RSS v{self.VERSION} initialisé")
    
    def _setup_logging(self) -> logging.Logger:
        """Configure le logging."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("AggregateurRSS")
    
    def _afficher_banniere(self):
        """Affiche la bannière de l'application."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print("╔══════════════════════════════════════════════════╗")
        print("║         AGRÉGATEUR D'ACTUALITÉS RSS             ║")
        print("╠══════════════════════════════════════════════════╣")
        print(f"║  Version: {self.VERSION:<37}║")
        print(f"║  Flux chargés: {len(self.flux):<30}║")
        print("╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def _afficher_menu(self):
        """Affiche le menu principal."""
        print(f"\n{Colors.BOLD}Menu Principal:{Colors.RESET}")
        print("  1. Afficher les articles (page 1)")
        print("  2. Rafraîchir tous les flux")
        print("  3. Rechercher un article")
        print("  4. Ouvrir un article dans le navigateur")
        print("  5. Marquer comme lu/non lu")
        print("  6. Gérer les abonnements")
        print("  7. Statistiques")
        print("  8. Quitter")
        print()
    
    def charger_abonnements(self) -> bool:
        """
        Charge les abonnements depuis le fichier de configuration.
        
        Returns:
            True si succès, False sinon
        """
        abonnements = self.config.get("abonnements", [])
        if not abonnements:
            self.logger.warning("Aucun abonnement configuré")
            return False
        
        self.logger.info(f"Chargement de {len(abonnements)} abonnements...")
        return True
    
    def rafraichir_tous(self) -> int:
        """
        Rafraîchit tous les flux RSS.
        
        Returns:
            Nombre d'articles chargés
        """
        print(f"\n{Colors.BOLD}🔄 Rafraîchissement des flux...{Colors.RESET}\n")
        
        abonnements = self.config.get("abonnements", [])
        total_articles = 0
        
        for sub in abonnements:
            nom = sub.get("nom", "Inconnu")
            url = sub.get("url")
            
            if not url:
                continue
            
            print(f"   📥 {nom}...", end=" ", flush=True)
            
            # Vérifier le cache
            if self.cache.exists(url):
                contenu, age = self.cache.get(url)
                if age < 3600:  # 1 heure
                    print(f"✅ (cache, {age}s)")
                    flux = self.parser.parser_flux(contenu, sub)
                    self.flux.append(flux)
                    total_articles += flux.nb_articles
                    continue
            
            # Télécharger le flux
            contenu = self.fetcher.telecharger(url)
            if contenu:
                self.cache.set(url, contenu)
                flux = self.parser.parser_flux(contenu, sub)
                self.flux.append(flux)
                print(f"✅ ({flux.nb_articles} articles)")
                total_articles += flux.nb_articles
            else:
                print(f"❌ Erreur de téléchargement")
        
        print(f"\n{Colors.GREEN}✅ {total_articles} articles chargés{Colors.RESET}")
        return total_articles
    
    def afficher_articles(self, page: int = 1, filtre: str = "tous") -> bool:
        """
        Affiche les articles avec pagination.
        
        Args:
            page: Numéro de page
            filtre: Type de filtre (tous, non_lus, recent)
            
        Returns:
            True si succès
        """
        # Collecter et filtrer les articles
        tous_articles = []
        for flux in self.flux:
            articles = flux.articles if hasattr(flux, 'articles') else []
            if filtre == "non_lus":
                articles = [a for a in articles if a.statut_lecture.value == "non_lu"]
            elif filtre == "recents":
                articles = [a for a in articles if a.est_recent(7)]
            tous_articles.extend(articles)
        
        # Trier par date (plus récents en premier)
        tous_articles.sort(key=lambda a: a.date_publication, reverse=True)
        
        # Pagination
        total_pages = (len(tous_articles) + self.articles_par_page - 1) // self.articles_par_page
        page = max(1, min(page, total_pages))
        debut = (page - 1) * self.articles_par_page
        fin = debut + self.articles_par_page
        page_articles = tous_articles[debut:fin]
        
        # Affichage
        print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}ARTICLES - Page {page}/{total_pages}{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")
        
        for i, article in enumerate(page_articles, debut + 1):
            statut = "🆕" if article.statut_lecture.value == "non_lu" else "📖"
            date_str = article.date_publication.strftime("%d %b %Y, %H:%M")
            print(f"[{i}] {statut} {article.titre}")
            print(f"    📰 {article.source} | 📅 {date_str}")
            print()
        
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
        nav = []
        if page > 1:
            nav.append("[←] Précédent")
        nav.append(f"[{page}/{total_pages}]")
        if page < total_pages:
            nav.append("[→] Suivant")
        nav.append("[R] Rafraîchir | [Q] Quitter")
        print("  ".join(nav))
        
        return True
    
    def rechercher(self, terme: str) -> List[Article]:
        """
        Recherche un terme dans les articles.
        
        Args:
            terme: Terme de recherche
            
        Returns:
            Liste des articles correspondants
        """
        resultats = []
        terme = terme.lower()
        
        for flux in self.flux:
            for article in flux.articles:
                if (terme in article.titre.lower() or 
                    terme in article.description.lower()):
                    resultats.append(article)
        
        return resultats
    
    def marquer_lu(self, index: int, lu: bool = True):
        """
        Marque un article comme lu ou non lu.
        
        Args:
            index: Index de l'article
            lu: True pour marquer comme lu
        """
        tous = []
        for flux in self.flux:
            tous.extend(flux.articles)
        
        tous.sort(key=lambda a: a.date_publication, reverse=True)
        
        if 1 <= index <= len(tous):
            article = tous[index - 1]
            article.statut_lecture = LuStatus.LU if lu else LuStatus.NON_LU
            print(f"Article marqué comme {Colors.GREEN}lu{Colors.RESET}")
        else:
            print(f"{Colors.RED}Index invalide{Colors.RESET}")
    
    def afficher_statistiques(self):
        """Affiche les statistiques."""
        total = sum(len(f.articles) if hasattr(f, 'articles') else 0 for f in self.flux)
        non_lus = sum(
            sum(1 for a in f.articles if a.statut_lecture.value == "non_lu")
            for f in self.flux if hasattr(f, 'articles')
        )
        
        print(f"\n{Colors.BOLD}📊 Statistiques{Colors.RESET}")
        print(f"   Flux: {len(self.flux)}")
        print(f"   Total articles: {total}")
        print(f"   Non lus: {non_lus}")
        print(f"   Lus: {total - non_lus}")
    
    def executer_commande(self, commande: str) -> bool:
        """
        Exécute une commande directe.
        
        Args:
            commande: Commande à exécuter
            
        Returns:
            True pour continuer, False pour quitter
        """
        cmd = commande.lower().strip()
        
        if cmd in ["1", "afficher"]:
            self.afficher_articles(self.page_courante)
        elif cmd in ["2", "rafraichir", "refresh"]:
            self.flux.clear()
            self.rafraichir_tous()
        elif cmd in ["3", "rechercher", "search"]:
            terme = input("Terme de recherche: ")
            resultats = self.rechercher(terme)
            print(f"\n{Colors.BLUE}🔍 {len(resultats)} résultats:{Colors.RESET}")
            for i, art in enumerate(resultats[:10], 1):
                print(f"[{i}] {art.titre}")
        elif cmd in ["4", "ouvrir", "open"]:
            idx = input("Numéro de l'article: ")
            try:
                self._ouvrir_article(int(idx))
            except ValueError:
                print(f"{Colors.RED}Index invalide{Colors.RESET}")
        elif cmd in ["5", "marquer"]:
            idx = input("Numéro de l'article: ")
            self.marquer_lu(int(idx))
        elif cmd in ["6", "abonnements", "subscriptions"]:
            self._gerer_abonnements()
        elif cmd in ["7", "stats"]:
            self.afficher_statistiques()
        elif cmd in ["8", "q", "quit", "quitter", "exit"]:
            return False
        else:
            print(f"{Colors.RED}Commande inconnue{Colors.RESET}")
        
        return True
    
    def _ouvrir_article(self, index: int):
        """Ouvre un article dans le navigateur."""
        import webbrowser
        tous = []
        for flux in self.flux:
            tous.extend(flux.articles)
        tous.sort(key=lambda a: a.date_publication, reverse=True)
        
        if 1 <= index <= len(tous):
            article = tous[index - 1]
            print(f"Ouverture: {article.lien}")
            webbrowser.open(article.lien)
        else:
            print(f"{Colors.RED}Index invalide{Colors.RESET}")
    
    def _gerer_abonnements(self):
        """Gère les abonnements."""
        print(f"\n{Colors.BOLD}Abonnements:{Colors.RESET}")
        abonnements = self.config.get("abonnements", [])
        for i, sub in enumerate(abonnements, 1):
            print(f"[{i}] {sub.get('nom', 'Inconnu')} - {sub.get('url', 'Sans URL')}")
    
    def run_interactif(self):
        """Lance le mode interactif."""
        self._afficher_banniere()
        self.charger_abonnements()
        
        while True:
            self._afficher_menu()
            try:
                choix = input(f"{Colors.BOLD}Votre choix: {Colors.RESET}").strip()
                if not self.executer_commande(choix):
                    break
            except (EOFError, KeyboardInterrupt):
                print("\n\nAu revoir!")
                break
        
        self.logger.info("Application terminée")
    
    def run(self):
        """Point d'entrée principal."""
        self.logger.info("Démarrage de l'application")
        
        # Vérifier les arguments
        if len(sys.argv) > 1:
            self._traiter_arguments()
        else:
            # Mode interactif par défaut
            self.run_interactif()
    
    def _traiter_arguments(self):
        """Traite les arguments de ligne de commande."""
        parser = argparse.ArgumentParser(
            description="Agrégateur d'Actualités RSS",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Exemples:
    python src/main.py                    # Mode interactif
    python src/main.py --refresh         # Rafraîchir les flux
    python src/main.py --list           # Lister les articles
    python src/main.py --search Python   # Rechercher "Python"
            """
        )
        parser.add_argument("--refresh", "-r", action="store_true",
                           help="Rafraîchir tous les flux")
        parser.add_argument("--list", "-l", action="store_true",
                           help="Lister les articles")
        parser.add_argument("--search", "-s", metavar="TERME",
                           help="Rechercher un terme")
        parser.add_argument("--stats", action="store_true",
                           help="Afficher les statistiques")
        parser.add_argument("--version", action="version",
                           version=f"%(prog)s {self.VERSION}")
        
        args = parser.parse_args()
        
        if args.refresh:
            self.charger_abonnements()
            self.rafraichir_tous()
        elif args.list:
            self.charger_abonnements()
            self.rafraichir_tous()
            self.afficher_articles()
        elif args.search:
            self.charger_abonnements()
            self.rafraichir_tous()
            resultats = self.rechercher(args.search)
            print(f"\n🔍 {len(resultats)} résultats pour '{args.search}':")
            for i, art in enumerate(resultats[:10], 1):
                print(f"[{i}] {art.titre}")
                print(f"    {art.lien}")
        elif args.stats:
            self.charger_abonnements()
            self.rafraichir_tous()
            self.afficher_statistiques()


def main():
    """Point d'entrée."""
    app = AggregateurApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir!")
    except Exception as e:
        print(f"\n{Colors.RED}Erreur: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
