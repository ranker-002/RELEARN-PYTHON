# Chapitre 8 : Les Fonctions - Réutiliser ton Code

## Introduction : Pourquoi les fonctions ?

Une fonction est un bloc de code réutilisable. Au lieu d'écrire le même code plusieurs fois, tu le defines une fois et tu l'appelles quand tu veux !

---

## 1. Définir une fonction

```python
# Définir une fonction
def dire_bonjour():
    print("Bonjour !")

# Appeler la fonction
dire_bonjour()  # Affiche "Bonjour !"
```

---

## 2. Les paramètres

```python
# Fonction avec un paramètre
def dire_bonjour_a(nom):
    print(f"Bonjour {nom} !")

dire_bonjour_a("Alice")  # Bonjour Alice !
dire_bonjour_a("Bob")    # Bonjour Bob !

# Fonction avec plusieurs paramètres
def presenter(nom, age):
    print(f"Je m'appelle {nom} et j'ai {age} ans.")

presenter("Alice", 25 3. Les)
```

---

## valeurs de retour

```python
# Fonction qui retourne une valeur
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # 8
```

---

## 4. Les paramètres par défaut

```python
# Valeur par défaut si non spécifié
def saluer(nom="inconnu"):
    print(f"Bonjour {nom}")

saluer()           # Bonjour inconnu
saluer("Alice")    # Bonjour Alice
```

---

## 5. La portée des variables (scope)

```python
# Variable globale
message = "Hello"

def afficher():
    # Variable locale (n'existe que dans la fonction)
    local = "World"
    print(message)   # OK, accède à la globale
    print(local)     # OK

afficher()
# print(local)  # ERREUR ! Variable locale n'existe pas ici
```

---

## 6. Les fonctions lambda (functions anonymes)

```python
# Lambda = fonction courte sur une ligne
carre = lambda x: x ** 2
print(carre(5))  # 25

# Avec map()
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
print(carres)  # [1, 4, 9, 16, 25]
```

---

## 7. La documentation (docstring)

```python
def calculer_tva(prix, taux=0.20):
    """Calcule le montant de TVA.
    
    Args:
        prix: Le prix hors taxes
        taux: Le taux de TVA (défaut: 20%)
    
    Returns:
        Le montant de la TVA
    """
    return prix * taux
```

---

## Exercices

1. Crée une fonction qui calcule la factorielle
2. Crée une fonction qui vérifie si un mot est un palindrome
