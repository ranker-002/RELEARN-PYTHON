"""Package des exercices du Chapitre 1.

Ce package contient tous les exercices du chapitre 1 sous forme
 de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_hello_world import run as exercice_1_1
from .ex_02_presentation import run as exercice_1_2
from .ex_03_calcul_simple import run as exercice_1_3
from .ex_04_calculatrice import run as exercice_1_4
from .ex_05_temperature import run as exercice_1_5
from .ex_06_carre import run as exercice_1_6
from .ex_07_moyenne import run as exercice_1_7
from .ex_08_remise import run as exercice_1_8
from .ex_09_carte_visite import run as exercice_1_9
from .ex_10_interets import run as exercice_1_10
from .ex_11_devises import run as exercice_1_11
from .ex_12_imc import run as exercice_1_12
from .ex_13_panier import run as exercice_1_13
from .ex_14_email import run as exercice_1_14
from .ex_15_trajet import run as exercice_1_15

__all__ = [
    "exercice_1_1", "exercice_1_2", "exercice_1_3", "exercice_1_4",
    "exercice_1_5", "exercice_1_6", "exercice_1_7", "exercice_1_8",
    "exercice_1_9", "exercice_1_10", "exercice_1_11", "exercice_1_12",
    "exercice_1_13", "exercice_1_14", "exercice_1_15",
]
