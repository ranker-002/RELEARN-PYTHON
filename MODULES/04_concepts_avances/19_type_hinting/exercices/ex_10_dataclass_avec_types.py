"""
Exercice 19.10 - DATACLASS AVEC TYPES
=====================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser dataclass avec types."""
    # Crée un utilisateur

    user = Utilisateur(nom="Alice", age=25, email="alice@email.com")
    print(user)


# Pour tests manuels
if __name__ == "__main__":
    run()
