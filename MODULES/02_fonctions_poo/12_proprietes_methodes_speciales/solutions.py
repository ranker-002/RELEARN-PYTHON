# =============================================================================
# CHAPITRE 13: PROPRIETES ET METHODES SPECIALES - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 13.1 - PROPRIETE SIMPLE
# =============================================================================
def exercice_13_1():
    """Propriete avec validation."""
    class Temperature:
        def __init__(self, celsius):
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, valeur):
            if valeur < -273.15:
                raise ValueError("Temperature invalide: au-dessus du zero absolu")
            self._celsius = valeur
    
    t = Temperature(25)
    print(f"Initial: {t.celsius}°C")
    t.celsius = 30
    print(f"Modifie: {t.celsius}°C")


# =============================================================================
# EXERCICE 13.2 - PROPRIETE CALCULEE
# =============================================================================
def exercice_13_2():
    """Proprietes calculees en lecture seule."""
    class Rectangle:
        def __init__(self, largeur, hauteur):
            self.largeur = largeur
            self.hauteur = hauteur
        
        @property
        def aire(self):
            return self.largeur * self.hauteur
        
        @property
        def perimetre(self):
            return 2 * (self.largeur + self.hauteur)
    
    r = Rectangle(5, 3)
    print(f"Aire: {r.aire}")
    print(f"Perimetre: {r.perimetre}")


# =============================================================================
# EXERCICE 13.3 - __STR__ ET __REPR__
# =============================================================================
def exercice_13_3():
    """__str__ et __repr__ differents."""
    class Livre:
        def __init__(self, titre, auteur, annee):
            self.titre = titre
            self.auteur = auteur
            self.annee = annee
        
        def __str__(self):
            return f"{self.titre} par {self.auteur} ({self.annee})"
        
        def __repr__(self):
            return f"Livre('{self.titre}', '{self.auteur}', {self.annee})"
    
    l = Livre("1984", "Orwell", 1949)
    print(f"str: {str(l)}")
    print(f"repr: {repr(l)}")


# =============================================================================
# EXERCICE 13.4 - COMPARAISON SIMPLE
# =============================================================================
def exercice_13_4():
    """Comparaison avec total_ordering."""
    from functools import total_ordering
    
    @total_ordering
    class Age:
        def __init__(self, valeur):
            self.valeur = valeur
        
        def __eq__(self, autre):
            if not isinstance(autre, Age):
                return NotImplemented
            return self.valeur == autre.valeur
        
        def __lt__(self, autre):
            if not isinstance(autre, Age):
                return NotImplemented
            return self.valeur < autre.valeur
    
    a1 = Age(25)
    a2 = Age(30)
    print(f"a1 < a2: {a1 < a2}")
    print(f"a1 == a2: {a1 == a2}")
    print(f"a1 > a2: {a1 > a2}")
    print(f"a1 <= a2: {a1 <= a2}")


# =============================================================================
# EXERCICE 13.5 - ITERATEUR SIMPLE
# =============================================================================
def exercice_13_5():
    """Iterateur simple avec __iter__ et __next__."""
    class Compteur:
        def __init__(self, max):
            self.max = max
            self.current = 1
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current > self.max:
                raise StopIteration
            valeur = self.current
            self.current += 1
            return valeur
    
    print("Comptage jusqu'a 5:")
    for i in Compteur(5):
        print(i)


# =============================================================================
# EXERCICE 13.6 - CONTEXTE SIMPLE
# =============================================================================
def exercice_13_6():
    """Gestionnaire de contexte pour chronometrer."""
    import time
    
    class Chronometre:
        def __enter__(self):
            self.start = time.time()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.time()
            self.duree = self.end - self.start
            print(f"Execute en {self.duree:.4f} secondes")
            return False
    
    print("Debut du test:")
    with Chronometre() as c:
        total = sum(range(1000000))
    print(f"Resultat: {total}")


