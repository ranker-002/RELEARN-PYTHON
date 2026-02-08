"""
Exercice 17.4 - GENERATOR PUISSANCE
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Generator avec accumulateur."""
    def accumulateur(depart=0):
        total = start = 1
        while True:
            yield total
            total += start
            start += 1

    for i, v in enumerate(accumulateur()):
        if i >= 10:
            break
        print(v)


# Pour tests manuels
if __name__ == "__main__":
    run()
