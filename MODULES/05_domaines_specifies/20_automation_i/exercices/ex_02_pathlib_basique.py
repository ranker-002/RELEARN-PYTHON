"""
Exercice 20.2 - PATHLIB BASIQUE
===============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser pathlib pour lister les fichiers."""
    from pathlib import Path

    dossier = Path(".")
    for element in dossier.iterdir():
        if element.is_file():
            print(f"FICHIER: {element.name}")
        elif element.is_dir():
            print(f" DOSSIER: {element.name}/")


# Pour tests manuels
if __name__ == "__main__":
    run()
