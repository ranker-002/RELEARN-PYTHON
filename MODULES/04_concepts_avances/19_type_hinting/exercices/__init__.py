"""Package des exercices du Chapitre 19.

Ce package contient tous les exercices du chapitre 19 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_types_simples import run as exercice_19_1
from .ex_02_listes_tyées import run as exercice_19_2
from .ex_03_dictionnaires_tyées import run as exercice_19_3
from .ex_04_fonction_avec_types import run as exercice_19_4
from .ex_05_optional import run as exercice_19_5
from .ex_06_union import run as exercice_19_6
from .ex_07_callable import run as exercice_19_7
from .ex_08_tuple import run as exercice_19_8
from .ex_09_typedict import run as exercice_19_9
from .ex_10_dataclass_avec_types import run as exercice_19_10
from .ex_11_generic import run as exercice_19_11
from .ex_12_protocol import run as exercice_19_12
from .ex_13_complexe import run as exercice_19_13
from .ex_14_type_checking_simule import run as exercice_19_14
from .ex_15_module_complet import run as exercice_19_15

__all__ = [
    "exercice_19_1", "exercice_19_2", "exercice_19_3", "exercice_19_4", "exercice_19_5", "exercice_19_6", "exercice_19_7", "exercice_19_8", "exercice_19_9", "exercice_19_10", "exercice_19_11", "exercice_19_12", "exercice_19_13", "exercice_19_14", "exercice_19_15"
]
