# Chapitre 7: Dictionnaires et Sets

## Ce que vous allez apprendre

- Créer et manipuler des dictionnaires
- Créer et utiliser des sets (ensembles)
- Méthodes de dictionnaires
- Méthodes de sets
- Opérations sur les sets (union, intersection, différence)
- Compréhensions de dictionnaires
- Fusion et mise à jour de dictionnaires

---

## 1. Les Dictionnaires

### Création de Dictionnaires

```python
# Dictionnaire vide
vide = {}

# Dictionnaire avec paires clé-valeur
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Toutes les clés sont des chaînes (ici)
# Mais les clés peuvent être de nombreux types!

# Création avec dict()
coordonnees = dict(x=10, y=20, z=30)
# {'x': 10, 'y': 20, 'z': 30}

# Depuis une liste de tuples
paires = [("a", 1), ("b", 2), ("c", 3)]
dict(paires)  # {'a': 1, 'b': 2, 'c': 3}
```

### Accès aux Éléments

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}

# Accès par clé (KeyError si absent!)
print(personne["nom"])      # "Alice"
print(personne["age"])      # 25

# get() - retourne None ou une valeur par défaut
print(personne.get("nom"))           # "Alice"
print(personne.get("pays"))         # None
print(personne.get("pays", "France"))  # "France"

# Vérification de clé
if "nom" in personne:
    print("Clé 'nom' existe")

# Toutes les clés
print(personne.keys())   # dict_keys(['nom', 'age', 'ville'])

# Toutes les valeurs
print(personne.values())  # dict_values(['Alice', 25, 'Paris'])

# Toutes les paires
print(personne.items())   # dict_items([('nom', 'Alice'), ...])
```

---

## 2. Modification de Dictionnaires

### Ajout et Modification

```python
personne = {"nom": "Alice", "age": 25}

# Ajout d'une nouvelle paire
personne["ville"] = "Paris"
# {"nom": "Alice", "age": 25, "ville": "Paris"}

# Modification
personne["age"] = 26

# update() - fusion avec un autre dictionnaire
personne.update({"profession": "Ingénieur", "age": 27})

# setdefault() - ajoute si absent
personne.setdefault("pays", "France")
personne.setdefault("nom", "Bob")  # Ne change pas (clé existe)
```

### Suppression

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}

# pop() - supprime et retourne la valeur
nom = personne.pop("nom")   # "Alice"
# {'age': 25, 'ville': 'Paris'}

# popitem() - supprime et retourne la dernière paire
cle, valeur = personne.popitem()  # ('ville', 'Paris')

# del - suppression directe
del personne["age"]

# clear() - vide le dictionnaire
personne.clear()  # {}
```

---

## 3. Les Sets (Ensembles)

### Création de Sets

```python
# Set vide
vide = set()  # {} crée un dict, pas un set!

# Set avec éléments
couleurs = {"rouge", "vert", "bleu"}
nombres = {1, 2, 3, 4, 5}

# Set depuis une liste (supprime les doublons)
liste = [1, 2, 2, 3, 3, 3]
unique = set(liste)  # {1, 2, 3}

# set() avec compréhension
carres = {x ** 2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

### Caractéristiques des Sets

```python
# Pas de doublons
s = {1, 2, 2, 3, 3, 3}
print(s)  # {1, 2, 3}

# Pas d'ordre garanti
print({"a", "b", "c"})  # Peut afficher dans n'importe quel ordre!

# Pas d'indexation ni de slicing
# s[0]  # TypeError!

# Les éléments doivent être hachable (hashable)
# int, str, tuple, frozenset sont hashables
# list, dict, set ne sont PAS hashables
```

---

## 4. Opérations sur les Sets

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (tous les éléments)
print(A | B)      # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (éléments communs)
print(A & B)           # {4, 5}
print(A.intersection(B))  # {4, 5}

# Différence (dans A mais pas dans B)
print(A - B)           # {1, 2, 3}
print(A.difference(B)) # {1, 2, 3}

# Différence symétrique (dans A ou B, pas les deux)
print(A ^ B)               # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}

# Sous-ensemble et sur-ensemble
print(A <= B)   # False (A n'est pas sous-ensemble de B)
print(A < B)    # False (A n'est pas sous-ensemble strict de B)
print(A >= B)   # False
```

