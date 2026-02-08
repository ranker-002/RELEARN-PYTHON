# Chapitre 16 : Décorateurs et Générateurs - Du Code Plus Pythonique

## Introduction : Pourquoi ces concepts avancés ?

Imagine que tu écris une recette de cuisine. Au lieu de répéter "préchauffer le four à 180°C" à chaque étape, tu écris cette instruction une fois en haut de la recette et toutes les étapes qui suivent en bénéficient automatiquement.

Les **décorateurs** et **générateurs** sont des outils Python qui permettent d'écrire du code plus élégant, plus efficace et plus facile à maintenir. Ils peuvent sembler complexes au premier abord, mais une fois compris, ils deviennent indispensables.

**À la fin de ce chapitre, tu sauras :**
- Créer des décorateurs pour enrichir tes fonctions
- Utiliser les générateurs pour traiter des grandes quantités de données
- Comprendre quand utiliser ces outils pour un code plus performant

---

## Partie 1 : Les Décorateurs

### 1.1 Qu'est-ce qu'un décorateur ?

Un **décorateur** est une fonction qui prend une autre fonction en paramètre, lui ajoute des fonctionnalités, et retourne cette fonction "améliorée".

C'est comme ajouter une enveloppe autour d'une lettre : la lettre reste la même, mais elle est maintenant protégée et a plus de valeur.

### 1.2 Comprendre les fonctions comme objets

Avant de comprendre les décorateurs, il faut savoir qu'en Python, les fonctions sont des **objets** comme les autres. Tu peux :
- Les stocker dans des variables
- Les passer comme arguments
- Les retourner depuis d'autres fonctions

```python
def dire_bonjour():
    return "Bonjour !"

# Une fonction est un objet
print(type(dire_bonjour))  # <class 'function'>

# On peut la stocker dans une variable
ma_fonction = dire_bonjour
print(ma_fonction())  # Bonjour !

# On peut la passer à une autre fonction
def executer(fonction):
    return fonction()

print(executer(dire_bonjour))  # Bonjour !
```

### 1.3 Ton premier décorateur simple

```python
def mon_decorateur(fonction):
    """Un décorateur simple qui ajoute un message avant et après."""
    def wrapper():
        print("Avant l'execution...")
        resultat = fonction()
        print("Apres l'execution...")
        return resultat
    return wrapper

def dire_bonjour():
    print("Bonjour le monde !")

# Application manuelle du decorateur
dire_bonjour_decore = mon_decorateur(dire_bonjour)
dire_bonjour_decore()
```

**Résultat :**
```
Avant l'execution...
Bonjour le monde !
Apres l'execution...
```

### 1.4 La syntaxe @ (syntactic sugar)

Python propose une syntaxe plus élégante avec le symbole `@` :

```python
def mon_decorateur(fonction):
    def wrapper():
        print("=== DEBUT ===")
        resultat = fonction()
        print("=== FIN ===")
        return resultat
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

# Maintenant, dire_bonjour est deja decoree
dire_bonjour()
```

**Résultat :**
```
=== DEBUT ===
Bonjour !
=== FIN ===
```

C'est exactement équivalent à `dire_bonjour = mon_decorateur(dire_bonjour)`, mais beaucoup plus lisible !

### 1.5 Gérer les arguments avec *args et **kwargs

Les décorateurs doivent fonctionner avec n'importe quelle fonction, quels que soient ses arguments.

```python
def mon_decorateur(fonction):
    """Un decorateur universel qui gere tous les arguments."""
    def wrapper(*args, **kwargs):
        print(f"Arguments recus : {args}, {kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"Resultat : {resultat}")
        return resultat
    return wrapper

@mon_decorateur
def addition(a, b):
    return a + b

@mon_decorateur
def saluer(nom, message="Bonjour"):
    return f"{message}, {nom} !"

# Test avec differents arguments
addition(5, 3)
saluer("Alice")
saluer("Bob", message="Salut")
```

