#!/usr/bin/env python3
import re
"""
CHAPITRE 2 - Script de Vérification Automatique
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
    """Exécute une fonction et capture sa sortie."""
    ancien_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        func()
        sortie = sys.stdout.getvalue()
    finally:
        sys.stdout = ancien_stdout
    return sortie


def verifier_exercice_2_1():
    """Vérifie l'exercice 2.1: Affichage de variables."""
    from exercices import exercice_2_1
    try:
        exercice_2_1()
        print("✓ Exercice 2.1: Affichage de variables - CORRECT")
    except Exception as e:
        print(f"✗ Exercice 2.1: ERREUR - {e}")
        raise


def verifier_exercice_2_2():
    """Vérifie l'exercice 2.2: Conversion de température."""
    from exercices import exercice_2_2
    with mock.patch('builtins.input', return_value="77"):
        sortie = capturer_sortie(exercice_2_2)
    if contient_nombre(sortie, 25.0) and "77.0" in sortie:
        print("✓ Exercice 2.2: Conversion de température - CORRECT")
    else:
        raise VerificationError(f"Attendu 25.0°C pour 77°F\nSortie: {sortie}")


def verifier_exercice_2_3():
    """Vérifie l'exercice 2.3: Calcul de moyenne."""
    from exercices import exercice_2_3
    with mock.patch('builtins.input', side_effect=["10", "20", "30", "40"]):
        sortie = capturer_sortie(exercice_2_3)
    if contient_nombre(sortie, 25):
        print("✓ Exercice 2.3: Calcul de moyenne - CORRECT")
    else:
        raise VerificationError(f"Attendu moyenne de 25\nSortie: {sortie}")


def verifier_exercice_2_4():
    """Vérifie l'exercice 2.4: Validation d'âge."""
    from exercices import exercice_2_4
    with mock.patch('builtins.input', return_value="15"):
        sortie = capturer_sortie(exercice_2_4)
    if contient_terme(sortie, "True") and contient_terme(sortie, "False"):
        print("✓ Exercice 2.4: Validation d'âge - CORRECT")
    else:
        raise VerificationError(f"Attendu True/False pour mineur/majeur\nSortie: {sortie}")


def verifier_exercice_2_5():
    """Vérifie l'exercice 2.5: Analyseur de nombre."""
    from exercices import exercice_2_5
    with mock.patch('builtins.input', return_value="-7.5"):
        sortie = capturer_sortie(exercice_2_5)
    if contient_terme(sortie, "float") and "7.5" in sortie:
        print("✓ Exercice 2.5: Analyseur de nombre - CORRECT")
    else:
        raise VerificationError(f"Type float et valeur abs 7.5 attendus\nSortie: {sortie}")


def verifier_exercice_2_6():
    """Vérifie l'exercice 2.6: Manipulation de chaînes."""
    from exercices import exercice_2_6
    with mock.patch('builtins.input', return_value="Python"):
        sortie = capturer_sortie(exercice_2_6)
    if "PYTHON" in sortie and "python" in sortie and "P" in sortie and "n" in sortie:
        print("✓ Exercice 2.6: Manipulation de chaînes - CORRECT")
    else:
        raise VerificationError(f"Majuscules/minuscules attendues\nSortie: {sortie}")


def verifier_exercice_2_7():
    """Vérifie l'exercice 2.7: Formateur de prix."""
    from exercices import exercice_2_7
    with mock.patch('builtins.input', return_value="1234567.891"):
        sortie = capturer_sortie(exercice_2_7)
    if "1,234,567.89" in sortie or "1234567.89" in sortie:
        print("✓ Exercice 2.7: Formateur de prix - CORRECT")
    else:
        raise VerificationError(f"Format avec séparateurs attendu\nSortie: {sortie}")


def verifier_exercice_2_8():
    """Vérifie l'exercice 2.8: Calculateur de BMR."""
    from exercices import exercice_2_8
    with mock.patch('builtins.input', side_effect=["70", "175", "30"]):
        sortie = capturer_sortie(exercice_2_8)
    if "1680" in sortie or "167" in sortie or "168" in sortie:
        print("✓ Exercice 2.8: Calculateur de BMR - CORRECT")
    else:
        raise VerificationError(f"BMR proche de 1680 attendu\nSortie: {sortie}")


