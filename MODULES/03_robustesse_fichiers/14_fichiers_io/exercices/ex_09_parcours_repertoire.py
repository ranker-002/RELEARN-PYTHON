"""
Exercice 15.9 - PARCOURS REPERTOIRE
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lister les fichiers d'un repertoire."""
    import os

    for elem in os.listdir("."):
        chemin = os.path.join(".", elem)
        if os.path.isfile(chemin):
            print(f"F: {elem}")
        elif os.path.isdir(chemin):
            print(f"D: {elem}")


# Pour tests manuels
if __name__ == "__main__":
    run()
