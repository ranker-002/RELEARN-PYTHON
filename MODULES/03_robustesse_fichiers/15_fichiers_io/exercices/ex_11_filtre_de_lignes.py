"""
Exercice 15.11 - FILTRE DE LIGNES
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Filtrer les lignes contenant un mot."""
    def filtrer(fichier_in, fichier_out, mot):
        with open(fichier_in, "r") as entree:
            with open(fichier_out, "w") as sortie:
                for ligne in entree:
                    if mot in ligne:
                        sortie.write(ligne)

    filtrer("entree.txt", "sortie.txt", "erreur")


# Pour tests manuels
if __name__ == "__main__":
    run()
