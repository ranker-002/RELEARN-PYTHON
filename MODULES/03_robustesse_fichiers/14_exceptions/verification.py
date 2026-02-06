#!/usr/bin/env python3
"""
CHAPITRE 14 - Script de Verification Automatique
==============================================
"""

import sys
from io import StringIO


class VerificationError(Exception):
    pass


def verifier_exercice_14_1():
    from exercices import exercice_14_1
    try:
        exercice_14_1()
        print("✓ Exercice 14.1: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_2():
    from exercices import exercice_14_2
    try:
        exercice_14_2()
        print("✓ Exercice 14.2: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_3():
    from exercices import exercice_14_3
    try:
        exercice_14_3()
        print("✓ Exercice 14.3: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_4():
    from exercices import exercice_14_4
    try:
        exercice_14_4()
        print("✓ Exercice 14.4: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_5():
    from exercices import exercice_14_5
    try:
        exercice_14_5()
        print("✓ Exercice 14.5: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_6():
    from exercices import exercice_14_6
    try:
        exercice_14_6()
        print("✓ Exercice 14.6: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_7():
    from exercices import exercice_14_7
    try:
        exercice_14_7()
        print("✓ Exercice 14.7: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_8():
    from exercices import exercice_14_8
    try:
        exercice_14_8()
        print("✓ Exercice 14.8: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_9():
    from exercices import exercice_14_9
    try:
        exercice_14_9()
        print("✓ Exercice 14.9: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_10():
    from exercices import exercice_14_10
    try:
        exercice_14_10()
        print("✓ Exercice 14.10: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_11():
    from exercices import exercice_14_11
    try:
        exercice_14_11()
        print("✓ Exercice 14.11: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_12():
    from exercices import exercice_14_12
    try:
        exercice_14_12()
        print("✓ Exercice 14.12: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_13():
    from exercices import exercice_14_13
    try:
        exercice_14_13()
        print("✓ Exercice 14.13: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_14():
    from exercices import exercice_14_14
    try:
        exercice_14_14()
        print("✓ Exercice 14.14: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_14_15():
    from exercices import exercice_14_15
    try:
        exercice_14_15()
        print("✓ Exercice 14.15: CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 14: EXCEPTIONS")
    print("=" * 60)
    
    verifications = [
        ("14.1 try/except", verifier_exercice_14_1),
        ("14.2 Plusieurs", verifier_exercice_14_2),
        ("14.3 else/finally", verifier_exercice_14_3),
        ("14.4 Personnalisee", verifier_exercice_14_4),
        ("14.5 Validation", verifier_exercice_14_5),
        ("14.6 Hierarchie", verifier_exercice_14_6),
        ("14.7 Propagation", verifier_exercice_14_7),
        ("14.8 Relancer", verifier_exercice_14_8),
        ("14.9 Timer", verifier_exercice_14_9),
        ("14.10 Retry", verifier_exercice_14_10),
        ("14.11 Validateur", verifier_exercice_14_11),
        ("14.12 Fichiers", verifier_exercice_14_12),
        ("14.13 Chainee", verifier_exercice_14_13),
        ("14.14 Pagination", verifier_exercice_14_14),
        ("14.15 Logging", verifier_exercice_14_15),
    ]
    
    erreurs = 0
    for nom, verif in verifications:
        try:
            verif()
        except Exception as e:
            print(f"✗ {nom}: {e}")
            erreurs += 1
    
    print()
    if erreurs == 0:
        print("TOUS LES EXERCICES SONT CORRECTS!")
        return True
    else:
        print(f"{erreurs} erreur(s)")
        return False


if __name__ == "__main__":
    success = verifier_tous()
    sys.exit(0 if success else 1)
