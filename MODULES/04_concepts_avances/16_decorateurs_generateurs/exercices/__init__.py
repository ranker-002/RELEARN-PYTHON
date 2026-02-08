"""Package des exercices du Chapitre 17.

Ce package contient tous les exercices du chapitre 17 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_decorateur_simple import run as exercice_17_1
from .ex_02_decorateur_avec_arguments import run as exercice_17_2
from .ex_03_generator_simple import run as exercice_17_3
from .ex_04_generator_puissance import run as exercice_17_4
from .ex_05_yield_from import run as exercice_17_5
from .ex_06_decorateur_cache import run as exercice_17_6
from .ex_07_generator_de_nombres_premiers import run as exercice_17_7
from .ex_08_decorateur_validation import run as exercice_17_8
from .ex_09_generator_de_combinaisons import run as exercice_17_9
from .ex_10_decorateur_class import run as exercice_17_10

__all__ = [
    "exercice_17_1", "exercice_17_2", "exercice_17_3", "exercice_17_4", "exercice_17_5", "exercice_17_6", "exercice_17_7", "exercice_17_8", "exercice_17_9", "exercice_17_10"
]
