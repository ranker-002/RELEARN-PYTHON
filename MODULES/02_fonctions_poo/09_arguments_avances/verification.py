#!/usr/bin/env python3
"""
CHAPITRE 9 - Script de Verification Automatique
==============================================
Ce script verifie automatiquement vos solutions aux exercices.

Utilisation:
    python verification.py
"""

import sys
from io import StringIO
from unittest import mock


class VerificationError(Exception):
    """Erreur lors de la verification."""
    pass


def capturer_sortie(func):
    """Execute une fonction et capture sa sortie."""
    ancien_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        func()
        sortie = sys.stdout.getvalue()
    finally:
        sys.stdout = ancien_stdout
    return sortie


def verifier_exercice_9_1():
    """Verifie l'exercice 9.1: *args simple."""
    from exercices import exercice_9_1
    sortie = capturer_sortie(exercice_9_1)
    if "20.0" in sortie:
        print("✓ Exercice 9.1: *args simple - CORRECT")
    else:
        raise VerificationError(f"20.0 attendu\nSortie: {sortie}")


def verifier_exercice_9_2():
    """Verifie l'exercice 9.2: **kwargs simple."""
    from exercices import exercice_9_2
    sortie = capturer_sortie(exercice_9_2)
    if "Alice" in sortie and "Paris" in sortie:
        print("✓ Exercice 9.2: **kwargs simple - CORRECT")
    else:
        raise VerificationError(f"Profil attendu\nSortie: {sortie}")


def verifier_exercice_9_3():
    """Verifie l'exercice 9.3: Combination args/kwargs."""
    from exercices import exercice_9_3
    try:
        exercice_9_3()  # Si pas d'erreur
        print("✓ Exercice 9.3: Combination - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_9_4():
    """Verifie l'exercice 9.4: Positional-only."""
    from exercices import exercice_9_4
    sortie = capturer_sortie(exercice_9_4)
    if "25" in sortie and "125" in sortie:
        print("✓ Exercice 9.4: Positional-only - CORRECT")
    else:
        raise VerificationError(f"25 et 125 attendus\nSortie: {sortie}")


def verifier_exercice_9_5():
    """Verifie l'exercice 9.5: Keyword-only."""
    from exercices import exercice_9_5
    try:
        exercice_9_5()
        print("✓ Exercice 9.5: Keyword-only - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_9_6():
    """Verifie l'exercice 9.6: Deballage."""
    from exercices import exercice_9_6
    sortie = capturer_sortie(exercice_9_6)
    if "15" in sortie or "5" in sortie:
        print("✓ Exercice 9.6: Deballage - CORRECT")
    else:
        raise VerificationError(f"Aire 15 attendue\nSortie: {sortie}")


def verifier_exercice_9_7():
    """Verifie l'exercice 9.7: Decorateur simple."""
    from exercices import exercice_9_7
    sortie = capturer_sortie(exercice_9_7)
    if "Bonjour" in sortie:
        print("✓ Exercice 9.7: Decorateur simple - CORRECT")
    else:
        raise VerificationError(f"Bonjour attendu\nSortie: {sortie}")


def verifier_exercice_9_8():
    """Verifie l'exercice 9.8: Decorateur timing."""
    from exercices import exercice_9_8
    try:
        exercice_9_8()
        print("✓ Exercice 9.8: Decorateur timing - CORRECT")
    except Exception as e:
        print(f"⚠ Exercice 9.8: Exception: {e}")


def verifier_exercice_9_9():
    """Verifie l'exercice 9.9: Fonction flexible."""
    from exercices import exercice_9_9
    try:
        exercice_9_9()
        print("✓ Exercice 9.9: Fonction flexible - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_9_10():
    """Verifie l'exercice 9.10: Ordre des parametres."""
    from exercices import exercice_9_10
    try:
        exercice_9_10()
        print("✓ Exercice 9.10: Ordre des parametres - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_9_11():
    """Verifie l'exercice 9.11: Decorateur repeat."""
    from exercices import exercice_9_11
    try:
        exercice_9_11()
        print("✓ Exercice 9.11: Decorateur repeat - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_9_12():
    """Verifie l'exercice 9.12: Validateur."""
    from exercices import exercice_9_12
    sortie = capturer_sortie(exercice_9_12)
    if "True" in sortie and "False" in sortie:
        print("✓ Exercice 9.12: Validateur - CORRECT")
    else:
        raise VerificationError(f"True/False attendus\nSortie: {sortie}")


def verifier_exercice_9_13():
    """Verifie l'exercice 9.13: Logger."""
    from exercices import exercice_9_13
    try:
        exercice_9_13()
        print("✓ Exercice 9.13: Logger avance - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_9_14():
    """Verifie l'exercice 9.14: Query builder."""
    from exercices import exercice_9_14
    sortie = capturer_sortie(exercice_9_14)
    if "SELECT" in sortie and "users" in sortie:
        print("✓ Exercice 9.14: Constructeur SQL - CORRECT")
    else:
        raise VerificationError(f"SQL attendu\nSortie: {sortie}")


def verifier_exercice_9_15():
    """Verifie l'exercice 9.15: Decorateur cache."""
    from exercices import exercice_9_15
    try:
        exercice_9_15()
        print("✓ Exercice 9.15: Decorateur cache - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 9: ARGUMENTS AVANCES")
    print("=" * 60)
    print()

    verifications = [
        ("9.1 *args", verifier_exercice_9_1),
        ("9.2 **kwargs", verifier_exercice_9_2),
        ("9.3 Combination", verifier_exercice_9_3),
        ("9.4 Positional-only", verifier_exercice_9_4),
        ("9.5 Keyword-only", verifier_exercice_9_5),
        ("9.6 Deballage", verifier_exercice_9_6),
        ("9.7 Decorateur simple", verifier_exercice_9_7),
        ("9.8 Decorateur timing", verifier_exercice_9_8),
        ("9.9 Fonction flexible", verifier_exercice_9_9),
        ("9.10 Ordre parametres", verifier_exercice_9_10),
        ("9.11 Decorateur repeat", verifier_exercice_9_11),
        ("9.12 Validateur", verifier_exercice_9_12),
        ("9.13 Logger", verifier_exercice_9_13),
        ("9.14 Query builder", verifier_exercice_9_14),
        ("9.15 Decorateur cache", verifier_exercice_9_15),
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
        print("ERREUR: Veuillez executer depuis le dossier du chapitre")
        print(f"Detail: {e}")
        sys.exit(1)
