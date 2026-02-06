#!/usr/bin/env python3
"""
CHAPITRE 18 - Vérification Automatique
"""

import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class VerificationError(Exception):
    pass


def verifier_exercice_18_1():
    from exercices import exercice_18_1
    try:
        exercice_18_1()
        print("✓ 18.1: Thread simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_2():
    from exercices import exercice_18_2
    try:
        exercice_18_2()
        print("✓ 18.2: Plusieurs threads - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_3():
    from exercices import exercice_18_3
    try:
        exercice_18_3()
        print("✓ 18.3: Compteur sécurisé - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_4():
    from exercices import exercice_18_4
    try:
        exercice_18_4()
        print("✓ 18.4: ThreadPoolExecutor - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_5():
    from exercices import exercice_18_5
    try:
        exercice_18_5()
        print("✓ 18.5: Race condition - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_6():
    from exercices import exercice_18_6
    try:
        exercice_18_6()
        print("✓ 18.6: Queue Producteur-Consommateur - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_7():
    from exercices import exercice_18_7
    try:
        exercice_18_7()
        print("✓ 18.7: ThreadLocal - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_8():
    from exercices import exercice_18_8
    try:
        exercice_18_8()
        print("✓ 18.8: Barrier - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_9():
    from exercices import exercice_18_9
    try:
        exercice_18_9()
        print("✓ 18.9: Event threads - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_10():
    from exercices import exercice_18_10
    try:
        exercice_18_10()
        print("✓ 18.10: Timer thread - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_11():
    from exercices import exercice_18_11
    try:
        exercice_18_11()
        print("✓ 18.11: Semaphore - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_12():
    from exercices import exercice_18_12
    try:
        exercice_18_12()
        print("✓ 18.12: Callable Future - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_13():
    from exercices import exercice_18_13
    try:
        exercice_18_13()
        print("✓ 18.13: as_completed - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_14():
    from exercices import exercice_18_14
    try:
        exercice_18_14()
        print("✓ 18.14: ThreadPool avec callback - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_18_15():
    from exercices import exercice_18_15
    try:
        exercice_18_15()
        print("✓ 18.15: Threading dans classe - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 18: PROGRAMMATION CONCURRENTE")
    print("=" * 60)
    
    verifications = [
        ("18.1", verifier_exercice_18_1),
        ("18.2", verifier_exercice_18_2),
        ("18.3", verifier_exercice_18_3),
        ("18.4", verifier_exercice_18_4),
        ("18.5", verifier_exercice_18_5),
        ("18.6", verifier_exercice_18_6),
        ("18.7", verifier_exercice_18_7),
        ("18.8", verifier_exercice_18_8),
        ("18.9", verifier_exercice_18_9),
        ("18.10", verifier_exercice_18_10),
        ("18.11", verifier_exercice_18_11),
        ("18.12", verifier_exercice_18_12),
        ("18.13", verifier_exercice_18_13),
        ("18.14", verifier_exercice_18_14),
        ("18.15", verifier_exercice_18_15),
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
    else:
        print(f"{erreurs} erreur(s) trouvée(s)")


if __name__ == "__main__":
    try:
        verifier_tous()
    except ImportError as e:
        print(f"Erreur d'import: {e}")
        sys.exit(1)
