"""
Exercice 16.1 - JSON
====================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lire et ecrire JSON."""
    import json

    data = {"nom": "Alice", "age": 30, "villes": ["Paris", "Lyon"]}

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    with open("data.json", "r") as f:
        print(json.load(f))


# Pour tests manuels
if __name__ == "__main__":
    run()
