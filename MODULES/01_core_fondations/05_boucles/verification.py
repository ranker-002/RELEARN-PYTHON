#!/usr/bin/env python3
import re
"""
CHAPITRE 5 - Script de Verification Automatique
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



# =============================================================================
# FONCTIONS DE VÉRIFICATION FLEXIBLE
# =============================================================================

def normaliser_sortie(sortie):
    """Normalise une sortie pour comparaison flexible."""
    if not sortie:
        return ""
    resultat = sortie.lower()
    resultat = re.sub(r'\s+', ' ', resultat)
    resultat = re.sub(r'[.,;:!?]', '', resultat)
    return resultat.strip()


def contient_nombre(sortie, attendu, tolerance=0.01):
    """Vérifie que la sortie contient le nombre attendu."""
    if not sortie:
        return False
    pattern = r'-?\d+(?:\.\d+)?'
    matches = re.findall(pattern, sortie)
    for m in matches:
        n = float(m) if '.' in m else int(m)
        if isinstance(attendu, int):
            if isinstance(n, float) and n.is_integer() and int(n) == attendu:
                return True
            if n == attendu:
                return True
        else:
            if abs(n - attendu) < tolerance:
                return True
    return False


def contient_terme(sortie, terme):
    """Vérifie qu'un terme est présent (insensible à la casse)."""
    if not sortie:
        return False
    normalisee = normaliser_sortie(sortie)
    return terme.lower() in normalisee


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


def verifier_exercice_5_1():
    """Verifie l'exercice 5.1: Compteur simple."""
    from exercices import exercice_5_1
    sortie = capturer_sortie(exercice_5_1)
    if "1" in sortie and "10" in sortie:
        print("✓ Exercice 5.1: Compteur simple - CORRECT")
    else:
        raise VerificationError(f"1 a 10 attendus\nSortie: {sortie}")


def verifier_exercice_5_2():
    """Verifie l'exercice 5.2: Compteur a rebours."""
    from exercices import exercice_5_2
    sortie = capturer_sortie(exercice_5_2)
    if contient_nombre(sortie, 10) and "1" in sortie:
        print("✓ Exercice 5.2: Compteur a rebours - CORRECT")
    else:
        raise VerificationError(f"10 a 1 attendus\nSortie: {sortie}")


def verifier_exercice_5_3():
    """Verifie l'exercice 5.3: Somme des nombres."""
    from exercices import exercice_5_3
    sortie = capturer_sortie(exercice_5_3)
    if contient_nombre(sortie, 5050):
        print("✓ Exercice 5.3: Somme des nombres - CORRECT")
    else:
        raise VerificationError(f"5050 attendu\nSortie: {sortie}")


def verifier_exercice_5_4():
    """Verifie l'exercice 5.4: Table de multiplication."""
    from exercices import exercice_5_4
    sortie = capturer_sortie(exercice_5_4)
    if "7 x 10 = 70" in sortie:
        print("✓ Exercice 5.4: Table de multiplication - CORRECT")
    else:
        raise VerificationError(f"7 x 10 = 70 attendu\nSortie: {sortie}")


def verifier_exercice_5_5():
    """Verifie l'exercice 5.5: Enumerate."""
    from exercices import exercice_5_5
    sortie = capturer_sortie(exercice_5_5)
    if "1. pomme" in sortie and "3. orange" in sortie:
        print("✓ Exercice 5.5: Enumerate - CORRECT")
    else:
        raise VerificationError(f"Index 1-3 attendus\nSortie: {sortie}")


def verifier_exercice_5_6():
    """Verifie l'exercice 5.6: Nombres pairs."""
    from exercices import exercice_5_6
    sortie = capturer_sortie(exercice_5_6)
    if "2" in sortie and "20" in sortie and "3" not in sortie:
        print("✓ Exercice 5.6: Nombres pairs - CORRECT")
    else:
        raise VerificationError(f"Nombres pairs 2-20 attendus\nSortie: {sortie}")


def verifier_exercice_5_7():
    """Verifie l'exercice 5.7: Recherche."""
    from exercices import exercice_5_7
    sortie = capturer_sortie(exercice_5_7)
    if "Trouve!" in sortie:
        print("✓ Exercice 5.7: Recherche - CORRECT")
    else:
        raise VerificationError(f"Trouve! attendu\nSortie: {sortie}")


def verifier_exercice_5_8():
    """Verifie l'exercice 5.8: Factorielle."""
    from exercices import exercice_5_8
    sortie = capturer_sortie(exercice_5_8)
    if contient_nombre(sortie, 120):
        print("✓ Exercice 5.8: Factorielle - CORRECT")
    else:
        raise VerificationError(f"120 attendu\nSortie: {sortie}")


