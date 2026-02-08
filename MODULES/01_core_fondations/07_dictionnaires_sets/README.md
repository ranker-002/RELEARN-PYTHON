# Chapitre 7 : Dictionnaires et Sets - Les Collections Avancées

## Introduction

Les dictionnaires et les sets sont deux autres types de collections très utiles en Python.

---

## 1. Les dictionnaires (dict)

Un dictionnaire stocke des **paires clé-valeur**. C'est comme un vrai dictionnaire : tu cherches un mot (clé) pour trouver sa définition (valeur).

### Créer un dictionnaire

```python
# Dictionnaire vide
vide = {}

# Avec des données
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}
```

### Accéder et modifier

```python
personne = {"nom": "Alice", "age": 25}

# Accéder (avec les crochets)
print(personne["nom"])  # "Alice"

# Accéder (avec get, plus sûr)
print(personne.get("ville", "Inconnue"))  # "Inconnue" si la clé n'existe pas

# Modifier
personne["age"] = 26
personne["pays"] = "France"  # Ajouter une nouvelle clé

# Supprimer
del personne["ville"]
```

### Les méthodes utiles

```python
# Toutes les clés
print(personne.keys())     # ["nom", "age", "pays"]

# Toutes les valeurs
print(personne.values())    # ["Alice", 26, "France"]

# Les deux
print(personne.items())     # [("nom", "Alice"), ("age", 26), ...]

# Mettre à jour
autre = {"email": "alice@email.com"}
personne.update(autre)
```

---

## 2. Dictionnaires Imbriqués et Avancés

### Dictionnaires Imbriqués

Les dictionnaires peuvent contenir d'autres dictionnaires :

```python
# Dictionnaire complexe
bibliotheque = {
    "python": {
        "titre": "Apprendre Python",
        "auteur": "Mark Lutz",
        "annee": 2020
    },
    "javascript": {
        "titre": "JavaScript: The Good Parts",
        "auteur": "Douglas Crockford",
        "annee": 2008
    }
}

# Accéder aux données imbriquées
print(bibliotheque["python"]["titre"])
print(bibliotheque["python"]["auteur"])

# Modifier
bibliotheque["python"]["disponible"] = True
```

### Autres Méthodes Utiles

```python
personne = {"nom": "Alice", "age": 25}

# pop() - Supprime et retourne
age = personne.pop("age")
print(age)        # 25
print(personne)   # {"nom": "Alice"}

# popitem() - Supprime le dernier élément (Python 3.7+)
# (avant 3.7 : élément aléatoire)
dernier = personne.popitem()
print(dernier)    # ("nom", "Alice")

# setdefault() - Définit une valeur par défaut si clé absente
personne.setdefault("ville", "Paris")
print(personne["ville"])  # "Paris"

# Créer depuis deux listes
cles = ["a", "b", "c"]
valeurs = [1, 2, 3]
dico = dict(zip(cles, valeurs))
print(dico)  # {"a": 1, "b": 2, "c": 3}

# Créer avec fromkeys()
cles = ["nom", "age", "ville"]
defaut = "Inconnu"
dico = dict.fromkeys(cles, defaut)
print(dico)  # {"nom": "Inconnu", "age": "Inconnu", "ville": "Inconnu"}
```

### Compréhensions de Dictionnaires

Comme les listes, on peut créer des dictionnaires avec une syntaxe concise :

```python
# {clé: valeur for item in iterable}
carres = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Avec condition
pairs = {x: x*2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}

# Inverser un dictionnaire
original = {"a": 1, "b": 2, "c": 3}
inverse = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

### Fusionner des Dictionnaires

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Méthode 1 : update() (modifie dict1)
dict1.update(dict2)
print(dict1)  # {"a": 1, "b": 3, "c": 4}

# Méthode 2 : ** (dépaquetage)
dict1 = {"a": 1, "b": 2}
fusion = {**dict1, **dict2}
print(fusion)  # {"a": 1, "b": 3, "c": 4}

# Méthode 3 : | (Python 3.9+)
dict1 = {"a": 1, "b": 2}
fusion = dict1 | dict2
print(fusion)  # {"a": 1, "b": 3, "c": 4}
```

---

## 3. Les Sets (Ensembles)

Un set est une collection **sans ordre** et **sans doublons**. C'est comme un sac de billes : chaque élément est unique et l'ordre n'a pas d'importance.

### Créer un Set

```python
# Créer un set
fruits = {"pomme", "banane", "orange"}
print(fruits)  # {"pomme", "banane", "orange"} (ordre peut varier)

# Créer depuis une liste (supprime les doublons)
nombres = [1, 2, 2, 3, 3, 3]
uniques = set(nombres)  # {1, 2, 3}

# Set vide
vide = set()  # ⚠️ {} crée un dictionnaire vide !
```

### Modifier un Set

```python
fruits = {"pomme", "banane"}

# Ajouter un élément
fruits.add("orange")
fruits.add("pomme")  # Ignoré car déjà présent

# Ajouter plusieurs éléments
fruits.update(["raisin", "fraise"])

# Supprimer
fruits.remove("banane")  # Erreur si absent
fruits.discard("kiwi")   # Silencieux si absent

# Supprimer un élément aléatoire
fruit = fruits.pop()

# Vider
fruits.clear()
```

### Opérations sur les Sets

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (tout)
print(set1 | set2)              # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))

# Intersection (commun)
print(set1 & set2)              # {3, 4}
print(set1.intersection(set2))

