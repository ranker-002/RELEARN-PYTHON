# Chapitre 10: Modules et Packages

## Ce que vous allez apprendre

- Créer et importer des modules
- Organisation en packages
- Le système d'import de Python
- Variables speciales `__name__` et `__main__`
- Packages standards et installation avec pip
- Structure d'un projet Python

---

## 1. Les Modules

### Qu'est-ce qu'un Module?

Un module est un fichier contenant des definitions Python (fonctions, classes, variables). L'extension est `.py`.

```
mon_module.py    <-- C'est un module!
```

### Création d'un Module

```python
# math_utils.py

def additionner(a, b):
    """Retourne la somme de a et b."""
    return a + b

def multiplier(a, b):
    """Retourne le produit de a et b."""
    return a * b

PI = 3.14159
```

### Import de Modules

```python
# methode 1: importer tout le module
import math_utils
resultat = math_utils.additionner(5, 3)   # 8
print(math_utils.PI)                     # 3.14159

# methode 2: importer des elements specifiques
from math_utils import additionner, PI
resultat = additionner(5, 3)  # 8 (pas de prefixe!)
print(PI)                       # 3.14159

# methode 3: importer tout avec alias
from math_utils import additionner as add
resultat = add(5, 3)  # 8

# methode 4: importer tout le module avec alias
import math_utils as mu
resultat = mu.additionner(5, 3)  # 8
```

---

## 2. Les Packages

### Qu'est-ce qu'un Package?

Un package est un repertoire contenant des modules et un fichier `__init__.py`.

```
mon_package/           <-- C'est un package!
    __init__.py        <-- Fichier d'initialisation
    module_a.py
    module_b.py
    sous_package/
        __init__.py
        module_c.py
```

### Import depuis un Package

```python
# Depuis le package
from mon_package import module_a
from mon_package.module_a import ma_fonction

# Depuis un sous-package
from mon_package.sous_package import module_c

# Import avec alias
from mon_package import module_a as ma
```

---

## 3. Le Fichier `__init__.py`

### Rôle du `__init__.py`

Ce fichier initialise le package et peut definir ce qui est exporte.

```python
# mon_package/__init__.py

# Importer automatiquement certains modules
from . import module_a
from . import module_b

# Ou definir les exports publics
__all__ = ['fonction_principale', 'MaClasse']
```

### Import simplifie

```python
# Apres configuration du __init__.py
from mon_package import ma_fonction  # Fonction exportee
```

---

## 4. Variables Speciales

### `__name__` et `__main__`

```python
# mon_module.py

def ma_fonction():
    print("Fonction executee!")

# Ce code s'execute seulement si le fichier est lance directement
if __name__ == "__main__":
    print("Ce module est execute directement")
    ma_fonction()
```

**Utilisation:**

```bash
# Lancer directement
python mon_module.py
# Affiche: "Ce module est execute directement"
#          "Fonction executee!"

# Importer dans un autre fichier
from mon_module import ma_fonction
# NE affiche PAS "Ce module est execute directement"
```

### Autres Variables Speciales

```python
print(__name__)      # Nom du module (ou "__main__")
print(__file__)      # Chemin du fichier
print(__doc__)       # Docstring du module
print(__builtins__)  # Module des fonctions integrees
```

---

## 5. Modules Standards Courants

### Modules Integres

```python
import math
print(math.pi)           # 3.14159...
print(math.sqrt(16))      # 4.0
print(math.floor(3.7))    # 3
print(math.ceil(3.2))     # 4

import random
print(random.randint(1, 10))    # Nombre aleatoire 1-10
print(random.choice([1, 2, 3]))  # Element aleatoire
random.shuffle([1, 2, 3])        # Melange sur place

import datetime
aujourdhui = datetime.date.today()
print(aujourdhui)  # 2024-01-15

import os
print(os.getcwd())     # Repertoire courant
print(os.listdir())    # Liste des fichiers

import json
donnees = {"a": 1, "b": 2}
json_str = json.dumps(donnees)   # Dict -> JSON string
```

### Le Module `collections`

