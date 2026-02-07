"""
Exercice 18.1 - THREAD SIMPLE
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer et lancer un thread simple."""
    import threading
    import time

    def dire_bonjour():
        time.sleep(0.5)
        print("Bonjour depuis le thread!")

    t = threading.Thread(target=dire_bonjour)
    t.start()
    t.join()


# Pour tests manuels
if __name__ == "__main__":
    run()
