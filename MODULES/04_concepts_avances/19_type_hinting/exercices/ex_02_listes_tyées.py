"""
Exercice 19.2 - LISTES TYÉES
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser List avec types."""
    # Déclare une liste de nombres entiers: [1, 2, 3, 4, 5]
    # Déclare une liste de textes: ["Alice", "Bob", "Charlie"]

    nombres: List[int] = [1, 2, 3, 4, 5]
    noms: List[str] = ["Alice", "Bob", "Charlie"]

    print(f"Nombres: {nombres}")
    print(f"Noms: {noms}")


# Pour tests manuels
if __name__ == "__main__":
    run()
