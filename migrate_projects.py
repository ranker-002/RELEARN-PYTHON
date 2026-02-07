#!/usr/bin/env python3
"""
Script de migration pour les PROJETS RELEARN-PYTHON
Migre les projets vers le nouveau format avec validation intégrée.

Usage:
    python migrate_projects.py --list           # Liste les projets
    python migrate_projects.py --dry-run        # Simulation
    python migrate_projects.py [module]         # Migrer un module
    python migrate_projects.py                  # Tout migrer
"""

import sys
import shutil
from pathlib import Path
from typing import List, Dict, Tuple


def list_projects():
    """Liste tous les projets."""
    base = Path(__file__).parent / "PROJETS"
    print("\n=== PROJETS RELEARN-PYTHON ===\n")
    
    for module_dir in sorted(base.iterdir()):
        if not module_dir.is_dir() or module_dir.name.startswith('.'):
            continue
        
        print(f"📁 {module_dir.name}")
        for project_dir in sorted(module_dir.iterdir()):
            if project_dir.is_dir():
                status = "✅" if (project_dir / "src").exists() else "⚠️"
                print(f"   {status} {project_dir.name}")
        print()
    
    print(f"Dossier: {base}")
    print(f"Modules: {len([d for d in base.iterdir() if d.is_dir()])}")


def create_verification_py(info: dict) -> str:
    """Crée verification.py"""
    project_name = info['slug'].replace('_', ' ').title().replace(' ', '')
    
    return f'''#!/usr/bin/env python3
"""
{info['name']} - Vérification Automatique
{'=' * 50}
Vérifie que votre projet est complet et fonctionnel.

Usage: python verification.py
"""

import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))


def verifier(msg: str, test_func) -> bool:
    """Exécute un test et affiche le résultat."""
    try:
        result = test_func()
        print(f"✓ {{msg}}")
        return result if result is not None else True
    except Exception as e:
        print(f"✗ {{msg}}: {{e}}")
        return False


def test_structure() -> bool:
    """Vérifie la structure des dossiers."""
    required = ["src", "src/models", "src/services", "src/utils", "tests", "data"]
    return all((Path(__file__).parent / d).exists() for d in required)


def test_import() -> bool:
    """Vérifie l'import du module principal."""
    from src.main import {project_name}Application
    app = {project_name}Application()
    return True


def test_execution() -> bool:
    """Vérifie que le code s'exécute."""
    result = subprocess.run(
        ["python", "-c", "from src.main import *; print('OK')"],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent),
        timeout=10
    )
    return result.returncode == 0 and "OK" in result.stdout


def run():
    """Exécute toutes les vérifications."""
    print(f"\\n=== Vérification: {info['name']} ===\\n")
    
    tests = [
        ("Structure", test_structure),
        ("Import principal", test_import),
        ("Exécution", test_execution),
    ]
    
    passed = sum(1 for name, t in tests if verifier(name, t))
    
    print(f"\\n=== Résultat: {{passed}}/{{len(tests)}} ===\\n")
    if passed == len(tests):
        print("🎉 Projet validé!\\n")
    else:
        print(f"⚠️  {{len(tests) - passed}} test(s) en échec.\\n")


if __name__ == "__main__":
    run()
'''


def create_verify_server_py(info: dict) -> str:
    """Crée verify_server.py"""
    return f'''#!/usr/bin/env python3
"""
{info['name']} - Serveur de Vérification Web
Lance une interface web pour valider votre projet.

Note: FastAPI requis. Installez avec: uv sync --extra web
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from relearn_python.verify_server import run_server
except ImportError:
    print(f"""
╔══════════════════════════════════════════════════════════╗
║  {info['name']}                         ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  ⚠️  FastAPI non installé                                ║
║                                                          ║
║  Pour accéder à l'interface web:                          ║
║      uv sync --extra web                                 ║
║      python verify_server.py                             ║
║                                                          ║
║  Alternative: utilisez verification.py en ligne de commande║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    sys.exit(0)

if __name__ == "__main__":
    print(f"\\n=== {info['name']} ===")
    print("Interface: http://localhost:5000\\n")
    try:
        run_server(port=5000, auto_open=True, project_path=Path(__file__).parent)
    except KeyboardInterrupt:
        print("\\nArrêté.")
'''


