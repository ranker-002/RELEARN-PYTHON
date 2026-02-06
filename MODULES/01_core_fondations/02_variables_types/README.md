# Chapitre 2 : Variables et Types de Données - Comment Python Organise les Informations

## Introduction : Pourquoi les types sont importants ?

Imagine que tu as trois boîtes différentes :
- Une boîte pour ranger des mots
- Une boîte pour ranger des nombres entiers  
- Une boîte pour ranger des nombres à virgule

Tu ne mettrais pas le mot "chat" dans la boîte des nombres, n'est-ce pas ? Les types de données fonctionnent exactement comme ça : ils indiquent à Python quelle sorte d'information contient une variable.

Dans ce chapitre, tu vas découvrir tous les types de base de Python et apprendre à les manipuler !

---

## 1. Les nombres entiers (int)

### Qu'est-ce qu'un entier ?

Un entier est un nombre sans virgule, positif ou négatif. Python peut gérer des entiers de taille illimitée !

```python
# Nombres positifs
age = 25
compteur = 1000000
temperature = 0

# Nombres négatifs
dette = -500
temperature_moins_273 = -273

# Opérations de base
a = 10
b = 3

addition = a + b              # 13
soustraction = a - b          # 7
multiplication = a * b         # 30
division = a / b              # 3.333... (toujours décimal en Python !)
division_entiere = a // b      # 3 (sans virgule, juste l'entier)
reste = a % b                 # 1 (le "modulo", le reste de la division)
puissance = a ** b             # 1000 (10³)
```

### Le modulo (%) à quoi ça sert ?

Le modulo donne le reste d'une division. C'est très utile pour plein de choses !

```python
# Savoir si un nombre est pair
nombre = 7
print(nombre % 2)  # 1 (car 7 n'est pas divisible par 2)
print(6 % 2)       # 0 (car 6 EST divisible par 2)

# Obtenir le dernier chiffre d'un nombre
numero = 12345
print(numero % 10)  # 5 (le dernier chiffre)

# Faire un cycle de 0 à 3
compteur = 0
for i in range(10):
    print(i % 4, end=" ")  # Affiche: 0 1 2 3 0 1 2 3 0 1
```

---

## 2. Les nombres décimaux (float)

### Qu'est-ce qu'un float ?

Un "float" (pour "floating point" = "virgule flottante") est un nombre avec une virgule. Python utilise le point comme séparateur (comme en anglais).

```python
# Créer des floats
prix = 19.99
pi = 3.14159
temperature = -5.7
rien = 0.0

# Notation scientifique (pour les très grands ou très petits nombres)
grand_nombre = 1.5e10     # 15000000000.0
tres_petit = 1e-5         # 0.00001

# Opérations mixtes (int + float = float)
resultat = 10 + 5.5       # 15.5 (toujours un float)
resultat = 10 * 3.14      # 31.4
```

### Arrondir les nombres

```python
x = 3.14159

# Arrondir à n décimales
print(round(x, 2))   # 3.14
print(round(x, 3))   # 3.142

# Arrondir à l'entier le plus proche
print(round(3.5))    # 4
print(round(3.4))    # 3
print(round(-3.5))    # -3

# Tronquer (enlever la virgule, sans arrondir)
print(int(3.9))      # 3 (ça coupe, ça n'arrondit pas !)
print(int(-3.9))      # -3
```

### Attention aux limites des floats !

Les ordinateurs ne peuvent pas représenter tous les nombres décimaux exactement. C'est une limitation physique !

```python
# Résultat surprenant mais normal !
print(0.1 + 0.2)  # 0.30000000000000004 au lieu de 0.3 !

# Pour les calculs financiers (gros sous), utilise des entiers !
prix_en_centimes = 1999  # 19.99€, mais en centimes (entier)
```

---

## 3. Le type booléen (bool)

### Vrai ou Faux ?

Le type booléen n'a que deux valeurs possibles : `True` (vrai) ou `False` (faux).

```python
# Créer des booléens
est_majeur = True
est_connecte = False

# Le résultat d'une comparaison EST toujours un booléen
age = 20
print(age > 18)     # True (20 est plus grand que 18)
print(age < 10)     # False
print(age == 20)    # True (deux = pour comparer !)
print(age != 20)    # False (!= signifie "différent de")

# ATTENTION: Les mots-clés "True" et "False" ont une majuscule !
print(true)   # ERREUR !
print(True)   # OK
```

### Les opérations logiques