### 1.6 Préserver les métadonnées avec @functools.wraps

Quand tu crées un décorateur, la fonction décorée perd ses informations (nom, docstring, etc.). Utilise `@wraps` pour les conserver :

```python
from functools import wraps

def mon_decorateur(fonction):
    @wraps(fonction)  # Preserve les metadonnees
    def wrapper(*args, **kwargs):
        """Ceci est la docstring du wrapper."""
        print("Execution en cours...")
        return fonction(*args, **kwargs)
    return wrapper

@mon_decorateur
def ma_fonction():
    """Ceci est la docstring originale."""
    pass

# Sans @wraps, on verrait la docstring du wrapper
print(ma_fonction.__name__)       # ma_fonction (et pas wrapper)
print(ma_fonction.__doc__)        # Ceci est la docstring originale
```

**Sans `@wraps`**, `ma_fonction.__name__` afficherait "wrapper" au lieu de "ma_fonction".

### 1.7 Décorateurs pratiques : chronométrage

```python
import time
from functools import wraps

def chronometrer(fonction):
    """Mesure le temps d'execution d'une fonction."""
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"{fonction.__name__} a pris {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@chronometrer
def calcul_long():
    """Simule un calcul qui prend du temps."""
    total = 0
    for i in range(1000000):
        total += i
    return total

resultat = calcul_long()
```

### 1.8 Décorateurs pratiques : logger

```python
from functools import wraps

def logger(fonction):
    """Enregistre les appels de fonction."""
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Appel de {fonction.__name__}")
        print(f"      Args : {args}")
        print(f"      Kwargs : {kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"[LOG] Resultat : {resultat}")
        return resultat
    return wrapper

@logger
def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b

diviser(10, 2)
```

### 1.9 Décorateurs pratiques : validation des arguments

```python
from functools import wraps

def valider_types(**types_attendus):
    """Verifie que les arguments ont les bons types."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            # Verifier les arguments positionnels
            noms_params = list(fonction.__code__.co_varnames)
            for i, arg in enumerate(args):
                if i < len(noms_params):
                    nom = noms_params[i]
                    if nom in types_attendus and not isinstance(arg, types_attendus[nom]):
                        raise TypeError(f"{nom} doit etre de type {types_attendus[nom].__name__}")
            
            # Verifier les arguments nommes
            for nom, valeur in kwargs.items():
                if nom in types_attendus and not isinstance(valeur, types_attendus[nom]):
                    raise TypeError(f"{nom} doit etre de type {types_attendus[nom].__name__}")
            
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur

@valider_types(age=int, nom=str)
def creer_utilisateur(nom, age):
    return {"nom": nom, "age": age}

# Fonctionne
creer_utilisateur("Alice", 25)

# Leve une erreur
try:
    creer_utilisateur("Bob", "trente")
except TypeError as e:
    print(f"Erreur : {e}")
```

### 1.10 Décorateurs avec paramètres

Parfois, tu veux passer des arguments au décorateur lui-même :

```python
from functools import wraps

def repeter(nombre_fois):
    """Execute la fonction plusieurs fois."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            resultats = []
            for _ in range(nombre_fois):
                resultat = fonction(*args, **kwargs)
                resultats.append(resultat)
            return resultats
        return wrapper
    return decorateur

@repeter(3)
def dire_coucou():
    print("Coucou !")
    return "fait"

# Execute dire_coucou() 3 fois
dire_coucou()
```

**Résultat :**
```
Coucou !
Coucou !
Coucou !
```

### 1.11 Empiler les décorateurs

Tu peux appliquer plusieurs décorateurs à une même fonction. Ils s'appliquent de **bas en haut** :

```python
@decorateur_haut
def ma_fonction():
    pass

# Est equivalent a :
ma_fonction = decorateur_haut(ma_fonction)
```

