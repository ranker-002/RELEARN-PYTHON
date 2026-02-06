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

## Exercices

1. Affiche les nombres pairs de 0 à 20
2. Demande un mot de passe jusqu'à ce que ce soit "secret123"
