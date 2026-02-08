"""
Exercice 17.9 - GENERATOR DE COMBINAISONS
=========================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Generator de combinaisons."""
    def combinaisons(items, k):
        if k == 0:
            yield []
        else:
            for i in range(len(items)):
                for reste in combinaisons(items[i + 1:], k - 1):
                    yield [items[i]] + reste

    print(list(combinaisons([1, 2, 3], 2)))


# Pour tests manuels
if __name__ == "__main__":
    run()
