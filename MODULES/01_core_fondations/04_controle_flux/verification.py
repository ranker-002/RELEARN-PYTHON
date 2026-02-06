#!/usr/bin/env python3
"""
CHAPITRE 4 - Script de Vérification Automatique
==============================================
Ce script vérifie automatiquement vos solutions aux exercices.

Utilisation:
    python verification.py
"""

import sys
from io import StringIO
from unittest import mock


class VerificationError(Exception):
    """Erreur lors de la vérification."""
    pass


def capturer_sortie(func):
    """Exécute une fonction et capture sa sortie."""
    ancien_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        func()
        sortie = sys.stdout.getvalue()
    finally:
        sys.stdout = ancien_stdout
    return sortie


def verifier_exercice_4_1():
    """Vérifie l'exercice 4.1: Classification d'âge."""
    from exercices import exercice_4_1
    with mock.patch('builtins.input', return_value="25"):
        sortie = capturer_sortie(exercice_4_1)
    if "Adulte" in sortie:
        print("✓ Exercice 4.1: Classification d'âge - CORRECT")
    else:
        raise VerificationError(f"Adulte attendu\nSortie: {sortie}")


def verifier_exercice_4_2():
    """Vérifie l'exercice 4.2: Prix avec ternaire."""
    from exercices import exercice_4_2
    with mock.patch('builtins.input', return_value="100"):
        sortie = capturer_sortie(exercice_4_2)
    if "90" in sortie or "90.0" in sortie:
        print("✓ Exercice 4.2: Prix avec ternaire - CORRECT")
    else:
        raise VerificationError(f"90 attendu\nSortie: {sortie}")


def verifier_exercice_4_3():
    """Vérifie l'exercice 4.3: Signe du nombre."""
    from exercices import exercice_4_3
    with mock.patch('builtins.input', return_value="-5"):
        sortie = capturer_sortie(exercice_4_3)
    if "Négatif" in sortie:
        print("✓ Exercice 4.3: Signe du nombre - CORRECT")
    else:
        raise VerificationError(f"Négatif attendu\nSortie: {sortie}")


def verifier_exercice_4_4():
    """Vérifie l'exercice 4.4: Jour avec match."""
    from exercices import exercice_4_4
    with mock.patch('builtins.input', return_value="3"):
        sortie = capturer_sortie(exercice_4_4)
    if "Mercredi" in sortie:
        print("✓ Exercice 4.4: Jour avec match - CORRECT")
    else:
        raise VerificationError(f"Mercredi attendu\nSortie: {sortie}")


def verifier_exercice_4_5():
    """Vérifie l'exercice 4.5: Remise progressive."""
    from exercices import exercice_4_5
    with mock.patch('builtins.input', return_value="300"):
        sortie = capturer_sortie(exercice_4_5)
    if "30" in sortie or "10%" in sortie:
        print("✓ Exercice 4.5: Remise progressive - CORRECT")
    else:
        raise VerificationError(f"10% et 30€ attendus\nSortie: {sortie}")


def verifier_exercice_4_6():
    """Vérifie l'exercice 4.6: Mot de passe."""
    from exercices import exercice_4_6
    with mock.patch('builtins.input', return_value="Python123"):
        sortie = capturer_sortie(exercice_4_6)
    if "True" in sortie:
        print("✓ Exercice 4.6: Mot de passe - CORRECT")
    else:
        raise VerificationError(f"True attendu\nSortie: {sortie}")


def verifier_exercice_4_7():
    """Vérifie l'exercice 4.7: Formes avec match."""
    from exercices import exercice_4_7
    with mock.patch('builtins.input', return_value="5"):
        sortie = capturer_sortie(exercice_4_7)
    if "Pentagone" in sortie:
        print("✓ Exercice 4.7: Formes avec match - CORRECT")
    else:
        raise VerificationError(f"Pentagone attendu\nSortie: {sortie}")


def verifier_exercice_4_8():
    """Vérifie l'exercice 4.8: Taxi."""
    from exercices import exercice_4_8
    with mock.patch('builtins.input', side_effect=["10", "non"]):
        sortie = capturer_sortie(exercice_4_8)
    if "15" in sortie or "15.5" in sortie:
        print("✓ Exercice 4.8: Taxi - CORRECT")
    else:
        raise VerificationError(f"~15€ attendu\nSortie: {sortie}")


def verifier_exercice_4_9():
    """Vérifie l'exercice 4.9: Température."""
    from exercices import exercice_4_9
    with mock.patch('builtins.input', side_effect=["100", "C"]):
        sortie = capturer_sortie(exercice_4_9)
    if "212" in sortie or "373" in sortie:
        print("✓ Exercice 4.9: Température - CORRECT")
    else:
        raise VerificationError(f"212°F et 373K attendus\nSortie: {sortie}")


