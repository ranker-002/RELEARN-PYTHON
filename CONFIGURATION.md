# ⚙️ Configuration - Python Mastery

Guide complet pour configurer votre environnement de développement.

---

## 1. Installation de Python

### Windows

1. Télécharger Python depuis [python.org/downloads](https://python.org/downloads)
2. Choisir **Python 3.12.x** (latest stable)
3. **IMPORTANT**: Cocher "Add Python to PATH"
4. Cliquer sur "Install Now"

Vérifier l'installation:
```cmd
python --version
python -m pip --version
```

### macOS

```bash
# Via Homebrew (recommandé)
brew install python@3.12

# Ou via pyenv (pour gérer plusieurs versions)
brew install pyenv
pyenv install 3.12.0
pyenv global 3.12.0
```

Vérifier:
```bash
python3 --version
python3 -m pip --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3.12 python3-pip python3-venv
```

Vérifier:
```bash
python3 --version
python3 -m pip --version
```

---

## 2. Configuration de VS Code

### Installation de VS Code

Télécharger depuis [code.visualstudio.com](https://code.visualstudio.com/)

### Extensions Recommandées

1. **Python** (Microsoft) - Support Python complet
2. **Pylance** - Analyse de type rapide
3. **Jupyter** - Pour les notebooks
4. **autoDocstring** - Génération de docstrings
5. **Python Indent** - Meilleure indentation
6. **Material Icon Theme** - Meilleure organisation visuelle

### Configuration des Extensions

Créer `.vscode/settings.json` à la racine du projet:

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticMode": "workspace",
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "python.formatting.provider": "black",
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "files.associations": {
        "*.py": "python"
    }
}
```

### Raccourcis Clés Utiles

| Raccourci | Action |
|-----------|--------|
| `Ctrl+Shift+P` | Palette de commandes |
| `F1` | Palette de commandes |
| `Ctrl+B` | Toggle sidebar |
| `Ctrl+`` | Toggle terminal |
| `F5` | Déboguer |
| `Shift+Alt+F` | Formater le document |
| `Ctrl+/` | Commenter/Décommenter |
| `F2` | Renommer symbole |

---

## 3. Environnement Virtuel

### Création

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer (Linux/Mac)
source venv/bin/activate

# Activer (Windows)
.\venv\Scripts\activate

# Vérifier l'activation (doit montrer venv)
which python
python --version
```

### Installation des Dépendances

```bash
# Mise à jour de pip
python -m pip install --upgrade pip

# Installer les packages
pip install numpy pandas matplotlib pytest black flake8 mypy
pip install requests beautifulsoup4 selenium webdriver-manager
pip install scikit-learn torch torchvision
pip install flask fastapi uvicorn jinja2
pip install openpyxl pillow pyyaml tabulate tqdm
```

### Sortir de l'Environnement

```bash
deactivate
```

---

## 4. Git (Optionnel)

### Initialisation

```bash
# Initialiser un dépôt Git
git init

# Créer .gitignore
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo "venv/" >> .gitignore
echo ".vscode/" >> .gitignore
echo "*.egg-info/" >> .gitignore
```

### Configuration

```bash
git config user.name "Votre Nom"
git config user.email "votre@email.com"
```

---

## 5. Outils de Développement

### Linting (Analyse de Code)

```bash
# Vérifier le code avec flake8
flake8 votre_fichier.py

# Avec configuration personnalisée
flake8 --config=.flake8 votre_fichier.py
```

Créer `.flake8`:
```ini
[flake8]
max-line-length = 88
extend-ignore = E203
exclude =
    .git,
    __pycache__,
    .venv,
    venv,
    build,
    dist
```

### Formatting (Formatage)

```bash
# Formater un fichier avec black
black votre_fichier.py

# Vérifier sans modifier
black --check votre_fichier.py
```

### Type Checking

```bash
# Vérifier les types avec mypy
mypy votre_fichier.py

# Avec configuration stricte
mypy --strict votre_fichier.py
```

Créer `mypy.ini`:
```ini
[mypy]
python_version = 3.12
warn_return_any = True
warn_unused_configs = True
ignore_missing_imports = True
```

### Tests

```bash
# Exécuter les tests avec pytest
pytest

# Avec couverture
pytest --cov=.

# Tests spécifiques
pytest tests/test_fichier.py -v
```

---

## 6. Structure du Projet

```
PYTHON_MASTRY/
├── .vscode/
│   └── settings.json
├── CHAPITRES/
│   └── 01_premiers_pas/
│       ├── README.md
│       ├── exercices.py
│       ├── solutions.py
│       └── exemples/
├── EXERCICES/
│   ├── solutions/
│   └── projets/
├── OUTILS/
├── CONFIG/
├── venv/
├── .gitignore
├── .flake8
├── mypy.ini
├── install.sh
├── README.md
├── progres_apprentissage.md
└── CONFIGURATION.md
```

---

## 7. Bonnes Pratiques

### Organisation du Code

```python
# Imports standard
import os
import sys
from typing import List, Dict

# Imports tierces parties
import numpy as np
import pandas as pd

# Imports locaux (du projet)
from .module_local import MaClasse
from utils.helpers import fonction_utilitaire


# Constantes en haut du fichier
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30


class MaClasse:
    """Description de la classe."""

    CONSTANTE_DE_CLASSE = "valeur"

    def __init__(self, param: str) -> None:
        """Initialiser l'instance.

        Args:
            param: Description du paramètre
        """
        self.param = param

    def methode(self, valeur: int) -> bool:
        """Description de la méthode.

        Args:
            valeur: Description

        Returns:
            Description du retour
        """
        return True
```

### Convention de Nommage

| Type | Convention | Exemple |
|------|------------|---------|
| Variable | snake_case | `user_name`, `total_price` |
| Fonction | snake_case | `calculate_total()`, `get_data()` |
| Classe | PascalCase | `BankAccount`, `UserProfile` |
| Constante | UPPER_SNAKE_CASE | `MAX_SIZE`, `DEFAULT_TIMEOUT` |
| Variable privée | `_single_leading` | `_private_var` |
| Méthode magique | __dunder__ | `__init__`, `__str__` |

---

## 8. Dépannage

### Problèmes Courants

**"python command not found"**
```bash
# Vérifier que Python est dans PATH
which python3
# ou
where python

# Si absent, ajouter au PATH (Windows)
setx PATH "%PATH%;C:\Python312"
```

**"pip command not found"**
```bash
# Utiliser python -m pip
python -m pip install package_name

# Ou réinstaller pip
python -m ensurepip --upgrade
```

**"venv not supported"**
```bash
# Sur certaines distributions Linux
sudo apt install python3-venv

# Ou utiliser virtualenv
pip install virtualenv
virtualenv venv
```

**"Module not found" après installation**
```bash
# Vérifier que venv est activé
which python

# Réinstaller le package dans venv
pip install package_name

# Vérifier l'emplacement
pip show package_name
```

---

## 9. Ressources

### Documentation
- [Python.org](https://docs.python.org/fr/3/)
- [VS Code Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Real Python](https://realpython.com/)

### Outils
- [Black (formatage)](https://black.readthedocs.io/)
- [Flake8 (linting)](https://flake8.pycqa.org/)
- [Mypy (types)](https://mypy-lang.org/)
- [Pytest (tests)](https://docs.pytest.org/)

---

**Votre environnement est prêt ! Commencez par le Chapitre 1.**
