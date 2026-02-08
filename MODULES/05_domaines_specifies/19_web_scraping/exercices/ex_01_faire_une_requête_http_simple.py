"""
Exercice 21.1 - Faire une requête HTTP simple.
=============================================

Faire une requête HTTP simple.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    try:
        reponse = requests.get("https://httpbin.org/get", timeout=5)
        print(f"Status: {reponse.status_code}")
        print(f"URL: {reponse.url}")
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
