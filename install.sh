#!/bin/bash

# =============================================================================
# RELEARN PYTHON - Script d'Installation
# =============================================================================
# Usage: ./install.sh
# =============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
PURPLE='\033[0;35m'
PINK='\033[38;5;205m'
GRAY='\033[0;90m'
LIGHT_GREEN='\033[1;32m'
VIOLET_BLUE='\033[38;5;141m'
RESET='\033[0m'

# Logo RE:PY
LOGO="
   ${LIGHT_GREEN}██████╗ ███████╗${RESET}${WHITE}╗${RESET}${VIOLET_BLUE}██████╗ ██╗   ██╗${RESET}
   ${LIGHT_GREEN}██╔══██╗██╔════╝${RESET}${WHITE}║${RESET}${VIOLET_BLUE}██╔══██╗╚██╗ ██╔╝${RESET}
   ${LIGHT_GREEN}██████╔╝█████╗  ${RESET}${WHITE}:${RESET}${VIOLET_BLUE}██████╔╝ ╚████╔╝ ${RESET}
   ${LIGHT_GREEN}██╔══██╗██╔══╝  ${RESET}${WHITE}║${RESET}${VIOLET_BLUE}██╔═══╝   ╚██╔╝  ${RESET}
   ${LIGHT_GREEN}██║  ██║███████╗${RESET}${WHITE}╝${RESET}${VIOLET_BLUE}██║        ██║   ${RESET}
   ${LIGHT_GREEN}╚═╝  ╚═╝╚══════╝${RESET}${WHITE} ${RESET}${VIOLET_BLUE}╚═╝        ╚═╝   ${RESET}
"

# Print functions
print_header() {
    clear
    echo -e "${LOGO}"
    echo -e "${PURPLE}╔════════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${PURPLE}║${RESET}       ${WHITE}Apprentissage progressif et complet${RESET}           ${PURPLE}║${RESET}"
    echo -e "${PURPLE}╚════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
}

print_step() {
    local num=$1
    local msg=$2

    echo -e "   ${CYAN}▓${RESET}${GREEN}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░${RESET} ${WHITE}${BOLD}$msg${RESET}"
}

print_success() {
    echo -e "   ${GREEN}✓${RESET} ${GREEN}$1${RESET}"
}

print_info() {
    echo -e "   ${BLUE}›${RESET} $1"
}

print_menu_item() {
    local num=$1
    local icon=$2
    local label=$3
    local desc=$4
    printf "   ${WHITE}%2s${RESET}  %s ${WHITE}%s${RESET}   ${DIM}%s${RESET}\n" "$num" "$icon" "$label" "$desc"
}

print_divider() {
    echo ""
    echo -e "${GRAY}────────────────────────────────────────────────────────────────────────${RESET}"
    echo ""
}

# Main
main() {
    print_header

    echo -e "${WHITE}${BOLD} PREPARATION ${RESET}"
    echo ""

    # Step 0: uv
    print_step "0" "Vérification de uv"
    if ! command -v uv &> /dev/null; then
        print_info "Installation de uv..."
        curl -LsSf https://astral.sh/uv/install.sh  | sh > /dev/null 2>&1
        export PATH="$HOME/.local/bin:$PATH"
        print_success "uv installé"
    else
        print_success "uv $(uv --version | cut -d' ' -f2)"
    fi

    # Step 1: Python
    echo ""
    print_step "1" "Vérification de Python"
    local py_version=$(python3 --version 2>&1 | cut -d' ' -f2)
    print_success "Python $py_version"

    # Step 2: venv
    echo ""
    print_step "2" "Configuration du virtual environment"

    if [ -d ".venv" ]; then
        print_info "Un venv existe déjà"
        read -p "   Recréer ? [o/N]: " recreate
        if [[ "$recreate" =~ ^[oO]$ ]]; then
            rm -rf .venv
            uv venv .venv
            print_success "Virtual environment recréé"
        else
            print_success "Conservation du venv existant"
        fi
    else
        uv venv .venv
        print_success "Virtual environment créé"
    fi

    # Step 3: sync
    echo ""
    print_step "3" "Synchronisation des dépendances"

    print_divider

    echo -e "${WHITE}┌──────────────────────────────────────────────────────────────────┐${RESET}"
    echo -e "${WHITE}│${RESET}                     ${WHITE}${BOLD}INSTALLATION${RESET}                              ${WHITE}│${RESET}"
    echo -e "${WHITE}└──────────────────────────────────────────────────────────────────┘${RESET}"
    echo ""

    print_menu_item "1" "📊" "Data Science" "numpy, pandas, matplotlib"
    print_menu_item "2" "🌐" "Web Dev" "flask, fastapi, uvicorn"
    print_menu_item "3" "🤖" "Automation" "beautifulsoup4, selenium"
    print_menu_item "4" "📈" "Machine Learning" "scikit-learn, pillow"
    print_menu_item "5" "🧠" "Deep Learning" "torch, torchvision (~1.5 GB)"
    print_menu_item "6" "🔧" "Dev Tools" "pytest, black, ruff"
    echo ""
    print_menu_item "7" "✨" "TOUT INSTALLER" "Toutes les dépendances"
    print_menu_item "8" "⚡" "MINIMAL" "fastapi + dépendances de base"

    echo ""
    echo -e "   ${PINK}┌──────────────────────────────────────────────────────────────────┐${RESET}"
    echo -e "   ${PINK}│${RESET}  ${WHITE}Choisissez [1-8]${RESET}                                          ${PINK}│${RESET}"
    echo -e "   ${PINK}└──────────────────────────────────────────────────────────────────┘${RESET}"
    echo -ne "   ${CYAN}›${RESET}  "
    read choix

    echo ""

    case $choix in
        1) extra="core"; name="Data Science" ;;
        2) extra="web"; name="Web Development" ;;
        3) extra="automation"; name="Automation" ;;
        4) extra="data"; name="Machine Learning" ;;
        5) extra="ai"; name="Deep Learning" ;;
        6) extra="dev"; name="Dev Tools" ;;
        7) extra="core web automation data ai"; name="Installation complète" ;;
        8|"") extra="web"; name="Configuration minimale" ;;
        *) extra=""; name="Configuration minimale" ;;
    esac

    echo -e "   ${WHITE}›${RESET} ${BOLD}$name${RESET}"

    if [ -z "$extra" ]; then
        uv sync
    else
        # Installer core d'abord, puis les autres
        uv sync --extra core
        for e in $extra; do
            if [ "$e" != "core" ]; then
                uv pip install -e ".[$e]"
            fi
        done
    fi

    print_divider

    echo -e "${GREEN}                    ✨  TERMINÉ  ✨${RESET}"
    echo ""

    echo -e "${WHITE}${BOLD}  Commandes:${RESET}"
    echo ""
    echo -e "    ${CYAN}uv run script.py${RESET}     Exécuter un script"
    echo -e "    ${CYAN}just test${RESET}           Lancer les tests"
    echo -e "    ${CYAN}just format${RESET}         Formatter"
    echo -e "    ${CYAN}just lint${RESET}           Vérifier"
    echo ""
    echo -e "    ${DIM}cd MODULES && ls${RESET}     Accéder aux chapitres"
    echo ""
}

main