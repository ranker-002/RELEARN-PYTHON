"""
Exercice 15.12 - STATISTIQUES
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Calculer les statistiques d'un fichier."""
    def analyser(fichier):
        with open(fichier, "r") as f:
            lignes = f.readlines()
    
        return {
            "lignes": len(lignes),
            "mots": sum(len(l.split()) for l in lignes),
            "caracteres": sum(len(l) for l in lignes)
        }

    print(analyser("fichier.txt"))


# Pour tests manuels
if __name__ == "__main__":
    run()
