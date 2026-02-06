# Chapitre 2: Variables et Types de Données

## Ce que vous allez apprendre

- Comprendre ce qu'est une variable en Python
- Manipuler les types de données fondamentaux
- Effectuer des conversions entre types
- Comprendre la notion de mutabilité
- Utiliser les types de données appropriés

---

## 1. Les Variables en Profondeur

### Qu'est-ce qu'une Variable?

Une variable est un **conteneur nommé** qui stocke une valeur en mémoire. En Python, les variables sont des références vers des objets.

```python
# Création d'une variable
age = 25

# Ce qui se passe en réalité:
# 1. Python crée l'objet entier 25 en mémoire
# 2. La variable 'age' référence cet objet
# 3. Si on affecte age = 30, Python crée un nouvel objet 30
```

### Caractéristiques des Variables Python

```python
# Pas besoin de déclaration de type
nombre = 42          # Python déduit int
prix = 19.99         # Python déduit float
nom = "Alice"        # Python déduit str
est_actif = True     # Python déduit bool

# Le type peut changer dynamiquement
x = 10       # int
x = "dix"    # str - Python accepte!
x = 10.5     # float - Encore possible

# Affectation multiple
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Échange de valeurs
x, y = y, x

# Affectation augmentée
compteur = 0
compteur += 1     # compteur = compteur + 1
compteur -= 2     # compteur = compteur - 2
```

---

## 2. Les Types de Données Fondamentaux

### Les Entiers (int)

```python
# Nombres entiers de taille illimitée
petit = 42
grand = 1_000_000     # Le underscore est ignoré (Python 3.6+)
tres_grand = 10**100  # Python peut gérer des nombres gigantesques!

# Bases différentes
binaire = 0b1010      # 10 en décimal
octal = 0o755          # 493 en décimal
hexadecimal = 0xFF     # 255 en décimal

# Opérations sur les entiers
a = 17
b = 5

addition = a + b           # 22
soustraction = a - b       # 12
multiplication = a * b      # 85
division = a / b            # 3.4 (toujours float!)
division_entiere = a // b   # 3 (arrondi vers le bas)
reste = a % b              # 2 (modulo)
puissance = a ** b         # 1419857

# Fonctions utiles
abs(-42)           # 42 (valeur absolue)
round(3.7)         # 4 (arrondir)
pow(2, 3)          # 8 (puissance, équivalent à 2**3)
divmod(17, 5)      # (3, 2) (quotient et reste)
```

### Les Nombres à Virgule (float)

```python
# Nombres décimaux
pi = 3.14159
negatif = -2.5
tres_petit = 0.000001

# Notation scientifique
terre_masse = 5.972e24   # 5.972 × 10^24
electron_masse = 9.109e-31

# Précision et arrondi
from decimal import Decimal, getcontext

# Problème de précision avec float
0.1 + 0.2  # 0.30000000000000004 (erreur d'arrondi!)

# Solution: utiliser Decimal pour la précision
Decimal('0.1') + Decimal('0.2')  # Decimal('0.3')

# Arrondir correctement
round(3.14159, 2)    # 3.14
round(2.5)           # 2 (arrondi au pair le plus proche!)
round(2.5, 0)        # 2.0
```

### Les Chaînes de Caractères (str)

```python
# Créer des chaînes
simple = 'Bonjour'
double = "Bonjour"
triple = """Ceci est
sur plusieurs
lignes"""

# Les chaînes sont immuables
mot = "Python"
# mot[0] = "J"  # ERREUR! Impossible de modifier

# Accéder aux caractères
mot[0]      # 'P' (premier caractère)
mot[-1]     # 'n' (dernier caractère)
mot[0:2]    # 'Py' (slice: du début à avant l'index 2)
mot[::2]    # 'Pto' (un caractère sur deux)
mot[::-1]   # 'nohtyP' (inverser)

# Méthodes de chaînes
phrase = "  Bonjour le monde!  "
phrase.strip()           # "Bonjour le monde!" (enlève espaces)
phrase.lower()           # "  bonjour le monde!  "
phrase.upper()           # "  BONJOUR LE MONDE!  "
phrase.replace("Bonjour", "Salut")  # "  Salut le monde!  "
phrase.split(" ")        # ["", "", "Bonjour", "le", "monde!  "]
",".join(["a", "b", "c"])  # "a,b,c"
len(phrase)              # 24 (longueur)
"le" in phrase           # True (recherche)
phrase.startswith("  ")  # True

# Formattage de chaînes
nom = "Alice"
age = 25

# Méthode 1: f-string (recommandée, Python 3.6+)
f"Bonjour, je m'appelle {nom} et j'ai {age} ans."

# Méthode 2: format()
"Bonjour, je m'appelle {} et j'ai {} ans.".format(nom, age)
"Bonjour, je m'appelle {0} et j'ai {1} ans.".format(nom, age)
"Bonjour, je m'appelle {nom} et j'ai {age} ans.".format(nom=nom, age=age)

# Méthode 3: % (ancienne méthode)
"Bonjour, je m'appelle %s et j'ai %d ans." % (nom, age)

# Formatage avancé
prix = 49.99
quantite = 3

f"Total: {prix * quantite:.2f} €"     # "Total: 149.97 €"
f"Pourcentage: {0.125:.1%}"           # "Pourcentage: 12.5%"
f"Décimal: {42:05d}"                  # "Décimal: 00042"
```

