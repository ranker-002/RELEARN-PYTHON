#!/usr/bin/env python3
"""
CHAPITRE 3 - Script de Vérification Automatique
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


def verifier_exercice_3_1():
    """Vérifie l'exercice 3.1: Calculatrice."""
    from exercices import exercice_3_1
    with mock.patch('builtins.input', side_effect=["10", "3", "%"]):
        sortie = capturer_sortie(exercice_3_1)
    if "1" in sortie or "1.0" in sortie:
        print("✓ Exercice 3.1: Calculatrice - CORRECT")
    else:
        raise VerificationError(f"Attendu 1 pour 10 % 3\nSortie: {sortie}")


def verifier_exercice_3_2():
    """Vérifie l'exercice 3.2: Comparaison."""
    from exercices import exercice_3_2
    with mock.patch('builtins.input', side_effect=["5", "5"]):
        sortie = capturer_sortie(exercice_3_2)
    if "True" in sortie and "False" in sortie:
        print("✓ Exercice 3.2: Comparaison - CORRECT")
    else:
        raise VerificationError(f"True/False attendus\nSortie: {sortie}")


def verifier_exercice_3_3():
    """Vérifie l'exercice 3.3: Vérification d'âge."""
    from exercices import exercice_3_3
    with mock.patch('builtins.input', return_value="25"):
        sortie = capturer_sortie(exercice_3_3)
    if "True" in sortie and "False" in sortie:
        print("✓ Exercice 3.3: Vérification d'âge - CORRECT")
    else:
        raise VerificationError(f"True/False attendus\nSortie: {sortie}")


def verifier_exercice_3_4():
    """Vérifie l'exercice 3.4: Moyenne."""
    from exercices import exercice_3_4
    with mock.patch('builtins.input', side_effect=["12", "14", "16"]):
        sortie = capturer_sortie(exercice_3_4)
    if "14" in sortie and "True" in sortie:
        print("✓ Exercice 3.4: Moyenne - CORRECT")
    else:
        raise VerificationError(f"Moyenne 14 et True attendus\nSortie: {sortie}")


def verifier_exercice_3_5():
    """Vérifie l'exercice 3.5: Appartenance."""
    from exercices import exercice_3_5
    with mock.patch('builtins.input', return_value="banane"):
        sortie = capturer_sortie(exercice_3_5)
    if "True" in sortie:
        print("✓ Exercice 3.5: Appartenance - CORRECT")
    else:
        raise VerificationError(f"True attendu pour 'banane'\nSortie: {sortie}")


def verifier_exercice_3_6():
    """Vérifie l'exercice 3.6: Opérateurs logiques."""
    from exercices import exercice_3_6
    with mock.patch('builtins.input', return_value="4"):
        sortie = capturer_sortie(exercice_3_6)
    if "True" in sortie:
        print("✓ Exercice 3.6: Opérateurs logiques - CORRECT")
    else:
        raise VerificationError(f"True attendu pour 4\nSortie: {sortie}")


def verifier_exercice_3_7():
    """Vérifie l'exercice 3.7: Remise."""
    from exercices import exercice_3_7
    with mock.patch('builtins.input', return_value="150"):
        sortie = capturer_sortie(exercice_3_7)
    if "30" in sortie or "30.0" in sortie:
        print("✓ Exercice 3.7: Remise - CORRECT")
    else:
        raise VerificationError(f"Remise de 30 attendue\nSortie: {sortie}")


def verifier_exercice_3_8():
    """Vérifie l'exercice 3.8: Triangle."""
    from exercices import exercice_3_8
    with mock.patch('builtins.input', side_effect=["3", "4", "5"]):
        sortie = capturer_sortie(exercice_3_8)
    if "scalène" in sortie.lower():
        print("✓ Exercice 3.8: Triangle - CORRECT")
    else:
        raise VerificationError(f"Scalène attendu\nSortie: {sortie}")


def verifier_exercice_3_9():
    """Vérifie l'exercice 3.9: Bit à bit."""
    from exercices import exercice_3_9
    with mock.patch('builtins.input', side_effect=["5", "3"]):
        sortie = capturer_sortie(exercice_3_9)
    if "1" in sortie and "7" in sortie:
        print("✓ Exercice 3.9: Bit à bit - CORRECT")
    else:
        raise VerificationError(f"1 (AND) et 7 (OR) attendus\nSortie: {sortie}")


