# Chapitre 4: Contrôle de Flux

## Ce que vous allez apprendre

- Utiliser les conditions `if`, `elif`, `else`
- Le nouvel opérateur `match` (Python 3.10+)
- L'opérateur ternaire
- Les conditions composées avec `and`, `or`, `not`
- La vérification d'appartenance avec `in`
- Les chaînes de conditions et l'indentation

---

## 1. Les Conditions `if`, `elif`, `else`

### La Structure de Base

```python
# Condition simple
age = 18

if age >= 18:
    print("Vous êtes majeur")
```

### Avec Alternative `else`

```python
age = 15

if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

### Conditions Multiples avec `elif`

```python
note = 14

if note >= 16:
    print("Excellent")
elif note >= 14:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

### Imbrication de Conditions

```python
age = 25
est_etudiant = True

if age >= 18:
    if est_etudiant:
        print("Étudiant majeur")
    else:
        print("Majeur non étudiant")
else:
    if est_etudiant:
        print("Étudiant mineur")
    else:
        print("Mineur non étudiant")
```

---

## 2. L'Opérateur `match` (Python 3.10+)

### Syntaxe de Base

```python
jour = "lundi"

match jour:
    case "lundi":
        print("Début de semaine")
    case "vendredi":
        print("Fin de semaine")
    case "samedi" | "dimanche":
        print("Week-end")
    case _:
        print("Jour de semaine")
```

### Matching avec Conditions

```python
age = 25

match age:
    case x if x < 0:
        print("Âge invalide")
    case x if x < 18:
        print("Mineur")
    case x if x < 65:
        print("Adulte")
    case _:
        print("Senior")
```

### Matching de Structures

```python
# Tuple matching
point = (0, 0)

match point:
    case (0, 0):
        print("Origine")
    case (x, 0):
        print(f"Axe X: {x}")
    case (0, y):
        print(f"Axe Y: {y}")
    case (x, y):
        print(f"Point: ({x}, {y})")
```

---

## 3. L'Opérateur Ternaire

### Syntaxe

```python
# Condition classique
if condition:
    resultat = valeur_si_vrai
else:
    resultat = valeur_si_faux

# Version ternaire (une ligne)
resultat = valeur_si_vrai if condition else valeur_si_faux
```

### Exemples

```python
age = 15
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # "mineur"

# Autre exemple
x = 10
y = 20
max_val = x if x > y else y
print(max_val)  # 20

# Imbrication (à éviter si trop complexe)
note = 12
mention = "TB" if note >= 16 else "B" if note >= 14 else "AB" if note >= 12 else "Passable"
```

---

## 4. Conditions Composées

### Opérateurs Logiques

```python
# AND - Toutes les conditions doivent être vraies
age = 25
revenu = 50000

if age >= 18 and revenu >= 30000:
    print("Éligible au prêt")

# OR - Au moins une condition doit être vraie
jour = "samedi"

if jour == "samedi" or jour == "dimanche":
    print("Week-end!")

# NOT - Inverse la condition
est_connecte = False

if not est_connecte:
    print("Déconnecté")
```

### Priorité des Opérateurs

```python
# De la plus haute à la plus basse priorité:
# 1. not
# 2. and
# 3. or

# Exemple
x = True
y = False
z = False

resultat = not x or y and z
# Équivalent à: (not x) or (y and z)
# = False or False
# = False
```

---

## 5. Vérification d'Appartenance avec `in`

```python
# Dans une liste
couleurs = ["rouge", "vert", "bleu"]
couleur = "vert"

if couleur in couleurs:
    print(f"{couleur} est dans la liste")

# Dans une chaîne
mot = "programmation"
lettre = "g"

if lettre in mot:
    print(f"'{lettre}' est dans '{mot}'")

# Dans un dictionnaire (vérifie les clés)
scores = {"Alice": 85, "Bob": 92}

if "Alice" in scores:
    print("Alice a un score")

# Avec negateion
if "Charlie" not in scores:
    print("Charlie n'a pas de score")
```

---

## 6. Vérification d'Identité avec `is`

```python
# Comparer avec None
resultat = None

if resultat is None:
    print("Pas de résultat")

if resultat is not None:
    print("Il y a un résultat")

# Différence entre == et is
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (même contenu)
print(a is b)   # False (objets différents)

c = a
print(c is a)   # True (même objet)
```

---

## 7. Structure Recommandée: Early Return

```python
def valider_utilisateur(nom, age, email):
    # Vérifications négatives d'abord (early return)
    if not nom:
        return "Nom requis"
    
    if len(nom) < 2:
        return "Nom trop court"
    
    if age < 18:
        return "Doit être majeur"
    
    if "@" not in email:
        return "Email invalide"
    
    # Si toutes les vérifications passent
    return "Utilisateur valide"
```

---

## 8. Patterns Avancés

### Match avec Guard Clauses

```python
def analyser_nombre(n):
    match n:
        case 0:
            return "Zéro"
        case x if x > 0 and x % 2 == 0:
            return "Pair positif"
        case x if x > 0:
            return "Impair positif"
        case x if x < 0 and x % 2 == 0:
            return "Pair négatif"
        case x if x < 0:
            return "Impair négatif"
```

### Match avec Types (Python 3.10+)

```python
def decrire(valeur):
    match valeur:
        case str():
            return f"Texte: '{valeur}'"
        case int():
            return f"Entier: {valeur}"
        case float():
            return f"Décimal: {valeur}"
        case bool():
            return f"Booléen: {valeur}"
        case list():
            return f"Liste de {len(valeur)} éléments"
        case _:
            return "Type inconnu"
```

---

## Points Clés à Retenir

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| Condition simple | `if condition:` | `if age >= 18:` |
| Alternative | `else:` | `else: print("mineur")` |
| Conditions multiples | `elif condition:` | `elif note >= 10:` |
| Ternaire | `A if C else B` | `"oui" if ok else "non"` |
| Matching | `match x:` | `case "a":` |
| ET logique | `and` | `a > 0 and b > 0` |
| OU logique | `or` | `a == 0 or b == 0` |
| Négation | `not` | `not est_vide` |
| Appartenance | `in` | `"a" in "chaine"` |

---

## Erreurs Courantes

```python
# ❌ ERREUR: Oublier les deux-points
if x > 0
    print("positif")

# ✅ CORRECT
if x > 0:
    print("positif")

# ❌ ERREUR: Indentation incohérente
if x > 0:
print("positif")
else:
    print("non")

# ✅ CORRECT
if x > 0:
    print("positif")
else:
    print("non")

# ❌ ERREUR: Comparer avec == pour None
if x == None:
    pass

# ✅ CORRECT
if x is None:
    pass

# ❌ ERREUR: Confondre = et ==
if x = 10:  # ERREUR de syntaxe
    pass

# ✅ CORRECT
if x == 10:
    pass
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez les **boucles** pour répéter des actions efficacement.
