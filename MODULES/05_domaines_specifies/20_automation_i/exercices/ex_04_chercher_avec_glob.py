"""
Exercice 20.4 - CHERCHER AVEC GLOB
==================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Trouver tous les fichiers Python."""
    import glob

    py_files = glob.glob("*.py")
    print(f"Fichiers Python trouvés: {py_files}")


# Pour tests manuels
if __name__ == "__main__":
    run()
