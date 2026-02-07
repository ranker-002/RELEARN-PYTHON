"""
Exercice 17.6 - DECORATEUR CACHE
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Decorateur avec memoisation."""
    def cache(func):
        memo = {}
        def wrapper(n):
            if n not in memo:
                memo[n] = func(n)
            return memo[n]
        return wrapper

    @cache
    def factorielle(n):
        print(f"Calcul {n}")
        return 1 if n <= 1 else n * factorielle(n - 1)

    print(fact(5))
    print(fact(5))  # Pas de recalcul


# Pour tests manuels
if __name__ == "__main__":
    run()
