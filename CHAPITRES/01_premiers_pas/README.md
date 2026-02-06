# Chapitre 1: Premiers Pas avec Python

## Ce que vous allez apprendre

Dans ce chapitre, vous allez découvrir:
- Qu'est-ce que Python et pourquoi l'apprendre
- Comment installer Python sur votre ordinateur
- Configurer VS Code pour programmer confortablement
- Écrire et exécuter votre premier script Python
- Comprendre la syntaxe de base du langage

---

## 1. Introduction à Python

### Qu'est-ce que Python?

Python est un langage de programmation créé en 1991 par Guido van Rossum. Il est devenu l'un des langages les plus populaires au monde grâce à sa philosophie axée sur la lisibilité et la simplicité.

**Les forces de Python:**

| Avantage | Description |
|----------|-------------|
| **Syntaxe claire** | Code facile à lire et à comprendre |
| **Polyvalent** | Web, IA, automation, data science, jeux... |
| **Vaste écosystème** | Des milliers de bibliothèques disponibles |
| **Communauté** | Aide abondante et ressources gratuites |
| **Multiplateforme** | Fonctionne sur Windows, Mac, Linux |

### Pourquoi Python pour l'IA?

Python domine le monde de l'intelligence artificielle car:
- Bibliothèques puissantes: TensorFlow, PyTorch, scikit-learn
- Manipulation de données facile: NumPy, Pandas
- Prototypage rapide
- Intégration avec d'autres langages

---

## 2. Installation de Python

### Vérifier si Python est installé

Ouvrez un terminal (invite de commandes) et tapez:

```bash
# Sur Linux/Mac
python3 --version

# Sur Windows
python --version
```

Si vous voyez `Python 3.12.x` ou une version similaire, Python est installé.

### Installation si nécessaire

