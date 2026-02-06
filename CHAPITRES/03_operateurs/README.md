# Chapitre 3: Opérateurs

## Ce que vous allez apprendre

- Opérateurs arithmétiques
- Opérateurs de comparaison
- Opérateurs d'appartenance
- Opérateurs logiques
- Opérateurs bit à bit
- Priorité des opérateurs
- Combinaison d'opérateurs

---

## 1. Opérateurs Arithmétiques

```python
# Addition
a = 10 + 5    # 15

# Soustraction
b = 10 - 5    # 5

# Multiplication
c = 10 * 5    # 50

# Division (toujours float)
d = 10 / 5    # 2.0

# Division entière (arrondi vers le bas)
e = 10 // 3   # 3

# Modulo (reste de la division)
f = 10 % 3    # 1

# Puissance
g = 2 ** 10   # 1024

# Opérateurs augmentés
x = 10
x += 5        # x = x + 5 (équivalent à x = 15)
x -= 3        # x = x - 3
x *= 2        # x = x * 2
x /= 4        # x = x / 4
x //= 2       # x = x // 2
x %= 3        # x = x % 3
x **= 2       # x = x ** 2
```

---

## 2. Opérateurs de Comparaison

```python
a = 10
b = 5

# Égal
a == b        # False

# Différent
a != b        # True

# Strictement supérieur
a > b         # True

# Strictement inférieur
a < b         # False

# Supérieur ou égal
a >= b        # True

# Inférieur ou égal
a <= b        # False

# Comparaison de chaînes
"apple" < "banana"  # True (ordre alphabétique)
"Python" == "python"  # False (sensibilité à la casse)
```

---

## 3. Opérateurs d'Appartenance

```python
# Vérifie si une valeur est dans une séquence
fruits = ["pomme", "orange", "banane"]

"pomme" in fruits        # True
"raisin" in fruits       # False

# Avec negation
"raisin" not in fruits   # True

# Dans une chaîne
mot = "programmation"
"gram" in mot            # True
"z" in mot               # False

# Dans un dictionnaire (vérifie les clés)
scores = {"Alice": 85, "Bob": 92}
"Alice" in scores        # True
85 in scores             # False (85 est une valeur, pas une clé)
```

---

## 4. Opérateurs Logiques

```python
x = True
y = False

# AND: True si les deux sont True
x and y          # False

# OR: True si au moins un est True
x or y           # True

# NOT: inverse la valeur
not x            # False
not y            # True

# Utilisation pratique
age = 25
revenu = 50000

if age >= 18 and revenu >= 30000:
    print("Éligible")

if age < 18 or age > 65:
    print("Catégorie speciale")

if not (age < 18):
    print("Adulte")
```

---

## 5. Opérateurs Bit à Bit

```python
# Travaillent sur les représentations binaires

a = 5      # 0b0101
b = 3      # 0b0011

# AND bit à bit
a & b      # 0b0001 = 1

# OR bit à bit
a | b      # 0b0111 = 7

# XOR (OU exclusif)
a ^ b      # 0b0110 = 6

# NOT (inversion bit à bit)
~a         # -6 (complément à deux)

# Décalage à gauche (multiplication par 2^n)
a << 1     # 0b1010 = 10

# Décalage à droite (division par 2^n)
a >> 1     # 0b0010 = 2

# Cas d'usage: vérifier si un bit est activé
def check_bit(n, bit_position):
    return (n >> bit_position) & 1 == 1

check_bit(5, 0)  # True (bit 0 de 5 est 1)
check_bit(5, 1)  # False (bit 1 de 5 est 0)
```

---

## 6. Priorité des Opérateurs

```python
# De la plus haute à la plus basse priorité:

# 1. ()
# 2. **
# 3. +x, -x, ~x (unaire)
# 4. *, /, //, %
# 5. +, - (binaire)
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. ==, !=, >, <, >=, <=, is, is not, in, not in
# 11. not
# 12. and
# 13. or

# Exemples
resultat = 2 + 3 * 4        # 14 (multiplication avant addition)
resultat = (2 + 3) * 4      # 20 (parentèses prioritaires)
resultat = 10 - 2 + 5       # 13 (même priorité: gauche à droite)
resultat = 2 ** 3 ** 2      # 512 (droite à gauche: 2 ** (3 ** 2))
```

---

## 7. Valeurs "Truthy" et "Falsy"

```python
# Valeurs considérées comme False:
bool(False)      # False
bool(None)       # False
bool(0)          # False
bool(0.0)        # False
bool("")         # False
bool([])         # False
bool({})         # False
bool(set())      # False
bool(range(0))   # False

# Toutes les autres valeurs sont True:
bool(1)          # True
bool(-1)         # True
bool("a")        # True
bool([1, 2])     # True
bool({"a": 1})   # True

# Utilisation pratique
def afficher_si_non_vide(texte):
    if texte:  # Équivalent à "if texte != ''"
        print(f"Texte: {texte}")
```

---

## 8. Combinaison Pratique

```python
# Vérifier si un nombre est dans une plage
def dans_plage(valeur, min_val, max_val):
    return min_val <= valeur <= max_val

# Vérifier les conditions multiples
def peut_conduire(age, permis):
    return age >= 18 and permis

# Chaîne de comparaisons (Python 3)
score = 75
10 < score < 100        # True
-5 < score < 0          # False

# Opérateurs ternaires combinés
statut = "Adulte" if 18 <= age < 65 else "Senior" if age >= 65 else "Mineur"
```

---

## Points Clés à Retenir

| Catégorie | Opérateurs |
|-----------|------------|
| Arithmétiques | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparaison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Appartenance | `in`, `not in` |
| Logiques | `and`, `or`, `not` |
| Bit à bit | `&`, `|`, `^`, `~`, `<<`, `>>` |
| Augmentés | `+=`, `-=`, `*=`, etc. |

---

## Erreurs Courantes

```python
# ERREUR: Confondre = et ==
if x = 5:      # SyntaxError!
    pass

# CORRECT
if x == 5:
    pass

# ERREUR: Comparer des types différents
"5" == 5       # False (string vs int)

# CORRECT
int("5") == 5  # True
"5" == "5"     # True

# ERREUR: Oublier la priorité
total = 10 + 5 * 2   # 20 (pas 30!)

# CORRECT
total = (10 + 5) * 2  # 30
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez le **contrôle de flux** avec les conditions if/elif/else et le matching.
