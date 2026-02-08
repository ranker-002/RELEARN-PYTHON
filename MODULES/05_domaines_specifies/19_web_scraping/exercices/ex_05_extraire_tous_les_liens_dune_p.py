"""
Exercice 21.5 - Extraire tous les liens d'une page.
==================================================

Extraire tous les liens d'une page.
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
            <a href="https://site.com/page1">Page 1</a>
            <a href="https://site.com/page2">Page 2</a>
            <a href="https://autre.com">Autre site</a>
        </body>
    </html>
    """

    soup = BeautifulSoup(html, "html.parser")

    liens = soup.find_all("a", href=True)
    print(f"Liens trouvés: {len(liens)}")

    for lien in liens:
        print(f"  Texte: {lien.get_text()}")
        print(f"  URL: {lien['href']}")





# Pour tests manuels
if __name__ == "__main__":
    run()
