# Chapitre 17 : La Concurrence - Faire Plusieurs Choses en Même Temps

## Introduction : Pourquoi la concurrence ?

Imagine que tu doives préparer un repas complet. Tu peux :
- Faire bouillir l'eau (10 minutes)
- Préparer les légumes (5 minutes)
- Cuire la viande (15 minutes)

**Approche séquentielle** : Tu fais tout l'un après l'autre. Temps total : 30 minutes.

**Approche concurrente** : Tu fais bouillir l'eau, et pendant que l'eau bout, tu prepared les légumes. Temps total : 15 minutes !

La programmation concurrente fonctionne exactement comme ça : certaines tâches peuvent se dérouler en même temps au lieu de l'une après l'autre.

---

## 1. Le Problème du Temps d'Attente

### Pourquoi attendre inutilement ?

Quand ton programme fait une requête réseau ou lit un gros fichier, il "attend" que l'opération finisse. Pendant ce temps, il ne fait rien d'autre !

```python
# Exemple : Ton programme qui télécharge des fichiers
import time

def telecharger_fichier(nom, duree):
    print(f"Début du téléchargement de {nom}...")
    time.sleep(duree)  # Simule le temps de téléchargement
    print(f"Fin de {nom} !")

# Téléchargement séquentiel - lent !
telecharger_fichier("fichier1.mp4", 2)
telecharger_fichier("fichier2.mp4", 2)
telecharger_fichier("fichier3.mp4", 2)
# Temps total : 6 secondes
```

Pendant ces 6 secondes, ton programme est bloqué ! Il ne peut rien faire d'autre.

---

## 2. Les Threads - L'Idée de Base

### Qu'est-ce qu'un thread ?

