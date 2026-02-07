"""Package de vérification web pour RELEARN-PYTHON.

Ce package fournit un serveur web FastAPI pour vérifier les exercices
avec une interface moderne style Vercel.
"""

from .server import run_server

__all__ = ["run_server"]
