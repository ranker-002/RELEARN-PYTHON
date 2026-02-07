#!/usr/bin/env python3
"""
Script pour créer les scaffolds complets pour tous les projets.
Applique la structure de l'agrégateur RSS aux autres projets.
"""

from pathlib import Path
import subprocess
import os


def create_complete_scaffold():
    """Crée les scaffolds pour tous les projets."""
    base = Path(__file__).parent / "PROJETS"
    
    print("\n=== Création des scaffolds ===\n")
    
    for module_dir in sorted(base.iterdir()):
        if not module_dir.is_dir():
            continue
        
        for project_dir in sorted(module_dir.iterdir()):
            if not project_dir.is_dir():
                continue
            
            src_dir = project_dir / "src"
            if not src_dir.exists():
                continue
            
            # Skip le projet déjà fait
            if "aggregateur_actualites" in project_dir.name:
                print(f"⏭️  {project_dir.name} (déjà fait)")
                continue
            
            create_scaffold_for_project(project_dir, module_dir.name)
            print(f"✅ {project_dir.name}")
    
    print("\n=== Terminé ===\n")


def create_scaffold_for_project(project_dir: Path, module_name: str):
    """Crée le scaffold pour un projet."""
    src_dir = project_dir / "src"
    
    # Créer main.py avec scaffold complet
    main_py = src_dir / "main.py"
    
    scaffold = f'''#!/usr/bin/env python3
"""
{project_dir.name}

Projet du module {module_name}.

Usage:
    python src/main.py                    # Mode interactif
    python src/main.py --help            # Aide
"""

import sys
from pathlib import Path
from typing import Optional, List
from datetime import datetime


class Colors:
    RESET = "\\033[0m"
    BOLD = "\\033[1m"
    BLUE = "\\033[94m"
    GREEN = "\\033[92m"
    YELLOW = "\\033[93m"
    RED = "\\033[91m"


class {project_dir.name.replace('_', ' ').title().replace(' ', '')}:
    """Application principale."""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        """Initialise l'application."""
        self.logger = self._setup_logging()
        self.logger.info(f"Application initialisée")
    
    def _setup_logging(self):
        """Configure le logging."""
        import logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("{module_name}")
    
    def _afficher_banniere(self):
        """Affiche la bannière."""
        print(f"\\n{{Colors.BOLD}}{{Colors.BLUE}}")
        print(f"╔══════════════════════════════════════════════════╗")
        print(f"║        {project_dir.name[:40]:^40} ║")
        print(f"╚══════════════════════════════════════════════════╝")
        print(f"{{Colors.RESET}}")
    
    def run(self):
        """Point d'entrée."""
        self._afficher_banniere()
        print("\\nTODO: Implémenter la logique du projet")


def main():
    """Point d'entrée."""
    app = {project_dir.name.replace('_', ' ').title().replace(' ', '')}()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\\n\\n👋 Au revoir!")
    except Exception as e:
        print(f"\\n{{Colors.RED}}Erreur: {{e}}{{Colors.RESET}}")


if __name__ == "__main__":
    main()
'''
    
    main_py.write_text(scaffold, encoding='utf-8')
    
    # Créer models/__init__.py
    models_init = project_dir / "src" / "models" / "__init__.py"
    models_init.write_text('"""Models package."""\n\n__all__ = []\n', encoding='utf-8')
    
    # Créer services/__init__.py
    services_init = project_dir / "src" / "services" / "__init__.py"
    services_init.write_text('"""Services package."""\n\n__all__ = []\n', encoding='utf-8')
    
    # Créer utils/__init__.py
    utils_init = project_dir / "src" / "utils" / "__init__.py"
    utils_init.write_text('"""Utils package."""\n\n__all__ = []\n', encoding='utf-8')


def update_verification_scripts():
    """Met à jour les scripts de vérification."""
    base = Path(__file__).parent / "PROJETS"
    
    for module_dir in sorted(base.iterdir()):
        if not module_dir.is_dir():
            continue
        
        for project_dir in sorted(module_dir.iterdir()):
            if not project_dir.is_dir():
                continue
            
            verif_py = project_dir / "verification.py"
            if not verif_py.exists():
                continue
            
            # Lire et mettre à jour
            content = verif_py.read_text()
            
            # Corriger test_execution
            if "PYTHONPATH" not in content:
                new_content = content.replace(
                    'def test_execution():',
                    '''def test_execution():
    import os'''
                )
                new_content = new_content.replace(
                    'capture_output=True,',
                    '''capture_output=True,
        cwd=str(Path(__file__).parent / "src"),'''
                )
                new_content = new_content.replace(
                    'timeout=10',
                    '''timeout=10,
        env={**os.environ, "PYTHONPATH": str(Path(__file__).parent / "src")}'''
                )
                verif_py.write_text(new_content)


if __name__ == "__main__":
    create_complete_scaffold()
    update_verification_scripts()
