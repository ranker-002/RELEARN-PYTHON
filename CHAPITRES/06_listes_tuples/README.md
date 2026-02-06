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

## 4. Les compréhensions de liste

Une façon élégante de créer des listes :

```python
# Créer [1, 4, 9, 16, 25]
carres = [x**2 for x in range(1, 6)]

# Créer avec condition
pairs = [x for x in range(10) if x % 2 == 0]
```

---

## Exercices

1. Crée une liste de nombres et affiche leur somme
2. Inverse une chaîne avec le slicing `[::-1]`
