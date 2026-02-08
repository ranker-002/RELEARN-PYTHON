"""
Exercice 15.13 - REMPLACER TEXTE
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Remplacer un mot par un autre."""
    def remplacer(fichier, ancien, nouveau):
        with open(fichier, "r") as f:
            contenu = f.read()
    
        with open(fichier, "w") as f:
            f.write(contenu.replace(ancien, nouveau))

    remplacer("fichier.txt", "ancien", "nouveau")


# Pour tests manuels
if __name__ == "__main__":
    run()
