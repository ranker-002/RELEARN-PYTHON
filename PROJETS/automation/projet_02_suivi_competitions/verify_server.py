#!/usr/bin/env python3
"""
Suivi de Compétitions E-sport - Serveur de Vérification Web
Lance une interface web pour valider votre projet.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from relearn_python.verify_server import run_server

if __name__ == "__main__":
    print(f"\n=== Suivi de Compétitions E-sport ===")
    print("Interface: http://localhost:5000\n")
    try:
        run_server(port=5000, auto_open=True, project_path=Path(__file__).parent)
    except KeyboardInterrupt:
        print("\nArrêté.")
