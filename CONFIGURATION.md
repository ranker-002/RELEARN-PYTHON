# Configuration - Python Mastery

Guide complet pour configurer votre environnement de développement Python avec le standard moderne (uv).

---

## 1. Prérequis

### Installation de uv (gestionnaire Python ultra-rapide)

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# Ajouter au PATH (si nécessaire)
export PATH="$HOME/.cargo/bin:$PATH"
```

### Python (si non installé)

```bash
# Arch Linux
sudo pacman -S python

# Ubuntu/Debian
sudo apt install python3 python3-venv

# macOS
brew install python

# Windows
# Télécharger depuis python.org
```

### Vérification

```bash
uv --version
python3 --version
```

---

## 2. Installation du Projet

```bash
# Cloner le projet
git clone <repo-url>
cd relearn-python

# Activer l'environnement virtuel
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Installer les dépendances
./install.sh
# Ou directement avec uv
uv sync
uv sync --extra dev
```

---

## 3. Utilisation Quotidienne

### Avec just (recommandé)

| Commande | Description |
|----------|-------------|
| `just run script.py` | Exécuter un script |
| `just test` | Lancer les tests |
| `just format` | Formatter le code (Black) |
| `just lint` | Vérifier le code (Ruff) |
| `just check` | Format + Lint + Type check |
| `just shell` | Ouvrir IPython interactif |
| `just deps` | Lister les dépendances |
| `just clean` | Nettoyer les fichiers temporaires |

### Avec uv directement

```bash
uv run python script.py           # Exécuter un script
uv run pytest                     # Lancer les tests
uv run black .                    # Formatter le code
uv run ruff check .               # Vérifier le code
uv run mypy                       # Vérification des types
uv run ipython                    # Ouvrir IPython
```

### Activer l'environnement virtuel

```bash
# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

## 4. Structure du Projet

```
relearn-python/
├── MODULES/                      # Contenu pédagogique
│   ├── 01_core_fondations/       # Chapitres 01-07
│   ├── 02_fonctions_poo/        # Chapitres 08-13
│   ├── 03_robustesse_fichiers/   # Chapitres 14-16
│   ├── 04_concepts_avances/     # Chapitres 17-19
│   └── 05_domaines_specifies/    # Chapitres 20-26
│
├── PROJETS/                      # Projets concrets
│   ├── core_fondations/
│   ├── fonctions_poo/
│   ├── robustesse_fichiers/
│   ├── concepts_avances/
│   ├── automation/
│   ├── web_scraping/
│   ├── data_science/
│   ├── visualisation/
│   ├── web_dev/
│   ├── machine_learning/
│   └── deep_learning/
│
├── relearn_python/               # Package utilitaire
├── .venv/                        # Environnement virtuel
├── .python-version              # Version Python
├── pyproject.toml               # Dépendances + config
├── Justfile                     # Commandes disponibles
├── .gitignore
├── install.sh                   # Script d'installation
├── README.md                    # Documentation principale
├── CONFIGURATION.md             # Ce fichier
└── progres_apprentissage.md      # Suivi de progression
```

---

## 5. VS Code - Configuration Recommandée

Créer `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.analysis.typeCheckingMode": "basic",
    "editor.formatOnSave": true,
    "editor.rulers": [100],
    "python.formatting.provider": "none",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.testing.pytestEnabled": true,
    "files.associations": {"*.py": "python"}
}
```

### Extensions VS Code Recommandées

| Extension | Description |
|-----------|-------------|
| **Python** (Microsoft) | Support Python complet |
| **Pylance** (Microsoft) | Analyse de type ultra-rapide |
| **Ruff** (Astral) | Linter ultra-rapide |
| **Black Formatter** | Formatage de code |
| **Error Lens** | Amélioration des erreurs |

---

## 6. Gestion des Dépendances

### Groupes de dépendances

```bash
# Core - numpy, pandas, matplotlib
uv sync --extra core

# Web - flask, fastapi, jinja2, uvicorn
uv sync --extra web

# Automation - beautifulsoup4, selenium, requests
uv sync --extra automation

# Data - scikit-learn, openpyxl, pillow
uv sync --extra data

# AI - torch, torchvision (lourd!)
uv sync --extra ai

# Tout installer
uv sync --extra core --extra web --extra automation --extra data --extra ai

# Outils de développement
uv sync --extra dev
```

### Dépendances par défaut (pyproject.toml)

| Groupe | Packages |
|--------|----------|
| Core | requests, pyyaml, tabulate, tqdm |
| Dev | pytest, black, ruff, mypy |

### Commandes utiles

| Action | Commande |
|--------|----------|
| Installer deps | `uv sync` |
| + outils dev | `uv sync --extra dev` |
| Lister deps | `uv tree` |
| Mettre à jour | `uv sync --upgrade` |
| Ajouter package | `uv add package` |
| Ajouter dev | `uv add --dev package` |
| Supprimer | `uv remove package` |
| Vider cache | `uv cache clean` |

---

## 7. Dépannage

### "uv: command not found"

```bash
export PATH="$HOME/.local/bin:$PATH"
# ou réinstaller uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### "Externally managed environment"

```bash
# Utiliser uv au lieu de pip system-wide
uv pip install package  # Installe dans .venv
```

### Erreurs de permissions

```bash
# Vérifier les droits
ls -la .venv/

# Recréer l'environnement si corrompu
rm -rf .venv
uv sync
```

### Problèmes de version Python

```bash
# Vérifier la version requise
cat .python-version

# Changer de version avec pyenv
pyenv install 3.12
pyenv local 3.12
```

---

## 8. Lancer les Exercices

### Exercices d'un chapitre

```bash
# Aller dans le chapitre
cd MODULES/01_core_fondations/01_premiers_pas/

# Exécuter les exercices
uv run python exercices.py

# Vérifier avec les tests
uv run python verification.py

# Voir la solution
uv run python solutions.py
```

### Projets

```bash
# Aller dans un projet
cd PROJETS/core_fondations/projet_01_calculatrice_cli/

# Lancer le projet
uv run python src/main.py

# Voir la solution
uv run python solution/main.py
```

---

## 9. Conventions de Code

### Style (PEP 8)

| Élément | Convention | Exemple |
|---------|------------|---------|
| Variables/fonctions | snake_case | `calculate_total` |
| Classes | PascalCase | `BankAccount` |
| Constantes | UPPER_SNAKE_CASE | `MAX_CONNECTIONS` |
| Attributs privés | _single_leading | `_private_var` |

### Formattage

```bash
# Formatter tout le code
just format

# Vérifier le formatage
just lint
```

### Type Hinting

Recommandé à partir du Module 4:

```python
def addition(a: float, b: float) -> float:
    return a + b
```

---

## 10. Ressources

- [Documentation uv](https://docs.astral.sh/uv/)
- [Documentation Python](https://docs.python.org/fr/3/)
- [Just - Command Runner](https://github.com/casey/just)
- [Black - Formateur](https://black.readthedocs.io/)
- [Ruff - Linter](https://beta.ruff.rs/docs/)

---

## Démarrage Rapide

```bash
# 1. Cloner et installer
git clone <repo-url>
cd relearn-python
./install.sh

# 2. Commencer avec le Module 1
cd MODULES/01_core_fondations/01_premiers_pas/

# 3. Lancer votre premier exercice
uv run python exercices.py

# 4. Suivre votre progression
# Éditer progres_apprentissage.md
```

**Bonne chance dans votre apprentissage Python ! 🐍**
