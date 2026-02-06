# Chapitre 1 : Premiers Pas avec Python - Votre Premier Programme

## Introduction : Pourquoi apprendre à programmer ?

Imagine que tu puisses créer ton propre assistant informatique qui fait exactement ce que tu lui demandes. Tu pourrais automatiser des tâches répétitives, créer des outils personnalisés, ou même construire des applications entières !

La programmation est exactement cela : donner des instructions à un ordinateur pour qu'il accomplisse des tâches pour toi.

Python est un excellent langage pour commencer car :
- Sa syntaxe est proche de l'anglais, donc facile à lire
- Tu peux voir des résultats rapidement
- Il est utilisé partout dans le monde réel

---

## 1. Qu'est-ce que Python ?

### Une histoire simple

Python a été créé par Guido van Rossum en 1991. Le nom ne vient pas du serpent, mais de la série télévisée "Monty Python" que Guido adorait !

Python est devenu l'un des langages les plus populaires au monde parce que :

1. **Lisibilité** : Le code Python ressemble à de l'anglais
2. **Simplicité** : Peu de règles compliquées à retenir
3. **Polyvalence** : Tu peux faire du web, de l'IA, des jeux, de l'analyse de données...
4. **Communauté** : Des millions de développeurs partagent leur code

### Comparons avec d'autres langages

Faisons la même chose dans différents langages :

```python
# Python - Simple et lisible
print("Bonjour le monde!")
```

```java
// Java - Plus verbeux
public class Main {
    public static void main(String[] args) {
        System.out.println("Bonjour le monde!");
    }
}
```

```c
// C - Encore plus complexe
#include <stdio.h>
int main() {
    printf("Bonjour le monde!\n");
    return 0;
}
```

Tu vois la différence ? Python te permet de te concentrer sur ce que tu veux accomplir, pas sur comment l'écrire !

---

## 2. Installer Python sur ton ordinateur

### Comment vérifier si Python est déjà installé ?

Ouvre un terminal (sur Windows : tape "cmd" dans la barre de recherche, sur Mac/Linux : ouvre "Terminal") et tape :

```bash
python --version
```

ou

```bash
python3 --version
```

Si tu vois quelque chose comme `Python 3.12.0`, parfait ! Python est installé.

Si tu vois "command not found" ou une erreur, il faut l'installer.

### Installation pas à pas

