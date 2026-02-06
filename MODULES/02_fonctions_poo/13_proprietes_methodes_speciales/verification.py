#!/usr/bin/env python3
"""
CHAPITRE 13 - Script de Verification Automatique
==============================================
Ce script verifie automatiquement vos solutions aux exercices.

Utilisation:
    python verification.py
"""

import sys
from io import StringIO


class VerificationError(Exception):
    """Erreur lors de la verification."""
    pass


def verifier_exercice_13_1():
    """Verifie l'exercice 13.1: Propriete simple."""
    from exercices import exercice_13_1
    try:
        exercice_13_1()
        print("✓ Exercice 13.1: Propriete simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_2():
    """Verifie l'exercice 13.2: Propriete calculee."""
    from exercices import exercice_13_2
    try:
        exercice_13_2()
        print("✓ Exercice 13.2: Propriete calculee - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_3():
    """Verifie l'exercice 13.3: __str__ et __repr__."""
    from exercices import exercice_13_3
    try:
        exercice_13_3()
        print("✓ Exercice 13.3: __str__ et __repr__ - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_4():
    """Verifie l'exercice 13.4: Comparaison simple."""
    from exercices import exercice_13_4
    try:
        exercice_13_4()
        print("✓ Exercice 13.4: Comparaison simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_5():
    """Verifie l'exercice 13.5: Iterateur simple."""
    from exercices import exercice_13_5
    try:
        exercice_13_5()
        print("✓ Exercice 13.5: Iterateur simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_6():
    """Verifie l'exercice 13.6: Contexte simple."""
    from exercices import exercice_13_6
    try:
        exercice_13_6()
        print("✓ Exercice 13.6: Contexte simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_7():
    """Verifie l'exercice 13.7: Operateurs arithmetiques."""
    from exercices import exercice_13_7
    try:
        exercice_13_7()
        print("✓ Exercice 13.7: Operateurs arithmetiques - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_8():
    """Verifie l'exercice 13.8: Conteneur personnalise."""
    from exercices import exercice_13_8
    try:
        exercice_13_8()
        print("✓ Exercice 13.8: Conteneur personnalise - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_9():
    """Verifie l'exercice 13.9: Iterateur filtre."""
    from exercices import exercice_13_9
    try:
        exercice_13_9()
        print("✓ Exercice 13.9: Iterateur filtre - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_10():
    """Verifie l'exercice 13.10: Propriete avec cache."""
    from exercices import exercice_13_10
    try:
        exercice_13_10()
        print("✓ Exercice 13.10: Propriete avec cache - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_11():
    """Verifie l'exercice 13.11: Hachage et set."""
    from exercices import exercice_13_11
    try:
        exercice_13_11()
        print("✓ Exercice 13.11: Hachage et set - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_12():
    """Verifie l'exercice 13.12: Generateur personnalise."""
    from exercices import exercice_13_12
    try:
        exercice_13_12()
        print("✓ Exercice 13.12: Generateur personnalise - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_13():
    """Verifie l'exercice 13.13: Methode d'appel."""
    from exercices import exercice_13_13
    try:
        exercice_13_13()
        print("✓ Exercice 13.13: Methode d'appel - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_14():
    """Verifie l'exercice 13.14: Classe sliceable."""
    from exercices import exercice_13_14
    try:
        exercice_13_14()
        print("✓ Exercice 13.14: Classe sliceable - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_13_15():
    """Verifie l'exercice 13.15: Systeme complet."""
    from exercices import exercice_13_15
    try:
        exercice_13_15()
        print("✓ Exercice 13.15: Systeme complet - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 13: PROPRIETES ET METHODES SPECIALES")
    print("=" * 60)
    print()

    verifications = [
        ("13.1 Propriete simple", verifier_exercice_13_1),
        ("13.2 Propriete calculee", verifier_exercice_13_2),
        ("13.3 __str__/__repr__", verifier_exercice_13_3),
        ("13.4 Comparaison", verifier_exercice_13_4),
        ("13.5 Iterateur simple", verifier_exercice_13_5),
        ("13.6 Contexte simple", verifier_exercice_13_6),
        ("13.7 Operateurs", verifier_exercice_13_7),
        ("13.8 Conteneur limite", verifier_exercice_13_8),
        ("13.9 Iterateur filtre", verifier_exercice_13_9),
        ("13.10 Cache", verifier_exercice_13_10),
        ("13.11 Hachage", verifier_exercice_13_11),
        ("13.12 Fibonacci", verifier_exercice_13_12),
        ("13.13 Callable", verifier_exercice_13_13),
        ("13.14 Matrice", verifier_exercice_13_14),
        ("13.15 Systeme complet", verifier_exercice_13_15),
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
