# Chapitre 8 : Les Fonctions - Organiser et Réutiliser ton Code

## Introduction : Pourquoi les fonctions ?

Imagine que tu écris une recette de gâteau. Si tu dois écrire "préchauffer le four à 180°C" à chaque fois que tu fais un gâteau, ce serait fastidieux ! Au lieu de ça, tu écris cette instruction une fois, et tu y fais référence quand tu en as besoin.

Les **fonctions** en programmation fonctionnent exactement de la même manière :
- Tu écris un bloc de code **une seule fois**
- Tu lui donnes un **nom**
- Tu peux l'**appeler** autant de fois que tu veux
- Tu peux le **réutiliser** dans différents programmes

**Les avantages des fonctions :**
1. **Évite la répétition** - Plus besoin de copier-coller le même code
2. **Organise le code** - Chaque fonction fait une chose précise
3. **Facilite la maintenance** - Un bug se corrige à un seul endroit
4. **Rend le code lisible** - Un nom de fonction explique ce qu'elle fait

---

## 1. Définir une fonction

### La syntaxe de base

```python
def nom_de_la_fonction():
    """Description de ce que fait la fonction (docstring)."""
    # Code de la fonction
    instruction1
    instruction2
```

**Exemple simple :**

```python
def dire_bonjour():
    """Affiche un message de bienvenue."""
    print("Bonjour le monde !")
    print("Bienvenue dans Python")

# Appeler la fonction
dire_bonjour()
dire_bonjour()  # On peut l'appeler autant de fois qu'on veut
```

**Résultat :**
```
Bonjour le monde !
Bienvenue dans Python
Bonjour le monde !
Bienvenue dans Python
```

### Les règles de nommage

| Bon | Mauvais | Explication |
|-----|---------|-------------|
| `calculer_moyenne` | `calculerMoyenne` | snake_case en Python |
| `verifier_email` | `verifierEmail` | Pas de camelCase |
| `trouver_max` | `trouver max` | Pas d'espaces |
| `valider_age` | `validerAge` | Tout en minuscule avec underscores |
| `obtenir_donnees` | `obtenirDonnees` | Convention Python |

**Conseil** : Choisis des noms qui décrivent **ce que fait** la fonction (verbe) et pas **comment** elle le fait.

---

## 2. Les paramètres et arguments

### Paramètres simples

Les **paramètres** sont des variables que la fonction attend pour travailler.

```python
def saluer(nom):
    """Salue une personne par son nom."""
    print(f"Bonjour {nom} !")

# Appel avec un argument
saluer("Alice")    # Bonjour Alice !
saluer("Bob")      # Bonjour Bob !
saluer("Marie")    # Bonjour Marie !
```

**Terminologie :**
- **Paramètre** : La variable dans la définition (`nom`)
- **Argument** : La valeur passée lors de l'appel (`"Alice"`)

### Plusieurs paramètres

```python
def presenter(nom, age, ville):
    """Presente une personne avec ses informations."""
    print(f"Je m'appelle {nom}")
    print(f"J'ai {age} ans")
    print(f"J'habite à {ville}")

# Appel avec plusieurs arguments
presenter("Alice", 25, "Paris")
```

**Résultat :**
```
Je m'appelle Alice
J'ai 25 ans
J'habite à Paris
```

### Ordre des arguments

Les arguments sont assignés aux paramètres dans l'ordre :

```python
def calculer_prix(produit, prix, quantite):
    total = prix * quantite
    print(f"{quantite} x {produit} = {total}€")

# Ordre important !
calculer_prix("Pommes", 2.5, 10)    # 10 x Pommes = 25.0€
```

**⚠️ Erreur fréquente :**
```python
calculer_prix(10, "Pommes", 2.5)    # Erreur logique !
```

### Arguments nommés (keyword arguments)

Pour éviter les erreurs d'ordre, utilise les arguments nommés :

```python
def creer_utilisateur(nom, email, age):
    print(f"Utilisateur : {nom}")
    print(f"Email : {email}")
    print(f"Age : {age}")

# Avec arguments nommes, l'ordre n'a pas d'importance
creer_utilisateur(
    age=25,
    nom="Alice",
    email="alice@email.com"
)
```

