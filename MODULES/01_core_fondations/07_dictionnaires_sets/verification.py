#!/usr/bin/env python3
import re
"""
CHAPITRE 7 - Script de Verification Automatique
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


def verifier_exercice_7_1():
    """Verifie l'exercice 7.1: Creation de dictionnaire."""
    from exercices import exercice_7_1
    sortie = capturer_sortie(exercice_7_1)
    if "Le Petit Prince" in sortie and "1943" in sortie:
        print("✓ Exercice 7.1: Creation de dictionnaire - CORRECT")
    else:
        raise VerificationError(f"Livre attendu\nSortie: {sortie}")


def verifier_exercice_7_2():
    """Verifie l'exercice 7.2: Acces aux valeurs."""
    from exercices import exercice_7_2
    sortie = capturer_sortie(exercice_7_2)
    if "Paris" in sortie:
        print("✓ Exercice 7.2: Acces aux valeurs - CORRECT")
    else:
        raise VerificationError(f"Paris attendu\nSortie: {sortie}")


def verifier_exercice_7_3():
    """Verifie l'exercice 7.3: Modification."""
    from exercices import exercice_7_3
    sortie = capturer_sortie(exercice_7_3)
    if "Paris" in sortie and "Alice" in sortie:
        print("✓ Exercice 7.3: Modification - CORRECT")
    else:
        raise VerificationError(f"Modification attendue\nSortie: {sortie}")


def verifier_exercice_7_4():
    """Verifie l'exercice 7.4: Creation de set."""
    from exercices import exercice_7_4
    sortie = capturer_sortie(exercice_7_4)
    if "{1, 2, 3}" in sortie or "1, 2, 3" in sortie:
        print("✓ Exercice 7.4: Creation de set - CORRECT")
    else:
        raise VerificationError(f"Set {1, 2, 3} attendu\nSortie: {sortie}")


def verifier_exercice_7_5():
    """Verifie l'exercice 7.5: Operations sur sets."""
    from exercices import exercice_7_5
    sortie = capturer_sortie(exercice_7_5)
    if "{1, 2, 3, 4, 5, 6, 7, 8}" in sortie or "4, 5" in sortie:
        print("✓ Exercice 7.5: Operations sur sets - CORRECT")
    else:
        raise VerificationError(f"Operations attendues\nSortie: {sortie}")


def verifier_exercice_7_6():
    """Verifie l'exercice 7.6: Boutique."""
    from exercices import exercice_7_6
    sortie = capturer_sortie(exercice_7_6)
    if "pomme" in sortie and "1.50" in sortie:
        print("✓ Exercice 7.6: Boutique - CORRECT")
    else:
        raise VerificationError(f"Inventaire attendu\nSortie: {sortie}")


def verifier_exercice_7_7():
    """Verifie l'exercice 7.7: Appartenance."""
    from exercices import exercice_7_7
    sortie = capturer_sortie(exercice_7_7)
    if contient_terme(sortie, "True") and contient_terme(sortie, "False"):
        print("✓ Exercice 7.7: Verification d'appartenance - CORRECT")
    else:
        raise VerificationError(f"True/False attendus\nSortie: {sortie}")


def verifier_exercice_7_8():
    """Verifie l'exercice 7.8: Compteur de lettres."""
    from exercices import exercice_7_8
    sortie = capturer_sortie(exercice_7_8)
    if "'p': 1" in sortie and "'r': 2" in sortie:
        print("✓ Exercice 7.8: Compteur de lettres - CORRECT")
    else:
        raise VerificationError(f"Compteur attendu\nSortie: {sortie}")


def verifier_exercice_7_9():
    """Verifie l'exercice 7.9: Comprehension."""
    from exercices import exercice_7_9
    sortie = capturer_sortie(exercice_7_9)
    if "1: 1" in sortie and "pair" in sortie:
        print("✓ Exercice 7.9: Comprehension de dictionnaire - CORRECT")
    else:
        raise VerificationError(f"Comprehension attendue\nSortie: {sortie}")


def verifier_exercice_7_10():
    """Verifie l'exercice 7.10: Gestion etudiants."""
    from exercices import exercice_7_10
    sortie = capturer_sortie(exercice_7_10)
    if "15" in sortie or "14" in sortie:
        print("✓ Exercice 7.10: Gestion d'etudiants - CORRECT")
    else:
        raise VerificationError(f"Notes attendues\nSortie: {sortie}")


def verifier_exercice_7_11():
    """Verifie l'exercice 7.11: Dedoublonnage."""
    from exercices import exercice_7_11
    sortie = capturer_sortie(exercice_7_11)
    if "[3, 1, 2, 4, 5]" in sortie:
        print("✓ Exercice 7.11: Dedoublonnage - CORRECT")
    else:
        raise VerificationError(f"[3, 1, 2, 4, 5] attendu\nSortie: {sortie}")


def verifier_exercice_7_12():
    """Verifie l'exercice 7.12: Groupement."""
    from exercices import exercice_7_12
    sortie = capturer_sortie(exercice_7_12)
    if "'a'" in sortie and "pomme" in sortie:
        print("✓ Exercice 7.12: Groupement par categorie - CORRECT")
    else:
        raise VerificationError(f"Groupement attendu\nSortie: {sortie}")


def verifier_exercice_7_13():
    """Verifie l'exercice 7.13: Union inventaires."""
    from exercices import exercice_7_13
    sortie = capturer_sortie(exercice_7_13)
    if "'pomme': 50" in sortie and "'banane': 50" in sortie:
        print("✓ Exercice 7.13: Union d'inventaires - CORRECT")
    else:
        raise VerificationError(f"Fusion attendue\nSortie: {sortie}")


def verifier_exercice_7_14():
    """Verifie l'exercice 7.14: Jeu de cartes."""
    from exercices import exercice_7_14
    sortie = capturer_sortie(exercice_7_14)
    if contient_nombre(sortie, 52):
        print("✓ Exercice 7.14: Jeu de cartes - CORRECT")
    else:
        raise VerificationError(f"52 cartes attendu\nSortie: {sortie}")


def verifier_exercice_7_15():
    """Verifie l'exercice 7.15: Analyseur de texte."""
    from exercices import exercice_7_15
    sortie = capturer_sortie(exercice_7_15)
    if "le" in sortie and "5" in sortie:
        print("✓ Exercice 7.15: Analyseur de texte - CORRECT")
    else:
        raise VerificationError(f"Analyse attendue\nSortie: {sortie}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 7: DICTIONNAIRES ET SETS")
    print("=" * 60)
    print()

    verifications = [
        ("7.1 Creation dict", verifier_exercice_7_1),
        ("7.2 Acces valeurs", verifier_exercice_7_2),
        ("7.3 Modification", verifier_exercice_7_3),
        ("7.4 Creation set", verifier_exercice_7_4),
        ("7.5 Operations sets", verifier_exercice_7_5),
        ("7.6 Boutique", verifier_exercice_7_6),
        ("7.7 Appartenance", verifier_exercice_7_7),
        ("7.8 Compteur lettres", verifier_exercice_7_8),
        ("7.9 Comprehension", verifier_exercice_7_9),
        ("7.10 Gestion etudiants", verifier_exercice_7_10),
        ("7.11 Dedoublonnage", verifier_exercice_7_11),
        ("7.12 Groupement", verifier_exercice_7_12),
        ("7.13 Union inventaires", verifier_exercice_7_13),
        ("7.14 Jeu de cartes", verifier_exercice_7_14),
        ("7.15 Analyseur texte", verifier_exercice_7_15),
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
