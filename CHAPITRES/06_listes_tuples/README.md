# Chapitre 6: Listes et Tuples

## Ce que vous allez apprendre

- Créer et manipuler des listes
- Créer et utiliser des tuples
- Indexation et slicing
- Méthodes de listes
- Immutabilité des tuples
- Packing et unpacking
- Compréhensions de listes
- Listes et tuples dans les fonctions

---

## 1. Les Listes

### Création de Listes

```python
# Liste vide
vide = []

# Liste avec elements
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "orange"]
melange = [1, "texte", True, 3.14]

# Liste avec range
carres = list(range(1, 11))  # [1, 4, 9, ..., 100]

# Liste avec comprehension
carres = [x ** 2 for x in range(11)]
```

### Indexation

```python
liste = ["a", "b", "c", "d", "e"]

# Index positif (debut a gauche)
liste[0]    # "a" (premier element)
liste[2]    # "c"
liste[4]    # "e" (dernier element)

# Index negatif (debut a droite)
liste[-1]   # "e" (dernier)
liste[-3]   # "c"
liste[-5]   # "a" (premier)

# Attention: Index hors plage!
# liste[5]    # IndexError!
# liste[-6]   # IndexError!
```

### Slicing (Decoupage)

```python
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [debut:fin] (fin non inclus)
liste[2:7]      # [2, 3, 4, 5, 6]
liste[:5]        # [0, 1, 2, 3, 4] (debut par defaut)
liste[5:]        # [5, 6, 7, 8, 9] (fin par defaut)
liste[:]          # [0, 1, 2, ..., 9] (copie)

# [debut:fin:pas]
liste[::2]       # [0, 2, 4, 6, 8] (un sur deux)
liste[1::2]      # [1, 3, 5, 7, 9]
liste[::-1]      # [9, 8, 7, ..., 0] (inversion)
```

---

## 2. Modification de Listes

### Ajout d'Elements

```python
liste = [1, 2, 3]

# append() - ajoute a la fin
liste.append(4)      # [1, 2, 3, 4]

# insert() -插入 a une position
liste.insert(1, 1.5)  # [1, 1.5, 2, 3, 4]

# extend() - fusionne avec une autre liste
liste.extend([5, 6])  # [1, 1.5, 2, 3, 4, 5, 6]

# + (concatenation)
nouvelle = liste + [7, 8]  # [1, 1.5, ..., 6, 7, 8]
```

### Suppression d'Elements

```python
liste = ["a", "b", "c", "d", "e"]

# remove() - supprime la premiere occurrence
liste.remove("c")    # ["a", "b", "d", "e"]

# pop() - supprime et retourne l'element
dernier = liste.pop()  # retourne "e", liste = ["a", "b", "d"]
element = liste.pop(1)   # retourne "b", liste = ["a", "d"]

# del - supprime par index
del liste[0]          # ["d"]

# clear() - vide la liste
liste.clear()         # []
```

### Tri et Recherche

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - trie sur place (modifie la liste)
nombres.sort()        # [1, 1, 2, 3, 4, 5, 6, 9]
nombres.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - retourne une nouvelle liste triee
ordonnes = sorted(nombres)

# reverse() - inverse la liste
nombres.reverse()

# index() - retourne l'index d'un element
nombres.index(4)      # 3

# count() - compte les occurrences
nombres.count(1)       # 2

# in - verification d'appartenance
1 in nombres           # True
```

---

## 3. Les Tuples

### Création de Tuples

```python
# Tuple vide
vide = ()

# Tuple avec elements
coordonnees = (10, 20)
personne = ("Alice", 25, "Paris")

# Tuple sans parentheses (packing)
simple = 1, 2, 3

# Tuple avec un element (virgule necessaire!)
un_element = (42,)      # CORRECT
pas_un_tuple = (42)      # Juste un entier!

# tuple() - convertir depuis une autre sequence
tuple([1, 2, 3])        # (1, 2, 3)
tuple("abc")             # ("a", "b", "c")
```

### Utilisation des Tuples

```python
# Indexation (comme les listes)
coord = (10, 20, 30)
coord[0]     # 10
coord[-1]    # 30

# Slicing (retourne un tuple)
coord[1:3]   # (20, 30)

# ATTENTION: Les tuples sont immuables!
# coord[0] = 5   # TypeError!
```

### Packing et Unpacking

```python
# Packing
tuplepacked = 1, 2, 3

# Unpacking basique
a, b, c = (1, 2, 3)
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Echange de valeurs (sans variable temporaire)
x, y = y, x

# Unpacking etendu (*)
premier, *milieu, dernier = [1, 2, 3, 4, 5]
print(premier)   # 1
print(milieu)    # [2, 3, 4]
print(dernier)   # 5

debut, *reste = "abcdef"
print(reste)     # ['b', 'c', 'd', 'e', 'f']
```

---

## 4. Operations Communes

### Concaténation

```python
# Listes
[1, 2] + [3, 4]        # [1, 2, 3, 4]

