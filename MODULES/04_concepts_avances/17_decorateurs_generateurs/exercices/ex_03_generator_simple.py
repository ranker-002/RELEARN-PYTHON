"""
Exercice 17.3 - GENERATOR SIMPLE
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Generator de carres."""
    def carres(n):
        for i in range(n):
            yield i ** 2

    for c in carres(5):
        print(c)


# Pour tests manuels
if __name__ == "__main__":
    run()