**Avantages :**
- Plus lisible
- Ordre flexible
- Auto-documenté

---

## 3. Les valeurs de retour (return)

### Retourner une valeur simple

Une fonction peut **retourner** un résultat avec `return` :

```python
def additionner(a, b):
    """Additionne deux nombres et retourne le resultat."""
    resultat = a + b
    return resultat

# Stocker le resultat dans une variable
somme = additionner(5, 3)
print(somme)           # 8

# Utiliser directement le resultat
print(additionner(10, 20))  # 30
```

**Important** : Dès qu'un `return` est exécuté, la fonction s'arrête immédiatement !

```python
def fonction_test():
    print("Avant return")
    return "fini"
    print("Apres return")  # Jamais execute !

resultat = fonction_test()  # Affiche : Avant return
print(resultat)             # fini
```

### Retourner plusieurs valeurs

Python permet de retourner plusieurs valeurs en les séparant par des virgules :

```python
def calculer_stats(nombres):
    """Calcule plusieurs statistiques."""
    minimum = min(nombres)
    maximum = max(nombres)
    moyenne = sum(nombres) / len(nombres)
    
    return minimum, maximum, moyenne

# Recuperer plusieurs valeurs
min_val, max_val, moyenne = calculer_stats([10, 20, 30, 40, 50])
print(f"Min : {min_val}, Max : {max_val}, Moyenne : {moyenne}")
```

**En réalité**, Python retourne un **tuple** :

```python
resultat = calculer_stats([1, 2, 3])
print(type(resultat))  # <class 'tuple'>
print(resultat)        # (1, 3, 2.0)
```

### Fonction sans retour explicite

Si une fonction n'a pas de `return`, elle retourne `None` :

```python
def afficher_message(message):
    print(message)
    # Pas de return

resultat = afficher_message("Hello")
print(resultat)  # None
```

---

## 4. Les paramètres par défaut

### Valeurs par défaut simples

Tu peux donner une valeur par défaut aux paramètres :

```python
def saluer(nom, message="Bonjour"):
    """Salue avec un message personnalisable."""
    print(f"{message}, {nom} !")

# Sans preciser le message
saluer("Alice")              # Bonjour, Alice !

# Avec un message personnalise
saluer("Bob", "Salut")       # Salut, Bob !
saluer("Marie", "Hello")     # Hello, Marie !
```

### Plusieurs valeurs par défaut

```python
def creer_profil(nom, age=18, ville="Inconnue", actif=True):
    """Cree un profil utilisateur avec valeurs par defaut."""
    print(f"Nom : {nom}")
    print(f"Age : {age}")
    print(f"Ville : {ville}")
    print(f"Actif : {actif}")
    print("-" * 30)

# Differents appels possibles
creer_profil("Alice")                                    # Valeurs par defaut
creer_profil("Bob", 25)                                  # Age specifie
creer_profil("Marie", ville="Lyon")                      # Argument nomme
creer_profil("Jean", 30, "Paris", False)                 # Tous specifies
```

### ⚠️ Piège des valeurs par défaut mutables

**ERREUR CLASSIQUE** à éviter absolument :

```python
# MAUVAIS - Ne fais jamais ca !
def ajouter_element(element, liste=[]):
    liste.append(element)
    return liste

# Premier appel
resultat1 = ajouter_element(1)
print(resultat1)  # [1]

# Deuxieme appel - Surprise !
resultat2 = ajouter_element(2)
print(resultat2)  # [1, 2] - La liste est partagee !
```

**Pourquoi ?** Les valeurs par défaut sont créées **une seule fois** quand Python lit la fonction, pas à chaque appel !

**SOLUTION CORRECTE :**

```python
# CORRECT - Utilise None comme valeur par defaut
def ajouter_element(element, liste=None):
    if liste is None:
        liste = []  # Cree une nouvelle liste a chaque appel
    liste.append(element)
    return liste

# Maintenant chaque appel est independant
resultat1 = ajouter_element(1)
resultat2 = ajouter_element(2)
print(resultat1)  # [1]
print(resultat2)  # [2]
```