# =============================================================================
# EXERCICE 13.7 - OPERATEURS ARITHMETIQUES
# =============================================================================
def exercice_13_7():
    """Operateurs arithmetiques sur Vecteur2D."""
    class Vecteur2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, autre):
            if not isinstance(autre, Vecteur2D):
                return NotImplemented
            return Vecteur2D(self.x + autre.x, self.y + autre.y)
        
        def __sub__(self, autre):
            if not isinstance(autre, Vecteur2D):
                return NotImplemented
            return Vecteur2D(self.x - autre.x, self.y - autre.y)
        
        def __mul__(self, scalaire):
            if not isinstance(scalaire, (int, float)):
                return NotImplemented
            return Vecteur2D(self.x * scalaire, self.y * scalaire)
        
        def __rmul__(self, scalaire):
            return self.__mul__(scalaire)
        
        def __repr__(self):
            return f"Vecteur2D({self.x}, {self.y})"
    
    v1 = Vecteur2D(1, 2)
    v2 = Vecteur2D(3, 4)
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v2 = {3 * v2}")


# =============================================================================
# EXERCICE 13.8 - CONTENEUR PERSONNALISE
# =============================================================================
def exercice_13_8():
    """Conteneur avec taille limitee."""
    class ListeLimitee:
        def __init__(self, max_size):
            self.max_size = max_size
            self.elements = []
        
        def __len__(self):
            return len(self.elements)
        
        def __getitem__(self, index):
            return self.elements[index]
        
        def __setitem__(self, index, valeur):
            self.elements[index] = valeur
        
        def __contains__(self, item):
            return item in self.elements
        
        def append(self, item):
            if len(self.elements) >= self.max_size:
                raise ValueError(f"Liste pleine (max: {self.max_size})")
            self.elements.append(item)
        
        def __repr__(self):
            return f"ListeLimitee({self.elements})"
    
    l = ListeLimitee(3)
    l.append(1)
    l.append(2)
    l.append(3)
    print(f"Liste: {l}")
    print(f"Longueur: {len(l)}")
    print(f"Contient 2: {2 in l}")


# =============================================================================
# EXERCICE 13.9 - ITERATEUR FILTRE
# =============================================================================
def exercice_13_9():
    """Iterateur avec predicat."""
    class FilterIterator:
        def __init__(self, iterable, predicat):
            self.iterable = list(iterable)
            self.predicat = predicat
            self.index = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            while self.index < len(self.iterable):
                item = self.iterable[self.index]
                self.index += 1
                if self.predicat(item):
                    return item
            raise StopIteration
    
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    pairs = FilterIterator(nombres, lambda x: x % 2 == 0)
    impairs = FilterIterator(nombres, lambda x: x % 2 == 1)
    
    print(f"Pairs: {list(pairs)}")
    print(f"Impairs: {list(impairs)}")


# =============================================================================
# EXERCICE 13.10 - PROPRIETE AVEC CACHE
# =============================================================================
def exercice_13_10():
    """Propriete avec mise en cache."""
    class FactorialCache:
        def __init__(self):
            self.cache = {0: 1, 1: 1}
        
        def factorielle(self, n):
            if n in self.cache:
                return self.cache[n]
            result = n * self.factorielle(n - 1)
            self.cache[n] = result
            return result
        
        @property
        def cache_size(self):
            return len(self.cache)
        
        def __repr__(self):
            return f"FactorialCache(cache_size={self.cache_size})"
    
    f = FactorialCache()
    print(f"5! = {f.factorielle(5)}")
    print(f"10! = {f.factorielle(10)}")
    print(f"5! (cache) = {f.factorielle(5)}")
    print(f"Taille du cache: {f.cache_size}")


# =============================================================================
# EXERCICE 13.11 - HACHAGE ET SET
# =============================================================================
def exercice_13_11():
    """Hachage pour utilisation dans des sets."""
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __eq__(self, autre):
            if not isinstance(autre, Point):
                return NotImplemented
            return self.x == autre.x and self.y == autre.y
        
        def __hash__(self):
            return hash((self.x, self.y))
        
        def __repr__(self):
            return f"Point({self.x}, {self.y})"
    
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)
    
    s = {p1, p2, p3}
    print(f"Set: {s}")
    print(f"Taille du set: {len(s)}")  # 2 car p1 == p2


