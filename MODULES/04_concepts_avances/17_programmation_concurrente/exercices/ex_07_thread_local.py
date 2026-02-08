"""
Exercice 18.7 - THREAD LOCAL
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser ThreadLocal pour des données spécifiques au thread."""
    import threading

    donnees_locales = threading.local()

    def worker(nom):
        if not hasattr(donnees_locales, "compteur"):
            donnees_locales.compteur = 0
        donnees_locales.compteur += 1
        print(f"{nom}: compteur = {donnees_locales.compteur}")

    threads = [threading.Thread(target=worker, args=(f"Thread-{i}",)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# Pour tests manuels
if __name__ == "__main__":
    run()
