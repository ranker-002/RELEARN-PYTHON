#!/usr/bin/env python3
"""
Sauvegarde Automatique avec Versioning - Solutions Commentées
======================================
⚠️  Regardez SEULEMENT après avoir tenté le projet!

Emplacement de la solution: solution/src/
"""


class Solution:
    """Classe de référence pour la solution complète."""
    
    def __init__(self):
        self.project_name = "Sauvegarde Automatique avec Versioning"
        self.module = "robustesse_fichiers"
    
    def run(self):
        """Exécute la solution complète."""
        from solution.src.main import Projet02SauvegardeAutomatiqueApplication
        app = Projet02SauvegardeAutomatiqueApplication()
        app.run()


if __name__ == "__main__":
    print(f"""
=== Sauvegarde Automatique avec Versioning ===
⚠️  Solutions dans: solution/src/

Conseils:
1. Tentez le projet par vous-même d'abord
2. Utilisez verification.py pour vérifier votre avancement
3. Consultez les solutions uniquement en dernier recours
    """)
