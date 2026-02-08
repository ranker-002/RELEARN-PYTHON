#!/usr/bin/env python3
import re
"""
CHAPITRE 23 - Script de Vérification Automatique
=============================================
Ce script vérifie automatiquement vos solutions aux exercices.
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


def verifier_graphique_cree(func, verificateur=None):
    """Vérifie qu'un graphique est créé sans erreur."""
    try:
        func()
        return True
    except Exception as e:
        raise VerificationError(f"Erreur lors de la création du graphique: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.1
# =============================================================================

def verifier_exercice_23_1():
    """Vérifie l'exercice 23.1: Premier graphique."""
    from exercices import exercice_23_1

    try:
        exercice_23_1()
        print("✓ Exercice 23.1: Premier graphique - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.2
# =============================================================================

def verifier_exercice_23_2():
    """Vérifie l'exercice 23.2: Diagramme en bâtons."""
    from exercices import exercice_23_2

    try:
        exercice_23_2()
        print("✓ Exercice 23.2: Diagramme en bâtons - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.3
# =============================================================================

def verifier_exercice_23_3():
    """Vérifie l'exercice 23.3: Histogramme."""
    from exercices import exercice_23_3

    try:
        exercice_23_3()
        print("✓ Exercice 23.3: Histogramme - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.4
# =============================================================================

def verifier_exercice_23_4():
    """Vérifie l'exercice 23.4: Nuage de points."""
    from exercices import exercice_23_4

    try:
        exercice_23_4()
        print("✓ Exercice 23.4: Nuage de points - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.5
# =============================================================================

def verifier_exercice_23_5():
    """Vérifie l'exercice 23.5: Diagramme circulaire."""
    from exercices import exercice_23_5

    try:
        exercice_23_5()
        print("✓ Exercice 23.5: Diagramme circulaire - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.6
# =============================================================================

def verifier_exercice_23_6():
    """Vérifie l'exercice 23.6: Sous-graphiques."""
    from exercices import exercice_23_6

    try:
        exercice_23_6()
        print("✓ Exercice 23.6: Sous-graphiques - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.7
# =============================================================================

def verifier_exercice_23_7():
    """Vérifie l'exercice 23.7: DataFrame plot."""
    from exercices import exercice_23_7

    try:
        exercice_23_7()
        print("✓ Exercice 23.7: DataFrame plot - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.8
# =============================================================================

def verifier_exercice_23_8():
    """Vérifie l'exercice 23.8: Personnalisation."""
    from exercices import exercice_23_8

    try:
        exercice_23_8()
        print("✓ Exercice 23.8: Personnalisation - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.9
# =============================================================================

def verifier_exercice_23_9():
    """Vérifie l'exercice 23.9: Multiples séries."""
    from exercices import exercice_23_9

    try:
        exercice_23_9()
        print("✓ Exercice 23.9: Multiples séries - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.10
# =============================================================================

def verifier_exercice_23_10():
    """Vérifie l'exercice 23.10: Boîte à moustaches."""
    from exercices import exercice_23_10

    try:
        exercice_23_10()
        print("✓ Exercice 23.10: Boîte à moustaches - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.11
# =============================================================================

def verifier_exercice_23_11():
    """Vérifie l'exercice 23.11: Sauvegarde."""
    from exercices import exercice_23_11

    try:
        exercice_23_11()
        import os
        if os.path.exists('sin_cos.png') and os.path.exists('sin_cos.pdf'):
            print("✓ Exercice 23.11: Sauvegarde - CORRECT")
        else:
            raise VerificationError("Les fichiers n'ont pas été créés")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.12
# =============================================================================

def verifier_exercice_23_12():
    """Vérifie l'exercice 23.12: Corrélation."""
    from exercices import exercice_23_12

    try:
        exercice_23_12()
        print("✓ Exercice 23.12: Corrélation - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.13
# =============================================================================

def verifier_exercice_23_13():
    """Vérifie l'exercice 23.13: Styles."""
    from exercices import exercice_23_13

    try:
        exercice_23_13()
        print("✓ Exercice 23.13: Styles - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.14
# =============================================================================

def verifier_exercice_23_14():
    """Vérifie l'exercice 23.14: Combinaison."""
    from exercices import exercice_23_14

    try:
        exercice_23_14()
        print("✓ Exercice 23.14: Combinaison - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATIONS EXERCICE 23.15
# =============================================================================

def verifier_exercice_23_15():
    """Vérifie l'exercice 23.15: Tableau de bord."""
    from exercices import exercice_23_15

    try:
        exercice_23_15()
        import os
        if os.path.exists('tableau_de_bord.png'):
            print("✓ Exercice 23.15: Tableau de bord - CORRECT")
        else:
            raise VerificationError("Le fichier n'a pas été créé")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


# =============================================================================
# VÉRIFICATION PRINCIPALE
# =============================================================================

def verifier_tous():
    """Exécute toutes les vérifications."""
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 23: VISUALISATION")
    print("=" * 60)
    print()

    verifications = [
        ("23.1 Premier graphique", verifier_exercice_23_1),
        ("23.2 Diagramme en bâtons", verifier_exercice_23_2),
        ("23.3 Histogramme", verifier_exercice_23_3),
        ("23.4 Nuage de points", verifier_exercice_23_4),
        ("23.5 Diagramme circulaire", verifier_exercice_23_5),
        ("23.6 Sous-graphiques", verifier_exercice_23_6),
        ("23.7 DataFrame plot", verifier_exercice_23_7),
        ("23.8 Personnalisation", verifier_exercice_23_8),
        ("23.9 Multiples séries", verifier_exercice_23_9),
        ("23.10 Boîte à moustaches", verifier_exercice_23_10),
        ("23.11 Sauvegarde", verifier_exercice_23_11),
        ("23.12 Corrélation", verifier_exercice_23_12),
        ("23.13 Styles", verifier_exercice_23_13),
        ("23.14 Combinaison", verifier_exercice_23_14),
        ("23.15 Tableau de bord", verifier_exercice_23_15),
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
        print("ERREUR: Veuillez installer les dépendances d'abord:")
        print("   uv sync --extra core")
        print(f"Détail: {e}")
        sys.exit(1)
