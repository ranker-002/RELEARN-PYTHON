"""Package des exercices du Chapitre 12.

Ce package contient tous les exercices du chapitre 12 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_heritage_simple import run as exercice_12_1
from .ex_02_super_et_constructeur import run as exercice_12_2
from .ex_03_methode_de_substitution import run as exercice_12_3
from .ex_04_appeler_le_parent import run as exercice_12_4
from .ex_05_polymorphisme_simple import run as exercice_12_5
from .ex_06_hierarchie_de_formes import run as exercice_12_6
from .ex_07_heritage_multiple import run as exercice_12_7
from .ex_08_mro_et_ordre_dheritage import run as exercice_12_8
from .ex_09_classe_abstraite import run as exercice_12_9
from .ex_10_systeme_de_paiement import run as exercice_12_10
from .ex_11_hierarchie_demployes import run as exercice_12_11
from .ex_12_duck_typing import run as exercice_12_12
from .ex_13___str___et___repr___avec_herit import run as exercice_12_13
from .ex_14_comparaison_et_heritage import run as exercice_12_14
from .ex_15_systeme_de_notifications import run as exercice_12_15

__all__ = [
    "exercice_12_1", "exercice_12_2", "exercice_12_3", "exercice_12_4", "exercice_12_5", "exercice_12_6", "exercice_12_7", "exercice_12_8", "exercice_12_9", "exercice_12_10", "exercice_12_11", "exercice_12_12", "exercice_12_13", "exercice_12_14", "exercice_12_15"
]
