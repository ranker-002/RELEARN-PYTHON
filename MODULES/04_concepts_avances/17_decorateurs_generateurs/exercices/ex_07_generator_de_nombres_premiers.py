"""
Exercice 17.7 - GENERATOR DE NOMBRES PREMIERS
=============================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Generator de nombres premiers."""
    def premiers(limite):
        for n in range(2, limite + 1):
            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    break
            else:
                yield n

    print(list(premiers(30)))


# Pour tests manuels
if __name__ == "__main__":
    run()