```python
from functools import wraps

def majuscules(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        resultat = fonction(*args, **kwargs)
        return resultat.upper()
    return wrapper

def ajouter_exclamation(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        resultat = fonction(*args, **kwargs)
        return resultat + " !!!"
    return wrapper

@majuscules
@ajouter_exclamation
def saluer():
    return "bonjour"

print(saluer())  # BONJOUR !!!

# Ordre d'execution :
# 1. ajouter_exclamation(saluer) -> "bonjour !!!"
# 2. majuscules(resultat) -> "BONJOUR !!!"
```

### 1.12 Décorateurs de classe

Tu peux aussi décorer des méthodes de classe :

```python
from functools import wraps

def methode_statique(fonction):
    """Simule @staticmethod pour comprendre."""
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper

class Calculatrice:
    @staticmethod
    def addition(a, b):
        return a + b
    
    @classmethod
    def info(cls):
        return f"Je suis une {cls.__name__}"

# Utilisation
print(Calculatrice.addition(5, 3))  # 8
print(Calculatrice.info())          # Je suis une Calculatrice
```

### 1.13 Cas d'usage réels des décorateurs

**1. Authentification :**
```python
def require_login(fonction):
    @wraps(fonction)
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("Connexion requise")
        return fonction(user, *args, **kwargs)
    return wrapper

@require_login
def voir_profil(user):
    return user.profile
```

**2. Cache simple (mémorisation) :**
```python
def memoize(fonction):
    cache = {}
    @wraps(fonction)
    def wrapper(*args):
        if args not in cache:
            cache[args] = fonction(*args)
        return cache[args]
    return wrapper

@memoize
def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

# Calcul rapide car resultats mis en cache
print(factorielle(100))
print(factorielle(100))  # Instantane !
```

**3. Retry sur erreur :**
```python
import time

def retry(max_tentatives=3, delai=1):
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            for tentative in range(max_tentatives):
                try:
                    return fonction(*args, **kwargs)
                except Exception as e:
                    if tentative == max_tentatives - 1:
                        raise
                    print(f"Tentative {tentative + 1} echouee, retry dans {delai}s...")
                    time.sleep(delai)
        return wrapper
    return decorateur

@retry(max_tentatives=3, delai=2)
def appel_api_risque():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Erreur reseau")
    return "Succes !"

# Essaie jusqu'a 3 fois avant d'abandonner
appel_api_risque()
```

---

## Partie 2 : Les Générateurs

### 2.1 Le problème des listes en mémoire

Quand tu traites une grande quantité de données, créer une liste complète peut consommer beaucoup de mémoire :

```python
# Probleme : cree une liste de 10 millions de nombres en memoire
nombres = list(range(10000000))
carres = [x**2 for x in nombres]  # Consomme beaucoup de RAM
```

Les **générateurs** permettent de générer les valeurs **une par une**, à la demande, sans tout stocker en mémoire.

### 2.2 Créer un générateur avec yield

Un générateur est une fonction qui utilise `yield` au lieu de `return`. À chaque appel, il reprend là où il s'était arrêté.

```python
def compteur_simple(maximum):
    """Un generateur simple qui compte."""
    compteur = 0
    while compteur < maximum:
        yield compteur
        compteur += 1

# Utilisation
for nombre in compteur_simple(5):
    print(nombre)
```

**Résultat :**
```
0
1
2
3
4
```

**Comment ça marche ?**
1. Premier appel : exécute jusqu'à `yield 0`, retourne 0, se met en pause
2. Deuxième appel : reprend après `yield`, incrémente, yield 1, pause
3. Et ainsi de suite jusqu'à la fin

### 2.3 Différence entre return et yield

```python
def fonction_avec_return():
    """Retourne tout d'un coup."""
    resultats = []
    for i in range(3):
        resultats.append(i)
    return resultats  # Retourne [0, 1, 2]

def fonction_avec_yield():
    """Retourne un a la fois."""
    for i in range(3):
        yield i  # Retourne 0, puis 1, puis 2

# Test
print(fonction_avec_return())  # [0, 1, 2]

# Le generateur est un objet iterateur
gen = fonction_avec_yield()
print(type(gen))  # <class 'generator'>

# On peut iterer dessus
for valeur in gen:
    print(valeur)
```

