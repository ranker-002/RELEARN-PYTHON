"""
Exercice 19.4 - FONCTION AVEC TYPES
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer une fonction avec types."""
    # Crée une fonction qui prend deux entiers et retourne leur somme

    def additionner(a: int, b: int) -> int:
        return a + b

    resultat = additionner(5, 3)
    print(f"5 + 3 = {resultat}")


# Pour tests manuels
if __name__ == "__main__":
    run()
