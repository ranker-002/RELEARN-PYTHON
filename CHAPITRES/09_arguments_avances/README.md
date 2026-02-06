# Chapitre 9: Arguments Avancés

## Ce que vous allez apprendre

- Arguments variables (*args)
- Arguments nommés (**kwargs)
- Combinaison de *args et **kwargs
- Arguments positionnels-only (/)
- Arguments keyword-only (*)
- Décorateurs de base
-Ordre des paramètres

---

## 1. Arguments Variables (*args)

### Utilisation de *args

```python
# *args capture tous les arguments positionnels en tuple
def somme(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

# Appels valides
somme(1, 2, 3)           # 6
somme(1, 2, 3, 4, 5)     # 15
somme()                   # 0

# *args avec d'autres paramètres
def presenter(prenom, *autres_noms):
    print(f"Premier: {prenom}")
    print(f"Autres: {autres_noms}")

presenter("Alice", "Bob", "Charlie")
# Premier: Alice
# Autres: ('Bob', 'Charlie')
```

---

## 2. Arguments Nommés (**kwargs)

### Utilisation de **kwargs

```python
# **kwargs capture tous les arguments nommés en dictionnaire
def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

# Appels valides
afficher_infos(nom="Alice", age=25, ville="Paris")
# nom: Alice
# age: 25
# ville: Paris

afficher_infos()  # Ne affiche rien (dictionnaire vide)
```

### Exemple Pratique

```python
def creer_utilisateur(**donnees):
    utilisateur = {
        "username": donnees.get("username", "anonyme"),
        "email": donnees.get("email", None),
        "role": donnees.get("role", "utilisateur")
    }
    return utilisateur

print(creer_utilisateur(username="alice", email="alice@email.com"))
# {'username': 'alice', 'email': 'alice@email.com', 'role': 'utilisateur'}
```

---

## 3. Combinaison *args et **kwargs

### Ordre des Paramètres

```python
# Ordre: params, *args, default_params, **kwargs
def fonction_complete(a, b, *args, cle=valeur_par_defaut, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"cle={cle}")
    print(f"kwargs={kwargs}")

# Appel
fonction_complete(1, 2, 3, 4, 5, cle="modifiee", x=10, y=20)
# a=1, b=2
# args=(3, 4, 5)
# cle=modifiee
# kwargs={'x': 10, 'y': 20}
```

### Exemple de Wrapper

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        resultat = func(*args, **kwargs)
        print(f"Résultat: {resultat}")
        return resultat
    return wrapper

@logger
def additionner(a, b):
    return a + b

additionner(5, 3)
# Appel de additionner
# Args: (5, 3)
# Kwargs: {}
# Résultat: 8
```

---

## 4. Arguments Positional-Only (/)

### Syntaxe

```python
def diviser(a, b, /):
    return a / b

diviser(10, 2)   # OK
# diviser(a=10, b=2)  # TypeError!

def presenter(nom, /, age):
    return f"{nom}, {age} ans"

presenter("Alice", 25)    # OK
presenter(nom="Alice", 25)  # TypeError!
```

### Cas d'Usage

```python
# Cas 1: Les paramètres n'ont pas de sens en tant que mots-clés
def creer_point(x, y, z, /):
    return (x, y, z)

# Cas 2: API claire et explicite
def creer_utilisateur(nom, /, email, role="utilisateur"):
    return {"nom": nom, "email": email, "role": role}
```

---

## 5. Arguments Keyword-Only (*)

### Syntaxe

```python
def afficher(*, message, sep=" "):
    print(sep.join(map(str, message)))

# Doit utiliser des mots-clés
afficher(message=[1, 2, 3])      # OK: "1 2 3"
# afficher([1, 2, 3])            # TypeError!

def calculer(a, b, *, puissance=1):
    return (a + b) ** puissance

calculer(2, 3)            # 5
calculer(2, 3, puissance=2)  # 25
# calculer(2, 3, 2)            # TypeError!
```

### Combinaison Complète

```python
# Ordre: positional-only, normal, * (keyword-only), **kwargs
def fonction_complete(
    pos_only,      # Positionnel uniquement
    /,             # Séparateur
    standard,      # Normal
    *args,         # Variables positionnelles
    kw_only,       # Keyword uniquement
    **kwargs       # Variables nommées
):
    print(f"pos_only={pos_only}")
    print(f"standard={standard}")
    print(f"args={args}")
    print(f"kw_only={kw_only}")
    print(f"kwargs={kwargs}")