Un **thread** (fil d'exécution) est comme un worker supplémentaire qui peut exécuter du code en parallèle.

```python
import threading
import time

def telecharger_fichier(nom, duree):
    print(f"Début de {nom}...")
    time.sleep(duree)
    print(f"Fin de {nom} !")

# Créer 3 threads
t1 = threading.Thread(target=telecharger_fichier, args=("fichier1.mp4", 2))
t2 = threading.Thread(target=telecharger_fichier, args=("fichier2.mp4", 2))
t3 = threading.Thread(target=telecharger_fichier, args=("fichier3.mp4", 2))

# Démarrer les threads
t1.start()
t2.start()
t3.start()

# Attendre que tous finissent
t1.join()
t2.join()
t3.join()

print("Tous les téléchargements sont terminés !")
```

**Résultat :** Les 3 fichiers se téléchargent **en même temps** ! Temps total : ~2 secondes au lieu de 6.

### Comment ça marche ?

| Sans threads | Avec threads |
|--------------|-------------|
| Tâche 1: 2 sec | Tâche 1: 2 sec |
| Tâche 2: 2 sec | Tâche 2: 2 sec |
| Tâche 3: 2 sec | Tâche 3: 2 sec |
| **Total: 6 sec** | **Total: ~2 sec** |

---

## 3. Les Thread Locals - Données Propres à Chaque Thread

Parfois, chaque thread a besoin de ses propres données. Les **ThreadLocals** permettent cela !

```python
import threading

# Une variable locale au thread
donnees_locales = threading.local()

def traiter_requete(utilisateur):
    # Chaque thread a sa propre copie de "connexion"
    if not hasattr(donnees_locales, "connexion"):
        print(f"Thread {threading.current_thread().name}: Création d'une nouvelle connexion")
        donnees_locales.connexion = f"Connexion pour {utilisateur}"
    else:
        print(f"Thread {threading.current_thread().name}: Réutilisation de la connexion")
    
    print(f"Traitement de {utilisateur} avec {donnees_locales.connexion}")

# Lancer plusieurs threads
threads = []
for user in ["Alice", "Bob", "Charlie"]:
    t = threading.Thread(target=traiter_requete, args=(user,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

Chaque thread a sa propre "connexion" sans interference avec les autres !

---

## 4. Les Verrous (Locks) - Éviter les Conflits

### Le problème de la données partagée

Quand plusieurs threads accedent à la même variable en même temps, des problèmes peuvent survenir !

```python
import threading

compteur = 0

def incrementer():
    global compteur
    for _ in range(100000):
        compteur += 1  # PAS SÛR !!

# 4 threads incrémentent le compteur
threads = [threading.Thread(target=incrementer) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Compteur final: {compteur}")
```

**Problème :** Le résultat devrait être 400000, mais tu auras probablement un nombre différent (ex: 378421) ! Pourquoi ?

### La solution : Le verrou (Lock)

Un verrou est comme un barrière : quand un thread passe, les autres doivent attendre.

```python
import threading

compteur = 0
lock = threading.Lock()

def incrementer_securise():
    global compteur
    for _ in range(100000):
        with lock:  # Un seul thread à la fois !
            compteur += 1

threads = [threading.Thread(target=incrementer_securise) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Compteur final: {compteur}")  # Toujours 400000 !
```

---

## 5. Les Thread Pools - Récupérer des Résultats

Parfois, les threads doivent retourner des résultats. Les **ThreadPoolExecutor** facilitent cela !

```python
from concurrent.futures import ThreadPoolExecutor
import time

def calculer_carre(n):
    time.sleep(0.5)  # Simule un calcul long
    return n ** 2

# Créer un pool de 3 workers
with ThreadPoolExecutor(max_workers=3) as executor:
    # Soumettre plusieurs tâches
    resultats = executor.map(calculer_carre, [1, 2, 3, 4, 5])
    
    # Récupérer les résultats
    for resultat in resultats:
        print(f"Résultat: {resultat}")
```

**Avantages du ThreadPoolExecutor :**
- Pas besoin de créer/joindre les threads manuellement
- Gestion automatique des workers
- Récupération facile des résultats

---

## 6. Le GIL (Global Interpreter Lock) - Une Limite de Python

### Pourquoi Python ne peut pas vraiment être parallèle ?

Python utilise un verrou appelé **GIL** qui empêche deux threads Python de s'exécuter simultanément. Cela peut sembler un problème, mais...

### Le GIL en images

```
Thread 1: [Prend le GIL] → [Travaille] → [Libère le GIL] → [Attend]
Thread 2:                [Prend le GIL] → [Travaille] → [Libère le GIL]
```

**Le GIL ne pose PAS de problème pour :**
- Les tâches liées aux entrées/sorties (réseau, fichiers)
- Les opérations qui passent leur temps à attendre

**Le GIL EST un problème pour :**
- Les calculs intensifs (maths, traitement d'images)

### La solution : multiprocessing

Le **multiprocessing** contourne le GIL en utilisant plusieurs processus au lieu de plusieurs threads.

```python
from concurrent.futures import ProcessPoolExecutor
import time

def calculer_carre(n):
    return n ** 2

# Utilise des processus au lieu de threads
with ProcessPoolExecutor(max_workers=4) as executor:
    resultats = list(executor.map(calculer_carre, range(100)))

print("Calculs terminés !")
```

---

## 7. Les Queues - Communication entre Threads

Parfois, les threads doivent s'envoyer des messages. Les **Queues** sont parfaites pour ça !

```python
import threading
import queue
import time

# Une file d'attente partagée
file = queue.Queue()

def consommateur():
    """Récupère et traite les messages."""
    while True:
        message = file.get()  # Bloque jusqu'à qu'un message arrive
        print(f"Reçu: {message}")
        if message == "FIN":
            break

def producteur():
    """Envoie des messages."""
    for i in range(5):
        file.put(f"Message {i}")
        time.sleep(0.5)
    file.put("FIN")

# Démarrer le consommateur
t_consommateur = threading.Thread(target=consommateur)
t_consommateur.start()

# Envoyer des messages
producteur()
t_consommateur.join()
```

---

## 8. Exemple Complet : Téléchargeur Multi-fichiers

Voici un exemple pratique qui combine plusieurs concepts :

```python
import threading
import queue
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class Telechargement:
    url: str
    nom_fichier: str

# Résultats des téléchargements
resultats = []
resultats_lock = threading.Lock()

def telecharger(telechargement):
    """Télécharge un fichier et retourne le résultat."""
    try:
        response = requests.get(telechargement.url, timeout=10)
        if response.status_code == 200:
            return (telechargement.nom_fichier, True, len(response.content))
        return (telechargement.nom_fichier, False, 0)
    except Exception as e:
        return (telechargement.nom_fichier, False, str(e))

# Liste des fichiers à télécharger
telechargements = [
    Telechargement("https://example.com/f1.txt", "fichier1.txt"),
    Telechargement("https://example.com/f2.txt", "fichier2.txt"),
    Telechargement("https://example.com/f3.txt", "fichier3.txt"),
]

# Utiliser ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(telecharger, t) for t in telechargements]
    
    for future in futures:
        resultat = future.result()
        print(f"[{resultat[0]}] - Succès: {resultat[1]}, Taille: {resultat[2]} octets")
```

---

## Résumé des Concepts

| Concept | À quoi ça sert | Exemple |
|---------|----------------|---------|
| `threading.Thread` | Créer un nouveau thread | `t = Thread(target=fonction)` |
| `start()` | Lancer un thread | `t.start()` |
| `join()` | Attendre la fin d'un thread | `t.join()` |
| `Lock` | Protéger une ressource partagée | `with lock:` |
| `ThreadPoolExecutor` | Pool de threads gérés | `with ThreadPoolExecutor() as e:` |
| `ProcessPoolExecutor` | Pool de processus (sans GIL) | `with ProcessPoolExecutor() as e:` |
| `Queue` | Communication entre threads | `q.get()`, `q.put()` |

---

## Quand Utiliser la Concurrence ?

### Utilise les threads pour :
- Requêtes réseau (API, téléchargements)
- Lecture/écriture de fichiers
- Interfaces graphiques (ne pas bloquer l'affichage)
- Opérations qui passent leur temps à attendre

### Utilise le multiprocessing pour :
- Calculs mathématiques intensifs
- Traitement d'images
- Analyse de données lourdes
- Machine learning

---

## Erreurs Courantes

### 1. Oublier de verrouiller les données partagées

```python
# MAUVAIS - Données corrompues possibles !
compteur = 0
def incrementer():
    global compteur
    for _ in range(100000):
        compteur += 1  # ERREUR ! Pas de protection

# CORRECT - Avec verrou
lock = threading.Lock()
def incrementer_securise():
    global compteur
    for _ in range(100000):
        with lock:
            compteur += 1
```

### 2. Créer trop de threads

```python
# MAUVAIS - 1000 threads pour 1000 tâches !
for i in range(1000):
    t = threading.Thread(target=une_tache)
    t.start()

# CORRECT - Limiter le nombre de threads
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(une_tache, range(1000))
```

### 3. Bloquer indéfiniement

```python
# MAUVAIS - Le thread attend pour toujours !
def tache():
    queue.get()  # Bloque sans timeout
    queue.task_done()

# CORRECT - Avec timeout
def tache_securisee():
    try:
        queue.get(timeout=5)
    except queue.Empty:
        print("Timeout atteint")
    queue.task_done()
```

---

## Exemples Pratiques

### Exercice 1 : Compteur Sécurisé
Crée un compteur partagé incrémenté par 4 threads, avec un verrou pour garantir le résultat correct.

### Exercice 2 : Téléchargeur de Photos
Télécharge plusieurs images depuis URLs en parallèle et affiche la progression.

### Exercice 3 : Producteur-Consommateur
Crée un système où des threads "producteurs" ajoutent des nombres dans une file, et des threads "consommateurs" les traitent.

### Exercice 4 : Pool de Connexions
Simule un pool de connexions à une base de données avec limite de 5 connexions actives.

---

## Prochain Chapitre

Dans le chapitre suivant, tu découvriras le **Type Hinting** (annotation de types). C'est une fonctionnalité Python qui permet de documenter clairement les types attendus dans ton code, facilitant la maintenance et permettant aux outils de détecter des erreurs avant l'exécution !

---

*La concurrence est un concept puissant mais complexe. Commence par des exemples simples et progresse vers des architectures plus complexes !*
