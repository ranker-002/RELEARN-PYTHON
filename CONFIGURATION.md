# ⚙️ Configuration - Python Mastery

Guide pour configurer votre environnement avec le standard moderne (uv).

---

## 1. Prérequis

### Installation de uv (gestionnaire Python)

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv | sh

# Windows (PowerShell)
irm https://astral.sh/uv | iex

# Ajouter au PATH
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

Vérifier:
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

# Installer les dépendances
./install.sh

# Ou directement avec uv
uv sync
uv sync --extra dev
```

---

## 3. Utilisation Quotidienne

### Avec just (recommandé)

```bash
just run script.py       # Exécuter un script
just test                # Lancer les tests
just format              # Formatter le code
just lint                # Vérifier le code
just check               # Format + Lint + Test
just shell               # Ouvrir IPython
```

### Avec uv directement

```bash
uv run python script.py           # Exécuter
uv run pytest                     # Tests
uv run black .                    # Format
uv run flake8 .                   # Lint
uv run mypy                       # Type checking
```

### Activer l'environnement virtuel

```bash
# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

## 4. VS Code

Créer `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.analysis.typeCheckingMode": "basic",
    "editor.formatOnSave": true,
    "editor.rulers": [100],
    "python.formatting.provider": "none",
    "python.linting.flake8Enabled": false,
    "python.linting.mypyEnabled": true,
    "python.testing.pytestEnabled": true,
    "files.associations": {"*.py": "python"}
}
```

Extensions recommandées:
- **Python** (Microsoft)
- **Pylance** (Microsoft)

---

## 5. Structure du Projet

```
relearn-python/
├── .venv/              # Environnement virtuel
├── .python-version     # Version Python
├── pyproject.toml      # Dépendances + config
├── Justfile            # Commandes
├── .gitignore
├── install.sh          # Script installation
├── README.md
└── CHAPITRES/
    └── 01_premiers_pas/
```

---

## 6. Commandes Utiles

| Action | Commande |
|--------|----------|
| Installer deps | `uv sync` |
| + outils dev | `uv sync --extra dev` |
| Exécuter | `uv run python file.py` |
| Tests | `uv run pytest` |
| Format | `uv run black .` |
| Lint | `uv run flake8 .` |
| Types | `uv run mypy` |
| Lister deps | `uv tree` |
| Mettre à jour | `uv sync --upgrade` |
| Nettoyer | `just clean` |

---

## 7. Dépannage

**"uv: command not found"**
```bash
export PATH="$HOME/.cargo/bin:$PATH"
# ou réinstaller uv
curl -LsSf https://astral.sh/uv | sh
```

**"Externally managed environment"**
```bash
# Utiliser uv au lieu de pip system-wide
uv pip install package  # Installe dans .venv
```

**Vider le cache uv**
```bash
uv cache clean
```

---

## 8. Ressources

- [Documentation uv](https://docs.astral.sh/uv/)
- [Python.org](https://docs.python.org/fr/3/)
- [Just](https://github.com/casey/just)

---

**Votre environnement est prêt ! Commencez avec: `just run CHAPITRES/01_premiers_pas/exemples/calculatrice.py`**
