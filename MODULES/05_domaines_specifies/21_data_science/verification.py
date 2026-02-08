#!/usr/bin/env python3
import re
"""
CHAPITRE 22 - Vérification Automatique
"""

import sys


class VerificationError(Exception):
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


def verifier_exercice_22_1():
    from exercices import exercice_22_1
    try:
        exercice_22_1()
        print("✓ 22.1: NumPy basique - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_2():
    from exercices import exercice_22_2
    try:
        exercice_22_2()
        print("✓ 22.2: Tableaux 2D - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_3():
    from exercices import exercice_22_3
    try:
        exercice_22_3()
        print("✓ 22.3: Pandas DataFrame - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_4():
    from exercices import exercice_22_4
    try:
        exercice_22_4()
        print("✓ 22.4: Sélection et filtre - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_5():
    from exercices import exercice_22_5
    try:
        exercice_22_5()
        print("✓ 22.5: Statistiques - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_6():
    from exercices import exercice_22_6
    try:
        exercice_22_6()
        print("✓ 22.6: Group by - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_7():
    from exercices import exercice_22_7
    try:
        exercice_22_7()
        print("✓ 22.7: Tri et rang - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_8():
    from exercices import exercice_22_8
    try:
        exercice_22_8()
        print("✓ 22.8: Valeurs manquantes - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_9():
    from exercices import exercice_22_9
    try:
        exercice_22_9()
        print("✓ 22.9: Créer colonne - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_10():
    from exercices import exercice_22_10
    try:
        exercice_22_10()
        print("✓ 22.10: Énumérer - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_11():
    from exercices import exercice_22_11
    try:
        exercice_22_11()
        print("✓ 22.11: Pivot table - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_12():
    from exercices import exercice_22_12
    try:
        exercice_22_12()
        print("✓ 22.12: Concaténation - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_13():
    from exercices import exercice_22_13
    try:
        exercice_22_13()
        print("✓ 22.13: Fusion - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_14():
    from exercices import exercice_22_14
    try:
        exercice_22_14()
        print("✓ 22.14: Test statistique - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_22_15():
    from exercices import exercice_22_15
    try:
        exercice_22_15()
        print("✓ 22.15: Analyse complète - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 22: DATA SCIENCE I")
    print("=" * 60)
    
    verifications = [
        ("22.1", verifier_exercice_22_1),
        ("22.2", verifier_exercice_22_2),
        ("22.3", verifier_exercice_22_3),
        ("22.4", verifier_exercice_22_4),
        ("22.5", verifier_exercice_22_5),
        ("22.6", verifier_exercice_22_6),
        ("22.7", verifier_exercice_22_7),
        ("22.8", verifier_exercice_22_8),
        ("22.9", verifier_exercice_22_9),
        ("22.10", verifier_exercice_22_10),
        ("22.11", verifier_exercice_22_11),
        ("22.12", verifier_exercice_22_12),
        ("22.13", verifier_exercice_22_13),
        ("22.14", verifier_exercice_22_14),
        ("22.15", verifier_exercice_22_15),
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
