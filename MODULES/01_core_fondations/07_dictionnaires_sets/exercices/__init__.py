"""Package des exercices du Chapitre 7.

Ce package contient tous les exercices du chapitre 7 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_creation_de_dictionnaire import run as exercice_7_1
from .ex_02_acces_aux_valeurs import run as exercice_7_2
from .ex_03_modification_de_dictionnaire import run as exercice_7_3
from .ex_04_creation_de_set import run as exercice_7_4
from .ex_05_operations_sur_sets import run as exercice_7_5
from .ex_06_boutique_simple import run as exercice_7_6
from .ex_07_verification_dappartenance import run as exercice_7_7
from .ex_08_compteur_de_lettres import run as exercice_7_8
from .ex_09_comprehension_de_dictionnaire import run as exercice_7_9
from .ex_10_gestion_detudiants import run as exercice_7_10
from .ex_11_dedoublonnage import run as exercice_7_11
from .ex_12_groupement_par_categorie import run as exercice_7_12
from .ex_13_union_dinventaires import run as exercice_7_13
from .ex_14_jeu_de_cartes import run as exercice_7_14
from .ex_15_analyseur_de_texte import run as exercice_7_15

__all__ = [
    "exercice_7_1", "exercice_7_2", "exercice_7_3", "exercice_7_4", "exercice_7_5", "exercice_7_6", "exercice_7_7", "exercice_7_8", "exercice_7_9", "exercice_7_10", "exercice_7_11", "exercice_7_12", "exercice_7_13", "exercice_7_14", "exercice_7_15"
]