### 2.4 Générateur de la suite de Fibonacci

```python
def fibonacci(n):
    """Genere les n premiers nombres de Fibonacci."""
    a, b = 0, 1
    compteur = 0
    while compteur < n:
        yield a
        a, b = b, a + b
        compteur += 1

# Utilisation
print("Suite de Fibonacci :")
for nombre in fibonacci(10):
    print(nombre, end=" ")
# Resultat : 0 1 1 2 3 5 8 13 21 34
```

**Avantage** : Calcule chaque nombre à la demande, sans stocker toute la liste.

### 2.5 Générateur infini

Un générateur peut produire des valeurs indéfiniment (avec précaution !) :

```python
def compteur_infini(debut=0):
    """Compte a l'infini."""
    compteur = debut
    while True:
        yield compteur
        compteur += 1

# Utilisation avec break pour eviter la boucle infinie
compteur = compteur_infini(100)
for _ in range(5):
    print(next(compteur))
```

**Résultat :**
```
100
101
102
103
104
```

### 2.6 La fonction next()

Tu peux demander explicitement la prochaine valeur avec `next()` :

```python
def generateur_lettres():
    yield "A"
    yield "B"
    yield "C"

mon_gen = generateur_lettres()

print(next(mon_gen))  # A
print(next(mon_gen))  # B
print(next(mon_gen))  # C

# Quand il n'y a plus de valeurs :
try:
    print(next(mon_gen))  # StopIteration exception
except StopIteration:
    print("Le generateur est epuise !")
```

### 2.7 Envoyer des valeurs dans un générateur avec send()

Les générateurs peuvent recevoir des valeurs avec `send()` :

```python
def generateur_interactif():
    """Un generateur qui recoit des valeurs."""
    print("Generateur demarre")
    valeur_recue = yield "Pret"  # Premier yield retourne "Pret"
    
    while True:
        print(f"Valeur recue : {valeur_recue}")
        if valeur_recue is None:
            break
        valeur_recue = yield f"Traitement de : {valeur_recue}"

# Utilisation
gen = generateur_interactif()
print(next(gen))           # Demarre le generateur -> "Pret"
print(gen.send("Bonjour")) # Envoie "Bonjour", recoit reponse
print(gen.send(42))        # Envoie 42, recoit reponse
gen.send(None)             # Arrete le generateur
```

### 2.8 Fermer un générateur avec close()

Tu peux forcer l'arrêt d'un générateur :

```python
def generateur_long():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Nettoyage du generateur")

gen = generateur_long()
print(next(gen))  # 1
gen.close()       # Force l'arret
# Affiche : Nettoyage du generateur
```

### 2.9 Expression génératrice (generator expression)

Comme les compréhensions de liste, mais avec des parenthèses :

```python
# Liste (tout en memoire)
carres_liste = [x**2 for x in range(1000000)]

# Generateur (un par un)
carres_gen = (x**2 for x in range(1000000))

print(type(carres_liste))  # <class 'list'>
print(type(carres_gen))    # <class 'generator'>

# Utilisation
total = sum(carres_gen)  # Calcule sans stocker tout en memoire
print(f"Somme des carres : {total}")
```

### 2.10 yield from - Déléguer à un autre générateur

Quand un générateur doit produire les valeurs d'un autre générateur :

```python
def sous_generateur():
    """Generateur simple."""
    yield 1
    yield 2
    yield 3

def generateur_principal():
    """Generateur qui delegue a un autre."""
    print("Debut")
    yield from sous_generateur()  # Delegue tout le travail
    print("Milieu")
    yield from sous_generateur()  # Peut etre appele plusieurs fois
    print("Fin")

# Utilisation
for valeur in generateur_principal():
    print(valeur)
```

**Résultat :**
```
Debut
1
2
3
Milieu
1
2
3
Fin
```

**Avantage** : Le code est plus simple et lisible.

