# Chapitre 11 : Classes et Objets - La Programmation Orientée Objet

## Introduction : Qu'est-ce que la POO ?

Imagine que tu dois créer un jeu vidéo avec des personnages. Chaque personnage a un nom, une santé, une force, et peut accomplir des actions comme attaquer ou se défendre.

Sans la programmation orientée objet, tu crérais probablement des variables séparées pour chaque personnage et des fonctions pour gérer leurs actions :

```python
# Approche traditionnelle (sans POO)
nom_hero = "Aragorn"
sante_hero = 100
force_hero = 25

nom_ennemi = "Sauron"
sante_ennemi = 500
force_ennemi = 80

def attaquer(attaquant, cible, force_attaquant):
    print(f"{attaquant} attaque {cible} avec {force_attaquant} de force!")
```

Cette approche pose problème quand tu as beaucoup de personnages :
- C'est difficile à maintenir (chaque personnage a ses propres variables)
- C'est facile de faire des erreurs (oublier une variable)
- C'est répétitif (le même code pour chaque personnage)

La programmation orientée objet (POO) résout ce problème en regroupant les données ET les comportements ensemble. Un "personnage" devient une entité autonome qui contient ses propres données et sait comment accomplir ses actions.

---

## 1. Le Concept de Classe

### Qu'est-ce qu'une classe ?

Une **classe** est comme un plan de construction ou un molde. C'est une définition abstraite qui décrit ce que sera un objet.

Pense à une classe comme une recette de cuisine :
- La recette dit quels ingrédients utiliser et comment les préparer
- Mais ce n'est pas un plat concret, c'est juste les instructions
- À partir d'une recette, tu peux préparer plusieurs exemplaires identiques

L'**objet** (ou **instance**) est le résultat concret : le plat préparé à partir de la recette.

### Exemple simple : Une classe Chat

Imaginons que tu veuilles représenter des chats dans ton programme. Tous les chats ont :
- Un nom
- Une race
- Un âge
- Ils peuvent miauler

Voici comment on définit cela avec une classe :

```python
class Chat:
    """Cette classe représente un chat."""
    
    # Cette méthode est appelée quand on crée un nouveau chat
    def __init__(self, nom, race, age):
        # self.nom est l'attribut "nom" de ce chat particulier
        self.nom = nom
        self.race = race
        self.age = age
    
    # Cette méthode permet au chat de miauler
    def miauler(self):
        print(f"{self.nom} dit : Miaou!")
    
    # Cette méthode affiche les infos du chat
    def presenter(self):
        print(f"Je m'appelle {self.nom}, je suis un {self.race} et j'ai {self.age} ans.")
```

Analysons ce code pas à pas :

1. `class Chat:` - On déclare une nouvelle classe appelée "Chat"
2. `def __init__(self, nom, race, age):` - C'est le **constructeur**. Il est automatiquement appelé quand on crée un nouveau chat. `self` représente l'objet qu'on est en train de créer.
3. `self.nom = nom` - On stocke le nom dans l'objet. Le premier `self.nom` est l'attribut de l'objet, le second (après le =) est le paramètre reçu.
4. Les autres méthodes définissent ce que le chat peut faire.

### Créer des objets à partir d'une classe

Une fois la classe définie, on peut créer autant de "chats" (objets) qu'on veut :

```python
# Création du premier chat
felix = Chat("Félix", "Europeen", 3)
felix.miauler()      # Félix dit : Miaou!
felix.presenter()    # Je m'appelle Félix, je suis un Europeen et j'ai 3 ans.

# Création du deuxième chat
minette = Chat("Minette", "Siamoise", 5)
minette.miauler()    # Minette dit : Miaou!
minette.presenter()  # Je m'appelle Minette, je suis un Siamoise et j'ai 5 ans.

# Changement d'âge de Félix
felix.age = 4
felix.presenter()    # Je m'appelle Félix, je suis un Europeen et j'ai 4 ans.
```

Remarque importante : chaque chat est indépendant. Modifier l'âge de Félix n'affecte pas Minette.

---

## 2. Comprendre `self`

### Pourquoi `self` est-il nécessaire ?

