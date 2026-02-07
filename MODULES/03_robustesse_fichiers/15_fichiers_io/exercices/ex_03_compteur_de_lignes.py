"""
Exercice 15.3 - COMPTEUR DE LIGNES
==================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Compter les lignes d'un fichier."""
    def compter_lignes(fichier):
        with open(fichier, "r") as f:
            return sum(1 for _ in f)

    print(f"Nombre de lignes: {compter_lignes('fichier.txt')}")


# Pour tests manuels
if __name__ == "__main__":
    run()
