"""Package des exercices du Chapitre 18.

Ce package contient tous les exercices du chapitre 18 sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
from .ex_01_thread_simple import run as exercice_18_1
from .ex_02_plusieurs_threads import run as exercice_18_2
from .ex_03_compteur_sécurisé import run as exercice_18_3
from .ex_04_threadpoolexecutor import run as exercice_18_4
from .ex_05_lock_avec_race_condition import run as exercice_18_5
from .ex_06_queue_producteur_consommateur import run as exercice_18_6
from .ex_07_thread_local import run as exercice_18_7
from .ex_08_barrier import run as exercice_18_8
from .ex_09_event_threads import run as exercice_18_9
from .ex_10_timer_thread import run as exercice_18_10
from .ex_11_semaphore import run as exercice_18_11
from .ex_12_callable_future import run as exercice_18_12
from .ex_13_as_complete import run as exercice_18_13
from .ex_14_threadpool_avec_callback import run as exercice_18_14
from .ex_15_threading_dans_classe import run as exercice_18_15

__all__ = [
    "exercice_18_1", "exercice_18_2", "exercice_18_3", "exercice_18_4", "exercice_18_5", "exercice_18_6", "exercice_18_7", "exercice_18_8", "exercice_18_9", "exercice_18_10", "exercice_18_11", "exercice_18_12", "exercice_18_13", "exercice_18_14", "exercice_18_15"
]
