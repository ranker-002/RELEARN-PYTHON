# Chapitre 12: Propriétés et Méthodes Spéciales

## Ce que vous allez apprendre

- Les propriétés avec `@property`
- Les getters et setters
- Les méthodes spéciales (dunder methods)
- Le protocole d'itération
- Le protocole de contexte
- Les opérateurs de comparaison
- Les méthodes arithmétiques
- La représentation d'objets

---

## 1. Les Propriétés Avancées

### Rappel sur les Propriétés

```python
class Personne:
    def __init__(self, nom):
        self._nom = nom
    
    @property
    def nom(self):
        """Getter pour le nom."""
        return self._nom
    
    @nom.setter
    def nom(self, valeur):
        """Setter pour le nom avec validation."""
        if not valeur:
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur

p = Personne("Alice")
print(p.nom)    # Appel du getter
p.nom = "Bob"   # Appel du setter
```

### Propriété en Lecture Seule

```python
class Cercle:
    def __init__(self, rayon):
        self._rayon = rayon
    
    @property
    def rayon(self):
        return self._rayon
    
    @property
    def aire(self):
        """Propriété calculée, lecture seule."""
        return 3.14159 * self._rayon ** 2
    
    @property
    def circonference(self):
        """Propriété calculée, lecture seule."""
        return 2 * 3.14159 * self._rayon

c = Cercle(5)
print(c.aire)          # 78.54...
c.rayon = 10           # OK
# c.aire = 100        # ERREUR! Lecture seule
```

### Propriété avec Cache

```python
class Calculateur:
    def __init__(self, valeur):
        self._valeur = valeur
        self._resultat_cached = None
    
    @property
    def resultat(self):
        """Calcul coûteux avec mise en cache."""
        if self._resultat_cached is None:
            print("Calcul en cours...")
            self._resultat_cached = self._valeur ** 2 + self._valeur * 2 + 1
        return self._resultat_cached

calc = Calculateur(10)
print(calc.resultat)  # "Calcul en cours..." puis 121
print(calc.resultat)   # 121 (pas de recalcul)
```

---

## 2. Les Méthodes Spéciales

### Méthodes de Représentation

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def __str__(self):
        """Représentation lisible par l'utilisateur."""
        return f"{self.nom} ({self.age} ans)"
    
    def __repr__(self):
        """Représentation technique pour debugging."""
        return f"Personne(nom={self.nom!r}, age={self.age!r})"

p = Personne("Alice", 30)
print(str(p))    # "Alice (30 ans)"
print(repr(p))   # "Personne(nom='Alice', age=30)"
```

### Méthodes de Comparaison

```python
class Nombre:
    def __init__(self, valeur):
        self.valeur = valeur
    
    def __eq__(self, autre):
        """=="""
        if not isinstance(autre, Nombre):
            return NotImplemented
        return self.valeur == autre.valeur
    
    def __ne__(self, autre):
        """!="""
        return not self.__eq__(autre)
    
    def __lt__(self, autre):
        """<"""
        if not isinstance(autre, Nombre):
            return NotImplemented
        return self.valeur < autre.valeur
    
    def __le__(self, autre):
        """<="""
        return self < autre or self == autre
    
    def __gt__(self, autre):
        """>"""
        if not isinstance(autre, Nombre):
            return NotImplemented
        return self.valeur > autre.valeur
    
    def __ge__(self, autre):
        """>="""
        return self > autre or self == autre

n1 = Nombre(5)
n2 = Nombre(10)
print(n1 < n2)   # True
print(n1 == n2)  # False
```

### `@functools.total_ordering`

```python
from functools import total_ordering

@total_ordering
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __eq__(self, autre):
        return self.celsius == autre.celsius
    
    def __lt__(self, autre):
        return self.celsius < autre.celsius
    
    def __str__(self):
        return f"{self.celsius}°C"