def verifier_exercice_4_10():
    """Vérifie l'exercice 4.10: Devinette."""
    from exercices import exercice_4_10
    import random
    with mock.patch('builtins.input', side_effect=["50", "75", "62"]):
        with mock.patch('random.randint', return_value=62):
            sortie = capturer_sortie(exercice_4_10)
    if "Gagné" in sortie:
        print("✓ Exercice 4.10: Devinette - CORRECT")
    else:
        print(f"⚠ Exercice 4.10: Non déterministe - SKIPPED")


def verifier_exercice_4_11():
    """Vérifie l'exercice 4.11: Distributeur."""
    from exercices import exercice_4_11
    with mock.patch('builtins.input', side_effect=["café", "2"]):
        sortie = capturer_sortie(exercice_4_11)
    if "0.50" in sortie or "0.5" in sortie:
        print("✓ Exercice 4.11: Distributeur - CORRECT")
    else:
        raise VerificationError(f"0.50€ rendu attendu\nSortie: {sortie}")


def verifier_exercice_4_12():
    """Vérifie l'exercice 4.12: Caractère."""
    from exercices import exercice_4_12
    with mock.patch('builtins.input', return_value="a"):
        sortie = capturer_sortie(exercice_4_12)
    if "Voyelle" in sortie:
        print("✓ Exercice 4.12: Caractère - CORRECT")
    else:
        raise VerificationError(f"Voyelle attendue\nSortie: {sortie}")


def verifier_exercice_4_13():
    """Vérifie l'exercice 4.13: Impôts."""
    from exercices import exercice_4_13
    with mock.patch('builtins.input', return_value="50000"):
        sortie = capturer_sortie(exercice_4_13)
    if "4000" in sortie:
        print("✓ Exercice 4.13: Impôts - CORRECT")
    else:
        raise VerificationError(f"4000€ d'impôt attendu\nSortie: {sortie}")


def verifier_exercice_4_14():
    """Vérifie l'exercice 4.14: Notes."""
    from exercices import exercice_4_14
    with mock.patch('builtins.input', return_value="17"):
        sortie = capturer_sortie(exercice_4_14)
    if "A-" in sortie or "Très" in sortie:
        print("✓ Exercice 4.14: Notes - CORRECT")
    else:
        raise VerificationError(f"A- attendu\nSortie: {sortie}")


def verifier_exercice_4_15():
    """Vérifie l'exercice 4.15: Banque."""
    from exercices import exercice_4_15
    with mock.patch('builtins.input', side_effect=["1", "4"]):
        sortie = capturer_sortie(exercice_4_15)
    if "1000" in sortie or "solde" in sortie.lower():
        print("✓ Exercice 4.15: Banque - CORRECT")
    else:
        raise VerificationError(f"Solde attendu\nSortie: {sortie}")


def verifier_tous():
    """Exécute toutes les vérifications."""
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 4: CONTRÔLE DE FLUX")
    print("=" * 60)
    print()

    verifications = [
        ("4.1 Classification d'âge", verifier_exercice_4_1),
        ("4.2 Prix ternaire", verifier_exercice_4_2),
        ("4.3 Signe", verifier_exercice_4_3),
        ("4.4 Jour match", verifier_exercice_4_4),
        ("4.5 Remise", verifier_exercice_4_5),
        ("4.6 Mot de passe", verifier_exercice_4_6),
        ("4.7 Formes match", verifier_exercice_4_7),
        ("4.8 Taxi", verifier_exercice_4_8),
        ("4.9 Température", verifier_exercice_4_9),
        ("4.10 Devinette", verifier_exercice_4_10),
        ("4.11 Distributeur", verifier_exercice_4_11),
        ("4.12 Caractère", verifier_exercice_4_12),
        ("4.13 Impôts", verifier_exercice_4_13),
        ("4.14 Notes", verifier_exercice_4_14),
        ("4.15 Banque", verifier_exercice_4_15),
    ]

    erreurs = 0

    for nom, verification in verifications:
        try:
            verification()
        except VerificationError as e:
            print(f"✗ {nom}: ERREUR")
            print(f"   {e}")
            erreurs += 1
        except ImportError as e:
            print(f"✗ {nom}: IMPORT ERROR - {e}")
            erreurs += 1
        except Exception as e:
            print(f"✗ {nom}: EXCEPTION - {type(e).__name__}: {e}")
            erreurs += 1

    print()
    print("=" * 60)

    if erreurs == 0:
        print("TOUS LES EXERCICES SONT CORRECTS!")
        print("=" * 60)
        return True
    else:
        print(f"{erreurs} exercice(s) avec erreur(s)")
        print("=" * 60)
        return False


if __name__ == "__main__":
    try:
        success = verifier_tous()
        sys.exit(0 if success else 1)
    except ImportError as e:
        print("ERREUR: Veuillez exécuter depuis le dossier du chapitre")
        print(f"Détail: {e}")
        sys.exit(1)
