"""
Exercice 21.3 - Parser du HTML simple.
=====================================

Parser du HTML simple.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    html = """
    <html>
        <body>
            <h1>Titre Principal</h1>
            <p>Premier paragraphe</p>
            <p>Deuxième paragraphe</p>
            <a href="https://example.com">Lien</a>
        </body>
    </html>
    """

    soup = BeautifulSoup(html, "html.parser")

    titre = soup.find("h1")
    if titre:
        print(f"Titre: {titre.get_text()}")

    paragraphes = soup.find_all("p")
    print(f"Paragraphes: {len(paragraphes)}")
    for p in paragraphes:
        print(f"  - {p.get_text()}")





# Pour tests manuels
if __name__ == "__main__":
    run()