```python
# ET (and) - Les deux doivent être vrais pour que ce soit vrai
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OU (or) - Au moins un doit être vrai
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# NON (not) - Inverse la valeur
print(not True)         # False
print(not False)        # True

# Exemple concret dans la vraie vie
age = 25
avec_permis = True

# Est-ce que cette personne peut conduire une voiture ?
peut_conduire = age >= 18 and avec_permis  # True
```

---

## 4. Les chaînes de caractères (str)

### Qu'est-ce qu'une chaîne ?

Une chaîne de caractères (string) est tout simplement du texte, entouré de guillemets.

```python
# Créer des chaînes
nom = "Alice"
ville = 'Paris'           # Les guillemets simples fonctionnent aussi
long_texte = """Ceci est
un texte
sur plusieurs lignes"""

# La chaîne vide
vide = ""

# Longueur d'une chaîne (combien de caractères ?)
print(len("Bonjour"))  # 7 caractères

# Accéder à un caractère (attention : ça commence à 0 !)
mot = "Python"
print(mot[0])   # 'P' (le premier caractère)
print(mot[1])   # 'y'
print(mot[-1])  # 'n' (le dernier caractère, trick super utile !)
print(mot[-2])  # 'o' (l'avant-dernier)
```

### Les opérations sur les chaînes

```python
# Concaténation (assembler des morceaux)
prenom = "Alice"
bonjour = "Bonjour " + prenom + " !"  # "Bonjour Alice !"

# Répétition
rire = "ha" * 3        # "hahaha"

# Minuscules et majuscules
texte = "Bonjour le monde"
print(texte.lower())       # "bonjour le monde"
print(texte.upper())       # "BONJOUR LE MONDE"
print(texte.capitalize())  # "Bonjour le monde"
print(texte.title())       # "Bonjour Le Monde"
```

### Les méthodes les plus utiles

```python
texte = "  Bonjour le monde  "

# Enlever les espaces au début et à la fin (trim)
print(texte.strip())    # "Bonjour le monde"

# Remplacer du texte
print(texte.replace("Bonjour", "Salut"))  # "Salut le monde  "

# Savoir si un texte est dedans
print("monde" in texte)      # True
print("coucou" in texte)     # False

# Couper une chaîne en morceaux
phrase = "le-chat-est-rouge"
mots = phrase.split("-")      # ["le", "chat", "est", "rouge"]

# Recoller des morceaux
mots = ["Le", "chat", "rouge"]
phrase = " ".join(mots)      # "Le chat rouge"
```

---

## 5. Le formatage de chaînes

Il existe plusieurs façons d'insérer des variables dans du texte :

```python
prenom = "Alice"
age = 25
prix = 19.99

# Ancienne méthode avec % (vieillot, évite si possible)
print("Je m'appelle %s et j'ai %d ans" % (prenom, age))

# Méthode avec .format()
print("Je m'appelle {} et j'ai {} ans".format(prenom, age))
print("Je m'appelle {0} et j'ai {1} ans".format(prenom, age))

# F-string (LA méthode recommandée en Python 3.6+)
print(f"Je m'appelle {prenom} et j'ai {age} ans")
print(f"Le prix est {prix:.2f}€")  # "Le prix est 19.99€"
print(f"Pi vaut {3.14159:.4f}")     # "Pi vaut 3.1416"
```

---

## 6. La conversion entre types

### Pourquoi convertir ?

Parfois, tu dois transformer un type en un autre. C'est comme transvaser le contenu d'une boîte dans une autre boîte de type différent !

```python
# Texte vers nombre
age_texte = "25"
age_nombre = int(age_texte)       # 25 (entier)
prix_texte = "19.99"
prix_nombre = float(prix_texte)   # 19.99 (décimal)

# Nombre vers texte
nombre = 42
texte = str(nombre)   # "42"

# En booléen
print(bool(1))        # True
print(bool(0))        # False (0 = False, tout le reste = True)
print(bool(""))        # False (chaîne vide)
print(bool("abc"))     # True (chaîne non vide)
```

### Tableau des conversions

```python
# En entier (int)
print(int(3.9))        # 3 (ça coupe, ça n'arrondit pas !)
print(int("42"))       # 42
print(int(True))       # 1

# En décimal (float)
print(float(42))       # 42.0
print(float("3.14"))   # 3.14

# En texte (str)
print(str(42))         # "42"
print(str(3.14))       # "3.14"
print(str(True))        # "True"
```

---

## 7. Les constantes

### Qu'est-ce qu'une constante ?

Une constante est comme une variable, mais sa valeur ne change jamais. C'est une valeur "figée" dans ton code. Par convention, Python utilise des MAJUSCULES pour les nommer.