def create_solutions_py(info: dict) -> str:
    """Crée solutions.py"""
    project_name = info['slug'].replace('_', ' ').title().replace(' ', '')
    
    return f'''#!/usr/bin/env python3
"""
{info['name']} - Solutions Commentées
======================================
⚠️  Regardez SEULEMENT après avoir tenté le projet!

Emplacement de la solution: solution/src/
"""


class Solution:
    """Classe de référence pour la solution complète."""
    
    def __init__(self):
        self.project_name = "{info['name']}"
        self.module = "{info['module']}"
    
    def run(self):
        """Exécute la solution complète."""
        from solution.src.main import {project_name}Application
        app = {project_name}Application()
        app.run()


if __name__ == "__main__":
    print(f"""
=== {info['name']} ===
⚠️  Solutions dans: solution/src/

Conseils:
1. Tentez le projet par vous-même d'abord
2. Utilisez verification.py pour vérifier votre avancement
3. Consultez les solutions uniquement en dernier recours
    """)
'''


def create_src_files(base_path: Path, info: dict):
    """Crée la structure src/ avec scaffold."""
    project_name = info['slug'].replace('_', ' ').title().replace(' ', '')
    
    # Créer les dossiers
    for subdir in ["models", "services", "utils"]:
        dir_path = base_path / "src" / subdir
        dir_path.mkdir(parents=True, exist_ok=True)
        (dir_path / "__init__.py").write_text('"""Package {{subdir}}."""\n')
    
    # Créer __init__.py principal
    (base_path / "src" / "__init__.py").write_text(f'"""Package {info["slug"]}."""\n\n__version__ = "1.0.0"\n')
    
    # Créer main.py
    main_content = f'''#!/usr/bin/env python3
"""
{info['name']}
Usage: python src/main.py
"""

from typing import Optional


class {project_name}Application:
    """Application principale pour {info['name']}."""
    
    def __init__(self, config: Optional[dict] = None):
        self.config = config or {{}}
        self.setup()
    
    def setup(self):
        """Configuration initiale."""
        print(f"Démarrage de {info['name']}...")
    
    def run(self):
        """Point d'entrée principal."""
        self.setup()
        print("TODO: Implémenter la logique du projet")


if __name__ == "__main__":
    app = {project_name}Application()
    app.run()
'''
    (base_path / "src" / "main.py").write_text(main_content)


def create_test_files(base_path: Path):
    """Crée les fichiers de tests."""
    tests_dir = base_path / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)
    
    (tests_dir / "__init__.py").write_text('"""Tests package."""\n')
    
    conftest = '''"""Pytest configuration."""
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

@pytest.fixture
def app():
    """Fixture pour l'application."""
    from src.main import Application
    return Application()
'''
    (tests_dir / "conftest.py").write_text(conftest)
    
    test_main = '''"""Tests pour main.py."""
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


class TestMain:
    def test_import(self):
        """Test que le module s'importe."""
        from src.main import Application
        assert Application is not None
    
    def test_initialization(self):
        """Test l'initialisation."""
        from src.main import Application
        app = Application()
        assert app is not None
'''
    (tests_dir / "test_main.py").write_text(test_main)


def create_data_files(base_path: Path):
    """Crée les dossiers data/."""
    for subdir in ["sample", "input"]:
        dir_path = base_path / "data" / subdir
        dir_path.mkdir(parents=True, exist_ok=True)
        (dir_path / ".gitkeep").write_text('')


def create_solution_structure(base_path: Path):
    """Crée la structure solution/ vide."""
    sol_dir = base_path / "solution" / "src"
    for subdir in ["", "models", "services", "utils"]:
        (sol_dir / subdir).mkdir(parents=True, exist_ok=True)
        if subdir:
            (sol_dir / subdir / "__init__.py").write_text('"""Solution package."""\n')


def create_requirements(base_path: Path, module: str):
    """Crée requirements.txt."""
    content = f"""# {base_path.name}
# Install: uv sync --extra {module.replace('_', '-')}

-r ../../requirements.txt

# Dépendances spécifiques au projet
"""
    (base_path / "requirements.txt").write_text(content)


def create_env_example(base_path: Path):
    """Crée .env.example."""
    content = """# Variables d'environnement
# Copiez ce fichier vers .env et remplissez les valeurs

# Configuration
DEBUG=false
LOG_LEVEL=INFO

# API (si nécessaire)
# API_KEY=votre_cle
# API_URL=https://api.exemple.com

# Base de données (si nécessaire)
# DATABASE_URL=postgresql://user:pass@localhost:5432/db
"""
    (base_path / ".env.example").write_text(content)


