# =============================================================================
# CHAPITRE 10: MODULES ET PACKAGES - EXERCICES
# =============================================================================
# Niveau: INTERMEDIAIRE
# Concepts abordes: import, modules, packages, __name__, pip, structure
# =============================================================================

# =============================================================================
# EXERCICE 10.1 - CREATION DE MODULE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez un module math_ops.py avec deux fonctions:
# - aire_carre(cote)
# - perimetre_carre(cote)
#
# Puis importez-le et testez-le dans ce fichier.
#
# INDICE: Vous pouvez tester avec exec() pour cet exercice
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_1():
    pass


# =============================================================================
# EXERCICE 10.2 - IMPORT SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Utilisez les modules math et random pour:
# - Calculer la racine carree de 16
# - Generer un nombre aleatoire entre 1 et 100
# - Calculer le factoriel de 5
#
# RESULTATS ATTENDUS:
# sqrt(16) = 4.0
# random entre 1-100
# factoriel(5) = 120
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_2():
    pass


# =============================================================================
# EXERCICE 10.3 - FROM IMPORT
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Importer specifiquement les fonctions suivantes:
# - random.randint
# - math.pi
# - datetime.date.today
#
# Affichez un message utilise ces imports.
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_3():
    pass


# =============================================================================
# EXERCICE 10.4 - ALIAS
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Importez les modules avec des alias:
# - datetime -> dt
# - collections -> col
# - os -> operating
#
# Utilisez ces alias pour afficher la date et lister les fichiers.
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_4():
    pass


# =============================================================================
# EXERCICE 10.5 - NOMME MAIN
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Verifiez la valeur de __name__ quand ce module est execute
# directement vs quand il est importe.
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_5():
    pass


# =============================================================================
# EXERCICE 10.6 - LE MODULE OS
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Utilisez os pour:
# - Afficher le repertoire courant
# - Creer un dossier "test_dir"
# - Lister le contenu du dossier courant
# - Supprimer "test_dir"
#
# INDICE: os.getcwd(), os.mkdir(), os.listdir(), os.rmdir()
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_6():
    pass


# =============================================================================
# EXERCICE 10.7 - LE MODULE JSON
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Utilisez json pour:
# - Convertir un dictionnaire en JSON string
# - Parser un JSON string en dictionnaire
#
# EXEMPLE:
# donnees = {"nom": "Alice", "age": 25}
# json_str = '{"nom": "Alice", "age": 25}'
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_7():
    pass


# =============================================================================
# EXERCICE 10.8 - LE MODULE COLLECTIONS
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Utilisez Counter pour compter les lettres dans "programmation".
# Utilisez defaultdict(list) pour creer un regroupement par lettre.
#
# INDICE:
# Counter("programmation") compte les lettres
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_8():
    pass


# =============================================================================
# EXERCICE 10.9 - STRUCTURE DE PACKAGE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Decrivez la structure de fichiers d'un projet avec:
# - Package principal: "bibliotheque"
# - Deux modules: "livres" et "auteurs"
# - Un fichier __init__.py dans chaque dossier
#
# Affichez cette structure en pseudo-code.
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_9():
    pass


# =============================================================================
# EXERCICE 10.10 - REQUIREMENTS.TXT
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez le contenu d'un fichier requirements.txt avec:
# - requests version 2.28.0
# - pandas version superieure a 1.4.0
# - numpy version superieure ou egale a 1.20.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_10():
    pass


# =============================================================================
# EXERCICE 10.11 - IMPORT RELATIF
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Expliquez comment faire un import relatif pour:
# - Depuis module_b, importer depuis le meme package (module_a)
# - Depuis module_c (sous-package), importer depuis le parent
# - Importer une fonction d'un sous-package
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_11():
    pass


# =============================================================================
# EXERCICE 10.12 - MODULE COMPLET
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez un module "convertisseur" avec fonctions:
# - celsius_vers_fahrenheit(c)
# - fahrenheit_vers_celsius(f)
# - metres_vers_pieds(m)
#
# Le module doit pouvoir etre execute directement pour des tests.
#
# INDICE: Utiliser if __name__ == "__main__"
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_12():
    pass


# =============================================================================
# EXERCICE 10.13 - PACKAGE MULTI-MODULES
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Decrivez un package "calculatrice" avec:
# - operations.py (add, sub, mul, div)
# - geometrie.py (aire_carre, aire_cercle)
# - __init__.py qui importe tout
#
# Donnez le code de __init__.py
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_13():
    pass


# =============================================================================
# EXERCICE 10.14 - SCRIPT PRINCIPAL
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un script principal qui:
# 1. Verifie si execute directement (pas dans un import)
# 2. Affiche un message de demarrage
# 3. Appelle une fonction de test
# 4. Affiche un message de fin
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_14():
    pass


# =============================================================================
# EXERCICE 10.15 - PROJET COMPLET
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Proposez une structure complete pour une application
# de gestion de bibliotheque avec:
# - Gestion des livres
# - Gestion des emprunts
# - Tests unitaires
# - Fichier requirements.txt
#
# Decrivez la structure en pseudo-code.
#
# VOTRE CODE CI-DESSOUS:
def exercice_10_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 10 - EXERCICES")
    print("=" * 50)
    print("Execez python verification.py pour valider")
    print("=" * 50)
