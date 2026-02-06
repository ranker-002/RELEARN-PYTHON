# Chapitre 3 : Les Opérateurs - Faire des Calculs et des Comparaisons

## Introduction : C'est quoi un opérateur ?

Un opérateur est comme un verbe en français : il décrit une action à effectuer. Par exemple, "+" est l'opérateur qui dit "additionne ces deux nombres".

Python a plusieurs kinds d'opérateurs :
- **Arithmétiques** : pour faire des calculs
- **Comparaison** : pour comparer des valeurs
- **Logiques** : pour combiner des conditions
- **Appartenance** : pour vérifier si quelque chose est dans une liste

---

## 1. Les opérateurs arithmétiques

Ce sont les opérateurs mathématiques de base, ceux que tu connais de l'école !

### Les opérateurs de base

```python
# Addition
a = 10 + 5    # 15

# Soustraction
b = 10 - 5    # 5

# Multiplication
c = 10 * 5    # 50

# Division
d = 10 / 5    # 2.0 (toujours un nombre décimal en Python !)
```

### La division entière et le modulo

```python
# Division entière (arrondit vers le bas)
e = 10 // 3   # 3 (ignorer le reste)

# Modulo (le reste de la division)
f = 10 % 3    # 1 (car 10 = 3×3 + 1)

# Puissance (exponentiation)
g = 2 ** 10   # 1024 (2 à la puissance 10)
h = 5 ** 2    # 25 (5 au carré)
```

### À quoi ça sert dans la vraie vie ?

```python
# Vérifier si un nombre est pair
nombre = 17
if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")

# Faire des groupes
total = 23
groupes_de_5 = total // 5    # 4 groupes complets
reste = total % 5           # 3 éléments restants
```

---

## 2. Les opérateurs de comparaison

Ces opérateurs comparent deux valeurs et renvoient `True` ou `False`.

```python
a = 10
b = 5

# Égal à
print(a == b)    # False

# Différent de
print(a != b)    # True

# Plus grand que
print(a > b)     # True

# Plus petit que
print(a < b)     # False

# Plus grand ou égal
print(a >= 10)   # True

# Plus petit ou égal
print(a <= 10)   # True
```

### Comparer des chaînes

```python
# Les chaînes se comparent par ordre alphabétique
print("apple" < "banana")   # True (a < b)
print("chat" == "Chien")   # False (les majuscules comptent !)

# Pour comparer sans tenir compte de la casse
print("apple".lower() == "Apple".lower())  # True
```

---

## 3. Les opérateurs logiques

Ces opérateurs combinent plusieurs conditions.

```python
a = True
b = False

# ET (and) : Les deux doivent être vrais
print(a and b)    # False (un seul est vrai)

# OU (or) : Au moins un doit être vrai
print(a or b)     # True

# NON (not) : Inverse la valeur
print(not a)      # False
```

### Exemple concret

```python
age = 25
avec_permis = True

# Peut-il conduire ?
peut_conduire = age >= 18 and avec_permis  # True

# Peut-il voter ? (18+ ET citoyen)
peut_voter = age >= 18  # et citizen == True (simplifié)
```

---

## 4. Les opérateurs d'appartenance

Ces opérateurs vérifient si une valeur est présente dans une séquence.

```python
# in : Est présent dans
fruits = ["pomme", "banane", "orange"]
print("pomme" in fruits)     # True
print("raisin" in fruits)    # False

# not in : N'est pas présent dans
print("raisin" not in fruits)  # True
```

---

## 5. Priorité des opérateurs

Python évalue les opérateurs dans un ordre précis (comme en maths) :

```python
# La multiplication avant l'addition
resultat = 2 + 3 * 4   # 14 (2 + 12), pas 20 !

# Forcer l'ordre avec parenthèses
resultat = (2 + 3) * 4   # 20

# Priorité (de la plus haute à la plus basse) :
# 1. ** (puissance)
# 2. * / // % (multiplication, division)
# 3. + - (addition, soustraction)
```

---

## Erreurs courantes

```python
# ERREUR : Confondre = et ==
if age = 18:   # ERREUR !
    pass

if age == 18:  # CORRECT
    pass
```

---

## Exercices

1. Calcule l'aire d'un cercle (π × r²)
2. Vérifie si un nombre est divisible par 3 et par 5
