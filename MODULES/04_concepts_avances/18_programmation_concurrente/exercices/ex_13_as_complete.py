"""
Exercice 18.13 - AS COMPLETE
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser as_completed pour traiter les résultats au fur et à mesure."""
    import time
    from concurrent.futures import ThreadPoolExecutor

    def tache(nom, duree):
        time.sleep(duree)
        return nom

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(tache, "A", 0.3),
            executor.submit(tache, "B", 0.1),
            executor.submit(tache, "C", 0.2),
        ]
    
        from concurrent.futures import as_completed
        for future in as_completed(futures):
            print(f"Terminé: {future.result()}")


# Pour tests manuels
if __name__ == "__main__":
    run()
