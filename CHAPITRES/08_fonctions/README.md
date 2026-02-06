# Chapitre 8: Fonctions

## Ce que vous allez apprendre

- Définir et appeler des fonctions
- Les paramètres et arguments
- Les valeurs de retour
- Les paramètres par défaut
- Portée des variables (scope)
- Les fonctions lambda
- La documentation des fonctions
- Le pattern early return

---

## 1. Introduction aux Fonctions

### Pourquoi Utiliser des Fonctions?

```python
# Sans fonction - répétition du code
print("Bonjour Alice")
print("Comment allez-vous?")
print("Au revoir!")

print("Bonjour Bob")
print("Comment allez-vous?")
print("Au revoir!")

# Avec fonction - code réutilisable
def saluer(nom):
    print(f"Bonjour {nom}")
    print("Comment allez-vous?")
    print("Au revoir!")

saluer("Alice")
saluer("Bob")
```

### Définition d'une Fonction

```python
# Syntaxe de base
def nom_de_la_fonction(parametre1, parametre2):
    """Docstring: description de la fonction."""
    # Corps de la fonction
    resultat = parametre1 + parametre2
    return resultat

# Appel de la fonction
somme = nom_de_la_fonction(5, 3)
print(somme)  # 8
```

---

## 2. Paramètres et Arguments

### Paramètres Simple

```python
def afficher_nom(nom):
    print(f"Votre nom est: {nom}")

afficher_nom("Alice")  # "Alice" est l'argument
afficher_nom("Bob")    # "Bob" est l'argument
```

### Paramètres Multiples

```python
def presenter(nom, age, ville):
    print(f"Je m'appelle {nom}, j'ai {age} ans et j'habite à {ville}.")

presenter("Alice", 25, "Paris")
# Arguments positionnels: dans l'ordre des paramètres

presenter(nom="Charlie", age=30, ville="Lyon")
# Arguments nommés: dans n'importe quel ordre
```

### Arguments Mixtes

```python
def calculer(a, b, operateur="+"):
    if operateur == "+":
        return a + b
    elif operateur == "-":
        return a - b

calculer(5, 3)           # OK: 8
calculer(5, 3, "-")       # OK: 2
calculer(5, b=3)          # OK: 8
# calculer(a=5, 3)         # ERREUR: après nommé, tout doit être nommé
```

---

## 3. Valeurs de Retour

### Return Simple

```python
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # 8
```

### Return Multiple (Tuple Unpacking)

```python
def calculer_statistiques(liste):
    total = sum(liste)
    moyenne = total / len(liste)
    return total, moyenne

# Unpacking du retour
somme, moyenne = calculer_statistiques([1, 2, 3, 4, 5])
print(somme)     # 15
print(moyenne)   # 3.0
```

### Return Anticipé (Early Return)

```python
def diviser_securise(a, b):
    if b == 0:
        return "Erreur: division par zéro"
    return a / b

# Avoid "arrow code" (pyramide d'indentation)
# STYLE A EVITER:
def diviser_mauvais(a, b):
    if b != 0:
        if a != 0:
            resultat = a / b
            return resultat
        else:
            return 0
    else:
        return "Erreur"
```

---

## 4. Paramètres par Défaut

```python
def saluer(nom, message="Bonjour"):
    print(f"{message}, {nom}!")

saluer("Alice")              # "Bonjour, Alice!"
saluer("Bob", "Salut")       # "Salut, Bob!"

# Valeurs par défaut mutables - Piège!
def ajouter_element(liste=[]):  # MAUVAIS!
    liste.append("element")
    return liste

# CORRECT: Utiliser None
def ajouter_element(liste=None):  # BON!
    if liste is None:
        liste = []
    liste.append("element")
    return liste
```

---

## 5. Portée des Variables (Scope)

### Variables Locales

```python
def ma_fonction():
    locale = "Je suis locale"
    print(locale)  # Accessible ici

ma_fonction()
# print(locale)  # NameError: locale n'existe pas ici
```

### Variables Globales

```python
globale = "Je suis globale"

def acceder_globale():
    print(globale)  # Accessible en lecture

def modifier_globale():
    global globale
    globale = "Modifiée"  # Utiliser 'global' pour modifier

acceder_globale()
modifier_globale()
print(globale)  # "Modifiée"
```