C'est une question qu'on se pose tous au début ! `self` représente **l'objet courant** - celui sur lequel on appelle la méthode.

Quand tu écris `felix.miauler()`, Python fait en réalité ceci en interne :

```python
Chat.miauler(felix)  # C'est comme ça que Python voit l'appel
```

`self` permet à chaque méthode de savoir sur quel objet elle travaille. Si on n'avait pas `self`, la méthode ne saurait pas quel chat elle doit faire miauler !

### Exemple concret pour comprendre `self`

Regarde cet exemple :

```python
class Compteur:
    def __init__(self):
        self.valeur = 0
    
    def incrementer(self):
        self.valeur += 1
        return self.valeur
    
    def afficher(self):
        print(f"Valeur actuelle : {self.valeur}")

# Création de deux compteurs indépendants
c1 = Compteur()
c2 = Compteur()

c1.incrementer()  # c1.valeur devient 1
c1.incrementer()  # c1.valeur devient 2
c2.incrementer()  # c2.valeur devient 1

c1.afficher()  # Affiche : Valeur actuelle : 2
c2.afficher()  # Affiche : Valeur actuelle : 1
```

Sans `self`, chaque méthode ne saurait pas quel compteur modifier. `self` est comme un "je" pour l'objet : quand un compteur dit "ma valeur", il parle de sa propre valeur grâce à `self`.

---

## 3. Les Attributs et Méthodes

### Attributs : les données de l'objet

Un **attribut** est une variable stockée dans un objet. Il représente une caractéristique de l'objet.

Il existe deux types d'attributs :

#### Attributs d'instance
Ce sont les attributs uniques à chaque objet. Ils sont définis dans `__init__` avec `self` :

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque    # Attribut d'instance
        self.modele = modele    # Attribut d'instance
        self.kilometres = 0     # Valeur par défaut
```

Chaque voiture a ses propres valeurs pour ces attributs.

#### Attributs de classe
Ce sont des attributs partagés par toutes les instances de la classe :

```python
class Voiture:
    nombre_de_roues = 4  # Attribut de classe
    
    def __init__(self, marque):
        self.marque = marque  # Attribut d'instance

# Même valeur pour toutes les instances
print(Voiture.nombre_de_roues)  # 4
ma_voiture = Voiture("Toyota")
print(ma_voiture.nombre_de_roues)  # 4 (accedé via l'instance aussi)
```

### Méthodes : les actions de l'objet

Une **méthode** est une fonction définie dans une classe. Elle représente ce que l'objet peut faire.

```python
class CompteBancaire:
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0
    
    def deposer(self, montant):
        """Ajoute de l'argent au compte."""
        self.solde += montant
        print(f"Dépôt de {montant}€. Nouveau solde : {self.solde}€")
    
    def retirer(self, montant):
        """Retire de l'argent du compte si possible."""
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant}€. Nouveau solde : {self.solde}€")
        else:
            print("Solde insuffisant!")
    
    def afficher_solde(self):
        """Affiche le solde actuel."""
        print(f"Solde de {self.titulaire} : {self.solde}€")
```

---

## 4. Les Propriétés (`@property`)

### Le problème des attributs publics

Par défaut, les attributs sont accessibles directement :

```python
class Personne:
    def __init__(self, nom):
        self.nom = nom

p = Personne("Alice")
print(p.nom)  # Accès direct - OK
p.nom = ""    # Problème ! Un nom vide n'a pas de sens
```

Comment empêcher quelqu'un de mettre un nom vide ? Ou un âge négatif ? Les **propriétés** permettent de contrôler l'accès aux attributs.

### Créer une propriété

Une propriété agit comme un intermédiaire entre l'utilisateur et l'attribut :

```python
class Personne:
    def __init__(self, nom, age):
        self._nom = nom    # Attribut "protégé" (convention)
        self._age = age
    
    @property
    def nom(self):
        """Getter pour le nom."""
        return self._nom
    
    @nom.setter
    def nom(self, valeur):
        """Setter pour le nom avec validation."""
        if not valeur:
            raise ValueError("Le nom ne peut pas être vide!")
        self._nom = valeur
    
    @property
    def age(self):
        """Getter pour l'âge."""
        return self._age
    
    @age.setter
    def age(self, valeur):
        """Setter pour l'âge avec validation."""
        if valeur < 0:
            raise ValueError("L'âge ne peut pas être négatif!")
        if valeur > 150:
            raise ValueError("L'âge semble irréaliste!")
        self._age = valeur

