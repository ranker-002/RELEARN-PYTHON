"""
Exercice 20.6 - INFOS FICHIER
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Afficher les informations d'un fichier."""
    from pathlib import Path
    from datetime import datetime

    fichier = Path("test_copy.txt")
    if fichier.exists():
        print(f"Nom: {fichier.name}")
        print(f"Taille: {fichier.stat().st_size} octets")
        mtime = datetime.fromtimestamp(fichier.stat().st_mtime)
        print(f"Modifié le: {mtime}")


# Pour tests manuels
if __name__ == "__main__":
    run()
