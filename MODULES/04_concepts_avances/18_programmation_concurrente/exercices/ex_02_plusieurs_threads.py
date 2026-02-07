"""
Exercice 18.2 - PLUSIEURS THREADS
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lancer plusieurs threads simultanément."""
    import threading
    import time

    def worker(num):
        time.sleep(0.5)
        print(f"Worker {num} terminé")

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Tous les threads terminés")


# Pour tests manuels
if __name__ == "__main__":
    run()
