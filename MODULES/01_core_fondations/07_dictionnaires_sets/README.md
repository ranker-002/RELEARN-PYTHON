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

## 2. Les sets (ensemble)

Un set est une collection **sans ordre** et **sans doublons**. C'est comme un sac de billes : chaque élément est unique et l'ordre n'a pas d'importance.

### Créer un set

```python
# Créer un set
fruits = {"pomme", "banane", "orange"}
print(fruits)  # {"pomme", "banane", "orange"} (ordre peut varier)

# Créer depuis une liste (supprime les doublons)
nombres = [1, 2, 2, 3, 3, 3]
uniques = set(nombres)  # {1, 2, 3}
```

### Les opérations sur les sets

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union (tout)
print(set1 | set2)    # {1, 2, 3, 4}
print(set1.union(set2))

# Intersection (commun)
print(set1 & set2)    # {2, 3}
print(set1.intersection(set2))

# Différence (dans set1 mais pas set2)
print(set1 - set2)    # {1}
```

---

## Résumé

| Type | Ordre | Doublons | Usage |
|------|-------|----------|-------|
| Liste | Oui | Oui | Séquence ordonnée |
| Tuple | Oui | Oui | Données fixes |
| Dict | Non* | Clés uniques | Paires clé-valeur |
| Set | Non | Non | Éléments uniques |

*Les dictionnaires Python 3.7+ gardent l'ordre d'insertion.

---

## Exercices

1. Crée un dictionnaire avec des informations sur toi
2. Trouve les éléments communs entre deux sets
