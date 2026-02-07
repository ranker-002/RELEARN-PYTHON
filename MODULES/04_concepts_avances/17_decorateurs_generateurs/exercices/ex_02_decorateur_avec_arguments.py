"""
Exercice 17.2 - DECORATEUR AVEC ARGUMENTS
=========================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Decorateur avec repetitions."""
    def repetitions(n):
        def decorateur(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func(*args, **kwargs)
            return wrapper
        return decorateur

    @repetitions(3)
    def dire_bonjour():
        print("Bonjour!")

    dire_bonjour()


# Pour tests manuels
if __name__ == "__main__":
    run()
