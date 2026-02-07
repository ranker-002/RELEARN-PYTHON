"""
Exercice 18.11 - SEMAPHORE
==========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Semaphore pour limiter les accès concurrents."""
    import threading
    import time

    semaphore = threading.Semaphore(2)  # Maximum 2 threads simultanés

    def acces_ressource(num):
        with semaphore:
            print(f"Thread {num}: Accès à la ressource")
            time.sleep(0.2)
            print(f"Thread {num}: Fin de l'accès")

    threads = [threading.Thread(target=acces_ressource, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# Pour tests manuels
if __name__ == "__main__":
    run()
