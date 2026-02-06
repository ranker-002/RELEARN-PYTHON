# =============================================================================
# CHAPITRE 13: PROPRIETES ET METHODES SPECIALES - EXERCICES
# =============================================================================
# Niveau: INTERMEDIAIRE
# Concepts abordes: @property, __str__, __repr__, __iter__, __enter__, __add__
# =============================================================================

# =============================================================================
# EXERCICE 13.1 - PROPRIETE SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Temperature avec:
# - Attribut prive: _celsius
# - Propriete celsius (lecture/écriture)
# - Validation: temperature >= -273.15
#
# EXEMPLE:
# t = Temperature(25)
# print(t.celsius)  # 25
# t.celsius = 30
# print(t.celsius)  # 30
# t.celsius = -300  # ValueError
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_1():
    pass


# =============================================================================
# EXERCICE 13.2 - PROPRIETE CALCULEE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Rectangle avec:
# - Attributs: largeur, hauteur
# - Propriete: aire (largeur * hauteur, lecture seule)
# - Propriete: perimetre (lecture seule)
#
# EXEMPLE:
# r = Rectangle(5, 3)
# print(r.aire)       # 15
# print(r.perimetre)  # 16
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_2():
    pass


# =============================================================================
# EXERCICE 13.3 - __STR__ ET __REPR__
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Livre avec:
# - Attributs: titre, auteur, annee
# - __str__: "titre par auteur (annee)"
# - __repr__: "Livre('titre', 'auteur', annee)"
#
# EXEMPLE:
# l = Livre("1984", "Orwell", 1949)
# print(str(l))    # "1984 par Orwell (1949)"
# print(repr(l))   # "Livre('1984', 'Orwell', 1949)"
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_3():
    pass


# =============================================================================
# EXERCICE 13.4 - COMPARAISON SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Age avec:
# - Attribut: valeur
# - __eq__ et __lt__ pour comparer
# Usez @total_ordering pour les autres comparaisons
#
# EXEMPLE:
# a1 = Age(25)
# a2 = Age(30)
# print(a1 < a2)   # True
# print(a1 == a2)  # False
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_4():
    pass


# =============================================================================
# EXERCICE 13.5 - ITERATEUR SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Compteur avec:
# - Attribut: max
# - __iter__ et __next__ pour iterer de 1 a max
#
# EXEMPLE:
# for i in Compteur(5):
#     print(i)  # 1, 2, 3, 4, 5
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_5():
    pass


# =============================================================================
# EXERCICE 13.6 - CONTEXTE SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez un gestionnaire de contexte Chronometre qui:
# - Mesure le temps d'execution avec time.time()
# - Affiche le temps à la sortie
#
# EXEMPLE:
# with Chronometre() as c:
#     sum(range(1000000))
# # Affiche: "Executé en X.XX secondes"
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_6():
    pass


# =============================================================================
# EXERCICE 13.7 - OPERATEURS ARITHMETIQUES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Vecteur2D avec:
# - Attributs: x, y
# - __add__, __sub__, __mul__ (scalaire)
# - __repr__ pour l'affichage
#
# EXEMPLE:
# v1 = Vecteur2D(1, 2)
# v2 = Vecteur2D(3, 4)
# print(v1 + v2)   # Vecteur2D(4, 6)
# print(v1 * 2)    # Vecteur2D(2, 4)
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_7():
    pass


# =============================================================================
# EXERCICE 13.8 - CONTENEUR PERSONNALISE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une classe ListeLimitee avec:
# - Attributs: max_size, elements
# - __len__, __getitem__, __setitem__
# - __contains__ pour "in"
# - Interdit depassement de max_size
#
# EXEMPLE:
# l = ListeLimitee(3)
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)  # ValueError
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_8():
    pass


# =============================================================================
# EXERCICE 13.9 - ITERATEUR FILTRE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une classe FilterIterator qui:
# - Prend une liste et un predicat (fonction)
# - Ne yield que les elements qui satisfont le predicat
#
# EXEMPLE:
# pairs = FilterIterator([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
# print(list(pairs))  # [2, 4]
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_9():
    pass


# =============================================================================
# EXERCICE 13.10 - PROPRIETE AVEC CACHE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une classe FactorialCache avec:
# - Methode factorielle(n) avec cache
# - Propriete cache_size
#
# EXEMPLE:
# f = FactorialCache()
# print(f.factorielle(10))  # 3628800 (calcule)
# print(f.factorielle(5))   # 120 (depuis cache)
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_10():
    pass


# =============================================================================
# EXERCICE 13.11 - HACHAGE ET SET
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe Point avec:
# - Attributs: x, y
# - __eq__ compare x et y
# - __hash__ pour permettre dans des sets
#
# EXEMPLE:
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# s = {p1, p2}
# print(len(s))  # 1 (car p1 == p2)
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_11():
    pass


# =============================================================================
# EXERCICE 13.12 - GENERATEUR PERSONNALISE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe FibGenerator qui:
# - Genere la suite de Fibonacci
# - Utilise __iter__ et __next__
#
# EXEMPLE:
# fib = FibGenerator()
# for i, f in zip(range(10), fib):
#     print(f)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_12():
    pass


# =============================================================================
# EXERCICE 13.13 - METHODE D'APPEL
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe FunctionWrapper qui:
# - Prend une fonction dans __init__
# - Utilise __call__ pour executer la fonction
# - Compte le nombre d'appels
#
# EXEMPLE:
# def double(x): return x * 2
# f = FunctionWrapper(double)
# print(f(5))      # 10
# print(f(10))     # 20
# print(f.nb_appels)  # 2
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_13():
    pass


# =============================================================================
# EXERCICE 13.14 - CLASSE SLICEABLE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe Matrice qui:
# - Accepte des dimensions (lignes, colonnes)
# - Support __getitem__ avec slices
# - __repr__ pour afficher la matrice
#
# EXEMPLE:
# m = Matrice(3, 3)
# m[0, 0] = 1
# print(m[0])      # [1, 0, 0]
# print(m[:, 1])   # [0, 0, 0] (colonne 1)
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_14():
    pass


# =============================================================================
# EXERCICE 15.15 - SYSTEME COMPLET
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme de temperature avec:
# - Classe Temperature (celsius, fahrenheit, kelvin)
# - Proprietes pour chaque unite
# - Conversions automatiques
# - __str__, __eq__, __add__
#
# EXEMPLE:
# t = Temperature(25)
# print(t.celsius)    # 25
# print(t.fahrenheit) # 77.0
# print(Temperature.from_kelvin(300))  # 26.85C
#
# VOTRE CODE CI-DESSOUS:
def exercice_13_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 13 - EXERCICES")
    print("=" * 50)
    print("Exercices disponibles:")
    print("  13.1 - Propriete simple")
    print("  13.2 - Propriete calculee")
    print("  13.3 - __str__ et __repr__")
    print("  13.4 - Comparaison simple")
    print("  13.5 - Iterateur simple")
    print("  13.6 - Contexte simple")
    print("  13.7 - Operateurs arithmetiques")
    print("  13.8 - Conteneur personnalise")
    print("  13.9 - Iterateur filtre")
    print("  13.10 - Propriete avec cache")
    print("  13.11 - Hachage et set")
    print("  13.12 - Generateur personnalise")
    print("  13.13 - Methode d'appel")
    print("  13.14 - Classe sliceable")
    print("  13.15 - Systeme complet")
    print("=" * 50)
