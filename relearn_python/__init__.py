"""relearn-python - Python Mastery Learning Package

Outils et utilitaires pour l'apprentissage de Python.
"""

__version__ = "1.0.0"

from .utils import (
    demander_entree,
    demander_nombre,
    demander_entier,
    demander_float,
    afficher_titre,
    afficher_boxe,
    separateur,
)

from .validators import (
    est_entier,
    est_float,
    est_nombre,
    valider_email,
    valider_telephone,
    valider_code_postal,
    valider_prix,
    valider_date,
)

__all__ = [
    "__version__",
    "demander_entree",
    "demander_nombre",
    "demander_entier",
    "demander_float",
    "afficher_titre",
    "afficher_boxe",
    "separateur",
    "est_entier",
    "est_float",
    "est_nombre",
    "valider_email",
    "valider_telephone",
    "valider_code_postal",
    "valider_prix",
    "valider_date",
]
