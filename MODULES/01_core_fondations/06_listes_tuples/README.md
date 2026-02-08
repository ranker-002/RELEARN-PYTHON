# Chapitre 6 : Listes et Tuples - Stocker Plusieures Valeurs

## Introduction : Pourquoi les listes ?

Parfois, une seule variable ne suffit pas. Si tu veux stocker tous les noms d'une classe, plutôt que `eleve1`, `eleve2`, `eleve3`..., utilise une **liste** !

---

## 1. Les listes

### Créer une liste

```python
# Liste vide
vide = []

# Liste avec des éléments
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "orange"]
melange = [1, "texte", True, 3.14]

# Liste avec range
carres = list(range(1, 11))  # [1, 4, 9, ..., 100]
```

### Accéder aux éléments (commence à 0 !)

```python
fruits = ["pomme", "banane", "orange"]

print(fruits[0])   # "pomme" (premier élément)
print(fruits[1])   # "banane"
print(fruits[-1])  # "orange" (dernier)
print(fruits[-2])  # "banane" (avant-dernier)
```

### Modifier une liste

```python
fruits = ["pomme", "banane"]

# Ajouter un élément
fruits.append("orange")
fruits.insert(1, "raisin")  # Ajoute à l'index 1

# Supprimer un élément
fruits.remove("banane")
popped = fruits.pop()  # Supprime et retourne le dernier

# Trier
nombres = [3, 1, 4, 1, 5]
nombres.sort()
print(nombres)  # [1, 1, 3, 4, 5]
```

---

## 2. Les tuples

Les tuples sont comme des listes, mais **on ne peut pas les modifier** après création.

```python
# Créer un tuple
coordonnees = (10, 20)
seul = (42,)  # Note la virgule !

# Accéder aux éléments (comme les listes)
print(coordonnees[0])  # 10

# ERREUR ! Les tuples sont immuables
coordonnees[0] = 15  # ERREUR !
```

---

## 3. Le slicing (trancher)

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nombres[2:5])    # [2, 3, 4] (de 2 à 5, exclu)
print(nombres[:5])     # [0, 1, 2, 3, 4] (du début à 5)
print(nombres[5:])     # [5, 6, 7, 8, 9] (de 5 à la fin)
print(nombres[::2])    # [0, 2, 4, 6, 8] (tous les 2)
print(nombres[::-1])   # [9, 8, 7, ..., 0] (inversé)
```

---

## 4. Méthodes Avancées des Listes

### Informations sur la Liste

```python
fruits = ["pomme", "banane", "orange", "pomme"]

# Compter les occurrences
print(fruits.count("pomme"))   # 2

# Trouver l'index
print(fruits.index("banane"))  # 1
# print(fruits.index("raisin"))  # ValueError !

# Taille de la liste
print(len(fruits))             # 4
```

### Copier une Liste

```python
# ❌ Mauvais : copie de référence
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)
print(liste1)  # [1, 2, 3, 4] - modifié aussi !

# ✅ Bon : vraie copie
liste1 = [1, 2, 3]
liste2 = liste1.copy()  # ou list(liste1) ou liste1[:]
liste2.append(4)
print(liste1)  # [1, 2, 3]
print(liste2)  # [1, 2, 3, 4]
```

### Copie Profonde (Deep Copy)

```python
import copy

# Liste imbriquée
liste1 = [[1, 2], [3, 4]]

# Copie superficielle
liste2 = liste1.copy()
liste2[0][0] = 999
print(liste1)  # [[999, 2], [3, 4]] - modifié aussi !

# Copie profonde
liste1 = [[1, 2], [3, 4]]
liste3 = copy.deepcopy(liste1)
liste3[0][0] = 999
print(liste1)  # [[1, 2], [3, 4]] - intact
print(liste3)  # [[999, 2], [3, 4]]
```

### Autres Méthodes Utiles

```python
nombres = [3, 1, 4, 1, 5]

# Étendre avec une autre liste
nombres.extend([9, 2, 6])
print(nombres)  # [3, 1, 4, 1, 5, 9, 2, 6]

# Vider la liste
nombres.clear()
print(nombres)  # []

# Inverser
nombres = [1, 2, 3]
nombres.reverse()
print(nombres)  # [3, 2, 1]

# Trier sans modifier l'original
desordonne = [3, 1, 4, 1, 5]
trie = sorted(desordonne)
print(trie)        # [1, 1, 3, 4, 5]
print(desordonne)  # [3, 1, 4, 1, 5]

# Trier en ordre décroissant
decroissant = sorted(desordonne, reverse=True)
```

---

## 5. Fonctions Built-in pour les Listes

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Somme
total = sum(nombres)           # 31

# Minimum et Maximum
minimum = min(nombres)         # 1
maximum = max(nombres)         # 9

# Trier
sorted_nombres = sorted(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Longueur
longueur = len(nombres)        # 8

# Énumérer (index + valeur)
for i, val in enumerate(nombres):
    print(f"{i}: {val}")

# Tout ou N'importe lequel
print(all([True, True, False]))  # False
print(any([False, True, False])) # True
```

