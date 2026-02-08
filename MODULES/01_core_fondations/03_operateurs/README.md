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

## 5. Les Opérateurs d'Assignation

### Assignation Simple

```python
x = 10  # Le classique
```

### Assignations Combinées

Ces opérateurs combinent une opération et une assignation :

```python
x = 10

# Addition puis assignation
x += 5   # Équivalent à : x = x + 5 → x vaut 15

# Soustraction puis assignation
x -= 3   # Équivalent à : x = x - 3 → x vaut 12

# Multiplication puis assignation
x *= 2   # Équivalent à : x = x * 2 → x vaut 24

# Division puis assignation
x /= 4   # Équivalent à : x = x / 4 → x vaut 6.0

# Division entière puis assignation
x //= 2  # Équivalent à : x = x // 2 → x vaut 3.0

# Modulo puis assignation
x %= 2   # Équivalent à : x = x % 2 → x vaut 1.0

# Puissance puis assignation
x **= 3  # Équivalent à : x = x ** 3 → x vaut 1.0
```

### Avec les Chaînes

```python
message = "Bonjour"
message += " "       # "Bonjour "
message += "Alice"   # "Bonjour Alice"

# Répétition
separateur = "-"
separateur *= 10     # "----------"
```

### Avec les Listes

```python
panier = ["pomme"]
panier += ["banane", "orange"]  # ["pomme", "banane", "orange"]
```

---

## 6. L'Opérateur Ternaire

L'opérateur ternaire permet d'écrire un if/else sur une seule ligne.

### Syntaxe

```python
valeur = valeur_si_vrai if condition else valeur_si_faux
```

### Exemples

```python
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # "majeur"

# Plus complexe
temperature = 25
message = "Il fait chaud" if temperature > 30 else "Il fait bon" if temperature > 15 else "Il fait froid"
print(message)  # "Il fait bon"

# Équivalent avec if/else classique (plus long)
if temperature > 30:
    message = "Il fait chaud"
elif temperature > 15:
    message = "Il fait bon"
else:
    message = "Il fait froid"
```

### Usage Courant

```python
# Valeur par défaut
nom_utilisateur = input("Votre nom : ") or "Anonyme"

# Limite min/max
score = 150
score_affiche = min(score, 100)  # Plafonné à 100

# Avec fonction
prix = 50
remise = 0.2 if prix > 100 else 0.1
prix_final = prix * (1 - remise)
```

---

## 7. Les Opérateurs d'Identité

Ces opérateurs vérifient si deux variables pointent vers le même objet en mémoire.

### Différence entre == et is

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# == compare les valeurs
print(a == b)   # True (mêmes valeurs)

# is compare l'identité (même objet en mémoire)
print(a is b)   # False (objets différents)
print(a is c)   # True (même objet !)
```

### Cas d'Usage

```python
# Vérifier si une variable est None
valeur = None
if valeur is None:
    print("Pas de valeur")

# Vérifier si c'est le même objet
x = 1000
y = 1000
print(x is y)   # False (grands entiers sont différents)

# Petit entier (-5 à 256) : Python les réutilise
x = 100
y = 100
print(x is y)   # True (même objet en mémoire)
```

### is not

```python
reponse = input("Continuer ? (o/n) : ")
if reponse is not None and reponse.lower() == "o":
    print("On continue !")
```

---

## 8. Les Opérateurs Binaires

Ces opérateurs travaillent sur la représentation binaire des nombres.

### Conversion Binaire

```python
# Afficher un nombre en binaire
print(bin(10))   # 0b1010
print(bin(5))    # 0b101

# 10 en binaire : 1010
# 5 en binaire  : 0101
```

### ET Bit à Bit (&)

```python
# 10 & 5
# 1010 (10)
# 0101 (5)
# ----
# 0000 (0)
resultat = 10 & 5   # 0

# 12 & 7
# 1100 (12)
# 0111 (7)
# ----
# 0100 (4)
resultat = 12 & 7   # 4
```

### OU Bit à Bit (|)

```python
# 10 | 5
# 1010 (10)
# 0101 (5)
# ----
# 1111 (15)
resultat = 10 | 5   # 15
```

### OU Exclusif (^)

```python
# 10 ^ 5
# 1010 (10)
# 0101 (5)
# ----
# 1111 (15)
resultat = 10 ^ 5   # 15
```

### Négation (~)

Inverse tous les bits (utile pour les masques) :
```python
x = 5   # 0b101
resultat = ~x   # -6 (inversion de tous les bits)
```

### Décalage de Bits

```python
# Décalage à gauche (<<) = multiplication par 2^n
x = 5        # 0b101
x << 1       # 0b1010 = 10 (×2)
x << 2       # 0b10100 = 20 (×4)
x << 3       # 0b101000 = 40 (×8)

