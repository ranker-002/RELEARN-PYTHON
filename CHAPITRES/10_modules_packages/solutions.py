# =============================================================================
# CHAPITRE 10: MODULES ET PACKAGES - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 10.1 - CREATION DE MODULE
# =============================================================================
def exercice_10_1():
    """Cree et teste un module de maths (demonstration)."""
    # Code du module math_ops.py (a creer dans un fichier separe):
    """
    def aire_carre(cote):
        return cote ** 2
    
    def perimetre_carre(cote):
        return cote * 4
    """
    
    # Simulation de l'import
    def aire_carre(cote):
        return cote ** 2
    
    def perimetre_carre(cote):
        return cote * 4
    
    # Test
    print(f"AIRE: aire_carre(5) = {aire_carre(5)}")      # 25
    print(f"PERIMETRE: perimetre_carre(5) = {perimetre_carre(5)}")  # 20


# =============================================================================
# EXERCICE 10.2 - IMPORT SIMPLE
# =============================================================================
def exercice_10_2():
    """Utilise les modules math et random."""
    import math
    import random
    
    # Racine carree de 16
    print(f"sqrt(16) = {math.sqrt(16)}")
    
    # Nombre aleatoire 1-100
    print(f"random(1-100) = {random.randint(1, 100)}")
    
    # Factoriel de 5
    print(f"factoriel(5) = {math.factorial(5)}")


# =============================================================================
# EXERCICE 10.3 - FROM IMPORT
# =============================================================================
def exercice_10_3():
    """Utilise from ... import."""
    from random import randint
    from math import pi
    from datetime import date
    
    print(f"Nombre aleatoire: {randint(1, 100)}")
    print(f"Pi: {pi}")
    print(f"Aujourd'hui: {date.today()}")


# =============================================================================
# EXERCICE 10.4 - ALIAS
# =============================================================================
def exercice_10_4():
    """Utilise les alias pour les modules."""
    import datetime as dt
    import os
    import collections as col
    
    print(f"Date: {dt.date.today()}")
    print(f"Repertoire: {os.getcwd()}")
    
    # Counter
    c = col.Counter("hello")
    print(f"Counter('hello'): {dict(c)}")


# =============================================================================
# EXERCICE 10.5 - NOMME MAIN
# =============================================================================
def exercice_10_5():
    """Affiche la valeur de __name__."""
    print(f"__name__ dans ce module: {__name__}")
    print(f"Est-ce __main__? {__name__ == '__main__'}")
    
    # Demonstration
    print("\nNote: Quand ce fichier est execute directement,")
    print("__name__ est '__main__'.")
    print("Quand il est importe, __name__ est le nom du module.")


# =============================================================================
# EXERCICE 10.6 - LE MODULE OS
# =============================================================================
def exercice_10_6():
    """Utilise les fonctions de base du module os."""
    import os
    
    print(f"Repertoire courant: {os.getcwd()}")
    print(f"Fichiers: {os.listdir('.')}")
    
    # Creer et supprimer un dossier test
    os.mkdir("test_dir_temp")
    print("Dossier 'test_dir_temp' cree")
    
    os.rmdir("test_dir_temp")
    print("Dossier 'test_dir_temp' supprime")


# =============================================================================
# EXERCICE 10.7 - LE MODULE JSON
# =============================================================================
def exercice_10_7():
    """Utilise le module json."""
    import json
    
    # Dict vers JSON string
    donnees = {"nom": "Alice", "age": 25, "ville": "Paris"}
    json_str = json.dumps(donnees)
    print(f"Dict -> JSON: {json_str}")
    
    # JSON string vers Dict
    json_input = '{"produit": "Livre", "prix": 29.99}'
    dict_parsed = json.loads(json_input)
    print(f"JSON -> Dict: {dict_parsed}")


# =============================================================================
# EXERCICE 10.8 - LE MODULE COLLECTIONS
# =============================================================================
def exercice_10_8():
    """Utilise Counter et defaultdict."""
    from collections import Counter, defaultdict
    
    # Counter: compter les lettres
    texte = "programmation"
    c = Counter(texte)
    print(f"Counter('programmation'): {dict(c)}")
    
    # defaultdict: regroupement par lettre
    texte_list = ["pomme", "abricot", "banane", "avocat"]
    par_lettre = defaultdict(list)
    for mot in texte_list:
        par_lettre[mot[0]].append(mot)
    
    print(f"Regroupement: {dict(par_lettre)}")