---

## 5. Nombre variable d'arguments

### Arguments positionnels variables (*args)

Quand tu ne sais pas combien d'arguments seront passés :

```python
def calculer_somme(*nombres):
    """Additionne tous les nombres passes en argument."""
    total = 0
    for nombre in nombres:
        total += nombre
    return total

# Appels avec differents nombres d'arguments
print(calculer_somme(1, 2, 3))      # 6
print(calculer_somme(10, 20))       # 30
print(calculer_somme())             # 0
print(calculer_somme(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
```

**Comment ça marche ?**
- `*nombres` rassemble tous les arguments dans un **tuple**
- Tu peux l'appeler comme tu veux (`*args` est la convention)

```python
def afficher_infos(*args):
    print(f"Nombre d'arguments : {len(args)}")
    print(f"Arguments : {args}")
    print(f"Type : {type(args)}")  # <class 'tuple'>

afficher_infos(1, 2, 3, "hello", True)
```

### Arguments nommés variables (**kwargs)

Pour un nombre variable d'arguments nommés :

```python
def creer_profil_complet(nom, **infos):
    """Cree un profil avec informations variables."""
    print(f"Profil de {nom}")
    print("-" * 30)
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")

# Appel avec differents arguments
creer_profil_complet(
    "Alice",
    age=25,
    ville="Paris",
    email="alice@email.com",
    hobbies=["lecture", "sport"]
)
```

**Comment ça marche ?**
- `**infos` rassemble tous les arguments nommés dans un **dictionnaire**
- Tu peux l'appeler comme tu veux (`**kwargs` est la convention)

### Combiner *args et **kwargs

```python
def fonction_complete(requis, *args, nom="defaut", **kwargs):
    """Exemple avec tous les types de parametres."""
    print(f"Requis : {requis}")
    print(f"Args : {args}")
    print(f"Nom : {nom}")
    print(f"Kwargs : {kwargs}")

# Exemple d'appel
fonction_complete(
    "valeur_obligatoire",           # requis
    1, 2, 3,                        # *args
    nom="personnalise",             # nom
    age=25, ville="Paris"           # **kwargs
)
```

**Ordre obligatoire :**
1. Paramètres normaux
2. Paramètres avec valeur par défaut
3. `*args`
4. `**kwargs`

---

## 6. La portée des variables (scope)

### Variables locales vs globales

```python
# Variable globale (accessible partout)
message_global = "Je suis global"

def ma_fonction():
    # Variable locale (accessible seulement dans la fonction)
    message_local = "Je suis local"
    print(message_local)      # OK
    print(message_global)     # OK - peut lire les globales

ma_fonction()
print(message_global)         # OK
# print(message_local)        # ERREUR ! Variable non definie
```

### Modifier une variable globale

Pour modifier une variable globale à l'intérieur d'une fonction :

```python
compteur = 0

def incrementer():
    global compteur  # Declare qu'on utilise la variable globale
    compteur += 1
    print(f"Compteur : {compteur}")

incrementer()  # Compteur : 1
incrementer()  # Compteur : 2
print(f"Valeur finale : {compteur}")  # 2
```

**⚠️ À éviter** : L'utilisation abusive de `global` rend le code difficile à comprendre. Préfère passer les variables en paramètre et retourner les résultats.

### Fonctions imbriquées et nonlocal

```python
def fonction_externe():
    x = 10  # Variable de l'environnement externe
    
    def fonction_interne():
        nonlocal x  # Modifie la variable de la fonction externe
        x = 20
        print(f"Interne : x = {x}")
    
    fonction_interne()
    print(f"Externe : x = {x}")

fonction_externe()
```

**Résultat :**
```
Interne : x = 20
Externe : x = 20
```

---

## 7. Fonctions lambda (fonctions anonymes)

### Syntaxe rapide

Les fonctions lambda sont des fonctions courtes sans nom :

```python
# Fonction normale
def carre(x):
    return x ** 2

# Equivalent en lambda
carre_lambda = lambda x: x ** 2

print(carre(5))         # 25
print(carre_lambda(5))  # 25
```

**Syntaxe :**
```python
lambda arguments: expression
```

