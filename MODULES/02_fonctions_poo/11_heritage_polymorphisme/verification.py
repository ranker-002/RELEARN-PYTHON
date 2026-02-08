#!/usr/bin/env python3
import re
"""
CHAPITRE 12 - Script de Verification Automatique
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


def verifier_exercice_12_1():
    """Verifie l'exercice 12.1: Heritage simple."""
    from exercices import exercice_12_1
    try:
        exercice_12_1()
        print("✓ Exercice 12.1: Heritage simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_2():
    """Verifie l'exercice 12.2: Super() et constructeur."""
    from exercices import exercice_12_2
    try:
        exercice_12_2()
        print("✓ Exercice 12.2: Super() et constructeur - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_3():
    """Verifie l'exercice 12.3: Methode de substitution."""
    from exercices import exercice_12_3
    try:
        exercice_12_3()
        print("✓ Exercice 12.3: Methode de substitution - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_4():
    """Verifie l'exercice 12.4: Appeler le parent."""
    from exercices import exercice_12_4
    try:
        exercice_12_4()
        print("✓ Exercice 12.4: Appeler le parent - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_5():
    """Verifie l'exercice 12.5: Polymorphisme simple."""
    from exercices import exercice_12_5
    try:
        exercice_12_5()
        print("✓ Exercice 12.5: Polymorphisme simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_6():
    """Verifie l'exercice 12.6: Hierarchie de formes."""
    from exercices import exercice_12_6
    try:
        exercice_12_6()
        print("✓ Exercice 12.6: Hierarchie de formes - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_7():
    """Verifie l'exercice 12.7: Heritage multiple."""
    from exercices import exercice_12_7
    try:
        exercice_12_7()
        print("✓ Exercice 12.7: Heritage multiple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_8():
    """Verifie l'exercice 12.8: MRO et heritage."""
    from exercices import exercice_12_8
    try:
        exercice_12_8()
        print("✓ Exercice 12.8: MRO et heritage - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_9():
    """Verifie l'exercice 12.9: Classe abstraite."""
    from exercices import exercice_12_9
    try:
        exercice_12_9()
        print("✓ Exercice 12.9: Classe abstraite - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_10():
    """Verifie l'exercice 12.10: Systeme de paiement."""
    from exercices import exercice_12_10
    try:
        exercice_12_10()
        print("✓ Exercice 12.10: Systeme de paiement - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_11():
    """Verifie l'exercice 12.11: Hierarchie d'employes."""
    from exercices import exercice_12_11
    try:
        exercice_12_11()
        print("✓ Exercice 12.11: Hierarchie d'employes - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_12():
    """Verifie l'exercice 12.12: Duck typing."""
    from exercices import exercice_12_12
    try:
        exercice_12_12()
        print("✓ Exercice 12.12: Duck typing - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_13():
    """Verifie l'exercice 12.13: __str__ et __repr__."""
    from exercices import exercice_12_13
    try:
        exercice_12_13()
        print("✓ Exercice 12.13: __str__ et __repr__ - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_14():
    """Verifie l'exercice 12.14: Comparaison et heritage."""
    from exercices import exercice_12_14
    try:
        exercice_12_14()
        print("✓ Exercice 12.14: Comparaison et heritage - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_12_15():
    """Verifie l'exercice 12.15: Systeme de notifications."""
    from exercices import exercice_12_15
    try:
        exercice_12_15()
        print("✓ Exercice 12.15: Systeme de notifications - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 12: HERITAGE ET POLYMORPHISME")
    print("=" * 60)
    print()

    verifications = [
        ("12.1 Heritage simple", verifier_exercice_12_1),
        ("12.2 Super()", verifier_exercice_12_2),
        ("12.3 Substitution", verifier_exercice_12_3),
        ("12.4 Appel parent", verifier_exercice_12_4),
        ("12.5 Polymorphisme", verifier_exercice_12_5),
        ("12.6 Formes", verifier_exercice_12_6),
        ("12.7 Heritage multiple", verifier_exercice_12_7),
        ("12.8 MRO", verifier_exercice_12_8),
        ("12.9 Classe abstraite", verifier_exercice_12_9),
        ("12.10 Systeme paiement", verifier_exercice_12_10),
        ("12.11 Hierarchie employes", verifier_exercice_12_11),
        ("12.12 Duck typing", verifier_exercice_12_12),
        ("12.13 __str__/__repr__", verifier_exercice_12_13),
        ("12.14 Comparaison", verifier_exercice_12_14),
        ("12.15 Notifications", verifier_exercice_12_15),
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
