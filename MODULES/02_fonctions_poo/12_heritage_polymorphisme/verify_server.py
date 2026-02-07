#!/usr/bin/env python3
"""Serveur de vérification - Interface web moderne pour les exercices.

Lance un serveur web local pour vérifier les exercices avec une interface
moderne et intuitive.

Utilisation:
    python verify_server.py
    # ou
    uv run python verify_server.py

Le serveur démarre sur http://localhost:5000 et s'ouvre automatiquement
dans le navigateur par défaut.
"""
import sys
from pathlib import Path

# Ajouter le package relearn_python au path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from relearn_python.verify_server import run_server

if __name__ == "__main__":
    run_server(port=5000, auto_open=True)
