"""Package des exercices du Chapitre 15.

Ce package contient tous les exercices du chapitre 15 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_lecture_simple import run as exercice_15_1
from .ex_02_ecriture_simple import run as exercice_15_2
from .ex_03_compteur_de_lignes import run as exercice_15_3
from .ex_04_lignes_avec_prefixe import run as exercice_15_4
from .ex_05_lecture_csv import run as exercice_15_5
from .ex_06_ecriture_csv import run as exercice_15_6
from .ex_07_json import run as exercice_15_7
from .ex_08_chemin_absolu import run as exercice_15_8
from .ex_09_parcours_repertoire import run as exercice_15_9
from .ex_10_copier_fichier import run as exercice_15_10
from .ex_11_filtre_de_lignes import run as exercice_15_11
from .ex_12_statistiques import run as exercice_15_12
from .ex_13_remplacer_texte import run as exercice_15_13
from .ex_14_fichier_temporaire import run as exercice_15_14
from .ex_15_gestionnaire_de_logs import run as exercice_15_15

__all__ = [
    "exercice_15_1", "exercice_15_2", "exercice_15_3", "exercice_15_4", "exercice_15_5", "exercice_15_6", "exercice_15_7", "exercice_15_8", "exercice_15_9", "exercice_15_10", "exercice_15_11", "exercice_15_12", "exercice_15_13", "exercice_15_14", "exercice_15_15"
]
