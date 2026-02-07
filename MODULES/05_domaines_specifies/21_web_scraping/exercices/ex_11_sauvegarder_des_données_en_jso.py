"""
Exercice 21.11 - Sauvegarder des données en JSON.
================================================

Sauvegarder des données en JSON.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    try:
        reponse = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
        posts = reponse.json()[:5]
    
        with open("posts.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
    
        print(f"Sauvegardé {len(posts)} posts dans posts.json")
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
