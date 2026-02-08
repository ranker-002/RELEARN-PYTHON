"""Package des exercices du Chapitre 25.

Ce package contient tous les exercices du chapitre 25 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_régression_linéaire_simple import run as exercice_25_1
from .ex_02_évaluation_r²_score import run as exercice_25_2
from .ex_03_régression_multiple import run as exercice_25_3
from .ex_04_régression_logistique import run as exercice_25_4
from .ex_05_knn_classification import run as exercice_25_5
from .ex_06_arbre_de_décision import run as exercice_25_6
from .ex_07_random_forest import run as exercice_25_7
from .ex_08_k_means_clustering import run as exercice_25_8
from .ex_09_validation_croisée import run as exercice_25_9
from .ex_10_prétraitement import run as exercice_25_10
from .ex_11_pipeline import run as exercice_25_11
from .ex_12_matrice_de_confusion import run as exercice_25_12
from .ex_13_roc_auc import run as exercice_25_13
from .ex_14_feature_selection import run as exercice_25_14
from .ex_15_projet_prédiction_de_prix_immo import run as exercice_25_15

__all__ = [
    "exercice_25_1", "exercice_25_2", "exercice_25_3", "exercice_25_4", "exercice_25_5", "exercice_25_6", "exercice_25_7", "exercice_25_8", "exercice_25_9", "exercice_25_10", "exercice_25_11", "exercice_25_12", "exercice_25_13", "exercice_25_14", "exercice_25_15"
]
