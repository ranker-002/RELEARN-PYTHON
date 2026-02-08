# Chapitre 5 : Les Boucles - Répéter des Actions

## Introduction : Pourquoi les boucles ?

Imagine que tu doives afficher "Bonjour" 100 fois. Tu ne vas quand même pas écrire 100 fois `print("Bonjour")` ! Les boucles permettent de répéter une action plusieurs fois.

---

## 1. La boucle for (pour)

```python
# Afficher chaque fruit
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(f"J'aime les {fruit}")

# Parcourir une chaîne
mot = "Python"
for lettre in mot:
    print(lettre)
```

---

## 2. La fonction range()

```python
# Compter de 0 à 4 (5 nombres)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Compter de 2 à 5
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# Compter de 0 à 10, de 2 en 2
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10
```

---

## 3. La boucle while (tant que)

```python
# Tant que la condition est vraie, on continue
compteur = 0
while compteur < 5:
    print(compteur)
    compteur = compteur + 1
```

**ATTENTION :** Si la condition ne devient jamais fausse, la boucle ne s'arrête jamais !

```python
# MAUVAIS (boucle infinie !)
while True:
    print("Pour toujours...")  # NE FAIS PAS ÇA !
```

---

## 4. break et continue

```python
# break : sortir de la boucle
for i in range(10):
    if i == 5:
        break  # Arrête quand i atteint 5
    print(i)

# continue : passer à l'itération suivante
for i in range(5):
    if i == 2:
        continue  # Saute le 2
    print(i)  # Affiche 0, 1, 3, 4
```

---

## 5. enumerate() - Index et Valeur

Quand tu as besoin de l'index ET de la valeur :

```python
fruits = ["pomme", "banane", "orange"]

# Méthode classique (moins élégante)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Méthode avec enumerate (mieux !)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Commencer à un index différent
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### Exemple Pratique

```python
scores = [85, 92, 78, 90, 88]

for rang, score in enumerate(sorted(scores, reverse=True), 1):
    print(f"{rang}ème: {score} points")
```

---

## 6. zip() - Parcourir Plusieurs Listes

Itère sur plusieurs listes en parallèle :

```python
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
villes = ["Paris", "Lyon", "Marseille"]

# Sans zip (moins lisible)
for i in range(len(noms)):
    print(f"{noms[i]}, {ages[i]} ans, {villes[i]}")

# Avec zip (plus propre)
for nom, age, ville in zip(noms, ages, villes):
    print(f"{nom}, {age} ans, {ville}")
```

### zip_longest (listes de tailles différentes)

```python
from itertools import zip_longest

groupes_a = ["Alice", "Bob"]
groupes_b = ["Charlie", "David", "Eve"]

# zip s'arrête à la liste la plus courte
for a, b in zip(groupes_a, groupes_b):
    print(f"{a} vs {b}")
# Affiche seulement Alice vs Charlie, Bob vs David

# zip_longest continue avec None
for a, b in zip_longest(groupes_a, groupes_b, fillvalue="Solo"):
    print(f"{a} vs {b}")
# Alice vs Charlie, Bob vs David, Solo vs Eve
```

---

## 7. Boucles Imbriquées

Une boucle dans une boucle :

```python
# Table de multiplication
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

### Exemple : Matrice

```python
# Afficher une matrice 3x3
for ligne in range(3):
    for colonne in range(3):
        print(f"[{ligne},{colonne}]", end=" ")
    print()
```

### Combiner avec des Conditions

```python
# Triangle d'étoiles
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

---

## 8. Le else dans les Boucles (Peu Connu !)

Le `else` s'exécute quand la boucle termine **normalement** (sans break).

```python
# Recherche dans une liste
fruits = ["pomme", "banane", "orange"]

cherche = "raisin"
for fruit in fruits:
    if fruit == cherche:
        print(f"Trouvé: {fruit}")
        break
else:
    # S'exécute si le break n'a pas été déclenché
    print(f"{cherche} n'est pas dans la liste")
```

### Exemple : Vérifier si Premier

```python
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} divisible par {i}")
            return False
    else:
        print(f"{n} est premier")
        return True

est_premier(17)  # 17 est premier
est_premier(18)  # 18 divisible par 2
```

---

## 9. La Fonction reversed()

Parcourir dans l'ordre inverse :

```python
compte_a_rebours = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for nombre in reversed(compte_a_rebours):
    print(nombre, end="... ")
