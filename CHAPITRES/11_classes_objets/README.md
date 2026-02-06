# Chapitre 11: Classes et Objets

## Ce que vous allez apprendre

- Les concepts fondamentaux de la POO
- Créer des classes et instancier des objets
- Les attributs et méthodes
- Le constructeur `__init__`
- La référence `self`
- Les méthodes d'instance et de classe
- Les propriétés avec `@property`
- Le cycle de vie des objets

---

## 1. Introduction à la POO

### Pourquoi la POO?

La programmation orientée objet permet d'organiser le code en regroupant:
- **Données** (attributs) et **Comportements** (méthodes)
- Des entités cohérentes et réutilisables

```python
# Sans POO: données et fonctions séparées
nom = "Alice"
age = 25

def presenter(nom, age):
    print(f"Je m'appelle {nom}, j'ai {age} ans")

# Avec POO: données et comportements regroupés
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def presenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

personne = Personne("Alice", 25)
personne.presenter()
```

---

## 2. Création d'une Classe

### Syntaxe de Base

```python
class MaClasse:
    """Documentation de la classe (docstring)."""
    
    # Attribut de classe (partagé par toutes les instances)
    compteur = 0
    
    def __init__(self, param1):
        # Attribut d'instance (unique à chaque objet)
        self.param1 = param1
        MaClasse.compteur += 1
    
    def ma_methode(self):
        """Méthode d'instance."""
        return self.param1
```

### Instanciation

```python
# Création d'un objet (instance)
objet1 = MaClasse("valeur1")
objet2 = MaClasse("valeur2")

# Appel de méthode
resultat = objet1.ma_methode()
print(resultat)  # "valeur1"

# Accès aux attributs
print(objet1.param1)  # "valeur1"
```

---

## 3. Le Constructeur `__init__`

### Initialisation des Attributs

```python
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometres = 0  # Valeur par défaut

# Instanciation
ma_voiture = Voiture("Toyota", "Corolla", 2022)
print(ma_voiture.marque)  # "Toyota"
```

### Valeurs par Défaut

```python
class Rectangle:
    def __init__(self, largeur=1, hauteur=1):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

# Différentes instanciations
r1 = Rectangle()          # 1x1
r2 = Rectangle(5)         # 5x1
r3 = Rectangle(5, 3)      # 5x3
```

---

## 4. La Référence `self`

### Pourquoi `self`?

`self` représente l'instance courante de la classe. Il permet:
- D'accéder aux attributs de l'instance
- D'appeler d'autres méthodes de l'instance

```python
class Personne:
    def __init__(self, nom):
        self.nom = nom  # Attribut d'instance
    
    def dire_bonjour(self):
        return f"Bonjour, je suis {self.nom}"
    
    def se_presenter(self):
        # Appel d'une autre méthode
        message = self.dire_bonjour()
        return f"{message} et j'ai {self.age} ans"

# self est automatiquement passé
p = Personne("Alice")
p.dire_bonjour()        # Python fait: Personne.dire_bonjour(p)
p.se_presenter()        # Python fait: Personne.se_presenter(p)
```

---

## 5. Les Méthodes

### Méthodes d'Instance

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde
    
    def deposer(self, montant):
        self.solde += montant
        return self.solde
    
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            return True
        return False
    
    def afficher_solde(self):
        print(f"Solde: {self.solde}€")

# Utilisation
compte = CompteBancaire("Alice", 100)
compte.deposer(50)
compte.retirer(30)
compte.afficher_solde()  # Solde: 120€
```

### Méthodes de Classe

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @classmethod
    from_fahrenheit(cls, f):
        # Crée une instance depuis Fahrenheit
        celsius = (f - 32) * 5/9
        return cls(celsius)
    
    @classmethod
    from_kelvin(cls, k):
        celsius = k - 273.15
        return cls(celsius)

# Utilisation des méthodes de classe
t1 = Temperature(25)              # Depuis Celsius
t2 = Temperature.from_fahrenheit(77)  # 25°C
t3 = Temperature.from_kelvin(300)      # ~26.85°C
```

### Méthodes Statiques

