"""
Exercice 15.10 - COPIER FICHIER
===============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Copier un fichier binaire."""
    def copier(source, destination):
        with open(source, "rb") as src:
            with open(destination, "wb") as dst:
                dst.write(src.read())

    copier("source.png", "destination.png")


# Pour tests manuels
if __name__ == "__main__":
    run()
