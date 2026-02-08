#!/usr/bin/env python3
"""
Analyseur de Prix - Projet d'apprentissage.

ÉNONCÉ:
--------
Implémentez un compareur de prix avec:
- Scraping de sites e-commerce (Amazon, Cdiscount, etc.)
- Comparaison de prix multi-sources
- Alertes de prix par email/SMS
- Historique des prix
- Export des données

TODO: Implémenter la logique du projet.
"""

import argparse
from typing import List, Optional


class Produit:
    """Produit à implémenter."""
    
    def __init__(self, nom: str, url: str):
        self.id = ""
        self.nom = nom
        self.url = url
        self.prix = 0.0
        self.disponible = True


class Scraper:
    """Scraper à implémenter."""
    
    def __init__(self):
        self.produits = []
    
    def scraper_produit(self, url: str) -> Optional[Produit]:
        """Scraper un produit."""
        raise NotImplementedError
    
    def comparer_prix(self, urls: List[str]) -> List[Produit]:
        """Comparer les prix."""
        raise NotImplementedError


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description="Analyseur de Prix CLI")
    parser.add_argument("--scan", metavar="URL", help="Scanner un produit")
    parser.add_argument("--compare", nargs="+", metavar="URL", help="Comparer plusieurs produits")
    parser.add_argument("--alert", nargs=2, metavar=("URL", "SEUIL"), help="Définir une alerte")
    
    args = parser.parse_args()
    
    print("=== Analyseur de Prix CLI ===")
    print("TODO: Implémenter la logique")
    
    if args.scan:
        print(f"Scanner: {args.scan}")
    elif args.compare:
        print(f"Comparer: {args.compare}")
    elif args.alert:
        print(f"Alerte: {args.alert}")


if __name__ == "__main__":
    main()
