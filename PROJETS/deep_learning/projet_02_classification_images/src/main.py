#!/usr/bin/env python3
"""
projet_02_classification_images

Projet du module deep_learning.

Usage:
    python src/main.py                    # Mode interactif
    python src/main.py --help            # Aide
"""

import sys
from pathlib import Path
from typing import Optional, List
from datetime import datetime


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"


class Projet02ClassificationImages:
    """Application principale."""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        """Initialise l'application."""
        self.logger = self._setup_logging()
        self.logger.info(f"Application initialisée")
    
    def _setup_logging(self):
        """Configure le logging."""
        import logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("deep_learning")
    
    def _afficher_banniere(self):
        """Affiche la bannière."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print(f"╔══════════════════════════════════════════════════╗")
        print(f"║            projet_02_classification_images      ║")
        print(f"╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def run(self):
        """Point d'entrée."""
        self._afficher_banniere()
        print("\nTODO: Implémenter la logique du projet")


def main():
    """Point d'entrée."""
    app = Projet02ClassificationImages()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir!")
    except Exception as e:
        print(f"\n{Colors.RED}Erreur: {e}{Colors.RESET}")


if __name__ == "__main__":
    main()
