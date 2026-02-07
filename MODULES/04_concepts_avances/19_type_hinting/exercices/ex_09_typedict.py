"""
Exercice 19.9 - TYPEDICT
========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser TypedDict."""
    # Crée une personne avec le TypedDict

    alice: Personne = {
        "nom": "Alice",
        "age": 25,
        "ville": "Paris"
    }

    print(f"{alice['nom']}, {alice['age']} ans, {alice['ville']}")


# Pour tests manuels
if __name__ == "__main__":
    run()