def verifier_exercice_2_9():
    """Vérifie l'exercice 2.9: Validateur d'email."""
    from exercices import exercice_2_9
    with mock.patch('builtins.input', return_value="test@example.com"):
        sortie = capturer_sortie(exercice_2_9)
    if contient_terme(sortie, "True"):
        print("✓ Exercice 2.9: Validateur d'email - CORRECT")
    else:
        raise VerificationError(f"Email valide attendu: True\nSortie: {sortie}")


def verifier_exercice_2_10():
    """Vérifie l'exercice 2.10: Convertisseur de durée."""
    from exercices import exercice_2_10
    with mock.patch('builtins.input', return_value="3661"):
        sortie = capturer_sortie(exercice_2_10)
    if "61" in sortie and "1" in sortie:
        print("✓ Exercice 2.10: Convertisseur de durée - CORRECT")
    else:
        raise VerificationError(f"61 minutes et 1 seconde attendus\nSortie: {sortie}")


def verifier_exercice_2_11():
    """Vérifie l'exercice 2.11: Intérêts composés."""
    from exercices import exercice_2_11
    with mock.patch('builtins.input', side_effect=["1000", "5", "10"]):
        sortie = capturer_sortie(exercice_2_11)
    if contient_nombre(sortie, 1628):
        print("✓ Exercice 2.11: Intérêts composés - CORRECT")
    else:
        raise VerificationError(f"Capital final proche de 1628 attendu\nSortie: {sortie}")


def verifier_exercice_2_12():
    """Vérifie l'exercice 2.12: Générateur d'acronyme."""
    from exercices import exercice_2_12
    with mock.patch('builtins.input', return_value="Python est vraiment génial"):
        sortie = capturer_sortie(exercice_2_12)
    if "PEG" in sortie or "PEG" in sortie:
        print("✓ Exercice 2.12: Générateur d'acronyme - CORRECT")
    else:
        raise VerificationError(f"Acronyme PEG attendu\nSortie: {sortie}")


def verifier_exercice_2_13():
    """Vérifie l'exercice 2.13: Convertisseur romain."""
    from exercices import exercice_2_13
    with mock.patch('builtins.input', return_value="7"):
        sortie = capturer_sortie(exercice_2_13)
    if "VII" in sortie:
        print("✓ Exercice 2.13: Convertisseur romain - CORRECT")
    else:
        raise VerificationError(f"VII attendu pour 7\nSortie: {sortie}")


def verifier_exercice_2_14():
    """Vérifie l'exercice 2.14: Calculateur de note."""
    from exercices import exercice_2_14
    with mock.patch('builtins.input', return_value="14.5"):
        sortie = capturer_sortie(exercice_2_14)
    if "B" in sortie:
        print("✓ Exercice 2.14: Calculateur de note - CORRECT")
    else:
        raise VerificationError(f"Lettre B attendue\nSortie: {sortie}")


def verifier_exercice_2_15():
    """Vérifie l'exercice 2.15: Pourcentage de votes."""
    from exercices import exercice_2_15
    with mock.patch('builtins.input', side_effect=["1500", "2000", "500"]):
        sortie = capturer_sortie(exercice_2_15)
    if "37.5" in sortie and "50.0" in sortie:
        print("✓ Exercice 2.15: Pourcentage de votes - CORRECT")
    else:
        raise VerificationError(f"37.5% et 50.0% attendus\nSortie: {sortie}")


def verifier_tous():
    """Exécute toutes les vérifications."""
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 2: VARIABLES ET TYPES")
    print("=" * 60)
    print()

    verifications = [
        ("2.1 Variables", verifier_exercice_2_1),
        ("2.2 Température", verifier_exercice_2_2),
        ("2.3 Moyenne", verifier_exercice_2_3),
        ("2.4 Validation âge", verifier_exercice_2_4),
        ("2.5 Analyseur nombre", verifier_exercice_2_5),
        ("2.6 Manipulation chaines", verifier_exercice_2_6),
        ("2.7 Formateur prix", verifier_exercice_2_7),
        ("2.8 BMR", verifier_exercice_2_8),
        ("2.9 Validateur email", verifier_exercice_2_9),
        ("2.10 Durée", verifier_exercice_2_10),
        ("2.11 Intérêts composés", verifier_exercice_2_11),
        ("2.12 Acronyme", verifier_exercice_2_12),
        ("2.13 Chiffres romains", verifier_exercice_2_13),
        ("2.14 Note lettre", verifier_exercice_2_14),
        ("2.15 Votes", verifier_exercice_2_15),
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