**Windows:**
1. Aller sur [python.org/downloads](https://python.org/downloads)
2. Télécharger Python 3.12
3. Exécuter l'installeur en cochant "Add Python to PATH"
4. Cliquer sur "Install Now"

**macOS:**
```bash
brew install python@3.12
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.12 python3-pip
```

---

## 3. Votre Premier Script Python

### Écrire le code

Créez un fichier nommé `bonjour.py` et écrivez:

```python
# Ceci est un commentaire - Python l'ignore
# Les commentaires servent à expliquer votre code

# Afficher un message à l'écran
print("Bonjour, monde!")
print("Bienvenue dans votre apprentissage Python")

# Les calculs sont effectués directement
print(2 + 2)  # Affiche 4
print(10 * 5)  # Affiche 50
```

### Exécuter le script

```bash
# Dans le terminal
python bonjour.py

# Sur certains systèmes
python3 bonjour.py
```

**Résultat attendu:**
```
Bonjour, monde!
Bienvenue dans votre apprentissage Python
4
50
```

---

## 4. La Fonction print()

La fonction `print()` est utilisée pour afficher des informations à l'écran.

### Syntaxe de base

```python
# Afficher du texte
print("Hello World")
print('Les guillemets simples fonctionnent aussi')

# Afficher des nombres
print(42)
print(3.14159)

# Afficher plusieurs éléments avec sep et end
print("A", "B", "C")           # Par défaut: A B C (espaces)
print("A", "B", "C", sep="-")  # A-B-C (séparateur personnalisé)
print("Bonjour", end=" ")       # Pas de retour à la ligne
print("le monde!")              # Affiche: Bonjour le monde!
```

### Les_caractères_échappés

Pour afficher des caractères spéciaux:

```python
print("Aller à la ligne\nNouvelle ligne")
print("Une\ttabulation")
print("Les guimets: \"texte entre guillemets\"")
print("Antislash: \\")
```

**Résultat:**
```
Aller à la ligne
Nouvelle ligne
Une	tabulation
Les guimets: "texte entre guillemets"
Antislash: \
```

---

## 5. Les Variables

Une variable est comme une boîte étiquetée qui stocke une valeur.

### Créer une variable

```python
# Affectation simple
nom = "Alice"
age = 25
taille = 1.65
est_etudiant = True

# Afficher les variables
print(nom)
print(age)
print(taille)
print(est_etudiant)
```

### Règles de nommage

| Valide | invalide | Raison |
|--------|----------|--------|
| `nom` | `123nom` | Ne peut pas commencer par un chiffre |
| `age_utilisateur` | `age-utilisateur` | Pas de tiret (confusion avec soustraction) |
| `PRIX_MAX` | `class` | Ne peut pas utiliser les mots-clés Python |
| `_secret` | `ma variable` | Pas d'espace |

### Bonnes pratiques de nommage

```python
# snake_case pour les variables et fonctions
prix_total = 100
calculer_moyenne = lambda x: sum(x) / len(x)

# PascalCase pour les classes
class GestionnaireUtilisateur:
    pass

# UPPER_SNAKE_CASE pour les constantes
TAUX_TVA = 0.20
NOMBRE_MAX_TENTATIVES = 3
```

---

## 6. Les Types de Données Fondamentaux

Python possède plusieurs types de données de base.

### Les entiers (int)

```python
# Nombres entiers (positifs, négatifs, zéro)
age = 30
temperature = -5
compteur = 0

# Opérations
addition = 10 + 5          # 15
soustraction = 20 - 8       # 12
multiplication = 6 * 7      # 42
division = 15 / 3          # 5.0 (toujours float!)
division_entiere = 15 // 3  # 5 (entier)
reste = 15 % 4             # 1 (modulo)
puissance = 2 ** 10        # 1024
```

### Les nombres à virgule (float)

```python
# Nombres décimaux
pi = 3.14159
prix = 19.99
temperature = -5.5

# Notation scientifique
grand_nombre = 1.5e10       # 15000000000.0
petit_nombre = 1e-5         # 0.00001

# Arrondir
rounded = round(3.14159, 2)  # 3.14
```

### Les chaînes de caractères (str)

```python
# Créer une chaîne
message = "Bonjour"
autre = 'Les guillemets simples aussi'
long = """Chaîne
sur
plusieurs
lignes"""

# Concaténation
prenom = "Alice"
bonjour = "Bonjour " + prenom  # "Bonjour Alice"

# Répétition
rire = "ha" * 3  # "hahaha"
```

### Les booléens (bool)

```python
# Vrai ou Faux
est_vrai = True
est_faux = False

# Opérations logiques
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

---

## 7. Interaction avec l'Utilisateur

### La fonction input()

```python
# Demander une information à l'utilisateur
nom = input("Quel est votre nom? ")
print("Bonjour, " + nom + "!")

# Demander un nombre
age = input("Quel est votre âge? ")
age = int(age)  # Convertir en entier
print("L'année prochaine, vous aurez", age + 1, "ans")

# Calculatrice simple
nombre1 = float(input("Premier nombre: "))
nombre2 = float(input("Deuxième nombre: "))
somme = nombre1 + nombre2
print("La somme est:", somme)
```

---

## 8. Exemples de Code Détaillés

### Exemple 1: Présentation Personnelle

```python
# Demander les informations
prenom = input("Prénom: ")
nom = input("Nom: ")
age = int(input("Âge: "))
ville = input("Ville: ")

# Créer un message de présentation
presentation = f"""
=======================================
       INFORMATIONS PERSONNELLES
=======================================
Prénom: {prenom}
Nom:    {nom}
Âge:    {age} ans
Ville:  {ville}
=======================================
"""

print(presentation)

# Calculer l'année de naissance (approximatif)
import datetime
annee_actuelle = datetime.date.today().year
annee_naissance = annee_actuelle - age
print(f"Année de naissance estimée: {annee_naissance}")
```

### Exemple 2: Calculateur de Surface

```python
# Calculer l'aire d'un rectangle
longueur = float(input("Longueur du rectangle: "))
largeur = float(input("Largeur du rectangle: "))

# Calculer l'aire et le périmètre
aire = longueur * largeur
perimetre = 2 * (longueur + largeur)

print(f"\nRectangle de {longueur} x {largeur}")
print(f"Surface (aire): {aire}")
print(f"Périmètre: {perimetre}")
```

---

## Points Clés à Retenir

| Concept | Description |
|---------|-------------|
| `print()` | Affiche du texte à l'écran |
| `input()` | Demande une information à l'utilisateur |
| Variables | Stockent des valeurs avec un nom |
| Types: `int`, `float`, `str`, `bool` | Types de données fondamentaux |
| `+`, `-`, `*`, `/`, `//`, `%`, `**` | Opérateurs arithmétiques |
| f-strings | Formater du texte avec variables: `f"{x}"` |
| `int()`, `float()`, `str()` | Convertir entre types |

---

## Ressources Complémentaires

- [Documentation Python - print()](https://docs.python.org/fr/3/library/functions.html#print)
- [Documentation Python - input()](https://docs.python.org/fr/3/library/functions.html#input)
- [Tutoriel Python officiel](https://docs.python.org/fr/3/tutorial/)

---

## Prochain Chapitre

Dans le chapitre suivant, vous allez approfondir les **variables et types de données** pour comprendre comment Python manipule différentes kinds d'informations.

---

*Félicitations! Vous avez écrit vos premiers scripts Python! 🐍*
