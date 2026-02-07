"""
Exercice 17.10 - DECORATEUR CLASS
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Decorateur de classe."""
    def classe_final(cls):
        cls.final = True
        return cls

    @classe_final
    class MaClasse:
        pass

    print(MaClasse.final)


# Pour tests manuels
if __name__ == "__main__":
    run()
