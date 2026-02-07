"""
Exercice 18.8 - BARRIER
=======================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Barrier pour synchroniser des threads."""
    import threading
    import time

    barrier = threading.Barrier(3)

    def phase1():
        print("Phase 1 début")
        time.sleep(0.1)
        print("Phase 1 fin, en attente...")
        barrier.wait()
        print("Phase 1 terminée")

    threads = [threading.Thread(target=phase1) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# Pour tests manuels
if __name__ == "__main__":
    run()
