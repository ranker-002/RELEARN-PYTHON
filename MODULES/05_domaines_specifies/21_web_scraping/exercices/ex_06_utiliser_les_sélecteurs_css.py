"""
Exercice 21.6 - Utiliser les sélecteurs CSS.
===========================================

Utiliser les sélecteurs CSS.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    html = """
    <div id="main">
        <div class="container">
            <p class="text">Premier</p>
            <p class="text">Deuxième</p>
        </div>
        <span class="info">Info</span>
    </div>
    """

    soup = BeautifulSoup(html, "html.parser")

    main = soup.select_one("#main")
    if main:
        print(f"Main content: {len(main.get_text())} chars")

    texts = soup.select(".text")
    print(f"Textes: {len(texts)}")
    for t in texts:
        print(f"  - {t.get_text()}")





# Pour tests manuels
if __name__ == "__main__":
    run()
