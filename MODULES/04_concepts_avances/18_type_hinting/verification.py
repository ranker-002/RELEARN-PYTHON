#!/usr/bin/env python3
import re
"""
CHAPITRE 19 - Vérification Automatique
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


def verifier_exercice_19_1():
    from exercices import exercice_19_1
    try:
        exercice_19_1()
        print("✓ 19.1: Types simples - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_2():
    from exercices import exercice_19_2
    try:
        exercice_19_2()
        print("✓ 19.2: Listes typées - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_3():
    from exercices import exercice_19_3
    try:
        exercice_19_3()
        print("✓ 19.3: Dictionnaires typés - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_4():
    from exercices import exercice_19_4
    try:
        exercice_19_4()
        print("✓ 19.4: Fonction avec types - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_5():
    from exercices import exercice_19_5
    try:
        exercice_19_5()
        print("✓ 19.5: Optional - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_6():
    from exercices import exercice_19_6
    try:
        exercice_19_6()
        print("✓ 19.6: Union - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_7():
    from exercices import exercice_19_7
    try:
        exercice_19_7()
        print("✓ 19.7: Callable - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_8():
    from exercices import exercice_19_8
    try:
        exercice_19_8()
        print("✓ 19.8: Tuple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_9():
    from exercices import exercice_19_9
    try:
        exercice_19_9()
        print("✓ 19.9: TypedDict - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_10():
    from exercices import exercice_19_10
    try:
        exercice_19_10()
        print("✓ 19.10: Dataclass - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_11():
    from exercices import exercice_19_11
    try:
        exercice_19_11()
        print("✓ 19.11: Generic - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_12():
    from exercices import exercice_19_12
    try:
        exercice_19_12()
        print("✓ 19.12: Protocol - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_13():
    from exercices import exercice_19_13
    try:
        exercice_19_13()
        print("✓ 19.13: Système Employé - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_14():
    from exercices import exercice_19_14
    try:
        exercice_19_14()
        print("✓ 19.14: Type checking - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_19_15():
    from exercices import exercice_19_15
    try:
        exercice_19_15()
        print("✓ 19.15: Inventaire complet - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 19: TYPE HINTING")
    print("=" * 60)
    
    verifications = [
        ("19.1", verifier_exercice_19_1),
        ("19.2", verifier_exercice_19_2),
        ("19.3", verifier_exercice_19_3),
        ("19.4", verifier_exercice_19_4),
        ("19.5", verifier_exercice_19_5),
        ("19.6", verifier_exercice_19_6),
        ("19.7", verifier_exercice_19_7),
        ("19.8", verifier_exercice_19_8),
        ("19.9", verifier_exercice_19_9),
        ("19.10", verifier_exercice_19_10),
        ("19.11", verifier_exercice_19_11),
        ("19.12", verifier_exercice_19_12),
        ("19.13", verifier_exercice_19_13),
        ("19.14", verifier_exercice_19_14),
        ("19.15", verifier_exercice_19_15),
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
