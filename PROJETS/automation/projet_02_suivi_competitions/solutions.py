#!/usr/bin/env python3
"""
Suivi de Compétitions E-sport - Solutions Commentées
======================================
⚠️  Regardez SEULEMENT après avoir tenté le projet!

Emplacement de la solution: solution/src/
"""


class Solution:
    """Classe de référence pour la solution complète."""
    
    def __init__(self):
        self.project_name = "Suivi de Compétitions E-sport"
        self.module = "automation"
    
    def run(self):
        """Exécute la solution complète."""
        from solution.src.main import Projet02SuiviCompetitionsApplication
        app = Projet02SuiviCompetitionsApplication()
        app.run()


if __name__ == "__main__":
    print(f"""
=== Suivi de Compétitions E-sport ===
⚠️  Solutions dans: solution/src/

Conseils:
1. Tentez le projet par vous-même d'abord
2. Utilisez verification.py pour vérifier votre avancement
3. Consultez les solutions uniquement en dernier recours
    """)