# Appel
fonction_complete(1, 2, 3, 4, kw_only="test", extra=5)
# pos_only=1
# standard=2
# args=(3, 4)
# kw_only=test
# kwargs={'extra': 5}
```

---

## 6. Décorateurs de Base

### Qu'est-ce qu'un Décorateur?

```python
# Un décorateur est une fonction qui modifie une autre fonction

def mon_decorateur(func):
    def wrapper(*args, **kwargs):
        print("Avant l'appel")
        resultat = func(*args, **kwargs)
        print("Après l'appel")
        return resultat
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour!")

dire_bonjour()
# Avant l'appel
# Bonjour!
# Après l'appel
```

### Décorateurs Utiles

```python
# Decorateur pour mesurer le temps
import time

def timer(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        temps = time.time() - debut
        print(f"{func.__name__}: {temps:.4f}s")
        return resultat
    return wrapper

@timer
def calculer_lent():
    time.sleep(0.5)
    return "Terminé"

calculer_lent()
# calculer_lent: 0.5002s
```

---

## 7. Args/Kwargs avec Appel de Fonction

### Déballage d'Arguments

```python
def presenter(a, b, c):
    print(f"a={a}, b={b}, c={c}")

# Déballer une liste/tuple avec *
params = [1, 2, 3]
presenter(*params)  # Identique à presenter(1, 2, 3)

# Déballer un dictionnaire avec **
options = {"a": 10, "b": 20, "c": 30}
presenter(**options)  # Identique à presenter(a=10, b=20, c=30)

# Combinaison
def configurer(serveur, port, ssl=True):
    print(f"Serveur: {serveur}, Port: {port}, SSL: {ssl}")

config_serveur = {"serveur": "localhost", "port": 8080}
configurer(**config_serveur, ssl=False)
```

---

## 8. Cas d'Usage Pratiques

### Fonction Flexible

```python
def creer_requete(method="GET", url="/", **kwargs):
    requete = {
        "method": method,
        "url": url,
        "headers": kwargs.get("headers", {}),
        "body": kwargs.get("body", None)
    }
    return requete

# Différentes façons d'appeler
requete1 = creer_requete()
requete2 = creer_requete(url="/api/users", headers={"Auth": "token"})
requete3 = creer_requete("POST", "/api/data", body={"key": "value"})
```

### Logger avec Niveaux

```python
def log(niveau, message, **kwargs):
    timestamp = kwargs.get("timestamp", True)
    format_json = kwargs.get("json", False)
    
    if timestamp:
        import datetime
        message = f"[{datetime.datetime.now()}] {message}"
    
    if format_json:
        import json
        print(json.dumps({"niveau": niveau, "message": message}))
    else:
        print(f"{niveau}: {message}")

log("INFO", "Application démarrée")
log("ERROR", "Erreur critique", json=True)
```

---

## Points Clés à Retenir

| Syntaxe | Usage |
|---------|-------|
| `*args` | Arguments positionnels variables |
| `**kwargs` | Arguments nommés variables |
| `/` | Fin des arguments positionnels-only |
| `*` | Début des arguments keyword-only |
| `def f(*, x):` | x doit être nommé |
| `def f(**kwargs):` | Dictionnaire des arguments nommés |
| `func(*args)` | Déballer liste/tuple |
| `func(**d)` | Déballer dictionnaire |

---

## Erreurs Courantes

```python
# ERREUR: Confondre l'ordre
def func(a, *args, b, **kwargs):  # OK
def func(a, b=1, *args):          # OK
# def func(a, *args, b=1):         # ERREUR! *args mange tout

# ERREUR: Appeler sans déballer
params = [1, 2, 3]
# func(params)                     # Passe une liste comme un argument!

# CORRECT: Déballer
func(*params)

# ERREUR: Mélanger / et *
# def func(pos, /, *, kw):         # ERREUR!
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez les **modules et packages** pour organiser votre code en fichiers séparés.
