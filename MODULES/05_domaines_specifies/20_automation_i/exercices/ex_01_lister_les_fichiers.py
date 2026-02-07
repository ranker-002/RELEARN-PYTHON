"""
Exercice 20.1 - LISTER LES FICHIERS
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lister les fichiers du dossier courant avec os."""
    import os

    fichiers = os.listdir(".")
    print("Fichiers dans le dossier courant:")
    for f in fichiers:
        print(f"  - {f}")


# Pour tests manuels
if __name__ == "__main__":
    run()
