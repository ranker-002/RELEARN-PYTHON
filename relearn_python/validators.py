"""Validators - Fonctions de validation pour les exercices."""

import re
from datetime import datetime
from typing import Any


def est_entier(valeur: Any) -> bool:
    """Vérifie si la valeur est un entier."""
    try:
        int(valeur)
        return True
    except (ValueError, TypeError):
        return False


def est_float(valeur: Any) -> bool:
    """Vérifie si la valeur est un nombre décimal."""
    try:
        float(valeur)
        return True
    except (ValueError, TypeError):
        return False


def est_nombre(valeur: Any) -> bool:
    """Vérifie si la valeur est un nombre (int ou float)."""
    return est_entier(valeur) or est_float(valeur)


def valider_email(email: str) -> bool:
    """Valide une adresse email."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def valider_telephone(tel: str) -> bool:
    """Valide un numéro de téléphone français."""
    tel = tel.replace(" ", "").replace(".", "-")
    pattern = r"^(\+33|0)[1-9](\d{2}){4}$"
    return bool(re.match(pattern, tel))


def valider_code_postal(cp: str) -> bool:
    """Valide un code postal français."""
    return bool(re.match(r"^[0-9]{5}$", cp))


def valider_prix(prix: Any) -> bool:
    """Valide un prix (nombre positif avec décimales)."""
    if not est_float(prix):
        return False
    return float(prix) >= 0


def valider_date(date_str: str, format_: str = "%d/%m/%Y") -> bool:
    """Valide une date au format spécifié."""
    try:
        datetime.strptime(date_str, format_)
        return True
    except ValueError:
        return False


def nettoyer_texte(texte: str) -> str:
    """Nettoie un texte (supprime espaces superflus)."""
    return " ".join(texte.split())


def contient_only_lettres(texte: str) -> bool:
    """Vérifie si le texte ne contient que des lettres."""
    return bool(re.match(r"^[a-zA-ZÀ-ÿ\s]+$", texte))


def contient_only_chiffres(texte: str) -> bool:
    """Vérifie si le texte ne contient que des chiffres."""
    return bool(re.match(r"^\d+$", texte))
