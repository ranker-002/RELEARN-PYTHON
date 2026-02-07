"""Package des exercices du Chapitre 2.

Ce package contient tous les exercices du chapitre 2 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_affichage_de_variables import run as exercice_2_1
from .ex_02_conversion_de_température import run as exercice_2_2
from .ex_03_calcul_de_moyenne_avec_précisi import run as exercice_2_3
from .ex_04_validation_dâge import run as exercice_2_4
from .ex_05_analyseur_de_nombre import run as exercice_2_5
from .ex_06_manipulation_de_chaînes import run as exercice_2_6
from .ex_07_formateur_de_prix import run as exercice_2_7
from .ex_08_calculateur_de_bmr_basal_metab import run as exercice_2_8
from .ex_09_validateur_demail_simplifié import run as exercice_2_9
from .ex_10_convertisseur_de_durée import run as exercice_2_10
from .ex_11_calculateur_dintérêts_composés import run as exercice_2_11
from .ex_12_générateur_dacronyme import run as exercice_2_12
from .ex_13_convertisseur_romain import run as exercice_2_13
from .ex_14_calculateur_de_note_avec_lettr import run as exercice_2_14
from .ex_15_calculateur_de_pourcentage_de_ import run as exercice_2_15

__all__ = [
    "exercice_2_1", "exercice_2_2", "exercice_2_3", "exercice_2_4", "exercice_2_5", "exercice_2_6", "exercice_2_7", "exercice_2_8", "exercice_2_9", "exercice_2_10", "exercice_2_11", "exercice_2_12", "exercice_2_13", "exercice_2_14", "exercice_2_15"
]
