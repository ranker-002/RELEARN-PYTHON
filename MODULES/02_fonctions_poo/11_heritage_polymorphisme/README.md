# Chapitre 11 : Héritage et Polymorphisme - Organiser tes Classes

## Introduction : Pourquoi l'Héritage ?

Imagine que tu construis un zoo virtuel. Tu as différents animaux : lions, tigres, singes, éléphants...

Chaque animal a des caractéristiques communes (un nom, un âge, ils peuvent tous dormir) mais aussi des particularités (le lion rugit, le singe grimpe aux arbres, l'éléphant a une trompe).

Sans héritage, tu devrais écrire chaque classe indépendamment, en répétant le code commun :

```python
# Approche sans héritage - très répétitive !
class Lion:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.faim = 0
    
    def dormir(self):
        print(f"{self.nom} le lion dort")
    
    def rugir(self):
        print(f"{self.nom} rugit! ROARRR!")

class Tigre:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.faim = 0
    
    def dormir(self):
        print(f"{self.nom} le tigre dort")
    
    def chasser(self):
        print(f"{self.nom} chasse une proie")
```

Tu remarques que `__init__` et `dormir()` sont identiques ! C'est lourd et difficile à maintenir.

L'**héritage** résout ce problème en permettant à une classe de "hériter" d'une autre. La classe enfant réutilise tout ce que la classe parent définit, et peut ajouter ou modifier ce qu'elle veut.

---

## 1. Le Concept d'Héritage

### Qu'est-ce que l'héritage ?

L'héritage est une relation "est-un" (is-a en anglais). Un lion **est un** animal. Un tigre **est un** animal.

La classe parent (aussi appelée "classe de base" ou "superclasse") contient le code commun.
Les classes enfants (aussi appelées "classes dérivées" ou "sous-classes") héritent de ce code et peuvent l'étendre.

### Exemple concret : Le zoo

```python
# Classe de base - l'animal
class Animal:
    """Classe de base pour tous les animaux."""
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.faim = 0
    
    def dormir(self):
        """Tous les animaux dorment."""
        print(f"{self.nom} dort")
    
    def manger(self):
        """Tous les animaux mangent."""
        self.faim = 0
        print(f"{self.nom} mange")

# Classe dérivée - le lion EST UN animal
class Lion(Animal):
    """Un lion est un animal avec des capacités supplémentaires."""
    
    def __init__(self, nom, age, criniere):
        # super() permet d'appeler le __init__ du parent
        super().__init__(nom, age)
        self.criniere = criniere  # Nouveau paramètre spécifique au lion
    
    def rugir(self):
        """Les lions rugissent!"""
        print(f"{self.nom} rugit! ROARRR!")

# Classe dérivée - le tigre EST UN animal
class Tigre(Animal):
    """Un tigre est un animal avec des capacités supplémentaires."""
    
    def chasser(self):
        """Les tigres chassent."""
        print(f"{self.nom} chasse une proie")
```

Analysons ce code pas à pas :

1. `class Animal:` - C'est la classe parent, la base de tous nos animaux
2. `class Lion(Animal):` - Les parenthèses signifient que Lion hérite d'Animal
3. `super().__init__(nom, age)` - Appelle le constructeur du parent pour initialiser `nom` et `age`

### Utiliser les classes

```python
# Création d'objets
simba = Lion("Simba", 5, True)
tony = Tigre("Tony", 7)

# simba EST UN Animal - il a toutes les méthodes d'Animal
simba.dormir()   # Simba dort (hérité de Animal)
simba.manger()   # Simba mange (hérité de Animal)

# simba a aussi ses propres méthodes
simba.rugir()    # Simba rugit! ROARRR!

# tony EST UN Animal ET un Tigre
tony.dormir()    # Tony dort (hérité)
tony.chasser()   # Tony chasse une proie (méthode de Tigre)
```

---

## 2. La Fonction `super()`

### À quoi sert `super()` ?

`super()` est comme un téléphone qui permet à une classe enfant d'appeler sa classe parent. C'est indispensable quand tu veux ajouter du comportement tout en gardant celui du parent.

### Exemple : Construire sur les épaules du parent

```python
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.vitesse = 0
    
    def accelerer(self, increment):
        self.vitesse += increment
        print(f"{self.marque} accélère. Vitesse: {self.vitesse} km/h")

class Voiture(Vehicule):
    def __init__(self, marque, modele, nombre_portes):
        # Appelle le __init__ de Vehicule pour initialiser marque et modele
        super().__init__(marque, modele)
        # Ensuite on ajoute ce qui est spécifique à Voiture
        self.nombre_portes = nombre_portes
    
    def ouvrir_toit(self):
        print("Toit ouvrant ouvert!")

ma_voiture = Voiture("Tesla", "Model 3", 4)
ma_voiture.accelerer(50)        # Hérité de Vehicule
ma_voiture.ouvrir_toit()        # Spécifique à Voiture
print(ma_voiture.nombre_portes)  # 4
```

Sans `super().__init__()`, les attributs `marque` et `modele` ne seraient pas initialisés !

### `super()` dans les méthodes

Tu peux aussi utiliser `super()` dans les méthodes pour appeler la version du parent :

```python
class Animal:
    def presenter(self):
        print(f"Je suis un animal")

class Chien(Animal):
    def presenter(self):
        # D'abord appeler la version du parent
        super().presenter()
        # Puis ajouter notre propre texte
        print("Plus précisément, je suis un chien!")

medor = Chien()
medor.presenter()
# Affiche:
# Je suis un animal
# Plus précisément, je suis un chien!
```

---

## 3. La Substitution de Méthodes (Override)

### Remplacer une méthode du parent

Parfois, le comportement du parent ne convient pas à l'enfant. On peut alors "substituer" (override) la méthode en la redéfinissant.

```python
class Oiseau:
    def __init__(self, nom):
        self.nom = nom
    
    def parler(self):
        print("L'oiseau fait un bruit")

class Perroquet(Oiseau):
    def parler(self):
        # On remplace complètement la méthode du parent
        print(f"{self.nom} dit: Coucou!")

class Canari(Oiseau):
    def parler(self):
        # Canari a son propre son
        print(f"{self.nom} chante: Cui-cuiiii!")

perroquet = Perroquet("Coco")
canari = Canari("Titi")

perroquet.parler()  # Coco dit: Coucou!
canari.parler()     # Titi chante: Cui-cuiiii!
```

### Combiner parent et enfant

Tu peux appeler le parent PUIS ajouter ton propre comportement :

```python
class Employe:
    def calculer_salaire(self):
        return 2000

class Manager(Employe):
    def calculer_salaire(self):
        # Appelle la méthode du parent
        salaire_base = super().calculer_salaire()
        # Ajoute le bonus
        return salaire_base + 1000

bob = Manager()
print(bob.calculer_salaire())  # 3000 (2000 + 1000)
```

---

## 4. Le Polymorphisme

### Qu'est-ce que le polymorphisme ?

Le mot "polymorphisme" semble compliqué, mais c'est simple : cela signifie "plusieurs formes". Un même message peut être compris différemment par différents objets.

Imagine que tu donnes l'ordre "Parle!" à un chien, un chat et un oiseau :
- Le chien aboie
- Le chat miaule
- L'oiseau chante

Tous ont une méthode `parler()`, mais chacune réagit différemment !

### Exemple concret

```python
# Classe de base
class Animal:
    def parler(self):
        pass  # Chaque animal aura sa propre implémentation

# Différentes sous-classes
class Chien(Animal):
    def parler(self):
        return "Wouf!"

class Chat(Animal):
    def parler(self):
        return "Miaou!"

class Oiseau(Animal):
    def parler(self):
        return "Cui-cui!"

# La magie du polymorphisme
def faire_parler(animal):
    print(f"{type(animal).__name__}: {animal.parler()}")

# Liste d'objets différents
animaux = [Chien(), Chat(), Oiseau()]

# On peut tous les traiter de la même façon !
for animal in animaux:
    faire_parler(animal)
# Affiche:
# Chien: Wouf!
# Chat: Miaou!
# Oiseau: Cui-cui!
```

### Le Duck Typing

Python utilise le "duck typing" (typage canard) : "Si ça marche comme un canard et cancane comme un canard, alors c'est un canard".

```python
class Canard:
    def nager(self):
        print("Le canard nage")

class CanardEnPlastique:
    def nager(self):
        print("Le canard en plastique flotte")

class Roche:
    def nager(self):
        print("La roche... coule?")

# Fonction qui accepte n'importe quel objet avec nager()
def activity_in_water(objet):
    print(f"{type(objet).__name__}:")
    objet.nager()

activity_in_water(Canard())          # Le canard nage
activity_in_water(CanardEnPlastique())  # Le canard en plastique flotte
activity_in_water(Roche())           # La roche... coule?
```

---

## 5. Les Classes Abstraites

### Le problème des classes incomplètes

Parfois, tu veux créer une classe de base qui ne peut pas être utilisée directement. Par exemple, `Animal` ne devrait pas être instancié directement - on devrait toujours créer un type d'animal spécifique.

Les **classes abstraites** permettent cela :

```python
from abc import ABC, abstractmethod

# Héritier de ABC = classe abstraite
class Forme(ABC):
    @abstractmethod
    def aire(self):
        """Cette méthode DOIT être implémentée par les sous-classes."""
        pass
    
    @abstractmethod
    def perimetre(self):
        """Cette méthode aussi."""
        pass
    
    def description(self):
        """Cette méthode a une implémentation par défaut."""
        return "C'est une forme géométrique"

# Maintenant, Forme ne peut PAS être instanciée directement
# forme = Forme()  # ERREUR!

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        """Obligatoire - sinon Rectangle est aussi abstrait!"""
        return self.largeur * self.hauteur
    
    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

r = Rectangle(5, 3)
print(f"Aire: {r.aire()}")  # 15
print(r.description())       # C'est une forme géométrique
```

---

## 6. L'Héritage Multiple

### Un objet peut hériter de plusieurs classes

Python permet à une classe d'hériter de plusieurs classes parents. C'est utile mais peut devenir complexe.

```python
class Volant:
    def voler(self):
        return "Je vole!"

class Nageant:
    def nager(self):
        return "Je nage!"

# Canard hérite de Volant ET Nageant
class Canard(Volant, Nageant):
    pass

mon_canard = Canard()
print(mon_canard.voler())  # Je vole! (de Volant)
print(mon_canard.nager())  # Je nage! (de Nageant)
```

### L'ordre de résolution (MRO)

Quand une méthode est appelée, Python cherche dans un ordre précis. Cet ordre s'appelle le MRO (Method Resolution Order).

```python
class A:
    def test(self):
        return "A"

class B(A):
    def test(self):
        return "B"

class C(A):
    def test(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.test())  # "B" - B est cherché avant C
print(D.mro())   # [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

## 7. Bonnes Pratiques avec l'Héritage

### Quand utiliser l'héritage ?

Utilise l'héritage pour une relation "est-un" (is-a) :
- Chien **est un** Animal ✓
- Voiture **est un** Vehicule ✓

Utilise la composition (attribut) pour une relation "a-un" (has-a) :
- Voiture **a un** Moteur ✓ (mieux : `self.moteur = Moteur()`)

### Exemple de bonne pratique

```python
# BON: Héritage
class Animal:
    def respirer(self):
        pass

class Chien(Animal):
    def respirer(self):
        print("Respire normalement")

# BON: Composition
class Moteur:
    def demarrer(self):
        pass

class Voiture:
    def __init__(self):
        self.moteur = Moteur()  # La voiture A un moteur
```

---

## 8. Résumé

| Concept | Exemple | À quoi ça sert |
|---------|---------|----------------|
| Héritage | `class Chien(Animal)` | Réutiliser le code d'une classe parent |
| `super()` | `super().__init__()` | Appeler le parent |
| Override | `def parler(self):` | Remplacer une méthode du parent |
| Polymorphisme | `animal.parler()` | Un même appel, comportements différents |
| @abstractmethod | `@abstractmethod` | Forcer l'implémentation |
| Héritage multiple | `class D(B, C)` | Hériter de plusieurs parents |

---

## Erreurs Courantes

### 1. Oublier `super().__init__()`

```python
# MAUVAIS - le parent n'est pas initialisé !
class Enfant(Parent):
    def __init__(self, nom):
        self.nom = nom  # Le parent n'est jamais initialisé

# CORRECT
class Enfant(Parent):
    def __init__(self, nom):
        super().__init__(nom)  # Appelle le parent
```

### 2. Héritage alors que composition suffirait

```python
# MAUVAIS - "Voiture a un moteur" n'est pas "Voiture EST UN moteur"
class Voiture(Moteur):  # Non!
    pass

# CORRECT
class Voiture:
    def __init__(self):
        self.moteur = Moteur()  # Composition
```

### 3. Modifier l'interface du parent

```python
# MAUVAIS - le parent attend (a, b), l'enfant change
class Parent:
    def methode(self, a, b):
        return a + b

class Enfant(Parent):
    def methode(self, x):  # Signature différente!
        return x * 2
```

---

## Exercices

### Exercice 1 : Héritage Simple
Crée une classe `Animal` avec `nom` et `age`, puis une classe `Chien` qui hérite d'Animal avec une méthode `aboyer()`.

### Exercice 2 : Substitution
Crée une classe `Forme` avec une méthode `aire()`, puis des classes `Carre` et `Triangle` qui substituent cette méthode.

### Exercice 3 : Polymorphisme
Crée plusieurs classes avec une méthode `parler()` et une fonction qui les appelle toutes.

### Exercice 4 : Classe Abstraite
Crée une classe abstraite `Employe` avec une méthode abstraite `calculer_salaire()`.

---

## Prochain Chapitre

Maintenant que tu maîtrises l'héritage et le polymorphisme, passons au **chapitre 13 : Propriétés et Méthodes Spéciales**. Tu apprendras à créer des classes Python professionnelles avec des comportements avancés !
