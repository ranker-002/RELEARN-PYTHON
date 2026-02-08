"""
Exercice 17.8 - DECORATEUR VALIDATION
=====================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Decorateur de validation."""
    def valider(types):
        def decorateur(func):
            def wrapper(*args):
                for arg, expected in zip(args, types):
                    if not isinstance(arg, expected):
                        raise TypeError(f"{arg} doit etre {expected}")
                return func(*args)
            return wrapper
        return decorateur

    @valider((int, int))
    def addition(a, b):
        return a + b

    print(addition(5, 3))


# Pour tests manuels
if __name__ == "__main__":
    run()