def migrate_project(project_path: Path, dry_run: bool = False) -> Tuple[bool, dict]:
    """Migre un projet."""
    readme_path = project_path / "README.md"
    if not readme_path.exists():
        return False, {"error": "README.md manquant"}
    
    # Extraire les infos du README
    content = readme_path.read_text(encoding='utf-8')
    
    # Parser les métadonnées
    import re
    name_match = re.search(r'^#\s*(?:Projet|Project):\s*(.+)$', content, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else project_path.name
    
    diff_match = re.search(r'\*\*([^*]+)\*\*', content)
    difficulty = diff_match.group(1).strip() if diff_match else "Intermediate"
    
    hours_match = re.search(r'(\d+[-\d]*)\s*heures?', content)
    hours = hours_match.group(1) if hours_match else "4-6"
    
    info = {
        'name': name,
        'slug': project_path.name,
        'module': project_path.parent.name,
        'difficulty': difficulty,
        'hours': hours,
    }
    
    changes = {
        'src': False,
        'tests': False,
        'data': False,
        'solution': False,
        'requirements': False,
        'env': False,
        'verification': False,
        'verify_server': False,
        'solutions': False,
    }
    
    if dry_run:
        print(f"  [DRY RUN] {info['name']}")
        return True, changes
    
    # Créer les fichiers
    if not (project_path / "src").exists():
        create_src_files(project_path, info)
        changes['src'] = True
    
    if not (project_path / "tests").exists():
        create_test_files(project_path)
        changes['tests'] = True
    
    if not (project_path / "data").exists():
        create_data_files(project_path)
        changes['data'] = True
    
    if not (project_path / "solution").exists():
        create_solution_structure(project_path)
        changes['solution'] = True
    
    # Fichiers toujours recréés/mis à jour
    create_requirements(project_path, info['module'])
    changes['requirements'] = True
    
    create_env_example(project_path)
    changes['env'] = True
    
    verif_py = project_path / "verification.py"
    if not verif_py.exists() or verif_py.stat().st_mtime < readme_path.stat().st_mtime:
        verif_py.write_text(create_verification_py(info))
        changes['verification'] = True
    
    vs_py = project_path / "verify_server.py"
    if not vs_py.exists() or vs_py.stat().st_mtime < readme_path.stat().st_mtime:
        vs_py.write_text(create_verify_server_py(info))
        changes['verify_server'] = True
    
    sol_py = project_path / "solutions.py"
    if not sol_py.exists() or sol_py.stat().st_mtime < readme_path.stat().st_mtime:
        sol_py.write_text(create_solutions_py(info))
        changes['solutions'] = True
    
    # Afficher les changements
    created = [k for k, v in changes.items() if v]
    if created:
        print(f"  ✅ {info['name']}")
        print(f"     Créés: {', '.join(created)}")
    
    return True, changes


def migrate_all(module_filter: str | None = None, dry_run: bool = False):
    """Migre tous les projets."""
    base = Path(__file__).parent / "PROJETS"
    
    print(f"\n{'='*60}")
    if dry_run:
        print("🔍 MODE SIMULATION - Aucun changement ne sera effectué")
    else:
        print("🚀 Migration des PROJETS")
    print(f"{'='*60}\n")
    
    total = migrated = 0
    
    for module_dir in sorted(base.iterdir()):
        if not module_dir.is_dir() or module_dir.name.startswith('.'):
            continue
        
        if module_filter and module_dir.name != module_filter:
            continue
        
        for project_dir in sorted(module_dir.iterdir()):
            if not project_dir.is_dir():
                continue
            
            total += 1
            success, _ = migrate_project(project_dir, dry_run=dry_run)
            if success:
                migrated += 1
    
    print(f"\n{'='*60}")
    print(f"📊 Résultat: {migrated}/{total} projets traités")
    if dry_run:
        print("⚠️  Simulation - aucun fichier créé")
    print(f"{'='*60}\n")


def main():
    """Point d'entrée."""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg == '--list':
            list_projects()
            return
        
        if arg == '--dry-run':
            migrate_all(dry_run=True)
            return
        
        # Vérifier si c'est un nom de module
        module_path = Path(__file__).parent / "PROJETS" / arg
        if module_path.exists():
            migrate_all(module_filter=arg)
            return
    
    migrate_all(dry_run=False)


if __name__ == "__main__":
    main()
