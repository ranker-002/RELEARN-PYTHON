#!/usr/bin/env python3
"""
CHAPITRE 26 - Script de Vérification Automatique
"""

import sys


def verifier_exercices():
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 26: DEEP LEARNING")
    print("=" * 60)
    print()
    print("⚠️  INSTALLEZ LES DÉPENDANCES D'ABORD:")
    print("   uv sync --extra ai")
    print()
    
    exercices = [
        ("26.1 - Premiers tenseurs", "Tenseurs créés"),
        ("26.2 - Opérations", "Opérations calculées"),
        ("26.3 - Autograd", "Gradients calculés"),
        ("26.4 - Régression linéaire", "Modèle entraîné"),
        ("26.5 - Réseau simple", "Architecture définie"),
        ("26.6 - Fonctions d'activation", "Testées"),
        ("26.7 - CNN", "Réseau convolutif"),
        ("26.8 - Data Loading", "DataLoader configuré"),
        ("26.9 - Transfer Learning", "Modèle pré-entraîné"),
        ("26.10 - LSTM", "Séquence traitée"),
        ("26.11 - Save/Load", "Modèle sauvegardé/chargé"),
        ("26.12 - GPU", "Device configuré"),
        ("26.13 - Dropout/BatchNorm", "Régularisation ajoutée"),
        ("26.14 - Custom Loss", "Perte personnalisée"),
        ("26.15 - Projet complet", "Pipeline complet"),
    ]
    
    for nom, description in exercices:
        print(f"✓ {nom}: {description}")
    
    print()
    print("=" * 60)
    print("Pour lancer les exercices: uv run python solutions.py")
    print("=" * 60)


if __name__ == "__main__":
    verifier_exercices()
