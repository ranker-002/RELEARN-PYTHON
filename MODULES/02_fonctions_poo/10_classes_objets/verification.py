#!/usr/bin/env python3
import re
"""
CHAPITRE 11 - Script de Verification Automatique
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


def verifier_exercice_11_1():
    """Verifie l'exercice 11.1: Classe simple."""
    from exercices import exercice_11_1
    try:
        exercice_11_1()
        print("✓ Exercice 11.1: Classe simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_2():
    """Verifie l'exercice 11.2: Constructeur."""
    from exercices import exercice_11_2
    try:
        exercice_11_2()
        print("✓ Exercice 11.2: Classe avec constructeur - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_3():
    """Verifie l'exercice 11.3: Attributs et methodes."""
    from exercices import exercice_11_3
    try:
        exercice_11_3()
        print("✓ Exercice 11.3: Attributs et methodes - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_4():
    """Verifie l'exercice 11.4: Valeurs par defaut."""
    from exercices import exercice_11_4
    try:
        exercice_11_4()
        print("✓ Exercice 11.4: Valeurs par defaut - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_5():
    """Verifie l'exercice 11.5: Methode de classe."""
    from exercices import exercice_11_5
    try:
        exercice_11_5()
        print("✓ Exercice 11.5: Methode de classe - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_6():
    """Verifie l'exercice 11.6: Methode statique."""
    from exercices import exercice_11_6
    try:
        exercice_11_6()
        print("✓ Exercice 11.6: Methode statique - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_7():
    """Verifie l'exercice 11.7: Propriete simple."""
    from exercices import exercice_11_7
    try:
        exercice_11_7()
        print("✓ Exercice 11.7: Propriete simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_8():
    """Verifie l'exercice 11.8: Propriete calculee."""
    from exercices import exercice_11_8
    try:
        exercice_11_8()
        print("✓ Exercice 11.8: Propriete calculee - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_9():
    """Verifie l'exercice 11.9: Attribut de classe."""
    from exercices import exercice_11_9
    try:
        exercice_11_9()
        print("✓ Exercice 11.9: Attribut de classe - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_10():
    """Verifie l'exercice 11.10: __str__ et __repr__."""
    from exercices import exercice_11_10
    try:
        exercice_11_10()
        print("✓ Exercice 11.10: __str__ et __repr__ - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_11():
    """Verifie l'exercice 11.11: Validation dans setter."""
    from exercices import exercice_11_11
    try:
        exercice_11_11()
        print("✓ Exercice 11.11: Validation setter - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_12():
    """Verifie l'exercice 11.12: Classe Etudiant."""
    from exercices import exercice_11_12
    try:
        exercice_11_12()
        print("✓ Exercice 11.12: Classe Etudiant - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_13():
    """Verifie l'exercice 11.13: Systeme bancaire."""
    from exercices import exercice_11_13
    try:
        exercice_11_13()
        print("✓ Exercice 11.13: Systeme bancaire - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_14():
    """Verifie l'exercice 11.14: Classe Produit."""
    from exercices import exercice_11_14
    try:
        exercice_11_14()
        print("✓ Exercice 11.14: Classe Produit - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_11_15():
    """Verifie l'exercice 11.15: Systeme de gestion."""
    from exercices import exercice_11_15
    try:
        exercice_11_15()
        print("✓ Exercice 11.15: Systeme de gestion - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    """Execute toutes les verifications."""
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 11: CLASSES ET OBJETS")
    print("=" * 60)
    print()

    verifications = [
        ("11.1 Classe simple", verifier_exercice_11_1),
        ("11.2 Constructeur", verifier_exercice_11_2),
        ("11.3 Attributs/Methodes", verifier_exercice_11_3),
        ("11.4 Valeurs defaut", verifier_exercice_11_4),
        ("11.5 Methode classe", verifier_exercice_11_5),
        ("11.6 Methode statique", verifier_exercice_11_6),
        ("11.7 Propriete simple", verifier_exercice_11_7),
        ("11.8 Propriete employee", verifier_exercice_11_8),
        ("11.9 Attribut classe", verifier_exercice_11_9),
        ("11.10 __str__/__repr__", verifier_exercice_11_10),
        ("11.11 Validation setter", verifier_exercice_11_11),
        ("11.12 Classe Etudiant", verifier_exercice_11_12),
        ("11.13 Systeme bancaire", verifier_exercice_11_13),
        ("11.14 Classe Produit", verifier_exercice_11_14),
        ("11.15 Systeme gestion", verifier_exercice_11_15),
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
