# =============================================================================
# CHAPITRE 8: FONCTIONS - EXERCICES
# =============================================================================
# Niveau: DEBUTANT
# Concepts abordes: def, return, parametres, arguments, scope, lambda
# =============================================================================

# =============================================================================
# EXERCICE 8.1 - FONCTION SIMPLE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Tres facile)
#
# ENONCE:
# Creez une fonction dire_bonjour() qui affiche "Bonjour!".
# Appelez la fonction.
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_1():
    pass


# =============================================================================
# EXERCICE 8.2 - FONCTION AVEC PARAMETRE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Tres facile)
#
# ENONCE:
# Creez une fonction saluer(nom) qui affiche "Bonjour, [nom]!".
#
# EXEMPLE:
# saluer("Alice") -> "Bonjour, Alice!"
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_2():
    pass


# =============================================================================
# EXERCICE 8.3 - FONCTION AVEC RETOUR
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Tres facile)
#
# ENONCE:
# Creez une fonction carre(nombre) qui retourne le carre.
#
# EXEMPLE:
# resultat = carre(5)
# print(resultat)  # 25
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_3():
    pass


# =============================================================================
# EXERCICE 8.4 - FONCTION AVEC PLUSIEURS PARAMETRES
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction presenter(nom, age, ville) qui retourne
# une phrase de presentation.
#
# EXEMPLE:
# presenter("Alice", 25, "Paris")
# -> "Alice, 25 ans, habite a Paris"
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_4():
    pass


# =============================================================================
# EXERCICE 8.5 - PARAMETRES PAR DEFAUT
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction salutation(nom, message="Bonjour") qui
# utilise "Bonjour" comme message par defaut.
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_5():
    pass


# =============================================================================
# EXERCICE 8.6 - RETOUR MULTIPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction divmod_custom(a, b) qui retourne le quotient
# et le reste de la division a // b et a % b.
#
# EXEMPLE:
# q, r = divmod_custom(17, 5)
# print(q, r)  # 3 2
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_6():
    pass


# =============================================================================
# EXERCICE 8.7 - ARGUMENTS NOMMES
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction afficher_info(prenom, nom, age) et appelez-la
# avec des arguments dans un ordre different.
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_7():
    pass


# =============================================================================
# EXERCICE 8.8 - PORTEE DES VARIABLES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Demontrez la portee des variables avec une variable globale
# et une variable locale.
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_8():
    pass


# =============================================================================
# EXERCICE 8.9 - FONCTION LAMBDA
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une lambda pour calculer le cube (x**3).
# Utilisez-la avec map() sur [1, 2, 3, 4].
#
# RESULTAT ATTENDU: [1, 8, 27, 64]
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_9():
    pass


# =============================================================================
# EXERCICE 8.10 - FILTER AVEC LAMBDA
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Utilisez filter() avec une lambda pour garder uniquement
# les nombres divisibles par 3 de la liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
#
# RESULTAT ATTENDU: [3, 6, 9]
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_10():
    pass


# =============================================================================
# EXERCICE 8.11 - FONCTION DE FACTORIELLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une fonction factorielle(n) recursive.
#
# INDICE: n! = n * (n-1)!
# 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_11():
    pass


# =============================================================================
# EXERCICE 8.12 - DOCSTRING
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une fonction avec une docstring decrivant son usage.
# Affichez la docstring avec help().
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_12():
    pass


# =============================================================================
# EXERCICE 8.13 - EARLY RETURN
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une fonction valider_age(age) qui:
# - Retourne "Mineur" si age < 18
# - Retourne "Majeur" si 18 <= age < 65
# - Retourne "Senior" sinon
#
# Utilisez early return (pas de else-if).
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_13():
    pass


# =============================================================================
# EXERCICE 8.14 - TRI AVEC LAMBDA
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Triez une liste de tuples par differentes cles.
#
# Personne: [("Alice", 25, 170), ("Bob", 30, 165), ("Charlie", 25, 180)]
# - Par age
# - Par age, puis par taille
#
# INDICE: key=lambda x: (x[1], x[2])
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_14():
    pass


# =============================================================================
# EXERCICE 8.15 - CALCULATRICE AVEC FONCTIONS
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme de calculatrice avec:
# - addition(a, b)
# - soustraction(a, b)
# - multiplication(a, b)
# - division(a, b)
# - Application: demander 2 nombres et une operation
#
# VOTRE CODE CI-DESSOUS:
def exercice_8_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 8 - EXERCICES")
    print("=" * 50)
    print("Executez python verification.py pour valider")
    print("=" * 50)
