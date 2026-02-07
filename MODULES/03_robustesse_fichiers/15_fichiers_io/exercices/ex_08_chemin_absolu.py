"""
Exercice 15.8 - CHEMIN ABSOLU
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Manipuler les chemins."""
    import os

    print(f"Chemin absolu: {os.path.abspath('fichier.txt')}")
    print(f"Est fichier: {os.path.isfile('fichier.txt')}")
    print(f"Est repertoire: {os.path.isdir('dossier')}")
    print(f"Taille: {os.path.getsize('fichier.txt')} octets")


# Pour tests manuels
if __name__ == "__main__":
    run()
