"""
Exercice 15.4 - LIGNES AVEC PREFIXE
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Ajouter un prefixe a chaque ligne."""
    with open("entree.txt", "r") as entree:
        with open("sortie.txt", "w") as sortie:
            for ligne in entree:
                sortie.write(f"[INFO] {ligne}")


# Pour tests manuels
if __name__ == "__main__":
    run()
