"""Package des exercices du Chapitre 11.

Ce package contient tous les exercices du chapitre 11 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_classe_simple import run as exercice_11_1
from .ex_02_classe_avec_constructeur import run as exercice_11_2
from .ex_03_attributs_et_methodes import run as exercice_11_3
from .ex_04_valeurs_par_defaut import run as exercice_11_4
from .ex_05_methode_de_classe import run as exercice_11_5
from .ex_06_methode_statique import run as exercice_11_6
from .ex_07_propriete_simple import run as exercice_11_7
from .ex_08_propriete_calculee import run as exercice_11_8
from .ex_09_attribut_de_classe import run as exercice_11_9
from .ex_10___str___et___repr__ import run as exercice_11_10
from .ex_11_validation_dans_le_setter import run as exercice_11_11
from .ex_12_classe_complete_etudiant import run as exercice_11_12
from .ex_13_classe_complete_banque import run as exercice_11_13
from .ex_14_classe_inventaire import run as exercice_11_14
from .ex_15_systeme_de_gestion import run as exercice_11_15

__all__ = [
    "exercice_11_1", "exercice_11_2", "exercice_11_3", "exercice_11_4", "exercice_11_5", "exercice_11_6", "exercice_11_7", "exercice_11_8", "exercice_11_9", "exercice_11_10", "exercice_11_11", "exercice_11_12", "exercice_11_13", "exercice_11_14", "exercice_11_15"
]
