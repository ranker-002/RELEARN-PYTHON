"""Package des exercices du Chapitre 9.

Ce package contient tous les exercices du chapitre 9 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_args_simple import run as exercice_9_1
from .ex_02_kwargs_simple import run as exercice_9_2
from .ex_03_combinaison_args_et_kwargs import run as exercice_9_3
from .ex_04_positional_only import run as exercice_9_4
from .ex_05_keyword_only import run as exercice_9_5
from .ex_06_deballage_darguments import run as exercice_9_6
from .ex_07_decorateur_simple import run as exercice_9_7
from .ex_08_decorateur_de_timing import run as exercice_9_8
from .ex_09_fonction_flexible import run as exercice_9_9
from .ex_10_ordre_des_parametres import run as exercice_9_10
from .ex_11_decorateur_avec_arguments import run as exercice_9_11
from .ex_12_validateur_avec_args import run as exercice_9_12
from .ex_13_logger_avance import run as exercice_9_13
from .ex_14_constructeur_de_requetes import run as exercice_9_14
from .ex_15_decorateur_de_cache import run as exercice_9_15

__all__ = [
    "exercice_9_1", "exercice_9_2", "exercice_9_3", "exercice_9_4", "exercice_9_5", "exercice_9_6", "exercice_9_7", "exercice_9_8", "exercice_9_9", "exercice_9_10", "exercice_9_11", "exercice_9_12", "exercice_9_13", "exercice_9_14", "exercice_9_15"
]