# Tuples
(1, 2) + (3, 4)        # (1, 2, 3, 4)

# Liste + Tuple (cast necessaire)
list([1, 2]) + list((3, 4))  # [1, 2, 3, 4]
```

### Répétition

```python
# Liste
[1, 2] * 3      # [1, 2, 1, 2, 1, 2]

# Tuple
("a", "b") * 2  # ("a", "b", "a", "b")
```

### Longueur

```python
len([1, 2, 3])    # 3
len(("a", "b"))   # 2
len("abc")        # 3 (sur une chaîne!)
```

---

## 5. Copie de Listes

```python
# ATTENTION: Copie par reference!
original = [1, 2, 3]
copie_mauvaise = original
copie_mauvaise[0] = 99
print(original)   # [99, 2, 3]  # Original modifie!

# Methodes de copie correctes
# Methode 1: Slicing
copie1 = original[:]

# Methode 2: list()
copie2 = list(original)

# Methode 3: copy()
copie3 = original.copy()

# Methode 4: deepcopy pour listes imbriquees
from copy import deepcopy
copie_profonde = deepcopy(original)
```

---

## 6. Listes Imbriquées (Matrices)

```python
# Matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder aux elements
matrice[0][0]    # 1 (premiere rangee, premiere colonne)
matrice[2][1]    # 8 (troisieme rangee, deuxieme colonne)

# Parourir une matrice
for rangee in matrice:
    for element in rangee:
        print(element, end=" ")
    print()

# List comprehension pour matrice
matrice_2x3 = [[i * j for j in range(3)] for i in range(2)]
# [[0, 0, 0], [0, 1, 2]]
```

---

## 7. Compréhensions de Listes

### Compréhension Simple

```python
# Methode traditionnelle
carres = []
for x in range(10):
    carres.append(x ** 2)

# Comprehension
carres = [x ** 2 for x in range(10)]
```

### Avec Condition

```python
# Condition a la fin
pairs = [x for x in range(20) if x % 2 == 0]

# Condition au debut
etats = ["pair" if x % 2 == 0 else "impair" for x in range(5)]
# ["pair", "impair", "pair", "impair", "pair"]
```

### Compréhensions Imbriquées

```python
# Table de multiplication
table = [[i * j for j in range(1, 11)] for i in range(1, 6)]
# [[1,2,3...10], [2,4,6...20], ...]

# Aplatir une liste
liste_2d = [[1, 2], [3, 4], [5, 6]]
aplatie = [element for rangee in liste_2d for element in rangee]
# [1, 2, 3, 4, 5, 6]
```

---

## 8. Tuples et Listes: Quand Utiliser?

| Critère | Liste | Tuple |
|---------|-------|-------|
| Modification | ✅ Mutable | ❌ Immutable |
| Performance | Plus lent | Plus rapide |
| Hachage | ❌ Non hachable | ✅ Hachable |
| Usage | Donnees changeantes | Donnees fixes |
| Exemple | Panier d'achat | Coordonnees |

```python
# Liste pour donnees changeantes
scores = [85, 92, 78]
scores.append(90)      # OK

# Tuple pour donnees fixes
coordonnees = (10, 20)  # Ne changera pas
# coordonnees[0] = 5   # ERREUR!

# Tuple comme cle de dictionnaire (immuable)
points = {
    (0, 0): "Origine",
    (1, 1): "Diagonale"
}
```

---

## Points Clés à Retenir

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| Creation liste | `[]` ou `list()` | `[1, 2, 3]` |
| Creation tuple | `()` | `(1, 2, 3)` |
| Index | `liste[i]` | `liste[0]` |
| Slicing | `liste[debut:fin]` | `liste[1:4]` |
| Append | `liste.append(x)` | Ajoute a la fin |
| Insert | `liste.insert(i, x)` | Insert a i |
| Remove | `liste.remove(x)` | Supprime x |
| Pop | `liste.pop()` | Retourne et supprime |
| Sort | `liste.sort()` | Trie sur place |
| Unpacking | `a, b = tuple` | `a, b = (1, 2)` |

---

## Erreurs Courantes

```python
# ERREUR: Modifier un tuple
t = (1, 2, 3)
t[0] = 10  # TypeError!

# CORRECT: Creer un nouveau tuple
t = (10, 2, 3)

# ERREUR: Oublier la virgule pour tuple unique
t = (42,)   # CORRECT
x = (42)    # int, pas tuple!

# ERREUR: Assigner a un element de tuple
a, b, c = (1, 2, 3)
a = 10     # OK (modifie la variable a)
# (1, 2, 3)[0] = 10  # ERREUR!

# ERREUR: Confondre == et is
a = [1, 2, 3]
b = [1, 2, 3]
a == b    # True (meme contenu)
a is b    # False (objets differents)
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous decouvrez les **dictionnaires et sets** pour des structures de donnees basees sur des cles.
