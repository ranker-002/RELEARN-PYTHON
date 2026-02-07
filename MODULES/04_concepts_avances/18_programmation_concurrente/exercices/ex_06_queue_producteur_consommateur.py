"""
Exercice 18.6 - QUEUE PRODUCTEUR CONSOMMATEUR
=============================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Système producteur-consommateur avec Queue."""
    import threading
    import queue
    import time

    file = queue.Queue()

    def consommateur():
        for _ in range(5):
            item = file.get()
            print(f"Consommé: {item}")
            file.task_done()

    def producteur():
        for i in range(5):
            time.sleep(0.1)
            file.put(i)
            print(f"Produit: {i}")

    t_consommateur = threading.Thread(target=consommateur)
    t_producteur = threading.Thread(target=producteur)

    t_producteur.start()
    t_consommateur.start()

    t_producteur.join()
    file.join()
    t_consommateur.join()

    print("Producteur-consommateur terminé")


# Pour tests manuels
if __name__ == "__main__":
    run()
