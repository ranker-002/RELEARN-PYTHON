"""
Exercice 15.6 - ECRITURE CSV
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Ecrire dans un fichier CSV."""
    import csv

    donnees = [
        ["Nom", "Age", "Ville"],
        ["Alice", 30, "Paris"],
        ["Bob", 25, "Lyon"]
    ]

    with open("output.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(donnees)


# Pour tests manuels
if __name__ == "__main__":
    run()