# =============================================================================
# EXERCICE 10.9 - STRUCTURE DE PACKAGE
# =============================================================================
def exercice_10_9():
    """Decrit la structure d'un package bibliotheque."""
    structure = """
bibliotheque/
    __init__.py           # from .livres import *
                         # from .auteurs import *
    
    livres/
        __init__.py
        roman.py          # class Roman
        bande_dessinee.py # class BD
    
    auteurs/
        __init__.py
        auteur.py         # class Auteur
        nationality.py    # Donnees nationalites
    """
    print(structure)


# =============================================================================
# EXERCICE 10.10 - REQUIREMENTS.TXT
# =============================================================================
def exercice_10_10():
    """Cree un fichier requirements.txt."""
    requirements = """# requirements.txt
requests==2.28.0
pandas>=1.4.0
numpy>=1.20.0
flask>=2.0.0
python-dateutil>=2.8.0
"""
    print(requirements)
    print("Pour installer: pip install -r requirements.txt")


# =============================================================================
# EXERCICE 10.11 - IMPORT RELATIF
# =============================================================================
def exercice_10_11():
    """Explique les imports relatifs."""
    imports_relatifs = """
# Dans le meme package (ex: package/module_b.py):
from . import module_a
from .module_a import fonction_a

# Depuis un sous-package (ex: package/sous/sous_module.py):
from .. import fonction_parent
from ..autre_module import fonction_c

# Import d'un sous-package:
from .sous_package import module_d
"""
    print(imports_relatifs)


# =============================================================================
# EXERCICE 10.12 - MODULE COMPLET
# =============================================================================
def exercice_10_12():
    """Cree un module convertisseur complet."""
    # Ce code irait dans un fichier convertisseur.py:
    """
    def celsius_vers_fahrenheit(c):
        return c * 9/5 + 32
    
    def fahrenheit_vers_celsius(f):
        return (f - 32) * 5/9
    
    def metres_vers_pieds(m):
        return m * 3.28084
    
    if __name__ == "__main__":
        # Tests quand le module est execute directement
        print("Tests du convertisseur:")
        print(f"25C = {celsius_vers_fahrenheit(25)}F")
        print(f"77F = {fahrenheit_vers_celsius(77)}C")
        print(f"2m = {metres_vers_pieds(2)} pieds")
    """
    
    # Demonstration
    print("Code du module (a mettre dans convertisseur.py):")
    print("def celsius_vers_fahrenheit(c):")
    print("    return c * 9/5 + 32")
    print()
    print("if __name__ == '__main__':")
    print("    print('Tests: 25C =', celsius_vers_fahrenheit(25), 'F')")


# =============================================================================
# EXERCICE 10.13 - PACKAGE MULTI-MODULES
# =============================================================================
def exercice_10_13():
    """Cree le code de __init__.py pour un package calculatrice."""
    init_code = """# calculatrice/__init__.py

from .operations import additionner, soustraire, multiplier, diviser
from .geometrie import aire_carre, aire_cercle

__all__ = [
    'additionner', 'soustraire', 'multiplier', 'diviser',
    'aire_carre', 'aire_cercle'
]
"""
    print(init_code)
    print("这样, on peut faire:")
    print("from calculatrice import additionner")
    print("from calculatrice.geometrie import aire_cercle")


# =============================================================================
# EXERCICE 10.14 - SCRIPT PRINCIPAL
# =============================================================================
def exercice_10_14():
    """Cree un script principal avec __name__ == '__main__'."""
    script = """
def fonction_principale():
    print("Execution de la logique principale...")
    return 42

if __name__ == "__main__":
    print("=== Demarrage de l'application ===")
    resultat = fonction_principale()
    print(f"Resultat: {resultat}")
    print("=== Fin de l'application ===")
"""
    print(script)


# =============================================================================
# EXERCICE 10.15 - PROJET COMPLET
# =============================================================================
def exercice_10_15():
    """Propose une structure complete pour une bibliotheque."""
    structure = """
bibliotheque_app/
    __init__.py              # Point d'entree du package
    
    # Gestion des livres
    livres/
        __init__.py
        models.py            # class Livre
        operations.py        # ajouter_livre(), chercher_livre()
        database.py          # Classe de connexion BDD
    
    # Gestion des emprunts
    emprunts/
        __init__.py
        models.py            # class Emprunt
        operations.py        # creer_emprunt(), retourner_livre()
    
    # Utilisateurs
    utilisateurs/
        __init__.py
        models.py            # class Utilisateur, class Admin
    
    # Utilitaires
    utils/
        __init__.py
        date_utils.py        # Fonctions de date
        validation.py       # Fonctions de validation
    
    # Point d'entree
    main.py                  # python main.py
    
    # Tests
    tests/
        __init__.py
        test_livres.py
        test_emprunts.py
        test_utils.py
    
    # Configuration
    requirements.txt
    README.md
    config.py                 # Configuration globale
"""
    print(structure)
