"""Package des exercices du Chapitre 26.

Ce package contient tous les exercices du chapitre 26 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_premiers_tenseurs import run as exercice_26_1
from .ex_02_opérations_sur_tenseurs import run as exercice_26_2
from .ex_03_autograd import run as exercice_26_3
from .ex_04_régression_linéaire_pytorch import run as exercice_26_4
from .ex_05_réseau_de_neurones_simple import run as exercice_26_5
from .ex_06_fonctions_dactivation import run as exercice_26_6
from .ex_07_cnn_simple import run as exercice_26_7
from .ex_08_data_loading import run as exercice_26_8
from .ex_09_transfer_learning import run as exercice_26_9
from .ex_10_lstm import run as exercice_26_10
from .ex_11_saveload_model import run as exercice_26_11
from .ex_12_gpu_utilisation import run as exercice_26_12
from .ex_13_dropout_et_batchnorm import run as exercice_26_13
from .ex_14_custom_loss import run as exercice_26_14
from .ex_15_projet_classification_dimages import run as exercice_26_15

__all__ = [
    "exercice_26_1", "exercice_26_2", "exercice_26_3", "exercice_26_4", "exercice_26_5", "exercice_26_6", "exercice_26_7", "exercice_26_8", "exercice_26_9", "exercice_26_10", "exercice_26_11", "exercice_26_12", "exercice_26_13", "exercice_26_14", "exercice_26_15"
]
