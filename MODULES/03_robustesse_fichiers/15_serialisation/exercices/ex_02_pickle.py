"""
Exercice 16.2 - PICKLE
======================


"""


def run():
    """Fonction principale de l'exercice."""
    """Serialiser avec Pickle."""
    import pickle

    class Personne:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age

    p = Personne("Bob", 25)

    with open("personne.pkl", "wb") as f:
        pickle.dump(p, f)

    with open("personne.pkl", "rb") as f:
        p2 = pickle.load(f)
        print(p2.nom, p2.age)


# Pour tests manuels
if __name__ == "__main__":
    run()