```python
from collections import Counter, defaultdict, OrderedDict

# Counter: compte les occurrences
c = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'd': 1, 'c': 1})

# defaultdict: dict avec valeur par defaut
d = defaultdict(list)
d["cles"].append("valeur")

# OrderedDict: dictionnaire ordonne (Python 3.7+: plus necessaire)
```

---

## 6. Installation de Packages avec pip

### Commandes de Base

```bash
# Installer un package
pip install requests

# Installer une version specifique
pip install requests==2.28.0

# Installer depuis un fichier requirements.txt
pip install -r requirements.txt

# Desinstaller un package
pip uninstall requests

# Lister les packages installes
pip list

# Afficher les informations d'un package
pip show requests
```

### Fichier `requirements.txt`

```text
# requirements.txt
requests==2.28.0
pandas>=1.4.0
numpy>=1.20.0
flask>=2.0.0
```

### Environment Virtuel

```bash
# Creer un environnement virtuel
python -m venv mon_env

# Activer (Linux/Mac)
source mon_env/bin/activate

# Activer (Windows)
.\mon_env\Scripts\activate

# Desactiver
deactivate
```

---

## 7. Structure d'un Projet Python

### Structure Recommandee

```
mon_projet/
    __init__.py          # Package principal
    main.py               # Point d'entree
    requirements.txt      # Dependances
    
    package_a/
        __init__.py
        module1.py
        module2.py
    
    package_b/
        __init__.py
        module3.py
    
    tests/
        __init__.py
        test_module1.py
        test_module2.py
    
    docs/
        README.md
        guide.md
    
    setup.py              # Configuration (optionnel)
    pyproject.toml        # Configuration moderne (optionnel)
```

### Exemple Complet

```
calculatrice/
    __init__.py          # from .operations import add, sub
    operations.py         # add(), sub(), mul(), div()
    utils.py              # format_result(), validate_input()
    main.py               # Point d'entree
    
    tests/
        __init__.py
        test_operations.py
```

---

## 8. Import Relatif et Absolu

### Import Relatif

```python
# Dans package_a/module1.py

# Importer depuis le meme package
from . import autre_module
from .autre_module import fonction_a

# Importer depuis un sous-package
from .sous_package import module_c

# Importer depuis le parent
from .. import fonction_globale
```

### Import Absolu

```python
# Importer depuis la racine du projet
from package_a.module1 import ma_fonction
from package_a.sous_package.module_c import autre_fonction
```

### Quand Utiliser L'un ou L'Another

- **Import relatif**: Pour les imports au sein d'un meme package
- **Import absolu**: Pour les imports depuis l'exterieur ou dans `__init__.py`

---

## 9. Bonnes Pratiques

### Organisation du Code

```python
# Ordre des imports (PEP 8)
# 1. Imports de la bibliotheque standard
import os
import sys
from datetime import datetime

# 2. Imports de tierces parties
import requests
import numpy as np

# 3. Imports locaux (du meme projet)
from . import mon_module
from .autre_module import MaClasse

# Exception pour __all__ si utilise
__all__ = ['MaClasse', 'ma_fonction']
```

### eviter les Import Cycles

```python
# PROBLEME: Import circulaire
# module_a.py: from .module_b import B
# module_b.py: from .module_a import A

# SOLUTIONS:
# 1. Importer a l'interieur des fonctions
def ma_fonction():
    from .module_b import B
    return B()

# 2. Reorganiser le code
```

---

## Points Cles a Retenir

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| Module | Fichier `.py` | `math_utils.py` |
| Package | Dossier avec `__init__.py` | `mon_package/` |
| Import | `import module` | `import math` |
| Import specifique | `from m import f` | `from math import sqrt` |
| Import relatif | `from . import m` | `from .module_a import f` |
| Alias | `import m as alias` | `import numpy as np` |
| `__name__` | Test si module ou script | `if __name__ == "__main__":` |

---

## Prochain Chapitre

Dans le chapitre suivant, vous decouvrez la **Programmation Orientee Objet (POO)** avec les classes et objets.
