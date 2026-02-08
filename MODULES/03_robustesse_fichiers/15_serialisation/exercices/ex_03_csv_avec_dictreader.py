"""
Exercice 16.3 - CSV AVEC DICTREADER
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """CSV avec dictionnaires."""
    import csv

    data = [
        {"nom": "Alice", "age": 30},
        {"nom": "Bob", "age": 25}
    ]

    with open("output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nom", "age"])
        writer.writeheader()
        writer.writerows(data)


# Pour tests manuels
if __name__ == "__main__":
    run()
