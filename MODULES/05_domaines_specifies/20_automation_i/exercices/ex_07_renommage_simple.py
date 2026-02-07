"""
Exercice 20.7 - RENOMMAGE SIMPLE
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Renommer un fichier."""
    from pathlib import Path

    original = Path("test_copy.txt")
    renomme = Path("test_renomme.txt")
    if original.exists():
        original.rename(renomme)
        print(f"Renommé en {renomme.name}")


# Pour tests manuels
if __name__ == "__main__":
    run()
