"""
Exercice 20.12 - NETTOYAGE DOSSIER
==================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Nettoyer les fichiers temporaires."""
    from pathlib import Path

    temp_files = []
    for element in Path(".").iterdir():
        if element.is_file():
            if element.name.endswith((".tmp", ".log", "~")):
                temp_files.append(element)

    for f in temp_files:
        print(f"Nettoyé: {f.name}")


# Pour tests manuels
if __name__ == "__main__":
    run()
