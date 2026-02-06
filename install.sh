#!/bin/bash

# =============================================================================
# PYTHON MASTERY - Script d'Installation des Dépendances (avec uv)
# =============================================================================
# Ce script installe toutes les dépendances nécessaires pour le projet
# Usage: ./install.sh
# Prérequis: uv doit être installé (https://github.com/astral-sh/uv)
# Installation rapide: curl -LsSf https://astral.sh/uv | sh
# =============================================================================

set -e

echo "🐍 Python Mastery - Installation des dépendances"
echo "================================================"
echo ""

VERT='\033[0;32m'
BLEU='\033[0;34m'
JAUNE='\033[1;33m'
NC='\033[0m'

info() { echo -e "${BLEU}[INFO]${NC} $1"; }
success() { echo -e "${VERT}[OK]${NC} $1"; }
warning() { echo -e "${JAUNE}[ATTENTION]${NC} $1"; }

info "Vérification de uv..."
if ! command -v uv &> /dev/null; then
    warning "uv non trouvé. Installation en cours..."
    curl -LsSf https://astral.sh/uv | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

UV_VERSION=$(uv --version 2>&1)
success "uv installé: $UV_VERSION"

info "Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    warning "Python non trouvé. Veuillez l'installer depuis python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1)
success "Python installé: $PYTHON_VERSION"

info "Création/Synchronisation de l'environnement virtuel..."
uv venv
success "Environnement virtuel prêt"

info "Installation des dépendances..."
uv sync

info "Installation des outils de développement..."
uv sync --extra dev

echo ""
echo "✅ Installation terminée !"
echo "================================================"
echo ""
echo "Pour activer l'environnement virtuel:"
echo ""
echo "  Linux/Mac:  source .venv/bin/activate"
echo "  Windows:     .venv\\Scripts\\activate"
echo ""
echo " puis commencer avec:"
echo "  cd CHAPITRES/01_premiers_pas && cat README.md"
echo ""
echo "Commandes utiles:"
echo "  uv run python script.py        # Exécuter un script"
echo "  uv run pytest                  # Lancer les tests"
echo "  uv run black .                 # Formater le code"
echo "  uv run flake8                  # Vérifier le code"
echo "  uv run mypy                    # Vérifier les types"
echo ""
