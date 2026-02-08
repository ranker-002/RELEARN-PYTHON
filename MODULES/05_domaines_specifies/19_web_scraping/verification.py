#!/usr/bin/env python3
"""
CHAPITRE 21 - Vérification Automatique
"""

import sys


class VerificationError(Exception):
    pass


def verifier_exercice_21_1():
    from exercices import exercice_21_1
    try:
        exercice_21_1()
        print("✓ 21.1: Requête simple - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_2():
    from exercices import exercice_21_2
    try:
        exercice_21_2()
        print("✓ 21.2: Headers personnalisés - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_3():
    from exercices import exercice_21_3
    try:
        exercice_21_3()
        print("✓ 21.3: BeautifulSoup basic - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_4():
    from exercices import exercice_21_4
    try:
        exercice_21_4()
        print("✓ 21.4: Trouver par classe - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_5():
    from exercices import exercice_21_5
    try:
        exercice_21_5()
        print("✓ 21.5: Extraire les liens - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_6():
    from exercices import exercice_21_6
    try:
        exercice_21_6()
        print("✓ 21.6: Sélecteurs CSS - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_7():
    from exercices import exercice_21_7
    try:
        exercice_21_7()
        print("✓ 21.7: Gestion erreurs - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_8():
    from exercices import exercice_21_8
    try:
        exercice_21_8()
        print("✓ 21.8: Paramètres de requête - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_9():
    from exercices import exercice_21_9
    try:
        exercice_21_9()
        print("✓ 21.9: JSON depuis API - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_10():
    from exercices import exercice_21_10
    try:
        exercice_21_10()
        print("✓ 21.10: Plusieurs requêtes - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_11():
    from exercices import exercice_21_11
    try:
        exercice_21_11()
        print("✓ 21.11: Sauvegarder JSON - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_12():
    from exercices import exercice_21_12
    try:
        exercice_21_12()
        print("✓ 21.12: Sauvegarder CSV - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_13():
    from exercices import exercice_21_13
    try:
        exercice_21_13()
        print("✓ 21.13: Tableau HTML vers CSV - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_14():
    from exercices import exercice_21_14
    try:
        exercice_21_14()
        print("✓ 21.14: User-Agent réaliste - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_exercice_21_15():
    from exercices import exercice_21_15
    try:
        exercice_21_15()
        print("✓ 21.15: Scraper complet - CORRECT")
    except Exception as e:
        raise VerificationError(f"Erreur: {e}")


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 21: WEB SCRAPING")
    print("=" * 60)
    
    verifications = [
        ("21.1", verifier_exercice_21_1),
        ("21.2", verifier_exercice_21_2),
        ("21.3", verifier_exercice_21_3),
        ("21.4", verifier_exercice_21_4),
        ("21.5", verifier_exercice_21_5),
        ("21.6", verifier_exercice_21_6),
        ("21.7", verifier_exercice_21_7),
        ("21.8", verifier_exercice_21_8),
        ("21.9", verifier_exercice_21_9),
        ("21.10", verifier_exercice_21_10),
        ("21.11", verifier_exercice_21_11),
        ("21.12", verifier_exercice_21_12),
        ("21.13", verifier_exercice_21_13),
        ("21.14", verifier_exercice_21_14),
        ("21.15", verifier_exercice_21_15),
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
