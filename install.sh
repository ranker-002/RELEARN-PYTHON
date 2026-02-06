#!/bin/bash

# =============================================================================
# PYTHON MASTERY - Script d'Installation des Dépendances
# =============================================================================
# Ce script installe toutes les dépendances nécessaires pour le projet
# Usage: ./install.sh
# =============================================================================

set -e  # Arrêter en cas d'erreur

echo "🐍 Python Mastery - Installation des dépendances"
echo "================================================"
echo ""

# Couleurs pour l'affichage
VERT='\033[0;32m'
BLEU='\033[0;34m'
JAUNE='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour afficher les messages
info() { echo -e "${BLEU}[INFO]${NC} $1"; }
success() { echo -e "${VERT}[OK]${NC} $1"; }
warning() { echo -e "${JAUNE}[ATTENTION]${NC} $1"; }

# Vérification de Python
info "Vérification de Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    success "Python installé: $PYTHON_VERSION"
else
    warning "Python non trouvé. Veuillez l'installer depuis python.org"
    exit 1
fi

# Mise à jour de pip
info "Mise à jour de pip..."
python3 -m pip install --upgrade pip
success "pip à jour"

# Création de l'environnement virtuel
info "Création de l'environnement virtuel..."
if [ -d "venv" ]; then
    warning "L'environnement virtuel existe déjà"
else
    python3 -m venv venv
    success "Environnement virtuel créé"
fi

# Activation et installation
info "Activation de l'environnement virtuel..."
source venv/bin/activate
success "Environnement virtuel activé"

echo ""
echo "📦 Installation des dépendances..."
echo "=================================="

# Phase 1-4: Core - Fondations
echo ""
info "Installation des packages Core..."
pip install --quiet numpy pandas matplotlib

# Phase 5-6: Avancé - Outils de développement
echo ""
info "Installation des outils de développement..."
pip install --quiet pytest black flake8 mypy

# Phase 7: Spécialisations - Web & Automation
echo ""
info "Installation des packages Web & Automation..."
pip install --quiet requests beautifulsoup4 selenium webdriver-manager

# Phase 7: Spécialisations - Data Science & ML
echo ""
info "Installation des packages Data Science & ML..."
pip install --quiet scikit-learn torch torchvision

# Phase 7: Spécialisations - Web Dev
echo ""
info "Installation des packages Web Dev..."
pip install --quiet flask fastapi uvicorn jinja2

# Phase 7: Spécialisations - Autres outils
echo ""
info "Installation des outils supplémentaires..."
pip install --quiet openpyxl pillow pyyaml tabulate tqdm

# Nettoyage
pip install --quiet --upgrade pip setuptools wheel 2>/dev/null || true

echo ""
echo "✅ Installation terminée !"
echo "================================================"
echo ""
echo "Prochaine étape: Activer l'environnement virtuel"
echo ""
echo "  Linux/Mac:  source venv/bin/activate"
echo "  Windows:     .\\venv\\Scripts\\activate"
echo ""
echo " puis commencer avec:"
echo "  cd CHAPITRES/01_premiers_pas && cat README.md"
echo ""
