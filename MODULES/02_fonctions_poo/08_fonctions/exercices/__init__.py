"""Package des exercices du Chapitre 8.

Ce package contient tous les exercices du chapitre 8 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_fonction_simple import run as exercice_8_1
from .ex_02_fonction_avec_parametre import run as exercice_8_2
from .ex_03_fonction_avec_retour import run as exercice_8_3
from .ex_04_fonction_avec_plusieurs_parame import run as exercice_8_4
from .ex_05_parametres_par_defaut import run as exercice_8_5
from .ex_06_retour_multiple import run as exercice_8_6
from .ex_07_arguments_nommes import run as exercice_8_7
from .ex_08_portee_des_variables import run as exercice_8_8
from .ex_09_fonction_lambda import run as exercice_8_9
from .ex_10_filter_avec_lambda import run as exercice_8_10
from .ex_11_fonction_de_factorielle import run as exercice_8_11
from .ex_12_docstring import run as exercice_8_12
from .ex_13_early_return import run as exercice_8_13
from .ex_14_tri_avec_lambda import run as exercice_8_14
from .ex_15_calculatrice_avec_fonctions import run as exercice_8_15

__all__ = [
    "exercice_8_1", "exercice_8_2", "exercice_8_3", "exercice_8_4", "exercice_8_5", "exercice_8_6", "exercice_8_7", "exercice_8_8", "exercice_8_9", "exercice_8_10", "exercice_8_11", "exercice_8_12", "exercice_8_13", "exercice_8_14", "exercice_8_15"
]
