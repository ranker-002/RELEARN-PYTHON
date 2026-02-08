"""
Exercice 17.5 - YIELD FROM
==========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Generator compose."""
    def gen1():
        for i in range(3):
            yield i

    def gen2():
        yield from gen1()
        yield from range(3, 6)

    print(list(gen2()))


# Pour tests manuels
if __name__ == "__main__":
    run()
