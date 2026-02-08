"""
Exercice 18.15 - THREADING DANS CLASSE
======================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer une classe avec des méthodes threadées."""
    import threading
    import time

    class Telechargeur:
        def __init__(self):
            self.fichiers = []
            self.lock = threading.Lock()
    
        def telecharger(self, nom, duree):
            print(f"Téléchargement de {nom}...")
            time.sleep(duree)
            with self.lock:
                self.fichiers.append(nom)
            print(f"{nom} téléchargé!")
    
        def lister_fichiers(self):
            with self.lock:
                return self.fichiers.copy()

    telechargeur = Telechargeur()

    threads = [
        threading.Thread(target=telechargeur.telecharger, args=(f"fichier{i}.mp4", 0.2))
        for i in range(3)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"Fichiers téléchargés: {telechargeur.lister_fichiers()}")


# Pour tests manuels
if __name__ == "__main__":
    run()