print("Décollage !")

# Avec chaîne
mot = "Python"
for lettre in reversed(mot):
    print(lettre, end="")
# nohtyP
```

---

## 10. Boucles avec Dictionnaires

```python
utilisateur = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Parcourir les clés
for cle in utilisateur:
    print(cle)

# Parcourir les valeurs
for valeur in utilisateur.values():
    print(valeur)

# Parcourir clés et valeurs
for cle, valeur in utilisateur.items():
    print(f"{cle}: {valeur}")
```

---

## Exercices Pratiques

### Exercice 1 : Table de Multiplication
Affiche la table de multiplication de 1 à 10 (format 10x10).

### Exercice 2 : Devinette avec Limite
Demande à l'utilisateur de deviner un nombre entre 1 et 100.
Il a maximum 7 essais. Affiche "Trop grand", "Trop petit" ou "Gagné !".
Si échec après 7 essais, affiche "Perdu ! Le nombre était X".

### Exercice 3 : Liste des Premiers
Affiche tous les nombres premiers entre 2 et 100.

### Exercice 4 : Analyse de Texte
Demande une phrase et calcule :
- Nombre de mots
- Nombre de caractères (sans espaces)
- Nombre de voyelles
- Mot le plus long

### Exercice 5 : Pyramide
Demande un nombre N et affiche une pyramide d'étoiles avec N étages :
```
   *
  ***
 *****
*******
```

### Exercice 6 : Fusion de Listes
Crée deux listes de noms et d'âges, puis affiche :
"Alice a 25 ans et habite à l'index 0"
Utilise enumerate et zip.

### Exercice 7 : Recherche dans Matrice
Crée une matrice 5x5 avec des nombres aléatoires (1-100).
Demande un nombre à chercher et affiche sa position (ligne, colonne).
Si non trouvé, affiche "Nombre absent".

### Exercice 8 : Menu Interactif
Crée un menu qui s'affiche en boucle :
1. Ajouter un nombre
2. Voir la liste
3. Calculer la moyenne
4. Quitter

Utilise while True avec break.

### Exercice 9 : Pattern d'Étoiles
Demande un nombre N et affiche :
```
*
**
***
****
```
Puis l'inverse :
```
****
***
**
*
```

### Exercice 10 : Anagramme
Demande deux mots et vérifie si ce sont des anagrammes
(mêmes lettres, ordre différent).
Ex: "listen" et "silent" → True

---

## Bonnes Pratiques

### 1. Préférer for à while quand possible
```python
# ❌ While pour parcourir une liste (risque d'erreur)
i = 0
while i < len(liste):
    print(liste[i])
    i += 1

# ✅ For plus simple et sûr
for element in liste:
    print(element)
```

### 2. Éviter les Modifications Pendant l'Itération
```python
# ❌ Danger : modifier la liste pendant la boucle
for i in range(len(liste)):
    if condition:
        liste.pop(i)  # ⚠️ Index décalé !

# ✅ Créer une nouvelle liste
liste = [x for x in liste if not condition]
```

### 3. Utiliser les Fonctions Python
```python
# ❌ Manuel
somme = 0
for nombre in nombres:
    somme += nombre

# ✅ Fonction intégrée
somme = sum(nombres)

# ❌ Manuel
max_val = nombres[0]
for n in nombres:
    if n > max_val:
        max_val = n

# ✅ Fonction intégrée
max_val = max(nombres)
```

---

## Résumé

| Concept | Syntaxe | Usage |
|---------|---------|-------|
| For simple | `for x in liste:` | Parcourir une séquence |
| Range | `range(debut, fin, pas)` | Générer des nombres |
| While | `while condition:` | Tant que condition vraie |
| Break | `break` | Sortir de la boucle |
| Continue | `continue` | Passer à l'itération suivante |
| Enumerate | `enumerate(liste)` | Index + valeur |
| Zip | `zip(liste1, liste2)` | Plusieurs listes |
| Else | `for...else:` | Si pas de break |

---

## Prochain Chapitre

Tu maîtrises les boucles ! Le chapitre suivant sur les **listes et tuples** te permettra de stocker et manipuler des collections de données.