t1 = Temperature(25)
t2 = Temperature(30)
print(t1 < t2)   # True
print(t1 >= t2)  # False (généré automatiquement)
```

---

## 3. Le Protocole d'Itération

### `__iter__` et `__next__`

```python
class RangePersonnalise:
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin
    
    def __iter__(self):
        """Retourne un itérateur."""
        return self
    
    def __next__(self):
        """Prochain élément."""
        if self.debut >= self.fin:
            raise StopIteration
        valeur = self.debut
        self.debut += 1
        return valeur

r = RangePersonnalise(1, 5)
for i in r:
    print(i)  # 1, 2, 3, 4

# Iteration manuelle
r = RangePersonnalise(1, 5)
it = iter(r)
print(next(it))  # 1
print(next(it))  # 2
```

### Itérateur avec Classe Separate

```python
class CaramelIterator:
    def __init__(self, caramel):
        self.caramel = caramel
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.caramel):
            raise StopIteration
        item = self.caramel[self.index]
        self.index += 1
        return item

class Caramel:
    def __init__(self, elements):
        self.elements = elements
    
    def __iter__(self):
        return CaramelIterator(self.elements)

c = Caramel([1, 2, 3, 4, 5])
for x in c:
    print(x)
```

### Generator Expression vs Iterator Class

```python
# Generator simple
def carre_gen(n):
    for i in range(n):
        yield i ** 2

# Utilisation
gen = carre_gen(5)
for x in gen:
    print(x)  # 0, 1, 4, 9, 16
```

---

## 4. Le Protocole de Contexte

### `__enter__` et `__exit__`

```python
class GestionnaireContexte:
    def __enter__(self):
        print("Entrée dans le contexte")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sortie du contexte")
        if exc_type:
            print(f"Exception: {exc_type.__name__}: {exc_val}")
        return False  # Propager l'exception

with GestionnaireContexte() as gc:
    print("À l'intérieur du contexte")
# Affiche:
# Entrée dans le contexte
# À l'intérieur du contexte
# Sortie du contexte

# Avec exception
with GestionnaireContexte():
    raise ValueError("Erreur!")
# Affiche:
# Entrée dans le contexte
# Sortie du contexte
# Exception: ValueError: Erreur!
```

### Classe Fichier Personnalisée

```python
class FichierTemporaire:
    def __init__(self, nom):
        self.nom = nom
        self.fichier = None
    
    def __enter__(self):
        self.fichier = open(self.nom, 'w')
        return self.fichier
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichier:
            self.fichier.close()
        return False

with FichierTemporaire("test.txt") as f:
    f.write("Hello, World!")

print("Fichier fermé automatiquement")
```

### `@contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def mon_contexte(msg):
    print(f"Entrée: {msg}")
    try:
        yield
    finally:
        print(f"Sortie: {msg}")

with mon_contexte("Test"):
    print("À l'intérieur")
# Affiche:
# Entrée: Test
# À l'intérieur
# Sortie: Test
```

---

## 5. Les Méthodes Arithmétiques

### Opérateurs Binaires

```python
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, autre):
        """+"""
        if not isinstance(autre, Vecteur):
            return NotImplemented
        return Vecteur(self.x + autre.x, self.y + autre.y)
    
    def __sub__(self, autre):
        """-"""
        if not isinstance(autre, Vecteur):
            return NotImplemented
        return Vecteur(self.x - autre.x, self.y - autre.y)
    
    def __mul__(self, scalaire):
        """*"""
        if not isinstance(scalaire, (int, float)):
            return NotImplemented
        return Vecteur(self.x * scalaire, self.y * scalaire)
    
    def __matmul__(self, autre):
        """@"""
        if not isinstance(autre, Vecteur):
            return NotImplemented
        return self.x * autre.x + self.y * autre.y
    
    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)
print(v1 + v2)    # Vecteur(4, 6)
print(v1 * 2)     # Vecteur(2, 4)
print(v1 @ v2)    # 11 (produit scalaire)
```

### Opérateurs RHS

```python
class Nombre:
    def __init__(self, valeur):
        self.valeur = valeur
    
    def __add__(self, autre):
        """self + autre"""
        if isinstance(autre, Nombre):
            return Nombre(self.valeur + autre.valeur)
        return Nombre(self.valeur + autre)
    
    def __radd__(self, autre):
        """autre + self"""
        return Nombre(autre + self.valeur)
    
    def __iadd__(self, autre):
        """self += autre"""
        self.valeur += autre.valeur if isinstance(autre, Nombre) else autre
        return self

