"""Package des exercices du Chapitre 16.

Ce package contient tous les exercices du chapitre 16 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_json import run as exercice_16_1
from .ex_02_pickle import run as exercice_16_2
from .ex_03_csv_avec_dictreader import run as exercice_16_3
from .ex_04_yaml import run as exercice_16_4
from .ex_05_configjson import run as exercice_16_5
from .ex_06_sauvegarde_etats import run as exercice_16_6
from .ex_07_xml import run as exercice_16_7
from .ex_08_message_json import run as exercice_16_8
from .ex_09_class_custom import run as exercice_16_9
from .ex_10_validation_json import run as exercice_16_10

__all__ = [
    "exercice_16_1", "exercice_16_2", "exercice_16_3", "exercice_16_4", "exercice_16_5", "exercice_16_6", "exercice_16_7", "exercice_16_8", "exercice_16_9", "exercice_16_10"
]
