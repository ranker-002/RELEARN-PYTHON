#!/bin/bash

# =============================================================================
# PYTHON MASTERY - Script d'Installation
# =============================================================================
# Usage: ./install.sh
# =============================================================================

set -e

echo "🐍 Python Mastery - Installation"
echo "================================"

# Vérifier/Installer uv
if ! command -v uv &> /dev/null; then
    echo "[INFO] Installation de uv..."
    curl -LsSf https://astral.sh/uv | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

echo "[INFO] uv version: $(uv --version)"
echo "[INFO] Python: $(python3 --version)"

echo ""
echo "📦 Installation des dépendances..."

uv venv 2>/dev/null || true
uv sync
uv sync --extra dev

echo ""
echo "✅ Installation terminée !"
echo ""
echo "Commandes:"
echo "  just install-dev    # Installer avec outils dev"
echo "  just test           # Lancer les tests"
echo "  just format         # Formatter le code"
echo "  just lint           # Vérifier le code"
echo ""