---

## 6. Listes Multidimensionnelles (Matrices)

```python
# Créer une matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accéder aux éléments
print(matrice[0])      # [1, 2, 3] - première ligne
print(matrice[0][1])   # 2 - première ligne, deuxième colonne
print(matrice[2][2])   # 9 - dernier élément

# Parcourir une matrice
for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()
```

### Exemple : Table de Multiplication

```python
# Créer une table de multiplication 10x10
table = []
for i in range(1, 11):
    ligne = []
    for j in range(1, 11):
        ligne.append(i * j)
    table.append(ligne)

# Afficher
for ligne in table:
    for nombre in ligne:
        print(f"{nombre:3}", end="")
    print()
```

---

## 7. Désempaquetage (Unpacking)

### Basique

```python
a, b = [1, 2]
print(a)  # 1
print(b)  # 2
```

### Avec *

```python
# Ignorer des valeurs
premier, *reste = [1, 2, 3, 4, 5]
print(premier)  # 1
print(reste)    # [2, 3, 4, 5]

# Premier et dernier
premier, *milieu, dernier = [1, 2, 3, 4, 5]
print(premier)  # 1
print(milieu)   # [2, 3, 4]
print(dernier)  # 5
```

### Dans les Boucles

```python
coordonnees = [(1, 2), (3, 4), (5, 6)]

for x, y in coordonnees:
    print(f"Point ({x}, {y})")
```

---

## 8. Les Compréhensions de Liste Avancées

### Syntaxe Complète

```python
# [expression for item in iterable if condition]

# Filtrer
pairs = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transformer
au_carre = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Filtrer ET transformer
gros_pairs = [x**2 for x in range(20) if x % 2 == 0 and x > 10]
# [144, 196, 256, 324]
```

### Avec if/else

```python
# Valeur différente selon condition
resultats = ["pair" if x % 2 == 0 else "impair" for x in range(5)]
# ['pair', 'impair', 'pair', 'impair', 'pair']
```

### Compréhensions Imbriquées

```python
# Créer une matrice
matrice = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Aplatir une matrice
plate = [element for ligne in matrice for element in ligne]
# [1, 2, 3, 2, 4, 6, 3, 6, 9]
```

---

## 9. Exercices Pratiques

### Exercice 1 : Manipulation de Base
Crée une liste de 5 nombres. Ajoute un nombre au début et à la fin. Supprime le troisième élément. Affiche la liste finale.

### Exercice 2 : Fonctions de Liste
Crée une liste de notes (0-20). Calcule la moyenne, trouve la meilleure et la pire note, et compte combien sont au-dessus de 10.

### Exercice 3 : Matrice
Crée une matrice 5x5 remplie de nombres aléatoires (1-100). Calcule la somme de chaque ligne et de chaque colonne.

### Exercice 4 : Compréhensions
Crée avec une seule ligne de code :
- Une liste des carrés de 1 à 20
- Une liste des nombres pairs entre 1 et 50
- Une liste des voyelles dans une chaîne donnée

### Exercice 5 : Palindrome
Demande un mot et vérifie si c'est un palindrome (se lit pareil dans les deux sens) en utilisant le slicing.

### Exercice 6 : Anagramme
Demande deux mots et vérifie si ce sont des anagrammes (trier les lettres et comparer).

### Exercice 7 : Trier une Liste de Dictionnaires
Crée une liste de dictionnaires avec nom et age. Trie par age croissant, puis par ordre alphabétique.

### Exercice 8 : Copie Profonde
Crée une liste imbriquée, fais une copie superficielle et une copie profonde. Modifie un élément interne et montre la différence.

### Exercice 9 : Désempaquetage
Crée une liste de 5 nombres. Utilise le désempaquetage pour récupérer le premier, le dernier, et les autres dans une liste.

### Exercice 10 : Plateau de Jeu
Crée une liste représentant un plateau de morpox (3x3). Permets au joueur de choisir une case (1-9) et de placer son symbole (X ou O). Affiche le plateau après chaque coup.

---

## Résumé

| Opération | Méthode | Exemple |
|-----------|---------|---------|
| Ajouter | `append()`, `insert()` | `liste.append(5)` |
| Supprimer | `remove()`, `pop()`, `clear()` | `liste.pop()` |
| Chercher | `index()`, `count()` | `liste.index(5)` |
| Trier | `sort()`, `sorted()` | `liste.sort()` |
| Copier | `copy()`, `[:]` | `liste.copy()` |
| Inverser | `reverse()` | `liste.reverse()` |
| Slicing | `[start:stop:step]` | `liste[1:5:2]` |
| Longueur | `len()` | `len(liste)` |

---

## Prochain Chapitre

Tu maîtrises les listes et tuples ! Le chapitre suivant sur les **dictionnaires et sets** te permettra de stocker des données avec des clés et des ensembles uniques.
