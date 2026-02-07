"""Package des exercices du Chapitre 5.

Ce package contient tous les exercices du chapitre 5 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_compteur_simple import run as exercice_5_1
from .ex_02_compteur_a_rebours import run as exercice_5_2
from .ex_03_somme_des_nombres import run as exercice_5_3
from .ex_04_table_de_multiplication import run as exercice_5_4
from .ex_05_liste_avec_enumerate import run as exercice_5_5
from .ex_06_nombres_pairs import run as exercice_5_6
from .ex_07_recherche_de_nombre import run as exercice_5_7
from .ex_08_factorielle import run as exercice_5_8
from .ex_09_nombre_mystere import run as exercice_5_9
from .ex_10_pyramide_detoiles import run as exercice_5_10
from .ex_11_validation_dentree import run as exercice_5_11
from .ex_12_sequence_de_fibonacci import run as exercice_5_12
from .ex_13_compteur_de_voyelles import run as exercice_5_13
from .ex_14_triangle_de_pascal import run as exercice_5_14
from .ex_15_jeu_de_devinette_avec_limite import run as exercice_5_15

__all__ = [
    "exercice_5_1", "exercice_5_2", "exercice_5_3", "exercice_5_4", "exercice_5_5", "exercice_5_6", "exercice_5_7", "exercice_5_8", "exercice_5_9", "exercice_5_10", "exercice_5_11", "exercice_5_12", "exercice_5_13", "exercice_5_14", "exercice_5_15"
]
