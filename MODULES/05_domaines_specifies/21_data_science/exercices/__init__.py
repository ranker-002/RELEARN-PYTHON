"""Package des exercices du Chapitre 22.

Ce package contient tous les exercices du chapitre 22 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_numpy_basique import run as exercice_22_1
from .ex_02_tableaux_2d import run as exercice_22_2
from .ex_03_pandas_dataframe import run as exercice_22_3
from .ex_04_sélection_et_filtre import run as exercice_22_4
from .ex_05_statistiques import run as exercice_22_5
from .ex_06_group_by import run as exercice_22_6
from .ex_07_tri_et_rang import run as exercice_22_7
from .ex_08_valeurs_manquantes import run as exercice_22_8
from .ex_09_créer_colonne import run as exercice_22_9
from .ex_10_enumérer import run as exercice_22_10
from .ex_11_pivot_table import run as exercice_22_11
from .ex_12_concaténation import run as exercice_22_12
from .ex_13_fusion import run as exercice_22_13
from .ex_14_test_statistique import run as exercice_22_14
from .ex_15_analyse_complete import run as exercice_22_15

__all__ = [
    "exercice_22_1", "exercice_22_2", "exercice_22_3", "exercice_22_4", "exercice_22_5", "exercice_22_6", "exercice_22_7", "exercice_22_8", "exercice_22_9", "exercice_22_10", "exercice_22_11", "exercice_22_12", "exercice_22_13", "exercice_22_14", "exercice_22_15"
]
