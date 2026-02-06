# =============================================================================
# CHAPITRE 6: LISTES ET TUPLES - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 6.1 - CREATION DE LISTE
# =============================================================================
def exercice_6_1():
    """Cree une liste et affiche son type."""
    liste = [1, 2, 3, 4, 5]
    print(f"Liste: {liste}")
    print(f"Type: {type(liste)}")


# =============================================================================
# EXERCICE 6.2 - ACCES AUX ELEMENTS
# =============================================================================
def exercice_6_2():
    """Accede aux elements d'une liste."""
    fruits = ["pomme", "banane", "orange", "raisin"]
    print(f"Premier: {fruits[0]}")
    print(f"Dernier: {fruits[-1]}")
    print(f"Troisieme: {fruits[2]}")


# =============================================================================
# EXERCICE 6.3 - SLICING DE LISTE
# =============================================================================
def exercice_6_3():
    """Demontre le slicing de listes."""
    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"3 premiers: {liste[:3]}")
    print(f"3e a 7e: {liste[2:7]}")
    print(f"Pairs: {liste[::2]}")
    print(f"Inverse: {liste[::-1]}")


# =============================================================================
# EXERCICE 6.4 - MODIFICATION DE LISTE
# =============================================================================
def exercice_6_4():
    """Modifie une liste avec differentes operations."""
    liste = [1, 2, 3, 4, 5]
    print(f"Original: {liste}")

    liste[2] = 10
    print(f"Apres remplacement: {liste}")

    liste.append(6)
    print(f"Apres append: {liste}")

    liste.insert(0, 0)
    print(f"Apres insert: {liste}")

    liste.remove(2)
    print(f"Apres remove: {liste}")


# =============================================================================
# EXERCICE 6.5 - CREATION DE TUPLE
# =============================================================================
def exercice_6_5():
    """Cree et affiche un tuple date."""
    date = (25, "decembre", 2024)
    print(f"Date: {date}")
    print(f"Jour: {date[0]}")
    print(f"Mois: {date[1]}")
    print(f"Annee: {date[2]}")


# =============================================================================
# EXERCICE 6.6 - PACKING ET UNPACKING
# =============================================================================
def exercice_6_6():
    """Demonte le packing et unpacking de tuple."""
    tuple_emp = ("Alice", 25, "Paris", 50000)
    nom, age, ville, salaire = tuple_emp
    print(f"Nom: {nom}")
    print(f"Age: {age}")
    print(f"Ville: {ville}")
    print(f"Salaire: {salaire}")


# =============================================================================
# EXERCICE 6.7 - TRI DE LISTE
# =============================================================================
def exercice_6_7():
    """Trie une liste dans les deux sens."""
    nombres = [64, 25, 12, 89, 45, 37]
    print(f"Original: {nombres}")

    nombres.sort()
    print(f"Croissant: {nombres}")

    nombres.sort(reverse=True)
    print(f"Decroissant: {nombres}")


# =============================================================================
# EXERCICE 6.8 - COMPTEUR DE MOTS
# =============================================================================
def exercice_6_8():
    """Compte les occurrences de chaque mot."""
    mots = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

    # Methode 1: avec count()
    compte = {}
    for mot in mots:
        compte[mot] = mots.count(mot)
    print(f"Resultat: {compte}")

    # Methode 2: avec Counter (plus efficace)
    # from collections import Counter
    # print(f"Counter: {Counter(mots)}")


# =============================================================================
# EXERCICE 6.9 - COMPREHENSION DE LISTE
# =============================================================================
def exercice_6_9():
    """Utilise les comprehensions de listes."""
    carres = [x ** 2 for x in range(10)]
    pairs = [x for x in range(20) if x % 2 == 0]
    carres_pairs = [x ** 2 for x in range(10) if x % 2 == 0]

    print(f"Carres: {carres}")
    print(f"Pairs: {pairs}")
    print(f"Carres pairs: {carres_pairs}")


# =============================================================================
# EXERCICE 6.10 - MATRICE SIMPLE
# =============================================================================
def exercice_6_10():
    """Cree une matrice identite 3x3."""
    # Methode 1: Creee puis modifier
    matrice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        matrice[i][i] = 1

    print("Matrice identite:")
    for rangee in matrice:
        print(rangee)


# =============================================================================
# EXERCICE 6.11 - ECHANGE DE VALEURS
# =============================================================================
def exercice_6_11():
    """Echange x et y sans variable temporaire."""
    x, y = 5, 10
    print(f"Avant: x={x}, y={y}")

    # unpacking tuple
    x, y = y, x

    print(f"Apres: x={x}, y={y}")


# =============================================================================
# EXERCICE 6.12 - LISTE DE LISTES
# =============================================================================
def exercice_6_12():
    """Accede aux elements d'une liste de listes."""
    eleves = [["Alice", 15], ["Bob", 12], ["Charlie", 14]]

    print(f"Eleve 2: {eleves[1][0]}")
    print(f"Note eleve 3: {eleves[2][1]}")

    notes = [eleve[1] for eleve in eleves]
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne: {moyenne:.2f}")


# =============================================================================
# EXERCICE 6.13 - APLATISSEMENT DE LISTE
# =============================================================================
def exercice_6_13():
    """Aplatit une liste de listes."""
    liste_2d = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

    # List comprehension imbriquee
    aplatie = [element for rangee in liste_2d for element in rangee]
    print(f"Aplatie: {aplatie}")


# =============================================================================
# EXERCICE 6.14 - GENERATEUR DE NOMBRES PREMIERS
# =============================================================================
def exercice_6_14():
    """Genere les nombres premiers entre 1 et 50."""
    premiers = []
    for n in range(2, 51):
        est_premier = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(n)

    print(f"Premiers (1-50): {premiers}")


# =============================================================================
# EXERCICE 6.15 - GESTION D'INVENTAIRE
# =============================================================================
def exercice_6_15():
    """Gere un inventaire de produits."""
    inventaire = [["pomme", 50], ["banane", 30], ["orange", 40]]

    # Tri par nom
    tries = sorted(inventaire, key=lambda x: x[0])
    print(f"Tri par nom: {tries}")

    # Produit avec max quantite
    max_qte = max(inventaire, key=lambda x: x[1])
    print(f"Plus grande quantite: {max_qte}")

    # Quantite totale
    total = sum(produit[1] for produit in inventaire)
    print(f"Quantite totale: {total}")
