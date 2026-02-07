"""
Exercice 20.3 - CRÉER DOSSIERS
==============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer une structure de dossiers."""
    from pathlib import Path

    structure = Path("test_folder/subfolder1/subfolder2")
    structure.mkdir(parents=True, exist_ok=True)
    print("Dossiers créés!")


# Pour tests manuels
if __name__ == "__main__":
    run()