```python
class MathUtils:
    @staticmethod
    def est_pair(n):
        return n % 2 == 0
    
    @staticmethod
    def factorielle(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorielle(n - 1)

# Appel sans instance
print(MathUtils.est_pair(10))  # True
```

---

## 6. Les Propriétés `@property`

### Getter avec `@property`

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self._age = age  # Attribut "protégé"
    
    @property
    def age(self):
        """Getter pour l'âge."""
        return self._age
    
    @property
    def est_majeur(self):
        return self._age >= 18

# Utilisation (sans parenthèses!)
p = Personne("Alice", 25)
print(p.age)           # Appel du getter
print(p.est_majeur)    # True
```

### Setter avec `@attribut.setter`

```python
class Personne:
    def __init__(self, nom):
        self._nom = nom
        self._age = 0
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, valeur):
        if valeur < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self._age = valeur

# Utilisation
p = Personne("Alice")
p.age = 25      # Appel du setter
print(p.age)   # 25
```

---

## 7. Les Attributs

### Attributs d'Instance

```python
class Voiture:
    def __init__(self, marque):
        self.marque = marque  # Attribut d'instance
        self.kilometres = 0   # Valeur initiale

v1 = Voiture("Toyota")
v2 = Voiture("Peugeot")

v1.kilometres = 100  # N'affecte que v1
print(v1.kilometres)  # 100
print(v2.kilometres)  # 0 (inchangé)
```

### Attributs de Classe

```python
class Voiture:
    moteur = "thermique"  # Attribut de classe
    
    def __init__(self, marque):
        self.marque = marque

# Partagé par toutes les instances
print(Voiture.moteur)  # "thermique"
v1 = Voiture("Toyota")
v2 = Voiture("Peugeot")
print(v1.moteur)       # "thermique" (via l'instance)
```

---

## 8. Le Cycle de Vie des Objets

### Création et Destruction

```python
class Exemple:
    def __init__(self, nom):
        self.nom = nom
        print(f"Création de {nom}")
    
    def __del__(self):
        print(f"Destruction de {self.nom}")

# Création
obj = Exemple("MonObjet")
# Affiche: "Création de MonObjet"

# Destruction (quand plus de référence)
del obj
# Affiche: "Destruction de MonObjet"
```

### Représentation avec `__str__` et `__repr__`

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def __str__(self):
        """Pour l'affichage user-friendly."""
        return f"{self.nom} ({self.age} ans)"
    
    def __repr__(self):
        """Pour le debugging (représentation technique)."""
        return f"Personne('{self.nom}', {self.age})"

p = Personne("Alice", 25)
print(str(p))    # "Alice (25 ans)"
print(repr(p))   # "Personne('Alice', 25)"
```

---

## Points Clés à Retenir

| Concept | Syntaxe | Usage |
|---------|---------|-------|
| Classe | `class MaClasse:` | Définition |
| Constructeur | `def __init__(self, ...):` | Initialisation |
| Méthode | `def ma_methode(self):` | Comportement |
| Instance | `obj = MaClasse()` | Création |
| `@property` | `@property` | Getter |
| Setter | `@attr.setter` | Setter contrôlé |
| `@classmethod` | `@classmethod` | Méthode de classe |
| `@staticmethod` | `@staticmethod` | Fonction de classe |

---

## Erreurs Courantes

```python
# ERREUR: Oublier self dans une méthode
class Mauvaise:
    def methode(self):
        return self.attribut  # OK
    def autre(self):
        return attribut  # ERREUR!

# ERREUR: Confondre attribut et paramètre
class Exemple:
    def __init__(self, valeur):
        valeur = valeur  # ERREUR! Écrase le paramètre
        # CORRECT: self.valeur = valeur

# ERREUR: Modifier un attribut sans passer par self
class Exemple:
    def modifier(self):
        nouvel_attribut = 42  # ERREUR! Variable locale

# ERREUR: Appeler une méthode sans parenthèses
p = Personne("Alice")
print(p.age)       # OK (c'est une propriété)
print(p.presenter)  # ERREUR! Renvoie la méthode, ne l'appelle pas
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez l'**héritage et le polymorphisme** pour créer des relations entre classes.
