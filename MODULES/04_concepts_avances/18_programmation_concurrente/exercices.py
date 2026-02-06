# =============================================================================
# CHAPITRE 18: PROGRAMMATION CONCURRENTE - EXERCICES
# =============================================================================

# =============================================================================
# EXERCICE 18.1 - THREAD SIMPLE
# =============================================================================
def exercice_18_1():
    """Créer et lancer un thread simple."""
    import threading
    import time
    
    def dire_bonjour():
        time.sleep(0.5)
        print("Bonjour depuis le thread!")
    
    t = threading.Thread(target=dire_bonjour)
    t.start()
    t.join()


# =============================================================================
# EXERCICE 18.2 - PLUSIEURS THREADS
# =============================================================================
def exercice_18_2():
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


# =============================================================================
# EXERCICE 18.3 - COMPTEUR SÉCURISÉ
# =============================================================================
def exercice_18_3():
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


# =============================================================================
# EXERCICE 18.4 - THREADPOOLEXECUTOR
# =============================================================================
def exercice_18_4():
    """Utiliser ThreadPoolExecutor."""
    from concurrent.futures import ThreadPoolExecutor
    import time
    
    def carre(n):
        time.sleep(0.1)
        return n * n
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        resultats = list(executor.map(carre, [1, 2, 3, 4, 5]))
    
    print(f"Résultats: {resultats}")


# =============================================================================
# EXERCICE 18.5 - LOCK AVEC RACE CONDITION
# =============================================================================
def exercice_18_5():
    """Montrer le problème du race condition."""
    import threading
    
    compteur = 0
    
    def incrementer_sans_lock():
        nonlocal compteur
        for _ in range(10000):
            compteur += 1
    
    threads = [threading.Thread(target=incrementer_sans_lock) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"Compteur sans lock: {compteur} (devrait être 40000)")


# =============================================================================
# EXERCICE 18.6 - QUEUE PRODUCTEUR CONSOMMATEUR
# =============================================================================
def exercice_18_6():
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


# =============================================================================
# EXERCICE 18.7 - THREAD LOCAL
# =============================================================================
def exercice_18_7():
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


# =============================================================================
# EXERCICE 18.8 - BARRIER
# =============================================================================
def exercice_18_8():
    """Utiliser Barrier pour synchroniser des threads."""
    import threading
    import time
    
    barrier = threading.Barrier(3)
    
    def phase1():
        print("Phase 1 début")
        time.sleep(0.1)
        print("Phase 1 fin, en attente...")
        barrier.wait()
        print("Phase 1 terminée")
    
    threads = [threading.Thread(target=phase1) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# =============================================================================
# EXERCICE 18.9 - EVENT THREADS
# =============================================================================
def exercice_18_9():
    """Utiliser Event pour communiquer entre threads."""
    import threading
    import time
    
    event = threading.Event()
    
    def attendent_levent():
        print("En attente de l'event...")
        event.wait()
        print("Event reçu! Continuation...")
    
    def declenche_levent():
        time.sleep(1)
        print("Déclenchement de l'event!")
        event.set()
    
    t1 = threading.Thread(target=attendent_levent)
    t2 = threading.Thread(target=declenche_levent)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


# =============================================================================
# EXERCICE 18.10 - TIMER THREAD
# =============================================================================
def exercice_18_10():
    """Utiliser Timer pour exécuter du code après un délai."""
    import threading
    import time
    
    print("Démarrage du timer...")
    
    def message_differe():
        print("Ce message apparaît après 0.5 secondes!")
    
    timer = threading.Timer(0.5, message_differe)
    timer.start()
    timer.join()


# =============================================================================
# EXERCICE 18.11 - SEMAPHORE
# =============================================================================
def exercice_18_11():
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


# =============================================================================
# EXERCICE 18.12 - CALLABLE FUTURE
# =============================================================================
def exercice_18_12():
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


# =============================================================================
# EXERCICE 18.13 - AS COMPLETE
# =============================================================================
def exercice_18_13():
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


# =============================================================================
# EXERCICE 18.14 - THREADpooL AVEC CALLBACK
# =============================================================================
def exercice_18_14():
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


# =============================================================================
# EXERCICE 18.15 - THREADING DANS CLASSE
# =============================================================================
def exercice_18_15():
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


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 18: PROGRAMMATION CONCURRENTE")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Exercice 18.{i} ---")
        try:
            eval(f"exercice_18_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