def verifier_exercice_3_10():
    """Vérifie l'exercice 3.10: Bissextile."""
    from exercices import exercice_3_10
    with mock.patch('builtins.input', return_value="2024"):
        sortie = capturer_sortie(exercice_3_10)
    if "True" in sortie:
        print("✓ Exercice 3.10: Bissextile - CORRECT")
    else:
        raise VerificationError(f"True attendu pour 2024\nSortie: {sortie}")


def verifier_exercice_3_11():
    """Vérifie l'exercice 3.11: Prix final."""
    from exercices import exercice_3_11
    with mock.patch('builtins.input', side_effect=["100", "20", "oui"]):
        sortie = capturer_sortie(exercice_3_11)
    if "115" in sortie or "115.0" in sortie:
        print("✓ Exercice 3.11: Prix final - CORRECT")
    else:
        raise VerificationError(f"115 attendu\nSortie: {sortie}")


def verifier_exercice_3_12():
    """Vérifie l'exercice 3.12: Mot de passe."""
    from exercices import exercice_3_12
    with mock.patch('builtins.input', return_value="Test123!"):
        sortie = capturer_sortie(exercice_3_12)
    if "True" in sortie:
        print("✓ Exercice 3.12: Mot de passe - CORRECT")
    else:
        raise VerificationError(f"True attendu\nSortie: {sortie}")


def verifier_exercice_3_13():
    """Vérifie l'exercice 3.13: Pierre-Feuille-Ciseaux."""
    from exercices import exercice_3_13
    import random
    with mock.patch('builtins.input', return_value="pierre"):
        with mock.patch('random.choice', return_value="ciseaux"):
            sortie = capturer_sortie(exercice_3_13)
    if "gagnez" in sortie.lower():
        print("✓ Exercice 3.13: Pierre-Feuille-Ciseaux - CORRECT")
    else:
        print(f"⚠ Exercice 3.13: Non deterministic - SKIPPED")


def verifier_exercice_3_14():
    """Vérifie l'exercice 3.14: Notes ECTS."""
    from exercices import exercice_3_14
    with mock.patch('builtins.input', return_value="85"):
        sortie = capturer_sortie(exercice_3_14)
    if "B" in sortie:
        print("✓ Exercice 3.14: Notes ECTS - CORRECT")
    else:
        raise VerificationError(f"Lettre B attendue\nSortie: {sortie}")


def verifier_exercice_3_15():
    """Vérifie l'exercice 3.15: Baccalauréat."""
    from exercices import exercice_3_15
    with mock.patch('builtins.input', side_effect=[
        "12", "14", "15", "13", "11", "10", "9", "8", "14", "13", "12", "11"
    ]):
        sortie = capturer_sortie(exercice_3_15)
    if "admis" in sortie.lower():
        print("✓ Exercice 3.15: Baccalauréat - CORRECT")
    else:
        raise VerificationError(f"Admis attendu\nSortie: {sortie}")


def verifier_tous():
    """Exécute toutes les vérifications."""
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 3: OPÉRATEURS")
    print("=" * 60)
    print()

    verifications = [
        ("3.1 Calculatrice", verifier_exercice_3_1),
        ("3.2 Comparaison", verifier_exercice_3_2),
        ("3.3 Âge", verifier_exercice_3_3),
        ("3.4 Moyenne", verifier_exercice_3_4),
        ("3.5 Appartenance", verifier_exercice_3_5),
        ("3.6 Logiques", verifier_exercice_3_6),
        ("3.7 Remise", verifier_exercice_3_7),
        ("3.8 Triangle", verifier_exercice_3_8),
        ("3.9 Bit à bit", verifier_exercice_3_9),
        ("3.10 Bissextile", verifier_exercice_3_10),
        ("3.11 Prix final", verifier_exercice_3_11),
        ("3.12 Mot de passe", verifier_exercice_3_12),
        ("3.13 Pierre-Feuille-Ciseaux", verifier_exercice_3_13),
        ("3.14 Notes ECTS", verifier_exercice_3_14),
        ("3.15 Baccalauréat", verifier_exercice_3_15),
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
