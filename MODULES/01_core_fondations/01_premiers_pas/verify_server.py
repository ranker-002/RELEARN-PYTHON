#!/usr/bin/env python3
"""Serveur de vérification - Chapitre 1: Premiers Pas avec Python.

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
import os
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent

def is_venv_active():
    if sys.prefix == sys.base_prefix:
        return False
    return True

def get_venv_python():
    venv_python = project_root / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return None

if not is_venv_active():
    venv_python = get_venv_python()
    if venv_python and os.path.exists(venv_python):
        os.execv(venv_python, [sys.executable, __file__])

sys.path.insert(0, str(project_root))

from relearn_python.verify_server import run_server

if __name__ == "__main__":
    run_server(port=5000, auto_open=True)
