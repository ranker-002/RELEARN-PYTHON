"""
Exercice 21.4 - Rechercher par classe CSS.
=========================================

Rechercher par classe CSS.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    html = """
    <div class="article">
        <h2 class="title">Article 1</h2>
        <p class="content">Contenu de l'article 1</p>
    </div>
    <div class="article">
        <h2 class="title">Article 2</h2>
        <p class="content">Contenu de l'article 2</p>
    </div>
    """

    soup = BeautifulSoup(html, "html.parser")

    articles = soup.find_all("div", class_="article")
    print(f"Articles trouvés: {len(articles)}")

    for i, article in enumerate(articles, 1):
        titre = article.find("h2", class_="title")
        contenu = article.find("p", class_="content")
        if titre and contenu:
            print(f"{i}. {titre.get_text()}: {contenu.get_text()}")





# Pour tests manuels
if __name__ == "__main__":
    run()
