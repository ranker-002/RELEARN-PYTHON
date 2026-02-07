"""
Exercice 20.11 - ORGANISATEUR SIMPLE
====================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Organiser les fichiers par extension."""
    from pathlib import Path
    import os

    dossier = Path(".")
    for element in dossier.iterdir():
        if element.is_file():
            ext = element.suffix.lower()[1:] if element.suffix else "autres"
            cible = dossier / ext
            cible.mkdir(exist_ok=True)
            element.rename(cible / element.name)
            print(f"{element.name} → {ext}/")


# Pour tests manuels
if __name__ == "__main__":
    run()
