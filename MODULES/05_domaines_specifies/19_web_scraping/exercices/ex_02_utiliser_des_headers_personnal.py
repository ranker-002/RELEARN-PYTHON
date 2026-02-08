"""
Exercice 21.2 - Utiliser des headers personnalisés.
==================================================

Utiliser des headers personnalisés.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    headers = {
        "User-Agent": "MonBot/1.0",
        "Accept": "application/json"
    }

    try:
        reponse = requests.get("https://httpbin.org/headers", headers=headers, timeout=5)
        print(reponse.json())
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
