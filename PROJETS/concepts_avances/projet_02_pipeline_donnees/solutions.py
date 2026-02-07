#!/usr/bin/env python3
"""
Pipeline de Données Concurrent - Solutions Commentées
======================================
⚠️  Regardez SEULEMENT après avoir tenté le projet!

Emplacement de la solution: solution/src/
"""


class Solution:
    """Classe de référence pour la solution complète."""
    
    def __init__(self):
        self.project_name = "Pipeline de Données Concurrent"
        self.module = "concepts_avances"
    
    def run(self):
        """Exécute la solution complète."""
        from solution.src.main import Projet02PipelineDonneesApplication
        app = Projet02PipelineDonneesApplication()
        app.run()


if __name__ == "__main__":
    print(f"""
=== Pipeline de Données Concurrent ===
⚠️  Solutions dans: solution/src/

Conseils:
1. Tentez le projet par vous-même d'abord
2. Utilisez verification.py pour vérifier votre avancement
3. Consultez les solutions uniquement en dernier recours
    """)