### Les Booléens (bool)

```python
# Valeurs booléennes
vrai = True
faux = False

# Opérations logiques
vrai and vrai     # True
vrai and faux     # False
vrai or faux      # True
not vrai          # False

# Valeurs "falsy" (considérées comme False)
bool(0)           # False
bool(0.0)         # False
bool("")          # False
bool([])          # False
bool(None)        # False

# Valeurs "truthy" (considérées comme True)
bool(1)           # True
bool("hello")     # True
bool([1, 2, 3])   # True

# Comparaisons
10 == 10          # True (égale)
10 != 5           # True (différent)
10 > 5            # True (supérieur)
10 < 5            # False (inférieur)
10 >= 10          # True (supérieur ou égal)
5 <= 10           # True (inférieur ou égal)
```

---

## 3. La Conversion de Types

```python
# String → Number
int("42")           # 42
float("3.14")       # 3.14
complex("1+2j")     # (1+2j)

# Number → String
str(42)             # "42"
str(3.14)           # "3.14"

# Number → Number
float(42)           # 42.0
int(3.14)           # 3 (tronque, pas arrondit!)
int(3.9)            # 3
round(3.9)          # 4

# Bool → Number
int(True)           # 1
int(False)          # 0
float(True)         # 1.0

# String → Bool
bool("")            # False
bool("any")         # True

# Conversion avec gestion d'erreur
def convertir_en_nombre(texte):
    try:
        return int(texte)
    except ValueError:
        try:
            return float(texte)
        except ValueError:
            return None

convertir_en_nombre("42")    # 42
convertir_en_nombre("3.14")  # 3.14
convertir_en_nombre("abc")   # None
```

---

## 4. Mutabilité et Immutabilité

```python
# Types immuables (ne peuvent pas être modifiés après création)
# int, float, str, tuple, frozenset, bytes

# Exemple avec str
mot = "Python"
# mot[0] = "J"  # ERREUR!
nouveau_mot = "J" + mot[1:]  # Créer un nouveau string: "Jython"

# Exemple avec tuple (immuble)
coordonnees = (10, 20)
# coordonnees[0] = 5  # ERREUR!
nouvelles = (5, 20)  # Créer un nouveau tuple

# Types muables (peuvent être modifiés après création)
# list, dict, set, bytearray

# Exemple avec list
nombres = [1, 2, 3]
nombres[0] = 10        # OK: [10, 2, 3]
nombres.append(4)      # OK: [10, 2, 3, 4]

# Exemple avec dict
personne = {"nom": "Alice", "age": 25}
personne["ville"] = "Paris"  # OK: ajoute une nouvelle clé
```

---

## 5. Le Type None

```python
# None représente l'absence de valeur
resultat = None
print(resultat)  # Affiche: None

# Vérifier si une valeur est None
if resultat is None:
    print("Aucune valeur")

# Cas d'usage typique
def chercher_element(liste, element):
    for i, val in enumerate(liste):
        if val == element:
            return i  # Retourne l'index
    return None  # Pas trouvé

index = chercher_element([1, 2, 3], 2)
if index is not None:
    print(f"Trouvé à l'index {index}")
else:
    print("Non trouvé")
```

---

## Points Clés à Retenir

| Concept | Description |
|---------|-------------|
| Variable | Référence vers un objet en mémoire |
| Types immuables | int, float, str, tuple - ne peuvent être modifiés |
| Types muables | list, dict, set - peuvent être modifiés |
| `type()` | Retourne le type d'une valeur |
| `isinstance()` | Vérifie le type d'une valeur |
| Conversion | `int()`, `float()`, `str()`, `bool()` |
| f-strings | Formatage moderne: `f"{variable}"` |
| `None` | Représente l'absence de valeur |

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez les **opérateurs** pour effectuer des calculs et comparisons plus complexes.
