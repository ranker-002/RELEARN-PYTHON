"""
Exercice 21.9 - Récupérer et parser du JSON.
===========================================

Récupérer et parser du JSON.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    try:
        reponse = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        data = reponse.json()
    
        print(f"Titre: {data['title']}")
        print(f"Corps: {data['body']}")
        print(f"ID: {data['id']}")
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