# Décalage à droite (>>) = division entière par 2^n
x = 40       # 0b101000
x >> 1       # 0b10100 = 20 (÷2)
x >> 2       # 0b1010 = 10 (÷4)
x >> 3       # 0b101 = 5 (÷8)
```

### Applications Pratiques

```python
# Vérifier si un nombre est pair (bit de poids faible)
def est_pair(n):
    return (n & 1) == 0

# Multiplier/Diviser par des puissances de 2 (rapide)
x = 10
x = x << 3   # Équivalent à x * 8, mais plus rapide

# Masques de bits (permissions)
PERMISSION_LECTURE = 1    # 0b001
PERMISSION_ECRITURE = 2   # 0b010
PERMISSION_EXECUTION = 4  # 0b100

# Définir les permissions
droits = PERMISSION_LECTURE | PERMISSION_ECRITURE  # 0b011 = 3

# Vérifier une permission
if droits & PERMISSION_LECTURE:
    print("Lecture autorisée")

# Ajouter une permission
droits |= PERMISSION_EXECUTION  # 0b111 = 7

# Retirer une permission
droits &= ~PERMISSION_ECRITURE  # Retire l'écriture
```

---

## 9. Priorité des Opérateurs

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

## Exercices Pratiques

### Exercice 1 : Calculs de Base
Calcule l'aire d'un cercle (π × r²) et affiche le résultat avec 2 décimales.

### Exercice 2 : Conditions Combinées
Vérifie si un nombre est divisible par 3 ET par 5 (utilise modulo).

### Exercice 3 : Assignations Combinées
Crée une variable `score` à 100, puis :
- Ajoute 50 points
- Multiplie par 2
- Divise par 5
- Affiche le résultat final

### Exercice 4 : Opérateur Ternaire
Demande l'âge de l'utilisateur et affiche :
- "Enfant" si < 13
- "Adolescent" si entre 13 et 19
- "Adulte" si ≥ 20

Utilise l'opérateur ternaire imbriqué.

### Exercice 5 : Vérification d'Identité
Crée deux listes identiques avec les mêmes valeurs. Vérifie :
- Si elles sont égales (==)
- Si elles sont le même objet (is)

Explique la différence.

### Exercice 6 : Opérateurs Binaires
Convertis ces nombres en binaire et effectue les opérations :
- 15 & 7
- 15 | 7
- 15 ^ 7
- 16 >> 2
- 3 << 3

### Exercice 7 : Système de Permissions
Crée un système de permissions utilisant des bits :
- Définis 3 permissions (lecture=1, écriture=2, exécution=4)
- Crée un utilisateur avec lecture + écriture
- Vérifie s'il a chaque permission
- Ajoute la permission exécution
- Retire la permission écriture

### Exercice 8 : Calculatrice Simple
Crée une mini-calculatrice qui :
1. Demande deux nombres
2. Demande l'opération (+, -, *, /, //, %, **)
3. Affiche le résultat
4. Utilise l'opérateur d'assignation combinée appropriée

### Exercice 9 : Validation de Mot de Passe
Vérifie si un mot de passe est valide (longueur ≥ 8) en utilisant l'opérateur ternaire.
Affiche "Valide" ou "Trop court".

### Exercice 10 : Mini-Jeu de Devinette
Génère un nombre aléatoire entre 1 et 100. Le joueur propose un nombre.
Utilise les opérateurs de comparaison pour dire si c'est :
- "Trop grand !"
- "Trop petit !"
- "Gagné !"

---

## Récapitulatif des Opérateurs

| Catégorie | Opérateurs | Exemple |
|-----------|-----------|---------|
| Arithmétiques | `+ - * / // % **` | `a + b` |
| Comparaison | `== != > < >= <=` | `a > b` |
| Logiques | `and or not` | `a and b` |
| Appartenance | `in not in` | `x in liste` |
| Assignation | `= += -= *= /= //= %=` | `a += 5` |
| Ternaire | `x if cond else y` | `a if b else c` |
| Identité | `is is not` | `a is None` |
| Binaires | `& | ^ ~ << >>` | `a & b` |

**Priorité** (de la plus haute à la plus basse) :
1. `**` (puissance)
2. `~ + -` (unaires)
3. `* / // %` (multiplication/division)
4. `+ -` (addition/soustraction)
5. `<< >>` (décalage)
6. `&` (ET bit)
7. `^` (XOR)
8. `|` (OU bit)
9. `== != > < >= <= is in` (comparaisons)
10. `not` (négation logique)
11. `and` (ET logique)
12. `or` (OU logique)
13. `if else` (ternaire)
14. `= += -=` (assignation)

---

## Prochain Chapitre

Tu maîtrises maintenant tous les opérateurs Python ! Dans le chapitre suivant, tu découvriras le **contrôle de flux** pour prendre des décisions et créer des programmes plus intelligents.
