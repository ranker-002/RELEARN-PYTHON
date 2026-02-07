"""Package des exercices du Chapitre 14.

Ce package contient tous les exercices du chapitre 14 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_tryexcept_simple import run as exercice_14_1
from .ex_02_plusieurs_exceptions import run as exercice_14_2
from .ex_03_else_et_finally import run as exercice_14_3
from .ex_04_exception_personnalisee import run as exercice_14_4
from .ex_05_validation_simple import run as exercice_14_5
from .ex_06_hierarchie_dexceptions import run as exercice_14_6
from .ex_07_propagation import run as exercice_14_7
from .ex_08_relancer_exception import run as exercice_14_8
from .ex_09_context_manager import run as exercice_14_9
from .ex_10_retry_pattern import run as exercice_14_10
from .ex_11_validateur_complet import run as exercice_14_11
from .ex_12_système_de_fichiers_sécurisé import run as exercice_14_12
from .ex_13_exception_chainee import run as exercice_14_13
from .ex_14_pagination_sécurisée import run as exercice_14_14
from .ex_15_système_de_logging_complet import run as exercice_14_15

__all__ = [
    "exercice_14_1", "exercice_14_2", "exercice_14_3", "exercice_14_4", "exercice_14_5", "exercice_14_6", "exercice_14_7", "exercice_14_8", "exercice_14_9", "exercice_14_10", "exercice_14_11", "exercice_14_12", "exercice_14_13", "exercice_14_14", "exercice_14_15"
]
