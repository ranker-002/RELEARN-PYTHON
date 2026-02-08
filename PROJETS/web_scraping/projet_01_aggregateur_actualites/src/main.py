#!/usr/bin/env python3
"""
Agrégateur d'Actualités RSS - Version simplifiée pour vérification
"""

import argparse
from typing import Optional, List
from datetime import datetime


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
    
    def __init__(self):
        """Initialise l'application."""
        self.flux = []
        self.articles = []
    
    def _afficher_banniere(self):
        """Affiche la bannière de l'application."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print("╔══════════════════════════════════════════════════╗")
        print("║         AGRÉGATEUR D'ACTUALITÉS RSS             ║")
        print("╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def run(self):
        """Point d'entrée de l'application."""
        self._afficher_banniere()
        print("\nAgrégateur RSS initialisé.")
        print("Utilisez --help pour voir les options disponibles.")


def main():
    """Point d'entrée principal."""
    parser = argparse.ArgumentParser(description="Agrégateur d'Actualités RSS")
    parser.add_argument("--refresh", action="store_true", help="Rafraîchir les flux")
    parser.add_argument("--list", action="store_true", help="Lister les articles")
    
    args = parser.parse_args()
    
    app = AggregateurApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\nAu revoir!")


if __name__ == "__main__":
    main()
