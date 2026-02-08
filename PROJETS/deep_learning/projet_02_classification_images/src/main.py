#!/usr/bin/env python3
"""
Classification d'Images

Application avec:
- Gestion complète des entités
- Interface CLI interactive
- Export et statistiques
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from models import Modele, Statut
from services.classificateur import Classificateur


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"


class Projet02ClassificationImages:
    """Application principale."""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        """Initialise l'application."""
        self.service = Classificateur()
        self.logger = self._setup_logging()
        self.logger.info("Application initialisée")
    
    def _setup_logging(self):
        """Configure le logging."""
        import logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("projet_02_classification_images")
    
    def _afficher_banniere(self):
        """Affiche la bannière."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print(f"╔══════════════════════════════════════════════════╗")
        print(f"║  CLASSIFICATION D'IMAGES              ║")
        print(f"╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def _afficher_menu(self):
        """Affiche le menu principal."""
        print(f"\n{Colors.BOLD}=== MENU PRINCIPAL ==={Colors.RESET}")
        print(f"{Colors.CYAN}1.{Colors.RESET} Créer")
        print(f"{Colors.CYAN}2.{Colors.RESET} Lister")
        print(f"{Colors.CYAN}3.{Colors.RESET} Rechercher")
        print(f"{Colors.CYAN}4.{Colors.RESET} Mettre à jour")
        print(f"{Colors.CYAN}5.{Colors.RESET} Supprimer")
        print(f"{Colors.CYAN}6.{Colors.RESET} Statistiques")
        print(f"{Colors.CYAN}7.{Colors.RESET} Quitter")
        print()
    
    def creer(self):
        """Crée un nouvel élément."""
        print(f"\n{Colors.BOLD}=== CRÉER ==={Colors.RESET}")
        nom = input(f"{Colors.CYAN}Nom: {Colors.RESET}").strip()
        
        if nom:
            item = self.service.creer(nom)
            print(f"\n{Colors.GREEN}Créé avec succès!{Colors.RESET}")
            print(f"{Colors.CYAN}ID: {Colors.RESET}{item.id[:8]}")
        else:
            print(f"\n{Colors.RED}Nom requis.{Colors.RESET}")
    
    def lister(self):
        """Liste tous les éléments."""
        items = self.service.get_all()
        if not items:
            print(f"\n{Colors.YELLOW}Aucun élément trouvé.{Colors.RESET}")
            return
        
        print(f"\n{Colors.BOLD}=== LISTE ({len(items)}) ==={Colors.RESET}")
        for item in items:
            print(f"{Colors.CYAN}-{Colors.RESET} {item.nom} ({item.statut.value})")
            print(f"   ID: {item.id[:8]}")
    
    def run(self):
        """Point d'entrée interactif."""
        self._afficher_banniere()
        
        while True:
            self._afficher_menu()
            choix = input(f"{Colors.CYAN}Choix: {Colors.RESET}").strip()
            
            if choix == "1":
                self.creer()
            elif choix == "2":
                self.lister()
            elif choix == "7":
                print(f"\n{Colors.YELLOW}Au revoir!{Colors.RESET}")
                break


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description="Classification d'Images")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    
    args = parser.parse_args()
    
    app = Projet02ClassificationImages()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir!")
    except Exception as e:
        print(f"\n{Colors.RED}Erreur: {e}{Colors.RESET}")


if __name__ == "__main__":
    main()
