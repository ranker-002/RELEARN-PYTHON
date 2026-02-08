#!/usr/bin/env python3
"""
CHAPITRE 10 - Script de Verification Automatique
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


def verifier_exercice_10_1():
    """Verifie l'exercice 10.1: Creation de module."""
    from exercices import exercice_10_1
    try:
        exercice_10_1()
        print("✓ Exercice 10.1: Creation de module - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_2():
    """Verifie l'exercice 10.2: Import simple."""
    from exercices import exercice_10_2
    try:
        exercice_10_2()
        print("✓ Exercice 10.2: Import simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_3():
    """Verifie l'exercice 10.3: From import."""
    from exercices import exercice_10_3
    try:
        exercice_10_3()
        print("✓ Exercice 10.3: From import - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_4():
    """Verifie l'exercice 10.4: Alias."""
    from exercices import exercice_10_4
    try:
        exercice_10_4()
        print("✓ Exercice 10.4: Alias - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_5():
    """Verifie l'exercice 10.5: __name__."""
    from exercices import exercice_10_5
    try:
        exercice_10_5()
        print("✓ Exercice 10.5: __name__ main - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_6():
    """Verifie l'exercice 10.6: Module os."""
    from exercices import exercice_10_6
    try:
        exercice_10_6()
        print("✓ Exercice 10.6: Module os - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_7():
    """Verifie l'exercice 10.7: Module json."""
    from exercices import exercice_10_7
    try:
        exercice_10_7()
        print("✓ Exercice 10.7: Module json - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_8():
    """Verifie l'exercice 10.8: Module collections."""
    from exercices import exercice_10_8
    try:
        exercice_10_8()
        print("✓ Exercice 10.8: Module collections - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_9():
    """Verifie l'exercice 10.9: Structure de package."""
    from exercices import exercice_10_9
    try:
        exercice_10_9()
        print("✓ Exercice 10.9: Structure de package - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_10():
    """Verifie l'exercice 10.10: Requirements.txt."""
    from exercices import exercice_10_10
    try:
        exercice_10_10()
        print("✓ Exercice 10.10: Requirements.txt - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_11():
    """Verifie l'exercice 10.11: Import relatif."""
    from exercices import exercice_10_11
    try:
        exercice_10_11()
        print("✓ Exercice 10.11: Import relatif - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_12():
    """Verifie l'exercice 10.12: Module complet."""
    from exercices import exercice_10_12
    try:
        exercice_10_12()
        print("✓ Exercice 10.12: Module complet - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_13():
    """Verifie l'exercice 10.13: Package multi-modules."""
    from exercices import exercice_10_13
    try:
        exercice_10_13()
        print("✓ Exercice 10.13: Package multi-modules - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_14():
    """Verifie l'exercice 10.14: Script principal."""
    from exercices import exercice_10_14
    try:
        exercice_10_14()
        print("✓ Exercice 10.14: Script principal - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_10_15():
    """Verifie l'exercice 10.15: Projet complet."""
    from exercices import exercice_10_15
    try:
        exercice_10_15()
        print("✓ Exercice 10.15: Projet complet - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 10: MODULES ET PACKAGES")
    print("=" * 60)
    print()

    verifications = [
        ("10.1 Creation module", verifier_exercice_10_1),
        ("10.2 Import simple", verifier_exercice_10_2),
        ("10.3 From import", verifier_exercice_10_3),
        ("10.4 Alias", verifier_exercice_10_4),
        ("10.5 __name__", verifier_exercice_10_5),
        ("10.6 Module os", verifier_exercice_10_6),
        ("10.7 Module json", verifier_exercice_10_7),
        ("10.8 Module collections", verifier_exercice_10_8),
        ("10.9 Structure package", verifier_exercice_10_9),
        ("10.10 Requirements.txt", verifier_exercice_10_10),
        ("10.11 Import relatif", verifier_exercice_10_11),
        ("10.12 Module complet", verifier_exercice_10_12),
        ("10.13 Package multi-modules", verifier_exercice_10_13),
        ("10.14 Script principal", verifier_exercice_10_14),
        ("10.15 Projet complet", verifier_exercice_10_15),
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
