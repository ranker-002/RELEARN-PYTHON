#!/usr/bin/env python3
"""
Analyseur de Prix - CLI pour comparer les prix sur plusieurs sites e-commerce.

Usage:
    python src/main.py                    # Mode interactif
    python src/main.py --scan URL        # Scanner un produit
    python src/main.py --compare URL1 URL2  # Comparer plusieurs produits
    python src/main.py --alert URL SEUIL  # Définir une alerte
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional, List
from datetime import datetime
import logging


try:
    from .models.produit import Produit, Prix, Disponibilite
    from .models.prix import Prix
    from .services.scraper import PriceScraper
    from .services.comparator import PriceComparator
    from .services.alerter import PriceAlerter
    from .services.history import PriceHistory
    from .utils.config import Config
    from .utils.date_utils import DateUtils
    from .utils.formatter import PriceFormatter
except ImportError:
    from models.produit import Produit, Prix, Disponibilite
    from models.prix import Prix
    from services.scraper import PriceScraper
    from services.comparator import PriceComparator
    from services.alerter import PriceAlerter
    from services.history import PriceHistory
    from utils.config import Config
    from utils.date_utils import DateUtils
    from utils.formatter import PriceFormatter


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"


class PriceAnalyzerApp:
    VERSION = "1.0.0"
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = Config.load(config_path) if config_path else Config()
        self.logger = self._setup_logging()
        self.scraper = PriceScraper()
        self.comparator = PriceComparator()
        self.alerter = PriceAlerter()
        self.history = PriceHistory()
        self.produits_suivis: List[Produit] = []
        self.page_courante = 1
        self.produits_par_page = 10
        
        self.logger.info(f"Analyseur de Prix v{self.VERSION} initialisé")
    
    def _setup_logging(self) -> logging.Logger:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("PriceAnalyzer")
    
    def _afficher_banniere(self):
        print(f"\n{Colors.BOLD}{Colors.CYAN}")
        print("╔══════════════════════════════════════════════════╗")
        print("║           ANALYSEUR DE PRIX                    ║")
        print("╠══════════════════════════════════════════════════╣")
        print(f"║  Version: {self.VERSION:<37}║")
        print(f"║  Produits suivis: {len(self.produits_suivis):<29}║")
        print("╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def _afficher_menu(self):
        print(f"\n{Colors.BOLD}Menu Principal:{Colors.RESET}")
        print("  1. Scanner un produit")
        print("  2. Lister les produits suivis")
        print("  3. Comparer des prix")
        print("  4. Définir une alerte")
        print("  5. Voir l'historique")
        print("  6. Exporter les données")
        print("  7. Quitter")
        print()
    
    def charger_produits(self) -> bool:
        produits_config = self.config.get("produits", [])
        if not produits_config:
            self.logger.warning("Aucun produit configuré")
            return False
        
        for prod_data in produits_config:
            produit = Produit(
                id=prod_data.get("id", f"prod_{len(self.produits_suivis)}"),
                nom=prod_data.get("nom", "Produit inconnu"),
                url=prod_data.get("url", ""),
                categorie=prod_data.get("categorie", ""),
                seuil_alerte=prod_data.get("seuil_alerte"),
            )
            self.produits_suivis.append(produit)
        
        self.logger.info(f"{len(self.produits_suivis)} produits chargés")
        return True
    
    def scanner_produit(self, url: str) -> Optional[dict]:
        print(f"\n{Colors.BOLD}🔍 Scanner: {url}{Colors.RESET}\n")
        
        resultat = self.scraper.scraper_produit(url)
        if resultat:
            print(f"  ✅ Titre: {resultat.get('titre', 'N/A')[:60]}")
            print(f"  💰 Prix: {resultat.get('prix', 'N/A')}")
            print(f"  🏪 Site: {resultat.get('site', 'N/A')}")
            print(f"  📦 Disponibilité: {resultat.get('disponible', 'N/A')}")
            
            self.history.ajouter(url, resultat)
            
            alertes = self.alerter.verifier(resultat)
            if alertes:
                print(f"\n{Colors.RED}🚨 ALERTES:{Colors.RESET}")
                for alerte in alertes:
                    print(f"  {alerte}")
        else:
            print(f"{Colors.RED}❌ Impossible de scanner le produit{Colors.RESET}")
        
        return resultat
    
    def comparer_produits(self, urls: List[str]) -> List[dict]:
        print(f"\n{Colors.BOLD}⚖️  Comparaison de {len(urls)} produits{Colors.RESET}\n")
        
        resultats = []
        for url in urls:
            resultat = self.scraper.scraper_produit(url)
            if resultat:
                resultats.append(resultat)
        
        if not resultats:
            print(f"{Colors.YELLOW}Aucun résultat trouvé{Colors.RESET}")
            return []
        
        comparaison = self.comparator.comparer(resultats)
        
        print(f"{Colors.BOLD}{'='*70}{Colors.RESET}")
        print(f"{Colors.BOLD}{'PRODUIT':<40} {'PRIX':<15} {'SITE':<15}{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*70}{Colors.RESET}")
        
        for i, item in enumerate(comparaison, 1):
            prix_formate = PriceFormatter.formater(item.get('prix', 0))
            site = item.get('site', 'N/A')[:15]
            titre = item.get('titre', 'N/A')[:40]
            print(f"{i:2}. {titre:<40} {prix_formate:<15} {site:<15}")
        
        print(f"{Colors.BOLD}{'='*70}{Colors.RESET}")
        
        if comparaison:
            moins_cher = min(comparaison, key=lambda x: x.get('prix', float('inf')))
            print(f"\n{Colors.GREEN}💡 Meilleur prix: {moins_cher.get('titre', 'N/A')[:40]}")
            print(f"   Prix: {PriceFormatter.formater(moins_cher.get('prix', 0))} sur {moins_cher.get('site', 'N/A')}{Colors.RESET}")
        
        return comparaison
    
    def definir_alerte(self, url: str, seuil: float):
        print(f"\n{Colors.BOLD}🔔 Définir une alerte{Colors.RESET}")
        print(f"  URL: {url}")
        print(f"  Seuil: {PriceFormatter.formater(seuil)}")
        
        self.alerter.ajouter_alerte(url, seuil)
        print(f"\n{Colors.GREEN}✅ Alerte définie!{Colors.RESET}")
    
    def afficher_historique(self, url: Optional[str] = None):
        print(f"\n{Colors.BOLD}📈 Historique des prix{Colors.RESET}\n")
        
        historique = self.history.obtenir_historique(url)
        if not historique:
            print(f"{Colors.YELLOW}Aucun historique disponible{Colors.RESET}")
            return
        
        print(f"{Colors.BOLD}{'DATE':<20} {'PRIX':<15} {'SITE':<15}{Colors.RESET}")
        print(f"{Colors.BOLD}{'-'*50}{Colors.RESET}")
        
        for entree in historique[-20:]:
            date = DateUtils.formater(entree.get('date_collecte'))
            prix = PriceFormatter.formater(entree.get('prix', 0))
            site = entree.get('site', 'N/A')[:15]
            print(f"{date:<20} {prix:<15} {site:<15}")
    
    def exporter_donnees(self, format: str = "csv"):
        print(f"\n{Colors.BOLD}📤 Export des données ({format}){Colors.RESET}\n")
        
        historique = self.history.obtenir_tout()
        if not historique:
            print(f"{Colors.YELLOW}Aucun données à exporter{Colors.RESET}")
            return
        
        if format == "csv":
            chemin = self.history.exporter_csv()
        elif format == "json":
            chemin = self.history.exporter_json()
        else:
            print(f"{Colors.RED}Format non supporté: {format}{Colors.RESET}")
            return
        
        print(f"{Colors.GREEN}✅ Exporté vers: {chemin}{Colors.RESET}")
    
    def executer_commande(self, commande: str) -> bool:
        cmd = commande.lower().strip()
        
        if cmd in ["1", "scanner", "scan"]:
            url = input("URL du produit: ")
            self.scanner_produit(url)
        elif cmd in ["2", "lister", "list"]:
            self.lister_produits()
        elif cmd in ["3", "comparer", "compare"]:
            urls = input("URLs séparées par des virgules: ").split(",")
            urls = [u.strip() for u in urls if u.strip()]
            self.comparer_produits(urls)
        elif cmd in ["4", "alerte", "alert"]:
            url = input("URL du produit: ")
            try:
                seuil = float(input("Seuil de prix (€): "))
                self.definir_alerte(url, seuil)
            except ValueError:
                print(f"{Colors.RED}Seuil invalide{Colors.RESET}")
        elif cmd in ["5", "historique", "history"]:
            self.afficher_historique()
        elif cmd in ["6", "exporter", "export"]:
            format_choisi = input("Format (csv/json): ").strip().lower()
            self.exporter_donnees(format_choisi)
        elif cmd in ["7", "q", "quit", "quitter", "exit"]:
            return False
        else:
            print(f"{Colors.RED}Commande inconnue{Colors.RESET}")
        
        return True
    
    def lister_produits(self):
        print(f"\n{Colors.BOLD}📦 Produits suivis ({len(self.produits_suivis)}){Colors.RESET}\n")
        
        if not self.produits_suivis:
            print(f"{Colors.YELLOW}Aucun produit suivi{Colors.RESET}")
            return
        
        for i, produit in enumerate(self.produits_suivis, 1):
            alert_emoji = "🔔" if produit.est_alerte() else "  "
            prix_str = PriceFormatter.formater(produit.prix_actuel.montant) if produit.prix_actuel else "N/A"
            print(f"{i:2}. {alert_emoji} {produit.nom[:40]}")
            print(f"      💰 {prix_str} | 📦 {produit.categorie}")
    
    def run_interactif(self):
        self._afficher_banniere()
        self.charger_produits()
        
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
        self.logger.info("Démarrage de l'application")
        
        if len(sys.argv) > 1:
            self._traiter_arguments()
        else:
            self.run_interactif()
    
    def _traiter_arguments(self):
        parser = argparse.ArgumentParser(
            description="Analyseur de Prix - Comparez les prix sur plusieurs sites",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Exemples:
    python src/main.py                    # Mode interactif
    python src/main.py --scan URL        # Scanner un produit
    python src/main.py --compare URL1 URL2  # Comparer plusieurs produits
    python src/main.py --alert URL SEUIL  # Définir une alerte
            """
        )
        parser.add_argument("--scan", "-s", metavar="URL",
                           help="Scanner un produit")
        parser.add_argument("--compare", "-c", nargs="+", metavar="URL",
                           help="Comparer plusieurs produits")
        parser.add_argument("--alert", "-a", nargs=2, metavar=("URL", "SEUIL"),
                           help="Définir une alerte de prix")
        parser.add_argument("--history", "-H", metavar="URL",
                           help="Voir l'historique d'un produit")
        parser.add_argument("--export", "-e", metavar="FORMAT",
                           help="Exporter les données (csv/json)")
        parser.add_argument("--version", action="version",
                           version=f"%(prog)s {self.VERSION}")
        
        args = parser.parse_args()
        
        if args.scan:
            self.scanner_produit(args.scan)
        elif args.compare:
            self.comparer_produits(args.compare)
        elif args.alert:
            url, seuil = args.alert
            try:
                self.definir_alerte(url, float(seuil))
            except ValueError:
                print(f"{Colors.RED}Seuil invalide{Colors.RESET}")
        elif args.history:
            self.afficher_historique(args.history)
        elif args.export:
            self.exporter_donnees(args.export)


def main():
    app = PriceAnalyzerApp()
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
