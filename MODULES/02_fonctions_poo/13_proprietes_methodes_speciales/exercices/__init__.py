"""Package des exercices du Chapitre 13.

Ce package contient tous les exercices du chapitre 13 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_propriete_simple import run as exercice_13_1
from .ex_02_propriete_calculee import run as exercice_13_2
from .ex_03___str___et___repr__ import run as exercice_13_3
from .ex_04_comparaison_simple import run as exercice_13_4
from .ex_05_iterateur_simple import run as exercice_13_5
from .ex_06_contexte_simple import run as exercice_13_6
from .ex_07_operateurs_arithmetiques import run as exercice_13_7
from .ex_08_conteneur_personnalise import run as exercice_13_8
from .ex_09_iterateur_filtre import run as exercice_13_9
from .ex_10_propriete_avec_cache import run as exercice_13_10
from .ex_11_hachage_et_set import run as exercice_13_11
from .ex_12_generateur_personnalise import run as exercice_13_12
from .ex_13_methode_dappel import run as exercice_13_13
from .ex_14_classe_sliceable import run as exercice_13_14

__all__ = [
    "exercice_13_1", "exercice_13_2", "exercice_13_3", "exercice_13_4", "exercice_13_5", "exercice_13_6", "exercice_13_7", "exercice_13_8", "exercice_13_9", "exercice_13_10", "exercice_13_11", "exercice_13_12", "exercice_13_13", "exercice_13_14"
]
