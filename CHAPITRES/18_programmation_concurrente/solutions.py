# =============================================================================
# CHAPITRE 18: PROGRAMMATION CONCURRENTE - SOLUTIONS
# =============================================================================

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed


def exercice_18_1():
    """Thread simple."""
    def dire_bonjour():
        time.sleep(0.5)
        print("Bonjour depuis le thread!")
    
    t = threading.Thread(target=dire_bonjour)
    t.start()
    t.join()
    print("Thread terminé")


def exercice_18_2():
    """Plusieurs threads."""
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


def exercice_18_3():
    """Compteur avec verrou."""
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
    
    print(f"Compteur final: {compteur}")


def exercice_18_4():
    """ThreadPoolExecutor."""
    def carre(n):
        time.sleep(0.1)
        return n * n
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        resultats = list(executor.map(carre, [1, 2, 3, 4, 5]))
    
    print(f"Résultats: {resultats}")


def exercice_18_5():
    """Race condition."""
    compteur = 0
    
    def incrementer():
        nonlocal compteur
        for _ in range(10000):
            compteur += 1
    
    threads = [threading.Thread(target=incrementer) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"Compteur (devrait être 40000): {compteur}")


def exercice_18_6():
    """Producteur-consommateur."""
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


def exercice_18_7():
    """ThreadLocal."""
    donnees_locales = threading.local()
    
    def worker(nom):
        if not hasattr(donnees_locales, "compteur"):
            donnees_locales.compteur = 0
        donnees_locales.compteur += 1
        print(f"{nom}: {donnees_locales.compteur}")
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"T-{i}",))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()


def exercice_18_8():
    """Barrier."""
    barrier = threading.Barrier(3)
    
    def phase1():
        print("Phase 1 début")
        time.sleep(0.1)
        barrier.wait()
        print("Phase 1 fin")
    
    threads = [threading.Thread(target=phase1) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def exercice_18_9():
    """Event."""
    event = threading.Event()
    
    def attendre():
        print("En attente de l'event...")
        event.wait()
        print("Event reçu!")
    
    def declencher():
        time.sleep(1)
        print("Déclenchement de l'event!")
        event.set()
    
    t1 = threading.Thread(target=attendre)
    t2 = threading.Thread(target=declencher)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


def exercice_18_10():
    """Timer."""
    def message_differe():
        print("Ce message apparaît après 0.5 secondes!")
    
    print("Démarrage du timer...")
    timer = threading.Timer(0.5, message_differe)
    timer.start()
    timer.join()


def exercice_18_11():
    """Semaphore."""
    semaphore = threading.Semaphore(2)
    
    def acces_ressource(num):
        with semaphore:
            print(f"Thread {num}: Accès à la ressource")
            time.sleep(0.2)
            print(f"Thread {num}: Fin de l'accès")
    
    threads = []
    for i in range(5):
        t = threading.Thread(target=acces_ressource, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()


def exercice_18_12():
    """Callable Future."""
    def calcul_long(duree, nom):
        time.sleep(duree)
        return f"{nom}: terminé après {duree}s"
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        f1 = executor.submit(calcul_long, 0.3, "Tâche 1")
        f2 = executor.submit(calcul_long, 0.1, "Tâche 2")
        
        print(f"Tâche 2 terminée: {f2.result()}")
        print(f"Tâche 1 terminée: {f1.result()}")


def exercice_18_13():
    """as_completed."""
    def tache(nom, duree):
        time.sleep(duree)
        return nom
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(tache, "A", 0.3),
            executor.submit(tache, "B", 0.1),
            executor.submit(tache, "C", 0.2),
        ]
        
        for future in as_completed(futures):
            print(f"Terminé: {future.result()}")


def exercice_18_14():
    """Callback."""
    def tache():
        time.sleep(0.2)
        return "Résultat"
    
    def callback(future):
        print(f"Callback: {future.result()} a terminé")
    
    with ThreadPoolExecutor() as executor:
        future = executor.submit(tache)
        future.add_done_callback(callback)
        resultat = future.result()
        print(f"Résultat: {resultat}")


def exercice_18_15():
    """Thread dans classe."""
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
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=telechargeur.telecharger, args=(f"fichier{i}.mp4", 0.2))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Fichiers téléchargés: {telechargeur.lister_fichiers()}")
