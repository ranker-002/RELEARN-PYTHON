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
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"

    # Activer uv pour la session courante
    for env_file in "$HOME/.local/bin/env" "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
        if [ -f "$env_file" ]; then
            source "$env_file" 2>/dev/null || true
        fi
    done
fi

echo "[INFO] uv version: $(uv --version)"
echo "[INFO] Python: $(python3 --version)"

echo ""
echo "📦 Installation des dépendances..."

uv venv 2>/dev/null || true

echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "                    CHOIX D'INSTALLATION"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "📖 PHASE 1-4: FONDATIONS & STRUCTURES (aucune dépendance externe)"
echo "   └── Inclus par défaut"
echo ""
echo "📊 PHASE 5-6: FICHIERS & CONCEPTS AVANCÉS"
echo "   └── Inclus par défaut"
echo ""
echo "🌐 PHASE 7: DOMAINES SPÉCIALISÉS"
echo ""
echo "   [1] 📊 Data Science         → numpy, pandas, matplotlib (chapitres 22-23)"
echo "       Utilisation: uv sync --extra core"
echo ""
echo "   [2] 🕸️  Web Dev              → flask, fastapi, jinja2, uvicorn (chapitre 24)"
echo "       Utilisation: uv sync --extra web"
echo ""
echo "   [3] 🤖 Automation           → beautifulsoup4, selenium, webdriver-manager (chapitres 20-21)"
echo "       Utilisation: uv sync --extra automation"
echo ""
echo "   [4] 📈 Machine Learning     → scikit-learn, openpyxl, pillow (chapitre 25)"
echo "       Utilisation: uv sync --extra data"
echo ""
echo "   [5] 🧠 Deep Learning        → torch, torchvision (chapitre 26)"
echo "       ⚠️  TRÈS LOURD (~1GB)"
echo "       Utilisation: uv sync --extra ai"
echo ""
echo "   [6] 🔧 Outils Dev           → pytest, black, ruff"
echo "       Utilisation: uv sync --extra dev"
echo ""
echo "   [7] ✅ TOUT INSTALLER       → Toutes les dépendances"
echo "       ⚠️  TRÈS LONG (~2-5 GB)"
echo ""
echo "   [8] ❌ MINIMUM              → Aucune dépendance optionnelle"
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo ""
read -p "Votre choix [1-8]: " choix

case $choix in
    1) echo ""; echo "Installation de Data Science..."; uv sync --extra core ;;
    2) echo ""; echo "Installation de Web Dev..."; uv sync --extra web ;;
    3) echo ""; echo "Installation de Automation..."; uv sync --extra automation ;;
    4) echo ""; echo "Installation de Machine Learning..."; uv sync --extra data ;;
    5) echo ""; echo "Installation de Deep Learning (ceci peut prendre plusieurs minutes)..."; uv sync --extra ai ;;
    6) echo ""; echo "Installation des outils de développement..."; uv sync --extra dev ;;
    7) echo ""; echo "Installation complète (toutes les dépendances)..."; uv sync --extra core --extra web --extra automation --extra data --extra ai ;;
    8) echo ""; echo "Installation minimale uniquement..."; uv sync ;;
    *) echo "Choix invalide, installation minimale uniquement"; uv sync ;;
esac

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "✅ Installation terminée !"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "📌 COMMANDES UTILES:"
echo ""
echo "   just install-dev    # Installer avec outils dev"
echo "   just test           # Lancer les tests"
echo "   just format         # Formatter le code"
echo "   just lint           # Vérifier le code"
echo "   just check          # Vérification complète"
echo ""
echo "   uv run python fichier.py     # Exécuter un script"
echo ""
echo "═══════════════════════════════════════════════════════════════════"
