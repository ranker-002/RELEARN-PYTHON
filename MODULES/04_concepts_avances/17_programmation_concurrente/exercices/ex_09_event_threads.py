"""
Exercice 18.9 - EVENT THREADS
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Event pour communiquer entre threads."""
    import threading
    import time

    event = threading.Event()

    def attendent_levent():
        print("En attente de l'event...")
        event.wait()
        print("Event reçu! Continuation...")

    def declenche_levent():
        time.sleep(1)
        print("Déclenchement de l'event!")
        event.set()

    t1 = threading.Thread(target=attendent_levent)
    t2 = threading.Thread(target=declenche_levent)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


# Pour tests manuels
if __name__ == "__main__":
    run()
