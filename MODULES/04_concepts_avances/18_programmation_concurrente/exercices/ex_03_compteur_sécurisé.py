"""
Exercice 18.3 - COMPTEUR SÉCURISÉ
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Compteur avec verrou pour éviter les race conditions."""
    import threading

    compteur = 0
    lock = threading.Lock()

    def incrementer():
        nonlocal compteur
        for _ in range(1000):
            with lock:
                compteur += 1

    threads = [threading.Thread(target=incrementer) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"Compteur final: {compteur} (attendu: 4000)")


# Pour tests manuels
if __name__ == "__main__":
    run()
