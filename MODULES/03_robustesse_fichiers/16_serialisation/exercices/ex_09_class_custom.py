"""
Exercice 16.9 - CLASS CUSTOM
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Serialiser classe personnalisee."""
    import pickle

    class GameState:
        def __init__(self):
            self.joueurs = []
            self.tour = 1
    
        def ajouter_joueur(self, nom):
            self.joueurs.append(nom)

    etat = GameState()
    etat.ajouter_joueur("Alice")
    etat.ajouter_joueur("Bob")

    with open("game.dat", "wb") as f:
        pickle.dump(etat, f)


# Pour tests manuels
if __name__ == "__main__":
    run()
