"""
Exercice 16.6 - SAUVEGARDE ETATS
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Sauvegarder et charger etat."""
    import pickle

    etat = {
        "score": 100,
        "niveau": 5,
        "objets": ["epee", "bouclier"]
    }

    with open("savegame.dat", "wb") as f:
        pickle.dump(etat, f)

    with open("savegame.dat", "rb") as f:
        charge = pickle.load(f)
        print(charge)


# Pour tests manuels
if __name__ == "__main__":
    run()
