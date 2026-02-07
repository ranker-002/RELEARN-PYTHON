"""
Exercice 21.7 - Gérer les erreurs de requête.
============================================

Gérer les erreurs de requête.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    urls = [
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://inexistant.xyz",
    ]

    for url in urls:
        try:
            reponse = requests.get(url, timeout=5)
            print(f"{url}: {reponse.status_code}")
        except Exception as e:
            print(f"{url}: ERREUR - {type(e).__name__}")





# Pour tests manuels
if __name__ == "__main__":
    run()
