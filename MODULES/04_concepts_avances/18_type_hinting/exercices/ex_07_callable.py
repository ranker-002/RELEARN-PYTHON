"""
Exercice 19.7 - CALLABLE
========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Callable pour fonctions."""
    # Crée une fonction qui prend un Callable

    def appliquer(fonction: Callable[[int], int], x: int) -> int:
        return fonction(x)

    def doubler(n: int) -> int:
        return n * 2

    resultat = appliquer(doubler, 5)
    print(f"doubler(5) = {resultat}")


# Pour tests manuels
if __name__ == "__main__":
    run()