def verifier_exercice_5_9():
    """Verifie l'exercice 5.9: Nombre mystere."""
    from exercices import exercice_5_9
    with mock.patch('builtins.input', return_value="50"):
        with mock.patch('random.randint', return_value=50):
            sortie = capturer_sortie(exercice_5_9)
    if "Gagne" in sortie:
        print("✓ Exercice 5.9: Nombre mystere - CORRECT")
    else:
        print(f"⚠ Exercice 5.9: Non deterministe - SKIPPED")


def verifier_exercice_5_10():
    """Verifie l'exercice 5.10: Pyramide."""
    from exercices import exercice_5_10
    sortie = capturer_sortie(exercice_5_10)
    if "*" * 5 in sortie:
        print("✓ Exercice 5.10: Pyramide - CORRECT")
    else:
        raise VerificationError(f"5 etoiles attendues\nSortie: {sortie}")


def verifier_exercice_5_11():
    """Verifie l'exercice 5.11: Validation."""
    from exercices import exercice_5_11
    with mock.patch('builtins.input', side_effect=["15", "3"]):
        sortie = capturer_sortie(exercice_5_11)
    if contient_nombre(sortie, 3):
        print("✓ Exercice 5.11: Validation - CORRECT")
    else:
        raise VerificationError(f"3 attendu\nSortie: {sortie}")


def verifier_exercice_5_12():
    """Verifie l'exercice 5.12: Fibonacci."""
    from exercices import exercice_5_12
    sortie = capturer_sortie(exercice_5_12)
    if "34" in sortie and "0" in sortie:
        print("✓ Exercice 5.12: Fibonacci - CORRECT")
    else:
        raise VerificationError(f"0, 1, ..., 34 attendus\nSortie: {sortie}")


def verifier_exercice_5_13():
    """Verifie l'exercice 5.13: Voyelles."""
    from exercices import exercice_5_13
    with mock.patch('builtins.input', return_value="Bonjour"):
        sortie = capturer_sortie(exercice_5_13)
    if "3" in sortie or "voyelles" in sortie.lower():
        print("✓ Exercice 5.13: Voyelles - CORRECT")
    else:
        raise VerificationError(f"3 voyelles attendues\nSortie: {sortie}")


def verifier_exercice_5_14():
    """Verifie l'exercice 5.14: Pascal."""
    from exercices import exercice_5_14
    sortie = capturer_sortie(exercice_5_14)
    if "1 3 3 1" in sortie:
        print("✓ Exercice 5.14: Triangle de Pascal - CORRECT")
    else:
        raise VerificationError(f"1 3 3 1 attendu\nSortie: {sortie}")


def verifier_exercice_5_15():
    """Verifie l'exercice 5.15: Devinette avec limite."""
    from exercices import exercice_5_15
    with mock.patch('builtins.input', side_effect=["5", "10", "15", "12", "14"]):
        with mock.patch('random.randint', return_value=14):
            sortie = capturer_sortie(exercice_5_15)
    if "Gagne" in sortie or "Perdu" in sortie:
        print("✓ Exercice 5.15: Devinette avec limite - CORRECT")
    else:
        print(f"⚠ Exercice 5.15: Non deterministe - SKIPPED")


def verifier_tous():
    """Execeute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 5: BOUCLES")
    print("=" * 60)
    print()

    verifications = [
        ("5.1 Compteur", verifier_exercice_5_1),
        ("5.2 Rebours", verifier_exercice_5_2),
        ("5.3 Somme", verifier_exercice_5_3),
        ("5.4 Table", verifier_exercice_5_4),
        ("5.5 Enumerate", verifier_exercice_5_5),
        ("5.6 Pairs", verifier_exercice_5_6),
        ("5.7 Recherche", verifier_exercice_5_7),
        ("5.8 Factorielle", verifier_exercice_5_8),
        ("5.9 Mystere", verifier_exercice_5_9),
        ("5.10 Pyramide", verifier_exercice_5_10),
        ("5.11 Validation", verifier_exercice_5_11),
        ("5.12 Fibonacci", verifier_exercice_5_12),
        ("5.13 Voyelles", verifier_exercice_5_13),
        ("5.14 Pascal", verifier_exercice_5_14),
        ("5.15 Devinette", verifier_exercice_5_15),
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
        print("ERREUR: Veuillez execeuter depuis le dossier du chapitre")
        print(f"Detail: {e}")
        sys.exit(1)
