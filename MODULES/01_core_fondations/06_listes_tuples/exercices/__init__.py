"""Package des exercices du Chapitre 6.

Ce package contient tous les exercices du chapitre 6 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_creation_de_liste import run as exercice_6_1
from .ex_02_acces_aux_elements import run as exercice_6_2
from .ex_03_slicing_de_liste import run as exercice_6_3
from .ex_04_modification_de_liste import run as exercice_6_4
from .ex_05_creation_de_tuple import run as exercice_6_5
from .ex_06_packing_et_unpacking import run as exercice_6_6
from .ex_07_tri_de_liste import run as exercice_6_7
from .ex_08_compteur_de_mots import run as exercice_6_8
from .ex_09_comprehension_de_liste import run as exercice_6_9
from .ex_10_matrice_simple import run as exercice_6_10
from .ex_11_echange_de_valeurs import run as exercice_6_11
from .ex_12_liste_de_listes import run as exercice_6_12
from .ex_13_aplatissement_de_liste import run as exercice_6_13
from .ex_14_generateur_de_nombres_premiers import run as exercice_6_14
from .ex_15_gestion_dinventaire import run as exercice_6_15

__all__ = [
    "exercice_6_1", "exercice_6_2", "exercice_6_3", "exercice_6_4", "exercice_6_5", "exercice_6_6", "exercice_6_7", "exercice_6_8", "exercice_6_9", "exercice_6_10", "exercice_6_11", "exercice_6_12", "exercice_6_13", "exercice_6_14", "exercice_6_15"
]
