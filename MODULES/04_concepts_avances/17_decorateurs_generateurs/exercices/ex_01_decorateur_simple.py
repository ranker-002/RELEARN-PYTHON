"""
Exercice 17.1 - DECORATEUR SIMPLE
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Decorateur qui mesure le temps."""
    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            debut = time.time()
            resultat = func(*args, **kwargs)
            print(f"Temps: {time.time() - debut:.4f}s")
            return resultat
        return wrapper

    @timer
    def lente():
        time.sleep(0.1)
        return "Fini"

    print(lente())


# Pour tests manuels
if __name__ == "__main__":
    run()
