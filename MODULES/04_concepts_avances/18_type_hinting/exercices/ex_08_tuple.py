"""
Exercice 19.8 - TUPLE
=====================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Tuple pour tuples typés."""
    # Déclare un tuple (nom, age, ville)

    personne: Tuple[str, int, str] = ("Alice", 25, "Paris")
    print(f"Personne: {personne}")
    print(f"Nom: {personne[0]}")


# Pour tests manuels
if __name__ == "__main__":
    run()
