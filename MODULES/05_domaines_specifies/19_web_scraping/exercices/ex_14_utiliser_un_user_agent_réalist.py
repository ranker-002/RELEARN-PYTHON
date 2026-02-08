"""
Exercice 21.14 - Utiliser un User-Agent réaliste.
================================================

Utiliser un User-Agent réaliste.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
    }

    try:
        reponse = requests.get("https://httpbin.org/headers", headers=headers, timeout=5)
        data = reponse.json()
        print("Headers envoyés:")
        for key, value in data["headers"].items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
