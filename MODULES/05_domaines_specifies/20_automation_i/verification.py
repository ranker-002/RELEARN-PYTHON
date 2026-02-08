#!/usr/bin/env python3
import re
"""
CHAPITRE 20 - Vérification Automatique
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


def verifier_exercice_20_1():
    from exercices import exercice_20_1
    try:
        exercice_20_1()
        print("✓ 20.1: Lister fichiers - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_2():
    from exercices import exercice_20_2
    try:
        exercice_20_2()
        print("✓ 20.2: pathlib basique - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_3():
    from exercices import exercice_20_3
    try:
        exercice_20_3()
        print("✓ 20.3: Créer dossiers - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_4():
    from exercices import exercice_20_4
    try:
        exercice_20_4()
        print("✓ 20.4: Chercher avec glob - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_5():
    from exercices import exercice_20_5
    try:
        exercice_20_5()
        print("✓ 20.5: Copier fichier - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_6():
    from exercices import exercice_20_6
    try:
        exercice_20_6()
        print("✓ 20.6: Infos fichier - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_7():
    from exercices import exercice_20_7
    try:
        exercice_20_7()
        print("✓ 20.7: Renommage simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_8():
    from exercices import exercice_20_8
    try:
        exercice_20_8()
        print("✓ 20.8: Suppression - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_9():
    from exercices import exercice_20_9
    try:
        exercice_20_9()
        print("✓ 20.9: Recherche récursive - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_10():
    from exercices import exercice_20_10
    try:
        exercice_20_10()
        print("✓ 20.10: Commandes système - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_11():
    from exercices import exercice_20_11
    try:
        exercice_20_11()
        print("✓ 20.11: Organisateur simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_12():
    from exercices import exercice_20_12
    try:
        exercice_20_12()
        print("✓ 20.12: Nettoyage dossier - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_13():
    from exercices import exercice_20_13
    try:
        exercice_20_13()
        print("✓ 20.13: Compression - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_14():
    from exercices import exercice_20_14
    try:
        exercice_20_14()
        print("✓ 20.14: Calcul taille dossier - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_20_15():
    from exercices import exercice_20_15
    try:
        exercice_20_15()
        print("✓ 20.15: Système backup complet - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 20: AUTOMATION I")
    print("=" * 60)
    
    verifications = [
        ("20.1", verifier_exercice_20_1),
        ("20.2", verifier_exercice_20_2),
        ("20.3", verifier_exercice_20_3),
        ("20.4", verifier_exercice_20_4),
        ("20.5", verifier_exercice_20_5),
        ("20.6", verifier_exercice_20_6),
        ("20.7", verifier_exercice_20_7),
        ("20.8", verifier_exercice_20_8),
        ("20.9", verifier_exercice_20_9),
        ("20.10", verifier_exercice_20_10),
        ("20.11", verifier_exercice_20_11),
        ("20.12", verifier_exercice_20_12),
        ("20.13", verifier_exercice_20_13),
        ("20.14", verifier_exercice_20_14),
        ("20.15", verifier_exercice_20_15),
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
