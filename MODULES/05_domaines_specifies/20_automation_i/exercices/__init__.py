"""Package des exercices du Chapitre 20.

Ce package contient tous les exercices du chapitre 20 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_lister_les_fichiers import run as exercice_20_1
from .ex_02_pathlib_basique import run as exercice_20_2
from .ex_03_créer_dossiers import run as exercice_20_3
from .ex_04_chercher_avec_glob import run as exercice_20_4
from .ex_05_copier_fichier import run as exercice_20_5
from .ex_06_infos_fichier import run as exercice_20_6
from .ex_07_renommage_simple import run as exercice_20_7
from .ex_08_suppression import run as exercice_20_8
from .ex_09_recherche_récursive import run as exercice_20_9
from .ex_10_commandes_système import run as exercice_20_10
from .ex_11_organisateur_simple import run as exercice_20_11
from .ex_12_nettoyage_dossier import run as exercice_20_12
from .ex_13_compression import run as exercice_20_13
from .ex_14_calcul_taille_dossier import run as exercice_20_14
from .ex_15_système_de_backup_complet import run as exercice_20_15

__all__ = [
    "exercice_20_1", "exercice_20_2", "exercice_20_3", "exercice_20_4", "exercice_20_5", "exercice_20_6", "exercice_20_7", "exercice_20_8", "exercice_20_9", "exercice_20_10", "exercice_20_11", "exercice_20_12", "exercice_20_13", "exercice_20_14", "exercice_20_15"
]
