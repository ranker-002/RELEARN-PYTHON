# Chapitre 5: Boucles

## Ce que vous allez apprendre

- La boucle `for` et son itération
- La boucle `while` et ses conditions
- La fonction `range()`
- La fonction `enumerate()`
- Les instructions `break` et `continue`
- La clause `else` dans les boucles
- Les boucles imbriquées
- Introduction aux compréhensions

---

## 1. La Boucle `for`

### Itération sur une Séquence

```python
# Sur une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Sur une chaîne
mot = "Python"
for lettre in mot:
    print(lettre)

# Sur un dictionnaire (itère sur les clés)
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
for cle in personne:
    print(f"{cle}: {personne[cle]}")
```

### Itération avec `range()`

```python
# range(fin) : de 0 à fin-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(debut, fin)
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(debut, fin, pas)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Compter à rebours
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

## 2. La Boucle `while`

### Structure de Base

```python
# Compteur simple
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1  # Ne pas oublier!

# Avec condition complexe
mot_de_passe = ""
while len(mot_de_passe) < 8:
    mot_de_passe = input("Mot de passe (8+ caractères): ")
print("Mot de passe valide!")
```

### Boucle Infinie et `break`

```python
# Boucle infinie avec break
while True:
    reponse = input("Tapez 'quit' pour sortir: ")
    if reponse == "quit":
        break
    print(f"Vous avez tapé: {reponse}")
```

---

## 3. `enumerate()` - Index et Valeur

```python
# Sans enumerate (methode manuelle)
fruits = ["pomme", "banane", "orange"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Avec enumerate (preferable)
fruits = ["pomme", "banane", "orange"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Commencer a un autre index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
```

---

## 4. `break` et `continue`

### `break` - Sortir de la Boucle

```python
# Rechercher un element et sortir
nombres = [1, 5, 10, 15, 20, 25]
for n in nombres:
    if n >= 15:
        print(f"Trouvé: {n}")
        break
# Affiche: Trouvé: 15
```

### `continue` - Passer à l'Itération Suivante

```python
# Ignorer certains elements
nombres = [1, 2, 3, 4, 5, 6]
for n in nombres:
    if n % 2 == 0:  # Skip les pairs
        continue
    print(n)  # Affiche: 1, 3, 5
```

---

## 5. La Clause `else` dans les Boucles

```python
# else s'execute si la boucle se termine normalement (sans break)

# Exemple 1: Recherche trouvee
nombres = [1, 3, 5, 7, 9]
for n in nombres:
    if n == 10:
        print("Trouvé!")
        break
else:
    print("Non trouvé dans la liste")
# Affiche: Non trouvé dans la liste

# Exemple 2: Verification complete
nombres = [2, 4, 6, 8]
for n in nombres:
    if n % 2 != 0:
        print(f"{n} est impair")
        break
else:
    print("Tous les nombres sont pairs")
# Affiche: Tous les nombres sont pairs
```

---

## 6. Boucles Imbriquées

```python
# Table de multiplication
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)

# Parcourir une matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for rangee in matrice:
    for element in rangee:
        print(element, end=" ")
    print()
```

---

## 7. Compréhensions de Listes (Introduction)

```python
# Methode traditionnelle
carres = []
for i in range(10):
    carres.append(i ** 2)

# Comprehension de liste
carres = [i ** 2 for i in range(10)]

# Avec condition
pairs = [i for i in range(20) if i % 2 == 0]

# Comprehension avec condition ternaire
etats = ["pair" if i % 2 == 0 else "impair" for i in range(5)]
# ['pair', 'impair', 'pair', 'impair', 'pair']
```

---

## 8. Fonctions Utiles avec `zip()`

```python
# Iterer sur plusieurs listes en meme temps
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
villes = ["Paris", "Lyon", "Marseille"]

for nom, age, ville in zip(noms, ages, villes):
    print(f"{nom}, {age} ans, habite a {ville}")
```

---

## Points Clés à Retenir

| Concept | Usage |
|---------|-------|
| `for x in sequence` | Iterer sur une sequence |
| `while condition` | Iterer tant qu'une condition est vraie |
| `range(debut, fin, pas)` | Generer une suite de nombres |
| `enumerate()` | Obtenir index et valeur |
| `break` | Sortir de la boucle |
| `continue` | Passer a l'iteration suivante |
| `else` dans for/while | Execute si pas de break |
| `zip()` | Iterer sur plusieurs sequences |

---

## Erreurs Courantes

```python
# ERREUR: Oublier d'incrementer le compteur
compteur = 0
while compteur < 5:
    print(compteur)
    # compteur += 1  # OUBLI!

# CORRECT
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# ERREUR: Modifier la liste pendant l'iteration
nombres = [1, 2, 3, 4, 5]
for n in nombres:
    if n == 3:
        nombres.remove(n)  # Comportement indefini!

# CORRECT: Utiliser une copie
nombres = [1, 2, 3, 4, 5]
for n in nombres[:]:  # Copie de la liste
    if n == 3:
        nombres.remove(n)
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous decouvrirez les **listes et tuples** pour organiser vos donnees en sequences.
