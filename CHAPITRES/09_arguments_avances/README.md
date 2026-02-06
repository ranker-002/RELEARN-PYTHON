# Chapitre 9 : Arguments Avancés - Flexibilité Maximale

## Introduction

Python permet de créer des fonctions très flexibles avec les arguments.

---

## 1. *args (arguments variables)

```python
# *args = tuple avec tous les arguments
def somme(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

print(somme(1, 2, 3))      # 6
print(somme(1, 2, 3, 4, 5))  # 15
print(somme())               # 0
```

---

## 2. **kwargs (arguments nommés)

```python
# **kwargs = dictionnaire avec tous les arguments nommés
def presenter(**info):
    for cle, valeur in info.items():
        print(f"{cle}: {valeur}")

presenter(nom="Alice", age=25, ville="Paris")
# nom: Alice
# age: 25
# ville: Paris
```

---

## 3. Combiner *args et **kwargs

```python
def tout_capturer(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

tout_capturer(1, 2, 3, nom="Alice", age=25)
# Args: (1, 2, 3)
# Kwargs: {'nom': 'Alice', 'age': 25}
```

---

## 4. Arguments par position ou par nom

```python
# Arguments uniquement par position (avant le /)
def diviser(a, b, /):
    return a / b

# Arguments uniquement par nom (après le *)
def afficher(*, nom, age):
    print(f"{nom}, {age} ans")

diviser(10, 2)    # OK
# diviser(a=10, b=2)  # ERREUR !

afficher(nom="Alice", age=25)  # OK
# afficher("Alice", 25)  # ERREUR !
```

---

## Exercices

1. Crée une fonction qui accepte n'importe quel nombre d'arguments
