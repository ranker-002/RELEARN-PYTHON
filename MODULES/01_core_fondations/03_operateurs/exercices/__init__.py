"""Package des exercices du Chapitre 3.

Ce package contient tous les exercices du chapitre 3 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_calculatrice_avec_opérateurs import run as exercice_3_1
from .ex_02_comparaison_de_nombres import run as exercice_3_2
from .ex_03_vérification_dâge import run as exercice_3_3
from .ex_04_calcul_de_moyenne_avec_conditi import run as exercice_3_4
from .ex_05_vérification_dappartenance import run as exercice_3_5
from .ex_06_opérateurs_logiques import run as exercice_3_6
from .ex_07_calculateur_de_remise import run as exercice_3_7
from .ex_08_classification_de_triangle import run as exercice_3_8
from .ex_09_opérateurs_bit_à_bit import run as exercice_3_9
from .ex_10_vérification_de_bisextile import run as exercice_3_10
from .ex_11_calculateur_de_prix_final import run as exercice_3_11
from .ex_12_validateur_de_mot_de_passe import run as exercice_3_12
from .ex_13_jeu_de_pierre_feuille_ciseaux import run as exercice_3_13
from .ex_14_convertisseur_de_notes_en_lett import run as exercice_3_14
from .ex_15_simulateur_de_baccalauréat import run as exercice_3_15

__all__ = [
    "exercice_3_1", "exercice_3_2", "exercice_3_3", "exercice_3_4", "exercice_3_5", "exercice_3_6", "exercice_3_7", "exercice_3_8", "exercice_3_9", "exercice_3_10", "exercice_3_11", "exercice_3_12", "exercice_3_13", "exercice_3_14", "exercice_3_15"
]