---

## 5. Méthodes de Sets

```python
s = {1, 2, 3, 4, 5}

# Ajouter des éléments
s.add(6)        # {1, 2, 3, 4, 5, 6}
s.update([7, 8, 9])  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Supprimer des éléments
s.remove(9)     # KeyError si absent!
s.discard(9)    # Pas d'erreur si absent
s.pop()         # Supprime et retourne un élément arbitraire
s.clear()       # Vide le set

# Vérifications
print(1 in s)    # True
print(len(s))    # Nombre d'éléments
```

---

## 6. Compréhensions de Dictionnaires

```python
# Création classique
carres = {}
for x in range(5):
    carres[x] = x ** 2
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Avec compréhension
carres = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Avec condition
pairs = {x: "pair" if x % 2 == 0 else "impair" for x in range(5)}
# {0: 'pair', 1: 'impair', 2: 'pair', 3: 'impair', 4: 'pair'}
```

---

## 7. Fusion de Dictionnaires (Python 3.9+)

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"a": 10, "e": 5}

# Fusion avec | (Python 3.9+)
fusion = d1 | d2
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Mise à jour avec |=
d1 |= d2  # d1 devient d1 + d2
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# En cas de clés doublons
fusion_avec_doublons = d1 | d3
# Les valeurs de d3 écrasent celles de d1
# {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

---

## 8. Cas d'Usage Courants

### Compteur avec Dictionnaire

```python
from collections import Counter

mots = ["pomme", "banane", "pomme", "orange", "pomme"]
compteur = Counter(mots)
print(compteur)  # Counter({'pomme': 3, 'banane': 1, 'orange': 1})
```

### Groupement de Données

```python
from collections import defaultdict

# Grouper par première lettre
mots = ["pomme", "abricot", "banane", "cerise"]
par_lettre = defaultdict(list)
for mot in mots:
    par_lettre[mot[0]].append(mot)

print(dict(par_lettre))
# {'a': ['pomme', 'abricot'], 'b': ['banane'], 'c': ['cerise']}
```

### Ensemble de Valeurs Uniques

```python
# Supprimer les doublons tout en conservant l'ordre
def dedoublonner_ordre(sequence):
    vu = set()
    resultat = []
    for elem in sequence:
        if elem not in vu:
            vu.add(elem)
            resultat.append(elem)
    return resultat

print(dedoublonner_ordre([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
```

---

## Points Clés à Retenir

| Concept | Dictionnaires | Sets |
|---------|--------------|------|
| Création | `{}` ou `dict()` | `set()` |
| Accès | `d[key]` ou `d.get(key)` | `in set` |
| Ajout | `d[key] = value` ou `d.update()` | `add()` |
| Suppression | `pop()`, `del`, `clear()` | `remove()`, `discard()`, `pop()` |
| Clés uniques | ✅ Oui | N/A (les éléments sont uniques) |
| Ordre | Python 3.7+: garanti | Non garanti |
| Hachable | Les clés doivent l'être | Les éléments doivent l'être |

---

## Erreurs Courantes

```python
# ERREUR: {} crée un dict, pas un set!
s = {}      # C'est un dict vide!
s = set()   # CORRECT pour un set vide

# ERREUR: Essayer d'indexer un dict avec le mauvais type
d = {"a": 1}
d[0]      # KeyError (pas "a")

# ERREUR: Modifier un set pendant l'itération
s = {1, 2, 3}
for elem in s:
    s.add(elem + 10)  # RuntimeError!

# CORRECT: Itérer sur une copie
s = {1, 2, 3}
for elem in list(s):
    s.add(elem + 10)

# ERREUR: Utiliser des clés non-hachables
d = {[1, 2]: "test"}  # TypeError!
# Les clés doivent être: int, str, tuple, frozenset
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous apprendrez à créer des **fonctions** pour organiser et réutiliser votre code.
