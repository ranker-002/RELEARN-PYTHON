"""
Exercice 15.2 - ECRITURE SIMPLE
===============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Ecrire dans un fichier."""
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Ligne 1\n")
        f.write("Ligne 2\n")


# Pour tests manuels
if __name__ == "__main__":
    run()
