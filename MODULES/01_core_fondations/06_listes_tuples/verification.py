#!/usr/bin/env python3
import re
"""
CHAPITRE 6 - Script de Verification Automatique
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


def verifier_exercice_6_1():
    """Verifie l'exercice 6.1: Creation de liste."""
    from exercices import exercice_6_1
    sortie = capturer_sortie(exercice_6_1)
    if "[1, 2, 3, 4, 5]" in sortie and "list" in sortie:
        print("✓ Exercice 6.1: Creation de liste - CORRECT")
    else:
        raise VerificationError(f"Liste [1-5] et type attendus\nSortie: {sortie}")


def verifier_exercice_6_2():
    """Verifie l'exercice 6.2: Acces aux elements."""
    from exercices import exercice_6_2
    sortie = capturer_sortie(exercice_6_2)
    if "pomme" in sortie and "raisin" in sortie and "orange" in sortie:
        print("✓ Exercice 6.2: Acces aux elements - CORRECT")
    else:
        raise VerificationError(f"pomme, orange, raisin attendus\nSortie: {sortie}")


def verifier_exercice_6_3():
    """Verifie l'exercice 6.3: Slicing."""
    from exercices import exercice_6_3
    sortie = capturer_sortie(exercice_6_3)
    if "[0, 1, 2]" in sortie and "[9, 8, 7" in sortie:
        print("✓ Exercice 6.3: Slicing - CORRECT")
    else:
        raise VerificationError(f"Slicing attendu\nSortie: {sortie}")


def verifier_exercice_6_4():
    """Verifie l'exercice 6.4: Modification."""
    from exercices import exercice_6_4
    sortie = capturer_sortie(exercice_6_4)
    if "[0, 1, 10, 4, 5, 6]" in sortie or "[0, 1, 10, 4, 5]" in sortie:
        print("✓ Exercice 6.4: Modification - CORRECT")
    else:
        raise VerificationError(f"Liste modifiee attendue\nSortie: {sortie}")


def verifier_exercice_6_5():
    """Verifie l'exercice 6.5: Tuple."""
    from exercices import exercice_6_5
    sortie = capturer_sortie(exercice_6_5)
    if contient_nombre(sortie, 25) and "decembre" in sortie and "2024" in sortie:
        print("✓ Exercice 6.5: Tuple - CORRECT")
    else:
        raise VerificationError(f"Date attendue\nSortie: {sortie}")


def verifier_exercice_6_6():
    """Verifie l'exercice 6.6: Unpacking."""
    from exercices import exercice_6_6
    sortie = capturer_sortie(exercice_6_6)
    if "Alice" in sortie and "50000" in sortie:
        print("✓ Exercice 6.6: Unpacking - CORRECT")
    else:
        raise VerificationError(f"Unpacking attendu\nSortie: {sortie}")


def verifier_exercice_6_7():
    """Verifie l'exercice 6.7: Tri."""
    from exercices import exercice_6_7
    sortie = capturer_sortie(exercice_6_7)
    if "[12, 25, 37, 45, 64, 89]" in sortie:
        print("✓ Exercice 6.7: Tri - CORRECT")
    else:
        raise VerificationError(f"Liste triee attendue\nSortie: {sortie}")


def verifier_exercice_6_8():
    """Verifie l'exercice 6.8: Compteur."""
    from exercices import exercice_6_8
    sortie = capturer_sortie(exercice_6_8)
    if "pomme" in sortie and "3" in sortie:
        print("✓ Exercice 6.8: Compteur - CORRECT")
    else:
        raise VerificationError(f"Compteur attendu\nSortie: {sortie}")


def verifier_exercice_6_9():
    """Verifie l'exercice 6.9: Comprehension."""
    from exercices import exercice_6_9
    sortie = capturer_sortie(exercice_6_9)
    if "[0, 1, 4, 9," in sortie and "[0, 2, 4," in sortie:
        print("✓ Exercice 6.9: Comprehension - CORRECT")
    else:
        raise VerificationError(f"Comprehensions attendues\nSortie: {sortie}")


def verifier_exercice_6_10():
    """Verifie l'exercice 6.10: Matrice."""
    from exercices import exercice_6_10
    sortie = capturer_sortie(exercice_6_10)
    if "1, 0, 0" in sortie and "0, 1, 0" in sortie:
        print("✓ Exercice 6.10: Matrice - CORRECT")
    else:
        raise VerificationError(f"Matrice identite attendue\nSortie: {sortie}")


def verifier_exercice_6_11():
    """Verifie l'exercice 6.11: Echange."""
    from exercices import exercice_6_11
    sortie = capturer_sortie(exercice_6_11)
    if "x=10" in sortie and "y=5" in sortie:
        print("✓ Exercice 6.11: Echange - CORRECT")
    else:
        raise VerificationError(f"x=10, y=5 attendus\nSortie: {sortie}")


def verifier_exercice_6_12():
    """Verifie l'exercice 6.12: Liste de listes."""
    from exercices import exercice_6_12
    sortie = capturer_sortie(exercice_6_12)
    if "Charlie" in sortie and "13" in sortie:
        print("✓ Exercice 6.12: Liste de listes - CORRECT")
    else:
        raise VerificationError(f"Charlie et 13 attendus\nSortie: {sortie}")


def verifier_exercice_6_13():
    """Verifie l'exercice 6.13: Aplatissement."""
    from exercices import exercice_6_13
    sortie = capturer_sortie(exercice_6_13)
    if "[1, 2, 3, 4, 5, 6, 7, 8, 9]" in sortie:
        print("✓ Exercice 6.13: Aplatissement - CORRECT")
    else:
        raise VerificationError(f"Liste aplanie attendue\nSortie: {sortie}")


def verifier_exercice_6_14():
    """Verifie l'exercice 6.14: Premiers."""
    from exercices import exercice_6_14
    sortie = capturer_sortie(exercice_6_14)
    if "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]" in sortie:
        print("✓ Exercice 6.14: Nombres premiers - CORRECT")
    else:
        raise VerificationError(f"Premiers attendus\nSortie: {sortie}")


def verifier_exercice_6_15():
    """Verifie l'exercice 6.15: Inventaire."""
    from exercices import exercice_6_15
    sortie = capturer_sortie(exercice_6_15)
    if "pomme" in sortie and "120" in sortie:
        print("✓ Exercice 6.15: Inventaire - CORRECT")
    else:
        raise VerificationError(f"Inventaire attendu\nSortie: {sortie}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 6: LISTES ET TUPLES")
    print("=" * 60)
    print()

    verifications = [
        ("6.1 Creation", verifier_exercice_6_1),
        ("6.2 Acces", verifier_exercice_6_2),
        ("6.3 Slicing", verifier_exercice_6_3),
        ("6.4 Modification", verifier_exercice_6_4),
        ("6.5 Tuple", verifier_exercice_6_5),
        ("6.6 Unpacking", verifier_exercice_6_6),
        ("6.7 Tri", verifier_exercice_6_7),
        ("6.8 Compteur", verifier_exercice_6_8),
        ("6.9 Comprehension", verifier_exercice_6_9),
        ("6.10 Matrice", verifier_exercice_6_10),
        ("6.11 Echange", verifier_exercice_6_11),
        ("6.12 Liste de listes", verifier_exercice_6_12),
        ("6.13 Aplatissement", verifier_exercice_6_13),
        ("6.14 Premiers", verifier_exercice_6_14),
        ("6.15 Inventaire", verifier_exercice_6_15),
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
