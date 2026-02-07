"""
Exercice 18.4 - THREADPOOLEXECUTOR
==================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser ThreadPoolExecutor."""
    from concurrent.futures import ThreadPoolExecutor
    import time

    def carre(n):
        time.sleep(0.1)
        return n * n

    with ThreadPoolExecutor(max_workers=3) as executor:
        resultats = list(executor.map(carre, [1, 2, 3, 4, 5]))

    print(f"Résultats: {resultats}")


# Pour tests manuels
if __name__ == "__main__":
    run()