### 2.11 Cas d'usage réels des générateurs

**1. Lecture de fichiers ligne par ligne :**
```python
def lire_fichier_ligne_par_ligne(chemin):
    """Lit un fichier sans le charger entierement en memoire."""
    with open(chemin, 'r', encoding='utf-8') as f:
        for ligne in f:
            yield ligne.strip()

# Traite un fichier de 10GB comme s'il faisait 1KB
for ligne in lire_fichier_ligne_par_ligne("gros_fichier.txt"):
    if "important" in ligne:
        print(ligne)
```

**2. Pagination d'API :**
```python
def recuperer_tous_les_utilisateurs(api_client):
    """Recupere tous les utilisateurs page par page."""
    page = 1
    while True:
        utilisateurs = api_client.get_users(page=page, limit=100)
        if not utilisateurs:
            break
        for user in utilisateurs:
            yield user
        page += 1

# Utilisation simple, meme s'il y a 10000 utilisateurs
for user in recuperer_tous_les_utilisateurs(api):
    traiter_utilisateur(user)
```

**3. Pipeline de traitement de données :**
```python
def lire_donnees(source):
    """Etape 1 : Lecture"""
    for item in source:
        yield item

def filtrer_donnees(source, condition):
    """Etape 2 : Filtrage"""
    for item in source:
        if condition(item):
            yield item

def transformer_donnees(source, fonction):
    """Etape 3 : Transformation"""
    for item in source:
        yield fonction(item)

# Pipeline complet
donnees = range(1000000)
pipeline = transformer_donnees(
    filtrer_donnees(
        lire_donnees(donnees),
        lambda x: x % 2 == 0
    ),
    lambda x: x ** 2
)

# Execution paresseuse - aucune donnee n'est chargee en memoire
total = sum(pipeline)
print(f"Total : {total}")
```

### 2.12 Comparaison performance : Liste vs Générateur

```python
import time
import sys

# Avec une liste
def traitement_avec_liste(n):
    """Cree une liste complete en memoire."""
    nombres = [x**2 for x in range(n)]
    return sum(nombres)

# Avec un generateur
def traitement_avec_generateur(n):
    """Genere les valeurs une par une."""
    nombres = (x**2 for x in range(n))
    return sum(nombres)

n = 10000000

# Test memoire
liste = [x**2 for x in range(n)]
gen = (x**2 for x in range(n))

print(f"Taille liste : {sys.getsizeof(liste)} octets")
print(f"Taille generateur : {sys.getsizeof(gen)} octets")

# Test temps
debut = time.time()
traitement_avec_liste(n)
print(f"Liste : {time.time() - debut:.2f}s")

debut = time.time()
traitement_avec_generateur(n)
print(f"Generateur : {time.time() - debut:.2f}s")
```

**Résultat typique :**
```
Taille liste : 80000064 octets (76 Mo)
Taille generateur : 200 octets
Liste : 2.5s
Generateur : 2.8s
```

**Conclusion** : Le générateur utilise ~380000 fois moins de mémoire pour un temps d'exécution similaire !

---

## Résumé et Bonnes Pratiques

### Décorateurs

| Concept | Syntaxe | Usage |
|---------|---------|-------|
| Décorateur simple | `@decorateur` | Ajouter une fonctionnalité |
| Décorateur avec paramètres | `@decorateur(arg)` | Configurer le décorateur |
| Préserver les métadonnées | `@wraps(fonction)` | Garder __name__ et __doc__ |
| Empiler | `@a` puis `@b` | Appliquer plusieurs décorateurs |
| Arguments universels | `*args, **kwargs` | Fonctionner avec toutes les fonctions |

### Générateurs

| Concept | Syntaxe | Usage |
|---------|---------|-------|
| Créer un générateur | `yield valeur` | Produire des valeurs une par une |
| Expression | `(x for x in iterable)` | Syntaxe concise |
| Déléguer | `yield from autre_gen` | Chaîner des générateurs |
| Valeur suivante | `next(gen)` | Obtenir la prochaine valeur |
| Envoyer une valeur | `gen.send(valeur)` | Communiquer avec le générateur |
| Fermer | `gen.close()` | Arrêter proprement |