### Cas d'usage courants

**1. Avec sorted() pour une clé personnalisée :**

```python
produits = [
    ("Pommes", 2.5),
    ("Bananes", 1.8),
    ("Oranges", 3.0)
]

# Trier par prix (deuxieme element)
trie = sorted(produits, key=lambda x: x[1])
print(trie)
# [('Bananes', 1.8), ('Pommes', 2.5), ('Oranges', 3.0)]

# Trier par nom (premier element)
trie = sorted(produits, key=lambda x: x[0])
print(trie)
```

**2. Avec map() pour transformer une liste :**

```python
nombres = [1, 2, 3, 4, 5]

# Doubler chaque nombre
doubles = list(map(lambda x: x * 2, nombres))
print(doubles)  # [2, 4, 6, 8, 10]

# Mettre au carre
carres = list(map(lambda x: x ** 2, nombres))
print(carres)   # [1, 4, 9, 16, 25]
```

**3. Avec filter() pour filtrer :**

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Garder seulement les pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4, 6, 8, 10]

# Garder seulement les superieurs a 5
grands = list(filter(lambda x: x > 5, nombres))
print(grands)  # [6, 7, 8, 9, 10]
```

### Limitations des lambda

Les fonctions lambda ne peuvent contenir qu'une seule expression. Pour du code complexe, utilise une fonction normale :

```python
# Lambda - OK pour simple
triple = lambda x: x * 3

# Fonction normale - necessaire pour complexe
def calcul_complexe(x):
    if x < 0:
        return 0
    elif x > 100:
        return 100
    else:
        return x ** 2
```

---

## 8. Documentation des fonctions (docstrings)

### Écrire une bonne docstring

```python
def calculer_moyenne(notes, coefficents=None):
    """
    Calcule la moyenne ponderee d'une liste de notes.
    
    Parameters
    ----------
    notes : list[float]
        Liste des notes sur 20
    coefficents : list[float], optional
        Liste des coefficients associés aux notes.
        Si None, tous les coefficients valent 1.
    
    Returns
    -------
    float
        La moyenne calculee sur 20
    
    Raises
    ------
    ValueError
        Si la liste de notes est vide
    
    Examples
    --------
    >>> calculer_moyenne([15, 12, 18])
    15.0
    >>> calculer_moyenne([15, 12], [2, 1])
    14.0
    """
    if not notes:
        raise ValueError("La liste de notes ne peut pas etre vide")
    
    if coefficents is None:
        return sum(notes) / len(notes)
    
    if len(notes) != len(coefficents):
        raise ValueError("Les listes doivent avoir la meme longueur")
    
    total = sum(note * coef for note, coef in zip(notes, coefficents))
    total_coef = sum(coefficents)
    return total / total_coef
```

### Accéder à la documentation

```python
# Voir la docstring
print(calculer_moyenne.__doc__)

# Voir le nom de la fonction
print(calculer_moyenne.__name__)

# Aide interactive
help(calculer_moyenne)
```

---

## 9. Fonctions récursives

Une fonction peut s'appeler elle-même : c'est la **récursivité**.

### Exemple : Factorielle

```python
def factorielle(n):
    """
    Calcule n! (factorielle de n).
    n! = n * (n-1) * (n-2) * ... * 1
    """
    # Cas de base
    if n <= 1:
        return 1
    
    # Cas recursif
    return n * factorielle(n - 1)

