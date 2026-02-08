"""
Exercice 15.5 - LECTURE CSV
===========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lire un fichier CSV."""
    import csv

    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Pour tests manuels
if __name__ == "__main__":
    run()