### Quand utiliser ?

**Utilise les décorateurs quand :**
- Tu répètes le même code avant/après plusieurs fonctions
- Tu veux ajouter du logging, du timing, de l'authentification
- Tu veux valider des arguments ou mettre en cache des résultats

**Utilise les générateurs quand :**
- Tu traites de grandes quantités de données
- Tu veux créer des séquences infinies
- Tu veux économiser de la mémoire
- Tu travailles avec des flux de données (fichiers, APIs)

---

## Erreurs Courantes à Éviter

### Décorateurs

```python
# ERREUR 1 : Oublier de retourner la fonction wrapper
def mauvais_decorateur(fonction):
    def wrapper():
        print("Avant")
        fonction()
        print("Apres")
    # Oublie : return wrapper

# ERREUR 2 : Oublier *args, **kwargs
def decorateur_inefficace(fonction):
    def wrapper():  # Ne gere pas les arguments !
        return fonction()
    return wrapper

# CORRECT
def bon_decorateur(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper

# ERREUR 3 : Oublier @wraps
def decorateur_sans_wraps(fonction):
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper  # Perd le __name__ et __doc__
```

### Générateurs

```python
# ERREUR 1 : Essayer d'iterer plusieurs fois
def mon_gen():
    yield 1
    yield 2

g = mon_gen()
print(list(g))  # [1, 2]
print(list(g))  # [] - Le generateur est epuise !

# Solution : Recreer le generateur
g = mon_gen()

# ERREUR 2 : Oublier qu'un generateur est paresseux
def traitement():
    print("Debut")
    yield 1
    print("Milieu")  # Ne s'affiche que si on demande la valeur
    yield 2
    print("Fin")

g = traitement()  # Rien ne s'affiche encore !
next(g)  # Affiche : Debut

# ERREUR 3 : Ne pas gerer StopIteration
g = (x for x in [1, 2])
print(next(g))  # 1
print(next(g))  # 2
try:
    print(next(g))  # StopIteration !
except StopIteration:
    print("Generateur vide")
```

---

## Exercices Pratiques

### Exercice 1 : Décorateur de temporisation
Crée un décorateur qui mesure le temps d'exécution et l'affiche de manière lisible (ex: "2.5 secondes").

### Exercice 2 : Décorateur de retry intelligent
Crée un décorateur qui réessaie une fonction en cas d'erreur, avec un nombre maximum de tentatives et un délai croissant entre chaque essai.

### Exercice 3 : Générateur de mots de passe
Crée un générateur qui produit des mots de passe aléatoires de longueur variable, avec options pour inclure chiffres, majuscules et caractères spéciaux.

### Exercice 4 : Pipeline de traitement
Crée trois générateurs qui se chaînent :
1. `lire_nombres(n)` : Génère les nombres de 1 à n
2. `filtrer_pairs(nombres)` : Ne garde que les nombres pairs
3. `doubler(nombres)` : Double chaque nombre

Utilise-les pour calculer la somme des doubles des nombres pairs jusqu'à 1 million.

### Exercice 5 : Décorateur de classe
Crée un décorateur `@singleton` qui garantit qu'une classe n'a qu'une seule instance.

---

## Prochain Chapitre

Maintenant que tu maîtrises les décorateurs et générateurs, tu es prêt pour le **Chapitre 17 : Programmation Concurrente**. Tu apprendras à exécuter plusieurs tâches simultanément pour des programmes plus rapides et réactifs !

Les concepts que tu viens d'apprendre te donneront une longueur d'avance pour comprendre la programmation asynchrone.

---

*Les décorateurs et générateurs sont des outils puissants qui font partie de l'âme de Python. Prends le temps de bien les comprendre - ils te serviront tous les jours !*
