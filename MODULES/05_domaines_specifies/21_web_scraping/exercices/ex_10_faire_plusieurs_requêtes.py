"""
Exercice 21.10 - Faire plusieurs requêtes.
=========================================

Faire plusieurs requêtes.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    ids = [1, 2, 3]

    for id_ in ids:
        try:
            reponse = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_}", timeout=5)
            data = reponse.json()
            print(f"{id_}: {data['title']}")
        except Exception as e:
            print(f"Erreur pour {id_}: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