# =============================================================================
# EXERCICE 13.12 - GENERATEUR PERSONNALISE
# =============================================================================
def exercice_13_12():
    """Generateur de Fibonacci."""
    class FibGenerator:
        def __init__(self):
            self.a, self.b = 0, 1
        
        def __iter__(self):
            return self
        
        def __next__(self):
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result
    
    fib = FibGenerator()
    print("10 premiers nombres de Fibonacci:")
    for i, f in zip(range(10), fib):
        print(f)


# =============================================================================
# EXERCICE 13.13 - METHODE D'APPEL
# =============================================================================
def exercice_13_13():
    """Classe appelable avec compteur."""
    class FunctionWrapper:
        def __init__(self, func):
            self.func = func
            self.nb_appels = 0
        
        def __call__(self, *args, **kwargs):
            self.nb_appels += 1
            return self.func(*args, **kwargs)
        
        def __repr__(self):
            return f"FunctionWrapper({self.func.__name__})"
    
    def double(x):
        return x * 2
    
    f = FunctionWrapper(double)
    print(f(5))
    print(f(10))
    print(f(20))
    print(f"Nombre d'appels: {f.nb_appels}")


# =============================================================================
# EXERCICE 13.14 - CLASSE SLICEABLE
# =============================================================================
def exercice_13_14():
    """Matrice avec support des slices."""
    class Matrice:
        def __init__(self, lignes, colonnes):
            self.lignes = lignes
            self.colonnes = colonnes
            self.data = [[0] * colonnes for _ in range(lignes)]
        
        def __getitem__(self, index):
            if isinstance(index, tuple):
                if len(index) == 2:
                    row, col = index
                    return self.data[row][col]
                elif len(index) == 1:
                    return self.data[index[0]]
            elif isinstance(index, slice):
                return self.data[index]
            raise IndexError("Index invalide")
        
        def __setitem__(self, index, valeur):
            if isinstance(index, tuple) and len(index) == 2:
                row, col = index
                self.data[row][col] = valeur
            else:
                raise IndexError("Index invalide")
        
        def __repr__(self):
            return "\n".join(str(row) for row in self.data)
    
    m = Matrice(3, 3)
    m[0, 0] = 1
    m[1, 1] = 2
    m[2, 2] = 3
    print(m)
    print(f"\nm[0] = {m[0]}")
    print(f"m[0,0] = {m[0, 0]}")


# =============================================================================
# EXERCICE 13.15 - SYSTEME COMPLET
# =============================================================================
def exercice_13_15():
    """Systeme de temperature complet."""
    class Temperature:
        ABSOLU_ZERO_C = -273.15
        
        def __init__(self, celsius):
            if celsius < self.ABSOLU_ZERO_C:
                raise ValueError("Temperature inferieure au zero absolu!")
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @property
        def fahrenheit(self):
            return self._celsius * 9/5 + 32
        
        @property
        def kelvin(self):
            return self._celsius + 273.15
        
        @classmethod
        def from_fahrenheit(cls, f):
            c = (f - 32) * 5/9
            return cls(c)
        
        @classmethod
        def from_kelvin(cls, k):
            c = k - 273.15
            return cls(c)
        
        def __str__(self):
            return f"{self._celsius:.2f}°C"
        
        def __repr__(self):
            return f"Temperature({self._celsius:.2f})"
        
        def __eq__(self, autre):
            if not isinstance(autre, Temperature):
                return NotImplemented
            return abs(self._celsius - autre._celsius) < 0.01
        
        def __add__(self, autre):
            if isinstance(autre, Temperature):
                return Temperature(self._celsius + autre._celsius)
            return Temperature(self._celsius + autre)
        
        def __radd__(self, autre):
            return self.__add__(autre)
    
    t = Temperature(25)
    print(f"Celsius: {t.celsius}°C")
    print(f"Fahrenheit: {t.fahrenheit}°F")
    print(f"Kelvin: {t.kelvin}K")
    
    t2 = Temperature.from_kelvin(300)
    print(f"\n300K = {t2.celsius:.2f}°C")
    
    t3 = Temperature(10) + Temperature(15)
    print(f"\n10°C + 15°C = {t3}")
