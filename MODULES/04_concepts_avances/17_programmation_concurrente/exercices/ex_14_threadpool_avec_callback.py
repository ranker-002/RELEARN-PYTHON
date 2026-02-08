"""
Exercice 18.14 - THREADpooL AVEC CALLBACK
=========================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser des callbacks sur les Future."""
    import time
    from concurrent.futures import ThreadPoolExecutor

    def tache(nom):
        time.sleep(0.2)
        return nom

    def callback(future):
        print(f"Callback: {future.result()} a terminé")

    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(tache, "Tâche avec callback")
        future.add_done_callback(callback)
    
        resultat = future.result()
        print(f"Résultat: {resultat}")


# Pour tests manuels
if __name__ == "__main__":
    run()
