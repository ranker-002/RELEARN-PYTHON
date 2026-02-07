"""
Exercice 21.8 - Utiliser des paramètres de requête.
==================================================

Utiliser des paramètres de requête.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    params = {
        "page": 2,
        "limit": 5,
        "sort": "date"
    }

    try:
        reponse = requests.get("https://httpbin.org/get", params=params, timeout=5)
        data = reponse.json()
        print(f"URL: {data['args']}")
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