# Utilisation
p = Personne("Alice", 25)
print(p.nom)   # Appel du getter - affiche "Alice"
print(p.age)   # Appel du getter - affiche 25

p.nom = "Bob"          # Appel du setter - OK
p.age = 30             # Appel du setter - OK
# p.nom = ""            # ValueError: Le nom ne peut pas être vide!
# p.age = -5            # ValueError: L'âge ne peut pas être négatif!
```

L'utilisation reste simple (`p.nom` et `p.age` comme avant), mais maintenant le code vérifie les valeurs avant de les accepter !

### Propriétés calculées

Parfois, un attribut n'est pas stocké mais calculé à la demande :

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    @property
    def aire(self):
        """Calcule l'aire au moment de la demande."""
        return self.largeur * self.hauteur
    
    @property
    def perimetre(self):
        """Calcule le périmètre."""
        return 2 * (self.largeur + self.hauteur)
    
    @property
    def est_carre(self):
        """Vérifie si c'est un carré."""
        return self.largeur == self.hauteur

r = Rectangle(5, 3)
print(r.aire)         # 15 (calculé)
print(r.perimetre)    # 16 (calculé)
print(r.est_carre)    # False (calculé)
```

---

## 5. Les Méthodes de Classe et Statiques

### Méthodes d'instance (standard)

Ce sont les méthodes qu'on a vues jusqu'ici. Elles reçoivent `self` et peuvent accéder à tous les attributs de l'objet :

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
    
    def presenter(self):  # Méthode d'instance
        print(f"Je suis une {self.marque} {self.modele}")
```

### Méthodes de classe (`@classmethod`)

Une méthode de classe reçoit la **classe elle-même** comme premier argument (conventionnellement `cls`). Elle permet de créer des instances de manière alternative :

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @classmethod
    def depuis_fahrenheit(cls, fahrenheit):
        """Crée une Temperature depuis une valeur en Fahrenheit."""
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)
    
    @classmethod
    def depuis_kelvin(cls, kelvin):
        """Crée une Temperature depuis une valeur en Kelvin."""
        celsius = kelvin - 273.15
        return cls(celsius)
    
    def afficher(self):
        print(f"{self.celsius}°C")

# Utilisation des méthodes de classe
temp1 = Temperature(25)                    # Depuis Celsius
temp2 = Temperature.depuis_fahrenheit(77)   # 25°C (77°F = 25°C)
temp3 = Temperature.depuis_kelvin(300)      # ~26.85°C

temp1.afficher()  # 25°C
temp2.afficher()  # 25°C
temp3.afficher()  # 26.85°C
```

### Méthodes statiques (`@staticmethod`)

Une méthode statique n'a accès ni à `self` ni à `cls`. Elle est essentiellement une fonction normale rangée dans la classe pour des raisons d'organisation :

```python
class MathUtils:
    @staticmethod
    def est_pair(n):
        """Vérifie si un nombre est pair."""
        return n % 2 == 0
    
    @staticmethod
    def factorielle(n):
        """Calcule la factorielle."""
        if n <= 1:
            return 1
        return n * MathUtils.factorielle(n - 1)
    
    @staticmethod
    def convertir_en_pourcentage(valeur, total):
        """Convertit une valeur en pourcentage."""
        if total == 0:
            return 0
        return round(valeur / total * 100, 2)

# Appel sans créer d'instance !
print(MathUtils.est_pair(10))        # True
print(MathUtils.factorielle(5))       # 120
print(MathUtils.convertir_en_pourcentage(3, 10))  # 30.0
```

---

## 6. Le Cycle de Vie des Objets

### Création : `__init__`

Quand on crée un objet, `__init__` est automatiquement appelé :

```python
class Animal:
    def __init__(self, nom):
        print(f"L'animal {nom} est créé!")
        self.nom = nom

mon_chien = Animal("Rex")  # Affiche : L'animal Rex est créé!
```

