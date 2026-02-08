"""
Exercice 21.15 - Scraper une page de données structurées.
========================================================

Scraper une page de données structurées.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    html = """
    <div class="products">
        <div class="product" data-id="1">
            <h3>Ordinateur Portable</h3>
            <span class="price">999.99 €</span>
            <span class="category">Informatique</span>
        </div>
        <div class="product" data-id="2">
            <h3>Smartphone</h3>
            <span class="price">599.99 €</span>
            <span class="category">Téléphonie</span>
        </div>
        <div class="product" data-id="3">
            <h3>Casque Audio</h3>
            <span class="price">149.99 €</span>
            <span class="category">Audio</span>
        </div>
    </div>
    """

    soup = BeautifulSoup(html, "html.parser")

    produits = []

    for product in soup.find_all("div", class_="product"):
        nom = product.find("h3")
        prix = product.find("span", class_="price")
        categorie = product.find("span", class_="category")
        id_ = product.get("data-id")
    
        if nom and prix and categorie:
            produits.append({
                "id": id_,
                "nom": nom.get_text(),
                "prix": prix.get_text(),
                "categorie": categorie.get_text()
            })

    print(f"Produits trouvés: {len(produits)}")
    for p in produits:
        print(f"  - {p['nom']}: {p['prix']} ({p['categorie']})")


    if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 21: WEB SCRAPING")
    print("=" * 50)

    for i in range(1, 16):
        print(f"\n--- Exercice 21.{i} ---")
        try:
            eval(f"exercice_21_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")


# Pour tests manuels
if __name__ == "__main__":
    run()
