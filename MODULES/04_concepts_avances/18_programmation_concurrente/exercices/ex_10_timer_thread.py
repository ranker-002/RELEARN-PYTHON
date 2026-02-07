"""
Exercice 18.10 - TIMER THREAD
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Timer pour exécuter du code après un délai."""
    import threading
    import time

    print("Démarrage du timer...")

    def message_differe():
        print("Ce message apparaît après 0.5 secondes!")

    timer = threading.Timer(0.5, message_differe)
    timer.start()
    timer.join()


# Pour tests manuels
if __name__ == "__main__":
    run()
