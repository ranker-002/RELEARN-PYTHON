"""
Exercice 18.12 - CALLABLE FUTURE
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Future pour récupérer des résultats."""
    import threading
    import time
    from concurrent.futures import ThreadPoolExecutor

    def calcul_long(duree, nom):
        time.sleep(duree)
        return f"{nom}: terminé après {duree}s"

    with ThreadPoolExecutor(max_workers=2) as executor:
        f1 = executor.submit(calcul_long, 0.3, "Tâche 1")
        f2 = executor.submit(calcul_long, 0.1, "Tâche 2")
    
        print(f"Tâche 2 terminée: {f2.result()}")
        print(f"Tâche 1 terminée: {f1.result()}")


# Pour tests manuels
if __name__ == "__main__":
    run()
