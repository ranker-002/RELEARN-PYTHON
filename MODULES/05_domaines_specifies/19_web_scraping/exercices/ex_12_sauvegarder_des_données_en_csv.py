"""
Exercice 21.12 - Sauvegarder des données en CSV.
===============================================

Sauvegarder des données en CSV.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    try:
        reponse = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
        users = reponse.json()[:3]
    
        with open("users.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "email", "city"])
            writer.writeheader()
            for user in users:
                writer.writerow({
                    "id": user["id"],
                    "name": user["name"],
                    "email": user["email"],
                    "city": user["address"]["city"]
                })
    
        print("Utilisateurs sauvegardés dans users.csv")
    except Exception as e:
        print(f"Erreur: {e}")





# Pour tests manuels
if __name__ == "__main__":
    run()