### Règle LEGB (Portée)

```python
# PortéeLocale > Emballée (Enclosing) > Globale > Built-in

x = "globale"

def fonction_externe():
    x = "emballee"
    
    def fonction_interne():
        x = "locale"
        print(x)  # "locale"
    
    fonction_interne()
    print(x)     # "emballee"

fonction_externe()
print(x)         # "globale"
```

---

## 6. Fonctions Lambda (Anonaymes)

```python
# Fonction classique
def carree(x):
    return x ** 2

# Lambda equivalent
carree = lambda x: x ** 2

# Utilisation
print(carree(5))  # 25

# Avec map()
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x ** 2, nombres))
# [1, 4, 9, 16, 25]

# Avec filter()
pairs = list(filter(lambda x: x % 2 == 0, nombres))
# [2, 4]

# Avec sorted()
points = [(1, 3), (2, 1), (3, 2)]
points_tries = sorted(points, key=lambda p: p[1])
# [(2, 1), (3, 2), (1, 3)]
```

---

## 7. Documentation des Fonctions

```python
def calculer_imc(poids, taille):
    """
    Calcule l'Indice de Masse Corporelle.
    
    Args:
        poids: poids en kilogrammes
        taille: taille en mètres
    
    Returns:
        float: L'IMC calculé
    
    Example:
        >>> calculer_imc(70, 1.75)
        22.86
    """
    imc = poids / (taille ** 2)
    return round(imc, 2)

# Afficher l'aide
print(calculer_imc.__doc__)
help(calculer_imc)
```

---

## 8. Fonctions Built-in Utiles

```python
# Conversion de type
int("42")      # 42
float("3.14")  # 3.14
str(42)        # "42"
bool(1)        # True

# Valeurs absolues et arrondis
abs(-5)        # 5
round(3.7)     # 4
round(3.14159, 2)  # 3.14

# Min/Max
min(1, 2, 3)   # 1
max(1, 2, 3)   # 3
sum([1, 2, 3]) # 6

# Énumération
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)  # 0 a, 1 b, 2 c
```

---

## 9. Style: Early Return

```python
# STYLE RECOMMANDÉ: Early Return
def valider_utilisateur(nom, age, email):
    # Vérifications négatives d'abord
    if not nom:
        return "Erreur: nom requis"
    
    if len(nom) < 2:
        return "Erreur: nom trop court"
    
    if age < 18:
        return "Erreur: doit être majeur"
    
    if "@" not in email:
        return "Erreur: email invalide"
    
    # Succès
    return "Utilisateur valide"


# STYLE A EVITER (Arrow Code)
def valider_utilisateur_mauvais(nom, age, email):
    if nom:
        if len(nom) >= 2:
            if age >= 18:
                if "@" in email:
                    return "Utilisateur valide"
                else:
                    return "Erreur: email invalide"
            else:
                return "Erreur: doit être majeur"
        else:
            return "Erreur: nom trop court"
    else:
        return "Erreur: nom requis"
```

---

## Points Clés à Retenir

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| Définition | `def nom(params):` | `def dire_bonjour():` |
| Paramètres | `def f(a, b=1):` | Valeur par défaut |
| Retour | `return valeur` | Retourne une valeur |
| Lambda | `lambda x: x**2` | Fonction anonayme |
| Appel | `f(1, 2)` | Avec arguments |
| Portée | Local → Global | Variables locales par défaut |

---

## Erreurs Courantes

```python
# ERREUR: Oublier les deux-points
def ma_fonction()  # ERREUR!
    pass

# ERREUR: Modifier une variable globale sans 'global'
compteur = 0
def incrementer():
    compteur += 1  # UnboundLocalError!

# CORRECT: Utiliser 'global' ou retourner
def incrementer():
    global compteur
    compteur += 1

# ERREUR: Paramètres par défaut mutables
def ajout(liste=[]):  # MAUVAIS!
    liste.append(1)
    return liste

# CORRECT
def ajout(liste=None):
    if liste is None:
        liste = []
    liste.append(1)
    return liste
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez les **arguments avancés** (*args, **kwargs, décorateurs).
