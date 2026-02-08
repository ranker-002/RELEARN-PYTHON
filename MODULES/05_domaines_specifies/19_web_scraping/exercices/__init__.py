"""Package des exercices du Chapitre 21.

Ce package contient tous les exercices du chapitre 21 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_faire_une_requête_http_simple import run as exercice_21_1
from .ex_02_utiliser_des_headers_personnal import run as exercice_21_2
from .ex_03_parser_du_html_simple import run as exercice_21_3
from .ex_04_rechercher_par_classe_css import run as exercice_21_4
from .ex_05_extraire_tous_les_liens_dune_p import run as exercice_21_5
from .ex_06_utiliser_les_sélecteurs_css import run as exercice_21_6
from .ex_07_gérer_les_erreurs_de_requête import run as exercice_21_7
from .ex_08_utiliser_des_paramètres_de_req import run as exercice_21_8
from .ex_09_récupérer_et_parser_du_json import run as exercice_21_9
from .ex_10_faire_plusieurs_requêtes import run as exercice_21_10
from .ex_11_sauvegarder_des_données_en_jso import run as exercice_21_11
from .ex_12_sauvegarder_des_données_en_csv import run as exercice_21_12
from .ex_13_parser_un_tableau_html_et_sauv import run as exercice_21_13
from .ex_14_utiliser_un_user_agent_réalist import run as exercice_21_14
from .ex_15_scraper_une_page_de_données_st import run as exercice_21_15

__all__ = [
    "exercice_21_1", "exercice_21_2", "exercice_21_3", "exercice_21_4", "exercice_21_5", "exercice_21_6", "exercice_21_7", "exercice_21_8", "exercice_21_9", "exercice_21_10", "exercice_21_11", "exercice_21_12", "exercice_21_13", "exercice_21_14", "exercice_21_15"
]
