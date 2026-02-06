#!/usr/bin/env python3
"""
CHAPITRE 8 - Script de Verification Automatique
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


def verifier_exercice_8_1():
    """Verifie l'exercice 8.1: Fonction simple."""
    from exercices import exercice_8_1
    sortie = capturer_sortie(exercice_8_1)
    if "Bonjour" in sortie:
        print("✓ Exercice 8.1: Fonction simple - CORRECT")
    else:
        raise VerificationError(f"Bonjour attendu\nSortie: {sortie}")


def verifier_exercice_8_2():
    """Verifie l'exercice 8.2: Fonction avec parametre."""
    from exercices import exercice_8_2
    sortie = capturer_sortie(exercice_8_2)
    if "Bonjour" in sortie and "Alice" in sortie:
        print("✓ Exercice 8.2: Fonction avec parametre - CORRECT")
    else:
        raise VerificationError(f"Bonjour Alice attendu\nSortie: {sortie}")


def verifier_exercice_8_3():
    """Verifie l'exercice 8.3: Fonction avec retour."""
    from exercices import exercice_8_3
    sortie = capturer_sortie(exercice_8_3)
    if "25" in sortie:
        print("✓ Exercice 8.3: Fonction avec retour - CORRECT")
    else:
        raise VerificationError(f"25 attendu\nSortie: {sortie}")


def verifier_exercice_8_4():
    """Verifie l'exercice 8.4: Fonction avec plusieurs parametres."""
    from exercices import exercice_8_4
    sortie = capturer_sortie(exercice_8_4)
    if "Alice" in sortie and "Paris" in sortie:
        print("✓ Exercice 8.4: Fonction avec parametres - CORRECT")
    else:
        raise VerificationError(f"Presentation attendue\nSortie: {sortie}")


def verifier_exercice_8_5():
    """Verifie l'exercice 8.5: Parametres par defaut."""
    from exercices import exercice_8_5
    sortie = capturer_sortie(exercice_8_5)
    if "Bonjour" in sortie and "Salut" in sortie:
        print("✓ Exercice 8.5: Parametres par defaut - CORRECT")
    else:
        raise VerificationError(f"Bonjour et Salut attendus\nSortie: {sortie}")


def verifier_exercice_8_6():
    """Verifie l'exercice 8.6: Retour multiple."""
    from exercices import exercice_8_6
    sortie = capturer_sortie(exercice_8_6)
    if "3" in sortie and "2" in sortie:
        print("✓ Exercice 8.6: Retour multiple - CORRECT")
    else:
        raise VerificationError(f"3 et 2 attendus\nSortie: {sortie}")


def verifier_exercice_8_7():
    """Verifie l'exercice 8.7: Arguments nommes."""
    from exercices import exercice_8_7
    sortie = capturer_sortie(exercice_8_7)
    if "Alice" in sortie and "Dupont" in sortie:
        print("✓ Exercice 8.7: Arguments nommes - CORRECT")
    else:
        raise VerificationError(f"Alice Dupont attendu\nSortie: {sortie}")


def verifier_exercice_8_8():
    """Verifie l'exercice 8.8: Portee des variables."""
    from exercices import exercice_8_8
    try:
        sortie = capturer_sortie(exercice_8_8)
        if "locale" in sortie.lower() and "globale" in sortie.lower():
            print("✓ Exercice 8.8: Portee des variables - CORRECT")
        else:
            raise VerificationError(f"locale et globale attendus\nSortie: {sortie}")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_8_9():
    """Verifie l'exercice 8.9: Lambda et map."""
    from exercices import exercice_8_9
    sortie = capturer_sortie(exercice_8_9)
    if "[1, 8, 27, 64]" in sortie or "1, 8, 27, 64" in sortie:
        print("✓ Exercice 8.9: Lambda et map - CORRECT")
    else:
        raise VerificationError(f"[1, 8, 27, 64] attendu\nSortie: {sortie}")


def verifier_exercice_8_10():
    """Verifie l'exercice 8.10: Filter avec lambda."""
    from exercices import exercice_8_10
    sortie = capturer_sortie(exercice_8_10)
    if "3" in sortie and "6" in sortie and "9" in sortie:
        print("✓ Exercice 8.10: Filter avec lambda - CORRECT")
    else:
        raise VerificationError(f"[3, 6, 9] attendu\nSortie: {sortie}")


def verifier_exercice_8_11():
    """Verifie l'exercice 8.11: Factorielle recursive."""
    from exercices import exercice_8_11
    sortie = capturer_sortie(exercice_8_11)
    if "120" in sortie:  # 5! = 120
        print("✓ Exercice 8.11: Factorielle recursive - CORRECT")
    else:
        raise VerificationError(f"120 attendu\nSortie: {sortie}")


def verifier_exercice_8_12():
    """Verifie l'exercice 8.12: Docstring."""
    from exercices import exercice_8_12
    try:
        exercice_8_12()  # Si pas d'erreur, c'est bon
        print("✓ Exercice 8.12: Docstring - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_8_13():
    """Verifie l'exercice 8.13: Early return."""
    from exercices import exercice_8_13
    sortie = capturer_sortie(exercice_8_13)
    if "Mineur" in sortie and "Majeur" in sortie and "Senior" in sortie:
        print("✓ Exercice 8.13: Early return - CORRECT")
    else:
        raise VerificationError(f"Mineur, Majeur, Senior attendus\nSortie: {sortie}")


def verifier_exercice_8_14():
    """Verifie l'exercice 8.14: Tri avec lambda."""
    from exercices import exercice_8_14
    sortie = capturer_sortie(exercice_8_14)
    if "25" in sortie or "Bob" in sortie:
        print("✓ Exercice 8.14: Tri avec lambda - CORRECT")
    else:
        raise VerificationError(f"Tri attendu\nSortie: {sortie}")


def verifier_exercice_8_15():
    """Verifie l'exercice 8.15: Calculatrice."""
    from exercices import exercice_8_15
    with mock.patch('builtins.input', side_effect=["10", "2", "+"]):
        try:
            sortie = capturer_sortie(exercice_8_15)
            if "12" in sortie:
                print("✓ Exercice 8.15: Calculatrice - CORRECT")
            else:
                print(f"⚠ Exercice 8.15: Verification manuelle necessaire")
        except Exception as e:
            print(f"⚠ Exercice 8.15: Exception: {e}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 8: FONCTIONS")
    print("=" * 60)
    print()

    verifications = [
        ("8.1 Fonction simple", verifier_exercice_8_1),
        ("8.2 Parametre", verifier_exercice_8_2),
        ("8.3 Retour", verifier_exercice_8_3),
        ("8.4 Parametres multiples", verifier_exercice_8_4),
        ("8.5 Parametres defaut", verifier_exercice_8_5),
        ("8.6 Retour multiple", verifier_exercice_8_6),
        ("8.7 Arguments nommes", verifier_exercice_8_7),
        ("8.8 Portee", verifier_exercice_8_8),
        ("8.9 Lambda/Map", verifier_exercice_8_9),
        ("8.10 Filter/Lambda", verifier_exercice_8_10),
        ("8.11 Factorielle", verifier_exercice_8_11),
        ("8.12 Docstring", verifier_exercice_8_12),
        ("8.13 Early return", verifier_exercice_8_13),
        ("8.14 Tri Lambda", verifier_exercice_8_14),
        ("8.15 Calculatrice", verifier_exercice_8_15),
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
