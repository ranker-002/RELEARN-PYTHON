"""
Exercice 19.3 - DICTIONNAIRES TYÉES
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Dict avec types."""
    # Déclare un dictionnaire age: {"Alice": 25, "Bob": 30, "Charlie": 35}

    ages: Dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}

    for nom, age in ages.items():
        print(f"{nom}: {age} ans")


# Pour tests manuels
if __name__ == "__main__":
    run()
