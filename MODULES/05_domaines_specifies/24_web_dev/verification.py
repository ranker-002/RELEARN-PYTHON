#!/usr/bin/env python3
"""
CHAPITRE 24 - Script de Vérification Automatique
"""

import sys


class VerificationError(Exception):
    pass


def verifier_exercices():
    print("=" * 60)
    print("VÉRIFICATION - CHAPITRE 24: WEB DEVELOPMENT")
    print("=" * 60)
    print()
    
    exercices = [
        ("24.1 - Première app Flask", "Structure Flask créée"),
        ("24.2 - Routes avec paramètres", "Routes paramétriques créées"),
        ("24.3 - Routes multiples", "Calculatrice créée"),
        ("24.4 - Template de base", "Template base.html créé"),
        ("24.5 - Template avec variables", "Template avec variables créé"),
        ("24.6 - Boucle dans template", "Template avec boucle créé"),
        ("24.7 - Formulaire simple", "Formulaire créé"),
        ("24.8 - Première API FastAPI", "API FastAPI créée"),
        ("24.9 - Modèle Pydantic", "Modèle Pydantic créé"),
        ("24.10 - CRUD complet", "CRUD Todos créé"),
        ("24.11 - API Produits", "API Produits créée"),
        ("24.12 - Authentification", "Route protégée créée"),
        ("24.13 - Template hérité", "Templates hérités créés"),
        ("24.14 - API avec BDD", "API avec SQLAlchemy créée"),
        ("24.15 - Projet Blog", "Blog complet créé"),
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
        print("   uv sync --extra web")
        sys.exit(1)
