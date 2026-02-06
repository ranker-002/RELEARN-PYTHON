#!/usr/bin/env python3
"""
CHAPITRE 1 - Script de Vérification Automatique
==============================================
Ce script vérifie automatiquement vos solutions aux exercices.

Utilisation:
    python verification.py

Ce script teste chaque fonction et affiche le résultat.
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


def creer_entree(simulee):
    """Crée un mock pour simuler input()."""
    return mock.patch('builtins.input', return_value=simulee)


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.1
# =============================================================================

def verifier_exercice_1_1():
    """Vérifie l'exercice 1.1: Hello World."""
    from exercices import exercice_1_1

    sortie = capturer_sortie(exercice_1_1)

    if "Hello" not in sortie or "World" not in sortie:
        raise VerificationError(
            "La sortie doit contenir 'Hello' et 'World'\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.1: Hello World - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.2
# =============================================================================

def verifier_exercice_1_2():
    """Vérifie l'exercice 1.2: Présentation."""
    from exercices import exercice_1_2

    with mock.patch('builtins.input', return_value="Alice"):
        sortie = capturer_sortie(exercice_1_2)

    if "Bonjour" not in sortie or "Alice" not in sortie:
        raise VerificationError(
            "La sortie doit contenir 'Bonjour' et le prénom saisi\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.2: Présentation - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.3
# =============================================================================

def verifier_exercice_1_3():
    """Vérifie l'exercice 1.3: Calcul simple."""
    from exercices import exercice_1_3

    with mock.patch('builtins.input', side_effect=["5", "3"]):
        sortie = capturer_sortie(exercice_1_3)

    if "8" not in sortie:
        raise VerificationError(
            "La somme de 5 et 3 doit être 8\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.3: Calcul simple - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.4
# =============================================================================

def verifier_exercice_1_4():
    """Vérifie l'exercice 1.4: Calculatrice."""
    from exercices import exercice_1_4

    with mock.patch('builtins.input', side_effect=["10", "2"]):
        sortie = capturer_sortie(exercice_1_4)

    # Vérifier les 4 opérations
    verificateurs = [
        ("Addition", "12"),
        ("Soustraction", "8"),
        ("Multiplication", "20"),
        ("Division", "5.0"),
    ]

    for nom, attendu in verificateurs:
        if attendu not in sortie:
            raise VerificationError(
                f"Vérifier l'opération {nom}: attendu '{attendu}'\n"
                f"Votre sortie: {sortie}"
            )

    print("✓ Exercice 1.4: Calculatrice - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.5
# =============================================================================

def verifier_exercice_1_5():
    """Vérifie l'exercice 1.5: Conversion température."""
    from exercices import exercice_1_5

    with mock.patch('builtins.input', return_value="25"):
        sortie = capturer_sortie(exercice_1_5)

    if "77" not in sortie:
        raise VerificationError(
            "25°C doit faire 77°F (ou 77.0)\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.5: Conversion température - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.6
# =============================================================================

def verifier_exercice_1_6():
    """Vérifie l'exercice 1.6: Carré."""
    from exercices import exercice_1_6

    with mock.patch('builtins.input', return_value="5"):
        sortie = capturer_sortie(exercice_1_6)

    if "20" not in sortie or "25" not in sortie:
        raise VerificationError(
            "Carré de côté 5: périmètre=20, aire=25\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.6: Carré - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.7
# =============================================================================

def verifier_exercice_1_7():
    """Vérifie l'exercice 1.7: Moyenne."""
    from exercices import exercice_1_7

    with mock.patch('builtins.input', side_effect=["15", "12", "18"]):
        sortie = capturer_sortie(exercice_1_7)

    if "15" not in sortie:
        raise VerificationError(
            "Moyenne de 15, 12, 18 = 15\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.7: Moyenne - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.8
# =============================================================================

def verifier_exercice_1_8():
    """Vérifie l'exercice 1.8: Remise."""
    from exercices import exercice_1_8

    with mock.patch('builtins.input', return_value="100"):
        sortie = capturer_sortie(exercice_1_8)

    if "20" not in sortie or "80" not in sortie:
        raise VerificationError(
            "Remise de 20% sur 100: remise=20, final=80\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.8: Remise - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.9
# =============================================================================

def verifier_exercice_1_9():
    """Vérifie l'exercice 1.9: Carte de visite."""
    from exercices import exercice_1_9

    with mock.patch('builtins.input', side_effect=["Jean", "Dupont", "30", "Paris"]):
        sortie = capturer_sortie(exercice_1_9)

    # Vérifier le format de base
    if "DUPONT" not in sortie or "JEAN" not in sortie:
        raise VerificationError(
            "Le nom et prénom doivent être en majuscules\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.9: Carte de visite - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.10
# =============================================================================

def verifier_exercice_1_10():
    """Vérifie l'exercice 1.10: Intérêts."""
    from exercices import exercice_1_10

    with mock.patch('builtins.input', side_effect=["1000", "5", "2"]):
        sortie = capturer_sortie(exercice_1_10)

    if "100" not in sortie or "1100" not in sortie:
        raise VerificationError(
            "Intérêts sur 1000€ à 5% pendant 2 ans = 100€\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.10: Intérêts - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.11
# =============================================================================

def verifier_exercice_1_11():
    """Vérifie l'exercice 1.11: Conversion devises."""
    from exercices import exercice_1_11

    with mock.patch('builtins.input', return_value="50"):
        sortie = capturer_sortie(exercice_1_11)

    if "55" not in sortie:
        raise VerificationError(
            "50 EUR à 1.10 = 55 USD\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.11: Conversion devises - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.12
# =============================================================================

def verifier_exercice_1_12():
    """Vérifie l'exercice 1.12: IMC."""
    from exercices import exercice_1_12

    with mock.patch('builtins.input', side_effect=["70", "1.75"]):
        sortie = capturer_sortie(exercice_1_12)

    if "22" not in sortie:
        raise VerificationError(
            "IMC de 70kg pour 1.75m ≈ 22.86\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.12: IMC - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.13
# =============================================================================

def verifier_exercice_1_13():
    """Vérifie l'exercice 1.13: Panier."""
    from exercices import exercice_1_13

    with mock.patch('builtins.input', side_effect=["10", "25", "15"]):
        sortie = capturer_sortie(exercice_1_13)

    if "50" not in sortie or "10" not in sortie or "60" not in sortie:
        raise VerificationError(
            "Panier: sous-total=50, TVA=10, total=60\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.13: Panier courses - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.14
# =============================================================================

def verifier_exercice_1_14():
    """Vérifie l'exercice 1.14: Email."""
    from exercices import exercice_1_14

    with mock.patch('builtins.input', side_effect=["Jean", "DUPONT", "exemple", "com"]):
        sortie = capturer_sortie(exercice_1_14)

    if "jean.dupont@exemple.com" not in sortie:
        raise VerificationError(
            "Email attendu: jean.dupont@exemple.com\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.14: Email - CORRECT")


# =============================================================================
# VÉRIFICATIONS EXERCICE 1.15
# =============================================================================

def verifier_exercice_1_15():
    """Vérifie l'exercice 1.15: Temps trajet."""
    from exercices import exercice_1_15

    with mock.patch('builtins.input', side_effect=["120", "60"]):
        sortie = capturer_sortie(exercice_1_15)

    if "2" not in sortie or "120" not in sortie:
        raise VerificationError(
            "120km à 60km/h = 2h = 120min\n"
            f"Votre sortie: {sortie}"
        )

    print("✓ Exercice 1.15: Temps trajet - CORRECT")


# =============================================================================
# VÉRIFICATION PRINCIPALE
# =============================================================================

def verifier_tous():
    """Exécute toutes les vérifications."""
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 1: PREMIERS PAS")
    print("=" * 60)
    print()

    verifications = [
        ("1.1 Hello World", verifier_exercice_1_1),
        ("1.2 Présentation", verifier_exercice_1_2),
        ("1.3 Calcul simple", verifier_exercice_1_3),
        ("1.4 Calculatrice", verifier_exercice_1_4),
        ("1.5 Température", verifier_exercice_1_5),
        ("1.6 Carré", verifier_exercice_1_6),
        ("1.7 Moyenne", verifier_exercice_1_7),
        ("1.8 Remise", verifier_exercice_1_8),
        ("1.9 Carte visite", verifier_exercice_1_9),
        ("1.10 Intérêts", verifier_exercice_1_10),
        ("1.11 Devises", verifier_exercice_1_11),
        ("1.12 IMC", verifier_exercice_1_12),
        ("1.13 Panier", verifier_exercice_1_13),
        ("1.14 Email", verifier_exercice_1_14),
        ("1.15 Trajet", verifier_exercice_1_15),
    ]

    erreurs = 0

    for nom, verification in verifications:
        try:
            verification()
        except VerificationError as e:
            print(f"✗ {nom}: ERREUR")
            print(f"   {e}")
            erreurs += 1
        except Exception as e:
            print(f"✗ {nom}: EXCEPTION")
            print(f"   {type(e).__name__}: {e}")
            erreurs += 1

    print()
    print("=" * 60)

    if erreurs == 0:
        print("🎉 TOUS LES EXERCICES SONT CORRECTS! 🎉")
        print("=" * 60)
        return True
    else:
        print(f"⚠️  {erreurs} exercice(s) avec erreur(s)")
        print("=" * 60)
        return False


if __name__ == "__main__":
    try:
        success = verifier_tous()
        sys.exit(0 if success else 1)
    except ImportError as e:
        print("ERREUR: Veuillez exécuter ce script depuis le dossier du chapitre")
        print(f"Détail: {e}")
        sys.exit(1)