n1 = Nombre(5)
n2 = Nombre(3)
n3 = n1 + n2          # __add__
n4 = 5 + n1           # __radd__
print(n3.valeur)      # 8
print(n4.valeur)      # 10
```

### Opérateurs Unaires

```python
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __neg__(self):
        """-v"""
        return Vecteur(-self.x, -self.y)
    
    def __pos__(self):
        """+v"""
        return Vecteur(+self.x, +self.y)
    
    def __abs__(self):
        """|v|"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

v = Vecteur(3, 4)
print(-v)        # Vecteur(-3, -4)
print(abs(v))    # 5.0
```

---

## 6. Les Méthodes de Conversion

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __int__(self):
        """int(t)"""
        return int(self.celsius)
    
    def __float__(self):
        """float(t)"""
        return float(self.celsius)
    
    def __bool__(self):
        """if t:"""
        return self.celsius > 0
    
    def __complex__(self):
        """complex(t)"""
        return complex(self.celsius, 0)
    
    def __str__(self):
        return f"{self.celsius}°C"

t = Temperature(25.7)
print(int(t))     # 25
print(float(t))   # 25.7
print(bool(t))    # True
print(complex(t)) # (25.7+0j)
```

---

## 7. Les Attributs Dynamiques

### `__getattr__` et `__getattribute__`

```python
class ObjetDynamique:
    def __init__(self):
        self.normal = "Valeur normale"
    
    def __getattr__(self, nom):
        """Appelé quand l'attribut n'est pas trouvé."""
        return f"Attribut '{nom}' non trouvé"
    
    def __getattribute__(self, nom):
        """TOUJOURS appelé pour tout accès."""
        print(f"Accès à: {nom}")
        return super().__getattribute__(nom)

obj = ObjetDynamique()
print(obj.normal)           # Accès normal
print(obj.inconnu)          # Via __getattr__
```

### `__setattr__` et `__delattr__`

```python
class ProtectionAttributs:
    def __init__(self):
        self.__dict__['_protégé'] = set()
    
    def __setattr__(self, nom, valeur):
        """Interdit les attributs commençant par '_'."""
        if nom.startswith('_') and nom != '_protégé':
            raise AttributeError(f"Attribut protégé: {nom}")
        super().__setattr__(nom, valeur)
    
    def __delattr__(self, nom):
        """Interdit la suppression."""
        raise AttributeError(f"Suppression interdite: {nom}")

obj = ProtectionAttributs()
obj.normal = "OK"
# obj._secret = "Non"  # ERREUR!
```

---

## 8. Les Méthodes de Conteneur

```python
class ListePersonnalisee:
    def __init__(self, elements=None):
        self._elements = list(elements) if elements else []
    
    def __len__(self):
        """len(l)"""
        return len(self._elements)
    
    def __getitem__(self, index):
        """l[index]"""
        return self._elements[index]
    
    def __setitem__(self, index, valeur):
        """l[index] = valeur"""
        self._elements[index] = valeur
    
    def __delitem__(self, index):
        """del l[index]"""
        del self._elements[index]
    
    def __contains__(self, item):
        """item in l"""
        return item in self._elements
    
    def __repr__(self):
        return f"Liste({self._elements})"

l = ListePersonnalisee([1, 2, 3])
print(len(l))        # 3
print(l[0])          # 1
print(2 in l)        # True
l[0] = 10
print(l)             # Liste([10, 2, 3])
```

---

## 9. Les Méthodes de Hachage

```python
class Identifiant:
    def __init__(self, valeur):
        self.valeur = valeur
    
    def __eq__(self, autre):
        if not isinstance(autre, Identifiant):
            return NotImplemented
        return self.valeur == autre.valeur
    
    def __hash__(self):
        """hash(obj)"""
        return hash(self.valeur)
    
    def __repr__(self):
        return f"Identifiant({self.valeur})"

id1 = Identifiant("abc")
id2 = Identifiant("abc")
print(id1 == id2)      # True
print(hash(id1))       # Même hash
print(id1 in {id1})    # True (utilisable dans un set)
```

---

## 10. Appelables et Description

### `__call__`

```python
class Multiplicateur:
    def __init__(self, facteur):
        self.facteur = facteur
    
    def __call__(self, valeur):
        """obj()"""
        return valeur * self.facteur

double = Multiplicateur(2)
print(double(5))      # 10
print(double(10))    # 20

# Utilisation comme callback
nombres = [1, 2, 3, 4, 5]
transformes = list(map(double, nombres))
print(transformes)    # [2, 4, 6, 8, 10]
```

### `__getitem__` avec Slicing

```python
class Matrice:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        """Support des slices."""
        if isinstance(index, slice):
            return [ligne[index] for ligne in self.data]
        return self.data[index]

m = Matrice([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(m[0])          # [1, 2, 3]
print(m[1:])          # [[4, 5, 6], [7, 8, 9]]
print(m[:, 1])        # [2, 5, 8] (colonne 1)
```

---

## 11. Bonnes Pratiques

### Quand Utiliser les Méthodes Spéciales

```python
# BON: __str__ pour l'affichage utilisateur
class Personne:
    def __str__(self):
        return f"{self.nom}"

# BON: __repr__ pour le debugging
class Personne:
    def __repr__(self):
        return f"Personne({self.nom!r}, {self.age!r})"

# BON: __eq__ pour les comparaisons
class Personne:
    def __eq__(self, autre):
        if type(self) != type(autre):
            return NotImplemented
        return self.nom == autre.nom

# MAUVAIS: Retourner des types différents
class Mauvais:
    def __str__(self):
        return 42  # Devrait être str
```

### Conservation de l'Invariant

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valeur):
        """Validation à chaque modification."""
        if valeur < -273.15:
            raise ValueError("Température invalide")
        self._celsius = valeur
    
    def __str__(self):
        return f"{self._celsius}°C"

t = Temperature(25)
print(t)
t.celsius = -300  # ValueError!
```

---

## Points Clés à Retenir

| Méthode | Usage | Exemple |
|---------|-------|---------|
| `__str__` | Affichage utilisateur | `print(obj)` |
| `__repr__` | Debugging | `repr(obj)` |
| `__eq__` | Comparaison `==` | `obj1 == obj2` |
| `__lt__`, `__gt__` | Comparaison `<`, `>` | `obj1 < obj2` |
| `__iter__` | Itération | `for x in obj` |
| `__next__` | Itération | `next(it)` |
| `__enter__` | Contexte `with` | `with obj:` |
| `__exit__` | Contexte `with` | Fin du `with` |
| `__add__` | Opérateur `+` | `obj1 + obj2` |
| `__getitem__` | Indexation `[]` | `obj[0]` |
| `__call__` | Appel `()` | `obj()` |
| `__len__` | Longueur | `len(obj)` |

---

## Erreurs Courantes

```python
# ERREUR: Retourner NotImplemented au lieu de False
class Mauvais:
    def __eq__(self, autre):
        return False  # ERREUR! Doit être NotImplemented
        # CORRECT: return NotImplemented

# ERREUR: Oublier de retourner dans __next__
class MauvaisIterateur:
    def __iter__(self):
        return self
    
    def __next__(self):
        # ERREUR! Ne retourne rien
        pass

# ERREUR: Modifier l'état dans __eq__
class Mauvais:
    def __eq__(self, autre):
        self.compteur += 1  # ERREUR! __eq__ ne devrait pas modifier l'état
        return self.valeur == autre.valeur

# ERREUR: Modifier la longueur pendant l'itération
class Problématique:
    def __init__(self):
        self.items = [1, 2, 3]
    
    def __iter__(self):
        for i, item in enumerate(self.items):
            if i == 1:
                self.items.append(4)  # ERREUR!
            yield item
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous découvrirez la **gestion des exceptions** pour créer du code robuste qui gère les erreurs gracieusement.
