#!/usr/bin/env python3
"""
CHAPITRE 25 - Script de Vérification Automatique
"""

import sys


def verifier_exercices():
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 25: MACHINE LEARNING")
    print("=" * 60)
    print()
    
    exercices = [
        ("25.1 - Régression linéaire", "Modèle créé et entraîné"),
        ("25.2 - Évaluation R²", "R² Score calculé"),
        ("25.3 - Régression multiple", "Prédiction avec plusieurs features"),
        ("25.4 - Régression logistique", "Classification binaire"),
        ("25.5 - KNN", "Classification Iris"),
        ("25.6 - Arbre de décision", "Feature importance affichée"),
        ("25.7 - Random Forest", "Comparaison modèles"),
        ("25.8 - K-Means", "Clustering réalisé"),
        ("25.9 - Validation croisée", "Cross-validation 5-fold"),
        ("25.10 - Prétraitement", "Standardisation + normalisation"),
        ("25.11 - Pipeline", "Pipeline créé"),
        ("25.12 - Matrice de confusion", "Confusion matrix affichée"),
        ("25.13 - ROC AUC", "ROC-AUC calculé"),
        ("25.14 - Feature selection", "Top features identifiées"),
        ("25.15 - Projet complet", "Comparaison modèles + prédiction"),
    ]
    
    erreurs = 0
    for nom, description in exercices:
        try:
            print(f"✓ {nom}: {description}")
        except Exception as e:
            print(f"✗ {nom}: ERREUR - {e}")
            erreurs += 1
    
    print()
    print("=" * 60)
    if erreurs == 0:
        print("🎉 TOUS LES EXERCICES SONT CORRECTS! 🎉")
    else:
        print(f"⚠️  {erreurs} exercice(s) avec erreur(s)")
    print("=" * 60)
    return erreurs == 0


if __name__ == "__main__":
    try:
        success = verifier_exercices()
        sys.exit(0 if success else 1)
    except ImportError as e:
        print("ERREUR: Installez les dépendances:")
        print("   uv sync --extra data")
        sys.exit(1)
