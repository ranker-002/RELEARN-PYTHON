# =============================================================================
# CHAPITRE 6: LISTES ET TUPLES - EXERCICES
# =============================================================================
# Niveau: DEBUTANT
# Concepts abordes: listes, tuples, indexation, slicing, methodes, comprehension
# =============================================================================

# =============================================================================
# EXERCICE 6.1 - CREATION DE LISTE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Tres facile)
#
# ENONCE:
# Creez une liste avec les nombres de 1 a 5.
# Affichez la liste et son type.
#
# EXEMPLE:
# Liste: [1, 2, 3, 4, 5]
# Type: <class 'list'>
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_1():
    pass


# =============================================================================
# EXERCICE 6.2 - ACCES AUX ELEMENTS
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Tres facile)
#
# ENONCE:
# Soit la liste fruits = ["pomme", "banane", "orange", "raisin"]
# Affichez:
# - Le premier element
# - Le dernier element
# - Le troisieme element
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_2():
    pass


# =============================================================================
# EXERCICE 6.3 - SLICING DE LISTE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Tres facile)
#
# ENONCE:
# Soit liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Affichez:
# - Les 3 premiers elements
# - Du 3e au 7e element
# - Les elements pairs (indices 0, 2, 4, 6, 8)
# - La liste inversee
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_3():
    pass


# =============================================================================
# EXERCICE 6.4 - MODIFICATION DE LISTE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Soit liste = [1, 2, 3, 4, 5]
# Realisez les operations:
# - Remplacez le 3e element par 10
# - Ajoutez 6 a la fin
# - Inserez 0 au debut
# - Supprimez le element 2
# Affichez la liste apres chaque operation.
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_4():
    pass


# =============================================================================
# EXERCICE 6.5 - CREATION DE TUPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez un tuple pour representer une date (jour, mois, annee).
# Affichez les elements un par un.
#
# EXEMPLE:
# Date: (25, "decembre", 2024)
# Jour: 25
# Mois: decembre
# Annee: 2024
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_5():
    pass


# =============================================================================
# EXERCICE 6.6 - PACKING ET UNPACKING
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Soit tuple_emp = ("Alice", 25, "Paris", 50000)
# Extraiez les valeurs dans 4 variables avec unpacking.
# Affichez chaque variable.
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_6():
    pass


# =============================================================================
# EXERCICE 6.7 - TRI DE LISTE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Soit nombres = [64, 25, 12, 89, 45, 37]
# Triez la liste par ordre croissant.
# Triez-la par ordre decroissant.
#
# EXEMPLE:
# Croissant: [12, 25, 37, 45, 64, 89]
# Decroissant: [89, 64, 45, 37, 25, 12]
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_7():
    pass


# =============================================================================
# EXERCICE 6.8 - COMPTEUR DE MOTS
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Comptez les occurrences de chaque mot dans la liste.
# Affichez le resultat sous forme de dictionaire {mot: count}.
#
# EXEMPLE:
# Liste: ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
# Resultat: {"pomme": 3, "banane": 2, "orange": 1}
#
# INDICE: list.count() ou collections.Counter
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_8():
    pass


# =============================================================================
# EXERCICE 6.9 - COMPREHENSION DE LISTE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez avec une seule ligne:
# 1. Liste des carres de 0 a 9
# 2. Liste des nombres pairs de 0 a 19
# 3. Liste des carres des nombres pairs seulement
#
# EXEMPLE:
# Carres: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Pairs: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Carres pairs: [0, 4, 16, 36, 64]
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_9():
    pass


# =============================================================================
# EXERCICE 6.10 - MATRICE SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une matrice 3x3 avec des zeros.
# Remplissez la diagonale avec des 1.
# Affichez la matrice.
#
# EXEMPLE:
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_10():
    pass


# =============================================================================
# EXERCICE 6.11 - ECHANGE DE VALEURS
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Echangez les valeurs de x et y sans utiliser de variable temporaire.
#
# EXEMPLE:
# Avant: x=5, y=10
# Apres: x=10, y=5
#
# INDICE: unpacking tuple
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_11():
    pass


# =============================================================================
# EXERCICE 6.12 - LISTE DE LISTES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Soit eleves = [["Alice", 15], ["Bob", 12], ["Charlie", 14]]
# Affichez:
# - Le nom du 2e eleve
# - La note du 3e eleve
# - La moyenne des notes
#
# EXEMPLE:
# Eleve 2: Bob
# Note eleve 3: 14
# Moyenne: 13.67
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_12():
    pass


# =============================================================================
# EXERCICE 6.13 - APLATISSEMENT DE LISTE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Soit liste_2d = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Aplatissez-la en une seule liste: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# INDICE: List comprehension imbriquee
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_13():
    pass


# =============================================================================
# EXERCICE 6.14 - GENERATEUR DE NOMBRES PREMIERS
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Generez tous les nombres premiers entre 1 et 50.
#
# INDICE: Testez la primalite avec une boucle
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_14():
    pass


# =============================================================================
# EXERCICE 6.15 - GESTION D'INVENTAIRE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Gerez un inventaire de produits:
# - Ajoutez un produit (nom, quantite)
# - Affichez l'inventaire trie par nom
# - Affichez le produit avec la plus grande quantite
# - Calculez la quantite totale
#
# EXEMPLE:
# Inventaire: [["pomme", 50], ["banane", 30], ["orange", 40]]
#
# INDICE: Usez sorted() avec key
#
# VOTRE CODE CI-DESSOUS:
def exercice_6_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 6 - EXERCICES")
    print("=" * 50)
    print("Execez python verification.py pour valider")
    print("=" * 50)