# Test
print(factorielle(5))   # 120 (5 * 4 * 3 * 2 * 1)
print(factorielle(3))   # 6
print(factorielle(0))   # 1
```

**Comment ça marche ?**
```
factorielle(5)
→ 5 * factorielle(4)
→ 5 * (4 * factorielle(3))
→ 5 * (4 * (3 * factorielle(2)))
→ 5 * (4 * (3 * (2 * factorielle(1))))
→ 5 * (4 * (3 * (2 * 1)))
→ 120
```

### Exemple : Suite de Fibonacci

```python
def fibonacci(n):
    """Retourne le n-ieme nombre de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Affiche les 10 premiers
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

**⚠️ Attention** : La récursivité peut être lente et consommer beaucoup de mémoire. Pour de grandes valeurs, utilise une boucle ou la mémorisation.

---

## 10. Fonctions d'ordre supérieur

Les fonctions qui prennent d'autres fonctions comme paramètre ou retournent des fonctions.

### Prendre une fonction en paramètre

```python
def appliquer_operation(nombres, operation):
    """Applique une operation a tous les nombres."""
    resultats = []
    for nombre in nombres:
        resultats.append(operation(nombre))
    return resultats

# Fonctions a passer
def doubler(x):
    return x * 2

def carre(x):
    return x ** 2

nombres = [1, 2, 3, 4, 5]

print(appliquer_operation(nombres, doubler))  # [2, 4, 6, 8, 10]
print(appliquer_operation(nombres, carre))    # [1, 4, 9, 16, 25]
```

### Retourner une fonction

```python
def creer_multiplicateur(facteur):
    """Cree une fonction qui multiplie par un facteur donne."""
    def multiplicateur(nombre):
        return nombre * facteur
    return multiplicateur

# Creer des fonctions specifiques
doubler = creer_multiplicateur(2)
tripler = creer_multiplicateur(3)

print(doubler(5))   # 10
print(tripler(5))   # 15
print(doubler(10))  # 20
```

---

## 11. Arguments Position-Only et Keyword-Only

Python permet de contrôler précisément comment les arguments doivent être passés.

### Arguments Position-Only (avant `/`)

Ces arguments **doivent** être passés par position, pas par nom.

```python
def diviser(a, b, /):
    """
    Divise a par b.
    Les arguments doivent être passés par position.
    """
    return a / b

# ✅ OK - Par position
diviser(10, 2)      # 5.0

# ❌ ERREUR - Par nom interdit
diviser(a=10, b=2)  # TypeError!
```

**Pourquoi utiliser ?**
- API claire : pas besoin de se souvenir des noms
- Performance légèrement meilleure
- Évite les conflits si tu ajoutes des paramètres plus tard

### Arguments Keyword-Only (après `*`)

Ces arguments **doivent** être passés par nom explicite.

```python
def configurer(*, host, port, debug=False):
    """
    Configure une connexion.
    host et port doivent être nommés explicitement.
    """
    print(f"Connexion à {host}:{port}")
    if debug:
        print("Mode debug activé")

# ✅ OK - Par nom explicite
configurer(host="localhost", port=8080)
configurer(host="api.example.com", port=443, debug=True)

# ❌ ERREUR - Par position interdit
configurer("localhost", 8080)  # TypeError!
```

**Pourquoi utiliser ?**
- Code plus lisible : `send_email(to="...", subject="...")` vs `send_email("...", "...")`
- Évite les erreurs d'ordre des arguments
- Documentation auto-explicative

### Combiner les deux

```python
def fonction_mixte(a, b, /, c, d, *, e, f):
    """
    a, b : position-only (avant /)
    c, d : position ou keyword (entre / et *)
    e, f : keyword-only (après *)
    """
    return a + b + c + d + e + f

# ✅ Utilisation correcte
resultat = fonction_mixte(1, 2, 3, 4, e=5, f=6)      # 21
resultat = fonction_mixte(1, 2, c=3, d=4, e=5, f=6) # 21

# ❌ Incorrect
def fonction_mixte(a=1, b=2, c=3)  # e et f manquent
```

### Exemple Pratique : API REST

```python
def appel_api(endpoint, /, methode="GET", timeout=30, *, auth_token, retry=True):
    """
    Appelle une API.
    
    Args:
        endpoint: URL de l'API (position-only)
        methode: GET, POST, etc. (position ou keyword)
        timeout: Temps d'attente (position ou keyword)
        auth_token: Token d'authentification (keyword-only, obligatoire)
        retry: Réessayer en cas d'échec (keyword-only)
    """
    print(f"Appel {methode} sur {endpoint}")
    print(f"Token: {auth_token}")
    # ...

# ✅ Clair et explicite
appel_api("/users", auth_token="abc123")
appel_api("/users", methode="POST", auth_token="abc123", retry=False)

# ❌ auth_token doit être explicite
appel_api("/users", "GET", 30, "abc123")  # ERREUR!
```

---

## Résumé des concepts clés

| Concept | Syntaxe | Explication |
|---------|---------|-------------|
| Définition | `def nom():` | Créer une fonction |
| Paramètre | `def f(param):` | Variable attendue |
| Argument | `f(valeur)` | Valeur passée |
| Retour | `return valeur` | Renvoyer un résultat |
| Valeur par défaut | `def f(p="val"):` | Valeur si non précisé |
| Args variables | `*args` | Tuple d'arguments |
| Kwargs variables | `**kwargs` | Dictionnaire d'arguments |
| Position-only | `def f(a, /)` | Argument par position uniquement |
| Keyword-only | `def f(*, a)` | Argument par nom uniquement |
| Variable globale | `global x` | Modifier une variable globale |
| Fonction lambda | `lambda x: x*2` | Fonction courte anonyme |
| Documentation | `"""doc"""` | Décrire la fonction |

---

## Erreurs courantes à éviter

### 1. Confondre print et return

```python
# MAUVAIS - N'utilise pas le resultat
def addition(a, b):
    print(a + b)  # Affiche mais ne retourne rien

resultat = addition(2, 3)  # resultat vaut None
print(resultat * 2)        # Erreur !

# CORRECT
def addition(a, b):
    return a + b  # Retourne le resultat

resultat = addition(2, 3)  # resultat vaut 5
print(resultat * 2)        # 10
```

### 2. Oublier de retourner dans toutes les branches

```python
# MAUVAIS - Certains cas ne retournent rien
def maximum(a, b):
    if a > b:
        return a
    # Que se passe-t-il si a <= b ?

print(maximum(5, 3))  # 5
print(maximum(3, 5))  # None !

# CORRECT
def maximum(a, b):
    if a > b:
        return a
    else:
        return b  # N'oublie jamais un cas
```

### 3. Modifier une liste par défaut

```python
# MAUVAIS - Revoir la section 4.3
def ajouter(element, liste=[]):
    liste.append(element)
    return liste

# CORRECT
def ajouter(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste
```

### 4. Appeler une fonction au lieu de la référencer

```python
def ma_fonction():
    return 42

# MAUVAIS - Appelle la fonction immédiatement
resultat = ma_fonction()  # resultat vaut 42

# Quand on veut passer la fonction comme argument
map(ma_fonction(), [1, 2, 3])  # Erreur !

# CORRECT - Passe la reference
def executer(fonction):
    return fonction()

executer(ma_fonction)  # OK - passe la fonction
```

---

## Exercices pratiques

### Exercice 1 : Fonction de conversion
Crée une fonction `convertir_temperature(valeur, unite_source, unite_cible)` qui convertit entre Celsius, Fahrenheit et Kelvin.

### Exercice 2 : Validation d'email
Crée une fonction `valider_email(email)` qui retourne True si l'email semble valide (contient @ et .), False sinon.

### Exercice 3 : Statistiques
Crée une fonction `statistiques(*nombres)` qui retourne un dictionnaire avec min, max, moyenne et médiane.

### Exercice 4 : Générateur de palindromes
Crée une fonction `est_palindrome(texte)` qui vérifie si un texte est un palindrome (se lit pareil dans les deux sens).

### Exercice 5 : Calculatrice avec *args
Crée une fonction `calculer(operation, *nombres)` qui effectue l'opération demandée (+, -, *, /) sur tous les nombres.

### Exercice 6 : Fonction récursive
Crée une fonction récursive `compter_voyelles(texte)` qui compte le nombre de voyelles dans un texte.

---

## Prochain Chapitre

Maintenant que tu maîtrises les fonctions, tu es prêt pour le **Chapitre 09 : Modules et Packages**. Tu apprendras comment organiser ton code en fichiers séparés et créer des bibliothèques réutilisables !

Tu découvriras comment importer des fonctions d'autres fichiers, créer tes propres packages, et gérer les dépendances avec pip.

---

*Les fonctions sont le cœur de la programmation modulaire. Plus tu en écriras, plus ton code deviendra élégant et facile à maintenir !*