**Sur Windows :**
1. Va sur [python.org/downloads](https://python.org/downloads)
2. Clique sur le gros bouton "Download Python"
3. **Important** : Coche la case "Add Python to PATH" en bas !
4. Clique sur "Install Now"
5. Attend que l'installation finisse

**Sur Mac :**
```bash
# Avec Homebrew (le plus simple)
brew install python
```

**Sur Linux (Ubuntu/Debian) :**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Comment savoir si l'installation a marché ?

Ouvre un nouveau terminal et tape :

```bash
python --version
```

Tu devrais voir la version de Python. Ensuite, tape :

```bash
python
```

Tu devrais voir `>>>` - c'est l'interpréteur interactif de Python ! Tape `exit()` pour sortir.

---

## 3. Écrire ton premier programme

### Créer ton premier fichier

Crée un nouveau fichier appelé `bonjour.py` (le `.py` dit à l'ordinateur que c'est un fichier Python).

Ouvre ce fichier avec un éditeur de texte (Notepad, VS Code, ou n'importe quel éditeur) et écris :

```python
# Ceci est un commentaire - Python l'ignore
# Les commentaires servent à expliquer ton code

print("Bonjour le monde!")
print("Bienvenue dans l'univers de la programmation")
```

### Exécuter ton programme

Ouvre un terminal dans le dossier où tu as saved ton fichier et tape :

```bash
python bonjour.py
```

Tu devrais voir :

```
Bonjour le monde!
Bienvenue dans l'univers de la programmation
```

Félicitations ! Tu viens d'exécuter ton premier programme Python !

---

## 4. La fonction print() - Afficher des choses à l'écran

### À quoi ça sert ?

`print()` est comme une imprimante pour ton code. Tout ce que tu mets entre les parenthèses sera affiché à l'écran.

### Les bases

```python
# Afficher du texte - utilise les guillemets
print("Bonjour!")
print('Les guillemets simples fonctionnent aussi')

# Afficher des nombres - pas besoin de guillemets
print(42)
print(3.14159)

# Faire des calculs directement
print(2 + 2)      # Affiche 4
print(10 * 5)     # Affiche 50
print(100 / 10)   # Affiche 10.0
```

### Pourquoi certains nombres ont-ils un point ?

Regarde cet exemple :

```python
print(10 / 2)    # Affiche 5.0 (avec un point)
print(10 // 2)   # Affiche 5 (sans point)
```

En Python :
- `/` fait une division "réelle" (peut donner des décimales)
- `//` fait une division entière (toujours un nombre entier)

### Afficher plusieurs choses

```python
# Séparateur par défaut : espace
print("A", "B", "C")        # A B C

# Changer le séparateur
print("A", "B", "C", sep="-")  # A-B-C

# Changer la fin (par défaut : retour à la ligne)
print("Bonjour", end=" ")
print("le monde!")           # Affiche : Bonjour le monde!
```

---

## 5. Les caractères spéciaux

### Le problème des guillemets

Tu veux afficher ce texte : Il a dit "Bonjour !" Comment écrire ça ?

```python
# ERREUR !
print("Il a dit "Bonjour !"")
# Python pense que "Bonjour !" est un texte, puis : et ! sont autre chose
```

### La solution : l'échappement

```python
# Le \ avant un guillemet dit à Python "c'est pas la fin du texte"
print("Il a dit \"Bonjour !\"")

# Résultat : Il a dit "Bonjour !"
```

### Les caractères spéciaux courants

| Caractère | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `\n` | Nouvelle ligne | `print("Ligne1\nLigne2")` | Ligne1<br>Ligne2 |
| `\t` | Tabulation | `print("A\tB")` | A    B |
| `\\` | Antislash | `print("\\")` | \ |
| `\"` | Guillemet | `print("\"")` | " |
| `\'` | Guillemet simple | `print("\'")` | ' |

---

## 6. Les variables - Stocker des informations

### Qu'est-ce qu'une variable ?

Une variable est comme une boîte avec une étiquette. Tu mets quelque chose dedans, et tu peux le récupérer plus tard en utilisant l'étiquette.

```python
# Créer une variable (une "boîte" appelée "nom")
nom = "Alice"

# Tu peux utiliser la boîte plus tard
print(nom)          # Affiche "Alice"
```

### Les types de variables

```python
# Texte (on appelle ça "string" ou "chaîne de caractères")
prenom = "Alice"
ville = 'Paris'

# Nombre entier (integer ou "int")
age = 25
compteur = 100

# Nombre décimal (floating-point ou "float")
prix = 19.99
taille = 1.75

# Vrai ou Faux (boolean ou "bool")
est_etudiant = True
a_le_permis = False
```

### Changer la valeur

```python
# Une variable peut changer de valeur
score = 0
print(score)    # Affiche 0

score = 100     # Maintenant score vaut 100
print(score)    # Affiche 100

score = score + 50  # score vaut maintenant 150
print(score)    # Affiche 150
```

### Les règles pour nommer tes variables

| Nom valide | Pourquoi ça marche |
|------------|-------------------|
| `nom` | Lettre minuscule, pas d'espace |
| `age_utilisateur` | snake_case (tiret bas) |
| `PRIX_MAX` | MAJUSCULES pour constantes |
| `_secret` | Tiret bas au début (privé) |

| Nom invalide | Pourquoi ça ne marche pas |
|--------------|--------------------------|
| `123nom` | Commence par un chiffre |
| `mon-nom` | Le tiret est une soustraction ! |
| `ma variable` | L'espace n'est pas autorisé |

### Bonnes pratiques

```python
# Convention Python : snake_case (tout en minuscule, tirets bas)
prix_total = 100
nom_utilisateur = "alice"

# Pour les constantes (qui ne changent jamais)
TAUX_TVA = 0.20
NOMBRE_DE_JOURS = 7

# CamelCase aussi acceptable mais moins "pythonique"
# nomUtilisateur = "alice"  (moins utilisé en Python)
```

---

## 7. Récupérer des informations de l'utilisateur

### La fonction input()

`input()` permet à l'utilisateur de taper quelque chose au clavier.

```python
# Demander le nom de l'utilisateur
prenom = input("Comment t'appelles-tu ? ")
print("Bonjour, " + prenom + "!")
```

**Résultat :**
```
Comment t'appelles-tu ? Alice
Bonjour, Alice!
```

### Attention aux types !

`input()` renvoie **toujours** du texte (une chaîne de caractères), même si l'utilisateur tape un nombre !

```python
# ERREUR COURANTE !
age = input("Quel est ton âge ? ")
print("L'année prochaine tu auras", age + 1)
# Si l'utilisateur tape "20", ça affiche "201" au lieu de "21" !
# Python a concaténé "20" et "1" au lieu d'additionner !

# CORRECTION : convertir en nombre
age = int(input("Quel est ton âge ? "))  # int() convertit en entier
print("L'année prochaine tu auras", age + 1)  # Maintenant ça marche !
```

### Les conversions de types

```python
# Texte -> Entier
nombre = int("42")        # 42

# Texte -> Décimal
prix = float("19.99")     # 19.99

# Nombre -> Texte
texte = str(42)           # "42"

# Décimal -> Entier
rounded = int(3.99)      # 3 (ça tronque, pas arrondit !)
```

---

## 8. Un exemple complet : Ton premier vrai programme

Voici un programme qui récupère des informations et fait des calculs :

```python
# === Programme de présentation ===

# Demander les informations à l'utilisateur
print("=== Formulaire de présentation ===")
prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))
ville = input("Dans quelle ville habites-tu ? ")

# Afficher les informations joliment
print("\n" + "=" * 30)
print("       INFORMATIONS")
print("=" * 30)
print(f"Prénom : {prenom}")
print(f"Âge    : {age} ans")
print(f"Ville  : {ville}")
print("=" * 30)

# Faire quelques calculs
age_doubling = age * 2
print(f"\nSi tu avais le double de ton âge, tu aurais {age_doubling} ans.")

# Calculer l'année de naissance (approximatif)
import datetime
annee_actuelle = datetime.date.today().year
annee_naissance = annee_actuelle - age
print(f"Tu es probablement né(e) en {annee_naissance}.")
```

**Résultat possible :**
```
=== Formulaire de présentation ===
Quel est ton prénom ? Alice
Quel est ton âge ? 25
Dans quelle ville habites-tu ? Paris

==============================
       INFORMATIONS
==============================
Prénom : Alice
Âge    : 25 ans
Ville  : Paris
==============================

Si tu avais le double de ton âge, tu aurais 50 ans.
Tu es probablement né(e) en 1999.
```

---

## Résumé de ce chapitre

| Concept | Ce que ça fait | Exemple |
|---------|-----------------|---------|
| `print()` | Affiche quelque chose à l'écran | `print("Bonjour")` |
| `input()` | Récupère ce que tape l'utilisateur | `nom = input("Ton nom ?")` |
| Variable | Stocke une valeur | `age = 25` |
| `int()` | Convertit en entier | `int("42")` → `42` |
| `float()` | Convertit en décimal | `float("3.14")` → `3.14` |
| `str()` | Convertit en texte | `str(42)` → `"42"` |

---

## Erreurs courantes à éviter

### 1. Oublier les guillemets

```python
# ERREUR - Python cherche une variable appelée message
print(message)

# CORRECT
print("message")  # Affiche le texte "message"
```

### 2. Confondre les parenthèses et les crochets

```python
# ERREUR
print["Bonjour"]  # Non !

# CORRECT
print("Bonjour")  # Parenthèses !
```

### 3. Utiliser une variable qui n'existe pas

```python
# ERREUR - la variable "nom" n'a pas été créée
print(nom)

# CORRECT - créer d'abord la variable
nom = "Alice"
print(nom)
```

### 4. Mélanger les types sans conversion

```python
# ERREUR
nombre = input("Un nombre : ")  # "10" (texte)
resultat = nombre + 5           # Erreur ou résultat bizarre !

# CORRECT
nombre = int(input("Un nombre : "))  # 10 (nombre)
resultat = nombre + 5                  # 15
```

---

## Exercices pratiques

### Exercice 1 : Dire bonjour
Écris un programme qui demande le prénom de l'utilisateur et affiche "Bonjour, [prénom] !"

### Exercice 2 : Calculatrice simple
Demande deux nombres à l'utilisateur et affiche leur somme.

### Exercice 3 : Conversion d'âge
Demande l'âge de l'utilisateur et affiche cet âge en mois (approximativement 12×).

### Exercice 4 : Présentation complète
Crée un programme qui demande le nom, l'âge et la ville, puis affiche une présentation formatée.



---

## Prochain Chapitre

Dans le chapitre suivant, nous allons approfondir les **variables et types de données**. Tu apprendras comment Python organise différentes kinds d'informations et comment les manipuler efficacement !

Tu es prêt à continuer ? Allons-y ! 🚀
