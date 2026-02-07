"""
Exercice 15.1 - LECTURE SIMPLE
==============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lire et afficher un fichier."""
    # Creez un fichier test.txt avec "Bonjour le monde!"
    # Puis lisez et affichez son contenu

    with open("test.txt", "r", encoding="utf-8") as f:
        print(f.read())


# Pour tests manuels
if __name__ == "__main__":
    run()