# Différence (dans set1 mais pas set2)
print(set1 - set2)              # {1, 2}
print(set1.difference(set2))

# Différence symétrique (dans un mais pas l'autre)
print(set1 ^ set2)              # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))

# Vérifier les relations
print(set1.issubset({1, 2, 3, 4, 5}))   # True (set1 inclus dans l'autre)
print(set1.issuperset({1, 2}))           # True (set1 inclut l'autre)
print(set1.isdisjoint({5, 6, 7}))        # False (ils ont des éléments communs)
```

### Frozenset - Set Immuable

Un frozenset est comme un set mais **on ne peut pas le modifier** :

```python
# Créer un frozenset
immutable = frozenset([1, 2, 3])

# On peut l'utiliser comme clé de dictionnaire
cache = {
    frozenset([1, 2]): "valeur1",
    frozenset([3, 4]): "valeur2"
}

# Mais on ne peut pas le modifier
# immutable.add(4)  # AttributeError !
```

---

## 4. Exemples Pratiques

### Exemple 1 : Compter les Mots

```python
texte = "le chat et le chien et le lapin"
mots = texte.split()

# Compter avec un dictionnaire
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1

print(compteur)
# {"le": 3, "chat": 1, "et": 2, "chien": 1, "lapin": 1}

# Avec collections.Counter (plus simple)
from collections import Counter
compteur = Counter(mots)
print(compteur.most_common(2))  # Les 2 plus fréquents
```

### Exemple 2 : Gestion d'Inventaire

```python
class Inventaire:
    def __init__(self):
        self.items = {}
    
    def ajouter(self, item, quantite=1):
        self.items[item] = self.items.get(item, 0) + quantite
    
    def retirer(self, item, quantite=1):
        if item in self.items:
            self.items[item] -= quantite
            if self.items[item] <= 0:
                del self.items[item]
    
    def contient(self, item):
        return item in self.items
    
    def liste(self):
        return list(self.items.items())

# Utilisation
inv = Inventaire()
inv.ajouter("pomme", 5)
inv.ajouter("épée")
inv.retirer("pomme", 2)
print(inv.liste())  # [("pomme", 3), ("épée", 1)]
```

### Exemple 3 : Détecter les Doublons

```python
def a_doublons(liste):
    return len(liste) != len(set(liste))

# Ou pour trouver les doublons
def trouver_doublons(liste):
    vu = set()
    doublons = set()
    for item in liste:
        if item in vu:
            doublons.add(item)
        else:
            vu.add(item)
    return doublons

emails = ["alice@test.com", "bob@test.com", "alice@test.com", "charlie@test.com"]
print(trouver_doublons(emails))  # {"alice@test.com"}
```

---

## 5. Résumé Complet

| Type | Ordre | Doublons | Modifiable | Usage |
|------|-------|----------|------------|-------|
| **Liste** | Oui | Oui | Oui | Séquence ordonnée |
| **Tuple** | Oui | Oui | Non | Données fixes |
| **Dict** | Oui* | Clés uniques | Oui | Paires clé-valeur |
| **Set** | Non | Non | Oui | Éléments uniques |
| **Frozenset** | Non | Non | Non | Set immuable |

*Python 3.7+ conserve l'ordre d'insertion

### Méthodes Clés

**Dictionnaires :**
- `keys()`, `values()`, `items()`
- `get()`, `update()`, `pop()`, `popitem()`
- `setdefault()`, `clear()`

**Sets :**
- `add()`, `update()`, `remove()`, `discard()`, `pop()`
- `union()`, `intersection()`, `difference()`
- `issubset()`, `issuperset()`, `isdisjoint()`

---

## 6. Exercices Pratiques

### Exercice 1 : Dictionnaire de Contacts
Crée un dictionnaire de contacts avec nom, téléphone, email.
Ajoute, modifie et supprime des contacts.

### Exercice 2 : Analyse de Texte
Demande une phrase et :
- Compte la fréquence de chaque mot (utilise un dictionnaire)
- Affiche les 3 mots les plus fréquents

### Exercice 3 : Fusion de Données
Tu as deux dictionnaires de notes d'étudiants. Fusionne-les en gardant la meilleure note si un étudiant est dans les deux.

### Exercice 4 : Set Operations
Crée deux sets de tags pour des articles de blog.
Trouve les tags communs, uniques à chaque article, et tous les tags.

### Exercice 5 : Cache avec Frozenset
Crée un cache qui stocke le résultat d'opérations coûteuses. Utilise des frozensets comme clés pour des opérations sur des ensembles.

### Exercice 6 : Validation de Données
Crée une fonction qui vérifie si un dictionnaire a toutes les clés requises et si les valeurs sont du bon type.

### Exercice 7 : Groupement
Tu as une liste de personnes avec ville et nom. Groupe les personnes par ville dans un dictionnaire.

### Exercice 8 : Compréhensions Complexes
Crée avec des compréhensions :
- Un dictionnaire {lettre: code_ascii} pour les voyelles
- Un set des carrés parfaits jusqu'à 100

### Exercice 9 : Inventaire
Crée un système d'inventaire avec ajout/retrait de produits. Gère les quantités et alerte si stock critique (< 5).

### Exercice 10 : Quiz
Crée un quiz avec un dictionnaire {question: (réponse, points)}. Demande les réponses, calcule le score final.

---

## Prochain Chapitre

Tu maîtrises maintenant toutes les collections Python ! Le prochain module sur les **fonctions** va te permettre d'organiser ton code de manière professionnelle.
