"""Package des exercices du Chapitre 24.

Ce package contient tous les exercices du chapitre 24 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_première_application_flask import run as exercice_24_1
from .ex_02_routes_avec_paramètres import run as exercice_24_2
from .ex_03_routes_multiples import run as exercice_24_3
from .ex_04_template_de_base import run as exercice_24_4
from .ex_05_template_avec_variables import run as exercice_24_5
from .ex_06_boucle_dans_template import run as exercice_24_6
from .ex_07_formulaire_simple import run as exercice_24_7
from .ex_08_première_api_fastapi import run as exercice_24_8
from .ex_09_modèle_pydantic import run as exercice_24_9
from .ex_10_crud_complet import run as exercice_24_10
from .ex_11_api_rest_produits import run as exercice_24_11
from .ex_12_authentification_simple import run as exercice_24_12
from .ex_13_template_hérité import run as exercice_24_13
from .ex_14_api_avec_base_de_données import run as exercice_24_14
from .ex_15_projet_blog_complet import run as exercice_24_15

__all__ = [
    "exercice_24_1", "exercice_24_2", "exercice_24_3", "exercice_24_4", "exercice_24_5", "exercice_24_6", "exercice_24_7", "exercice_24_8", "exercice_24_9", "exercice_24_10", "exercice_24_11", "exercice_24_12", "exercice_24_13", "exercice_24_14", "exercice_24_15"
]
