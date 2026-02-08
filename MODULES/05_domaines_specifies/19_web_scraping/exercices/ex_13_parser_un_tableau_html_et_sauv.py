"""
Exercice 21.13 - Parser un tableau HTML et sauvegarder en CSV.
=============================================================

Parser un tableau HTML et sauvegarder en CSV.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv


def run():
    """Fonction principale de l'exercice."""

    html = """
    <table>
        <tr>
            <th>Nom</th>
            <th>Age</th>
            <th>Ville</th>
        </tr>
        <tr>
            <td>Alice</td>
            <td>25</td>
            <td>Paris</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>30</td>
            <td>Lyon</td>
        </tr>
        <tr>
            <td>Charlie</td>
            <td>35</td>
            <td>Marseille</td>
        </tr>
    </table>
    """

    soup = BeautifulSoup(html, "html.parser")

    rows = soup.find_all("tr")

    with open("tableau.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
    
        for row in rows:
            cells = row.find_all(["td", "th"])
            if cells:
                writer.writerow([cell.get_text() for cell in cells])

    print("Tableau sauvegardé dans tableau.csv")





# Pour tests manuels
if __name__ == "__main__":
    run()
