"""Utils - Fonctions utilitaires pour les exercices."""

import sys
from typing import Any


def demander_entree(message: str) -> str:
    """Demande une entrée à l'utilisateur avec un message."""
    return input(message)


def demander_nombre(message: str, type_: type = float) -> Any:
    """Demande un nombre et le convertit au type spécifié."""
    while True:
        try:
            return type_(input(message))
        except ValueError:
            print(f"Erreur: Veuillez entrer un {type_.__name__} valide.")


def demander_entier(message: str, min_val: int | None = None, max_val: int | None = None) -> int:
    """Demande un entier avec des contraintes optionnelles."""
    while True:
        try:
            valeur = int(input(message))
            if min_val is not None and valeur < min_val:
                print(f"Erreur: La valeur doit être >= {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f"Erreur: La valeur doit être <= {max_val}")
                continue
            return valeur
        except ValueError:
            print("Erreur: Veuillez entrer un entier valide.")


def demander_float(message: str, min_val: float | None = None, max_val: float | None = None) -> float:
    """Demande un float avec des contraintes optionnelles."""
    while True:
        try:
            valeur = float(input(message))
            if min_val is not None and valeur < min_val:
                print(f"Erreur: La valeur doit être >= {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f"Erreur: La valeur doit être <= {max_val}")
                continue
            return valeur
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide.")


def afficher_titre(texte: str, caractere: str = "=", longueur: int = 50) -> None:
    """Affiche un titre encadré."""
    print(f"\n{caractere * longueur}")
    print(f"{texte:^{longueur}}")
    print(f"{caractere * longueur}\n")


def afficher_boxe(texte: str, titre: str = "") -> None:
    """Affiche du texte dans une boîte."""
    lignes = texte.strip().split("\n")
    max_len = max(len(ligne) for ligne in lignes)
    max_len = max(max_len, len(titre))

    print("┌" + "─" * (max_len + 2) + "┐")
    if titre:
        print(f"│ {titre:<{max_len + 1}} │")
        print("├" + "─" * (max_len + 2) + "┤")
    for ligne in lignes:
        print(f"│ {ligne:<{max_len + 1}} │")
    print("└" + "─" * (max_len + 2) + "┘")


def separateur(caractere: str = "-", longueur: int = 50) -> None:
    """Affiche un séparateur."""
    print(caractere * longueur)