```python
# Constantes mathématiques
PI = 3.14159
TAU = 2 * PI  # 6.28318...

# Constantes de configuration
TAUX_TVA = 0.20
NOMBRE_MAX_TENTATIVES = 3
CHEMIN_FICHIER = "/home/user/data.txt"

# Ces valeurs ne changent pas dans le code
print(f"Le taux de TVA est {TAUX_TVA * 100}%")
```

---

## 8. Exemple complet : Programme de facturation

Voici un exemple qui utilise plusieurs types ensemble :

```python
# === Programme de facturation ===

# Les constantes (en MAJUSCULES)
TAUX_TVA = 0.20

# Les variables (données du client)
nom_client = "Alice Martin"
adresse = "123 Rue de Paris"
nombre_articles = 3
prix_unitaire = 19.99

# Les calculs
sous_total = nombre_articles * prix_unitaire
montant_tva = sous_total * TAUX_TVA
total = sous_total + montant_tva

# L'affichage
print("=" * 40)
print("           FACTURE")
print("=" * 40)
print(f"Client : {nom_client}")
print(f"Adresse : {adresse}")
print("-" * 40)
print(f"Articles : {nombre_articles} x {prix_unitaire:.2f}€")
print(f"Sous-total : {sous_total:.2f}€")
print(f"TVA (20%) : {montant_tva:.2f}€")
print("-" * 40)
print(f"TOTAL : {total:.2f}€")
print("=" * 40)

# Vérification du nombre d'articles
if nombre_articles > 0:
    prix_moyen = sous_total / nombre_articles
    print(f"Prix moyen par article : {prix_moyen:.2f}€")
```

**Résultat :**
```
========================================
           FACTURE
========================================
Client : Alice Martin
Adresse : 123 Rue de Paris
----------------------------------------
Articles : 3 x 19.99€
Sous-total : 59.97€
TVA (20%) : 11.99€
----------------------------------------
TOTAL : 71.97€
========================================
Prix moyen par article : 19.99€
```

---

## Résumé des types

| Type | Nom Python | Exemple | Usage |
|------|-----------|---------|-------|
| Entier | `int` | `25`, `-5`, `0` | Compter, indices, calculs |
| Décimal | `float` | `3.14`, `-0.5` | Prix, mesures précises |
| Booléen | `bool` | `True`, `False` | Conditions, Oui/Non |
| Chaîne | `str` | `"Bonjour"` | Texte, messages |

---

## Erreurs courantes à éviter

### 1. Confondre = et ==

```python
# ATTENTION, c'est facile de confondre !
age = 25     # Un seul = = ASSIGNE 25 à age (correct)
age == 25    # Deux == = COMPARE age à 25 (donne True ou False)

# ERREUR classique !
if age = 25:   # ERREUR ! On ne peut pas assigner dans un if
    print("L'âge est 25")

# CORRECT !
if age == 25:
    print("L'âge est 25")
```

### 2. Concaténer sans convertir

```python
# ERREUR classique !
age = 25
print("J'ai " + age + " ans")  
# ERREUR ! On ne peut pas ajouter du texte et un nombre ensemble

# SOLUTIONS !
print("J'ai " + str(age) + " ans")           # Méthode 1 : convertir en texte
print("J'ai", age, "ans")                   # Méthode 2 : utiliser des virgules
print(f"J'ai {age} ans")                     # Méthode 3 : f-string (la meilleure !)
```

### 3. Oublier que les chaînes indexent à partir de 0

```python
mot = "Python"
print(mot[0])   # 'P' (premier caractère)
print(mot[5])   # 'n' (sixième caractère, dernier)
print(mot[6])   # ERREUR ! IndexError - il n'y a pas de 7ème caractère
print(mot[-1])  # 'n' (trick : -1 = dernier caractère)
```

---

## Exercices pratiques

### Exercice 1 : Conversion de température
Demande une température en Celsius et affiche-la en Fahrenheit.
Formule : F = C × 9/5 + 32

### Exercice 2 : Aire d'un cercle
Demande le rayon d'un cercle et calcule son aire (π × r²).

### Exercice 3 : Présentation formatée
Crée un programme qui demande le nom, l'âge et la ville, puis affiche :
"Bonjour [nom], tu as [age] ans et tu vis à [ville]"

### Exercice 4 : Calcul de TVA
Crée un programme qui demande un prix HT et affiche :
- Le montant de la TVA (20%)
- Le prix TTC

---

## Prochain Chapitre

Dans le chapitre suivant, nous aborderons les **opérateurs**. Tu apprendras à faire des calculs plus complexes, à comparer des valeurs et à créer des conditions dans ton code !

Tu progresses bien ! Continue comme ça ! 💪
