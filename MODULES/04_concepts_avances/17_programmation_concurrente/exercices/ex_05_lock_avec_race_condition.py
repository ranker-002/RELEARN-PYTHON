"""
Exercice 18.5 - LOCK AVEC RACE CONDITION
========================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Montrer le problème du race condition."""
    import threading

    compteur = 0

    def incrementer_sans_lock():
        nonlocal compteur
        for _ in range(10000):
            compteur += 1

    threads = [threading.Thread(target=incrementer_sans_lock) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"Compteur sans lock: {compteur} (devrait être 40000)")


# Pour tests manuels
if __name__ == "__main__":
    run()
