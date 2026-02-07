"""
Exercice 15.7 - JSON
====================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lire et ecrire JSON."""
    import json

    # Lire
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ecrire
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Pour tests manuels
if __name__ == "__main__":
    run()
