#!/usr/bin/env python3
"""
Classification Multi-classes - Serveur de Vérification Web
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
║  Classification Multi-classes                         ║
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
    print(f"\n=== Classification Multi-classes ===")
    print("Interface: http://localhost:5000\n")
    try:
        run_server(port=5000, auto_open=True, project_path=Path(__file__).parent)
    except KeyboardInterrupt:
        print("\nArrêté.")