### Représentation : `__str__` et `__repr__`

Ces méthodes définissent comment l'objet s'affiche :

```python
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
    
    def __str__(self):
        """Pour l'affichage lisible par un humain."""
        return f"'{self.titre}' par {self.auteur} ({self.annee})"
    
    def __repr__(self):
        """Pour le debugging (représentation technique)."""
        return f"Livre('{self.titre}', '{self.auteur}', {self.annee})"

livre = Livre("1984", "George Orwell", 1949)

print(str(livre))    # Affiche : '1984' par George Orwell (1949)
print(repr(livre))   # Affiche : Livre('1984', 'George Orwell', 1949)
```

**Différence importante** :
- `__str__` est pour l'utilisateur final (lisible)
- `__repr__` est pour les développeurs (technique, doit permettre de recréer l'objet)

### Destruction : `__del__`

Quand un objet n'est plus utilisé et va être supprimé de la mémoire, `__del__` peut être appelé :

```python
class Fichier:
    def __init__(self, nom):
        self.nom = nom
        print(f"Fichier {nom} ouvert")
    
    def __del__(self):
        print(f"Fichier {self.nom} fermé")

f = Fichier("donnees.txt")  # Affiche : Fichier donnees.txt ouvert
del f                        # Affiche : Fichier donnees.txt fermé
```

---

## 7. Résumé et Tableau de Référence

| Concept | Syntaxe | À quoi ça sert |
|---------|---------|----------------|
| Classe | `class MaClasse:` | Définir un nouveau type |
| Constructeur | `def __init__(self, ...):` | Initialiser un nouvel objet |
| Attribut d'instance | `self.attribut = valeur` | Donnée propre à chaque objet |
| Attribut de classe | `attribut = valeur` | Donnée partagée par toutes les instances |
| Méthode | `def methode(self):` | Action que l'objet peut faire |
| @property | `@property` | Contrôler l'accès aux attributs |
| @classmethod | `@classmethod` | Méthode de classe (reçoit `cls`) |
| @staticmethod | `@staticmethod` | Fonction liée à la classe (pas de `self`/`cls`) |
| `__str__` | `def __str__(self):` | Représentation lisible |
| `__repr__` | `def __repr__(self):` | Représentation technique |

---

## Erreurs Courantes à Éviter

### 1. Oublier `self` dans une méthode

```python
# MAUVAIS
class Mauvais:
    def methode(self):
        return self.valeur  # OK
    
    def autre(self):
        return valeur  # ERREUR! Pas de 'self'

# CORRECT
class Bon:
    def methode(self):
        return self.valeur
```

### 2. Confondre attribut et paramètre

```python
# MAUVAIS
class Exemple:
    def __init__(self, valeur):
        valeur = valeur  # Écrase le paramètre!

# CORRECT
class Exemple:
    def __init__(self, valeur):
        self.valeur = valeur  # Stocke dans l'attribut
```

### 3. Modifier un attribut sans passer par `self`

```python
# MAUVAIS
class Exemple:
    def modifier(self):
        nouvel_attribut = 42  # Crée une variable locale, pas un attribut!

# CORRECT
class Exemple:
    def modifier(self):
        self.nouvel_attribut = 42  # Crée l'attribut sur l'objet
```

---

## Exercices Pratiques

### Exercice 1 : Classe Simple
Crée une classe `Chien` avec un nom et une race, et une méthode `aboyer()`.

### Exercice 2 : Constructeur
Crée une classe `Rectangle` avec largeur et hauteur, et une méthode `aire()`.

### Exercice 3 : Propriété
Crée une classe `Temperature` avec un attribut Celsius protégé et une propriété Fahrenheit.

### Exercice 4 : Méthode de Classe
Crée une classe `Date` avec une méthode de classe `aujourd'hui()` qui retourne la date du jour.

---

## Prochain Chapitre

Maintenant que tu maîtrises les classes et objets, passons au **chapitre 12 : Héritage et Polymorphisme**. Tu apprendras comment créer des relations entre classes pour organiser encore mieux ton code !
