"""Package des exercices du Chapitre 23.

Ce package contient tous les exercices du chapitre 23 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_premier_graphique import run as exercice_23_1
from .ex_02_diagramme_en_bâtons import run as exercice_23_2
from .ex_03_histogramme import run as exercice_23_3
from .ex_04_nuage_de_points import run as exercice_23_4
from .ex_05_diagramme_circulaire import run as exercice_23_5
from .ex_06_graphique_avec_sous_graphiques import run as exercice_23_6
from .ex_07_dataframe_pandas_plot import run as exercice_23_7
from .ex_08_personnalisation_avancée import run as exercice_23_8
from .ex_09_multiples_séries import run as exercice_23_9
from .ex_10_boîte_à_moustaches import run as exercice_23_10
from .ex_11_sauvegarde_de_graphique import run as exercice_23_11
from .ex_12_matrice_de_corrélation_pandas import run as exercice_23_12
from .ex_13_graphique_interactif_basique import run as exercice_23_13
from .ex_14_combinaison_de_graphiques import run as exercice_23_14
from .ex_15_projet_tableau_de_bord import run as exercice_23_15

__all__ = [
    "exercice_23_1", "exercice_23_2", "exercice_23_3", "exercice_23_4", "exercice_23_5", "exercice_23_6", "exercice_23_7", "exercice_23_8", "exercice_23_9", "exercice_23_10", "exercice_23_11", "exercice_23_12", "exercice_23_13", "exercice_23_14", "exercice_23_15"
]
