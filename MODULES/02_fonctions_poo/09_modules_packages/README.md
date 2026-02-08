# Chapitre 09 : Modules et Packages - Organiser ton Code

## Introduction

Quand ton projet grandit, tu as besoin d'organiser ton code en fichiers séparés. Les modules et packages permettent cela !

---

## 1. Les modules

Un module est simplement un fichier Python (.py) avec du code réutilisable.

### Créer un module

```python
# mon_module.py
def dire_bonjour():
    print("Bonjour !")

PI = 3.14159
```

### Importer un module

```python
# Importer tout
import mon_module
mon_module.dire_bonjour()
print(mon_module.PI)

# Importer seulement ce qu'il faut
from mon_module import dire_bonjour, PI
dire_bonjour()
print(PI)

# Importer avec un alias
import math as mathematiques
print(mathematiques.sqrt(16))  # 4.0
```

---

## 2. Les packages

Un package est un dossier contenant plusieurs modules et un fichier `__init__.py`.

```
mon_package/
    __init__.py      # Rend le dossier importable
    module1.py
    module2.py
```

```python
from mon_package import module1
module1.une_fonction()
```

---

## 3. Le module `__name__`

Chaque fichier a une variable `__name__` :

```python
# Quand le fichier est exécuté directement
# __name__ = "__main__"

# Quand le fichier est importé
# __name__ = "nom_du_module"

def principale():
    print("Code du module")

if __name__ == "__main__":
    # Ce code s'exécute SEULEMENT si on lance le fichier directement
    principale()
```

---

## 4. Les modules standards

Python inclut plein de modules utiles :

```python
import math      # Fonctions mathématiques
import random   # Nombres aléatoires
import datetime # Dates et heures
import os       # Interactions avec le système
import json     # Lecture/écriture JSON
```

---

## 5. Le Chemin de Recherche (sys.path)

Python cherche les modules dans plusieurs emplacements :

```python
import sys

# Afficher les chemins de recherche
for chemin in sys.path:
    print(chemin)

# Ajouter un chemin personnalisé
sys.path.append("/chemin/vers/mes/modules")
```

### PYTHONPATH

Variable d'environnement pour ajouter des chemins :
```bash
# Linux/Mac
export PYTHONPATH="/chemin/vers/modules:$PYTHONPATH"

# Windows
set PYTHONPATH=C:\chemin\vers\modules;%PYTHONPATH%
```

---

## 6. Les Imports Relatifs

Dans un package, tu peux utiliser des imports relatifs :

```
mon_projet/
    __init__.py
    module_a.py
    sous_package/
        __init__.py
        module_b.py
```

```python
# Dans module_b.py
from ..module_a import ma_fonction  # Remonter d'un niveau
from . import autre_module          # Même niveau
```

---

## 7. Virtual Environments (Environnements Virtuels)

Les environnements virtuels isolent les dépendances de chaque projet.

### Créer un Environnement Virtuel

```bash
# Créer
python -m venv mon_env

# Activer (Linux/Mac)
source mon_env/bin/activate

# Activer (Windows)
mon_env\Scripts\activate

# Désactiver
deactivate
```

### Gestion des Dépendances

```bash
# Sauvegarder les packages installés
pip freeze > requirements.txt

# Installer depuis requirements.txt
pip install -r requirements.txt
```

**Exemple de requirements.txt :**
```
requests==2.28.1
pandas>=1.5.0
numpy<2.0.0
```

---

## 8. Créer un Package Installable

### Structure Complète

```
mon_package/
├── mon_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   └── test_module1.py
├── README.md
├── LICENSE
└── pyproject.toml
```

### Fichier pyproject.toml (Moderne)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mon-package"
version = "1.0.0"
authors = [
    {name = "Ton Nom", email = "ton@email.com"}
]
description = "Une description de ton package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
dependencies = [
    "requests>=2.28.0",
    "pandas>=1.5.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0"
]
```

### Installation en Mode Développement

```bash
# Permet de modifier le code sans réinstaller
pip install -e .
```

---

## 9. Bonnes Pratiques

### Organisation des Imports

```python
# Ordre recommandé :
# 1. Imports standard library
import os
import sys
from datetime import datetime

# 2. Imports de tiers
import requests
import pandas as pd

# 3. Imports locaux
from .utils import helper
from mon_package.module import fonction
```

### Éviter les Imports Circulaires

```python
# ❌ Mauvais - Import circulaire
# module_a.py
from module_b import fonction_b

def fonction_a():
    return fonction_b()

# module_b.py
from module_a import fonction_a  # ERREUR !

def fonction_b():
    return fonction_a()

# ✅ Bon - Import à l'intérieur de la fonction
# module_b.py
def fonction_b():
    from module_a import fonction_a  # Import différé
    return fonction_a()
```

### Le Fichier __init__.py

```python
# mon_package/__init__.py

# Version du package
__version__ = "1.0.0"

# Exporter les principales fonctions
from .module1 import fonction_principale
from .module2 import MaClasse

# Configuration
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
```

---

## 10. Modules Standards Utiles

```python
import os          # Système de fichiers
import sys         # Système et arguments
import math        # Mathématiques
import random      # Aléatoire
import datetime    # Dates et heures
import json        # JSON
import csv         # Fichiers CSV
import re          # Expressions régulières
import itertools   # Itérateurs
import collections # Structures de données
import functools   # Fonctions utilitaires
import hashlib     # Hachage
import base64      # Encodage
import typing      # Annotations de types
import pathlib     # Chemins de fichiers
import subprocess  # Exécution de commandes
import argparse    # Arguments en ligne de commande
import logging     # Journalisation
import unittest    # Tests unitaires
import pdb         # Débogueur
```

---

## Exercices Pratiques

### Exercice 1 : Créer un Module
Crée un module `calculs.py` avec des fonctions mathématiques (addition, soustraction, multiplication, division avec vérification). Importe-le dans un autre fichier et utilise ces fonctions.

### Exercice 2 : Créer un Package
Crée un package `mon_projet` avec :
- Un module `utils.py` avec des fonctions utilitaires
- Un module `main.py` qui utilise utils
- Teste les imports relatifs et absolus

### Exercice 3 : Gestion des Dépendances
Crée un fichier requirements.txt avec 3 packages (requests, pandas, numpy). Installe-les dans un environnement virtuel et vérifie avec `pip list`.

### Exercice 4 : __name__ == "__main__"
Crée un module qui peut être :
- Importé (sans exécuter le code principal)
- Exécuté directement (avec le code principal)
Utilise `if __name__ == "__main__":` correctement.

### Exercice 5 : Package Installable
Transforme ton projet en package installable avec pyproject.toml. Installe-le en mode développement avec `pip install -e .`.

### Exercice 6 : Imports Avancés
Pratique différentes méthodes d'import :
- Import complet
- Import spécifique
- Import avec alias
- Import relatif (dans un package)

### Exercice 7 : Gestion des Conflits
Installe deux versions différentes d'un même package dans deux environnements virtuels différents. Montre qu'ils sont isolés.

### Exercice 8 : Structure de Projet
Crée la structure complète d'un projet Python professionnel avec :
- Source code
- Tests
- Documentation
- Configuration

### Exercice 9 : Module de Configuration
Crée un module `config.py` qui charge des paramètres depuis un fichier JSON. Utilise-le dans ton programme principal.

### Exercice 10 : Plugin System
Crée un système de plugins où ton programme charge dynamiquement des modules depuis un dossier `plugins/`.

---

## Résumé

| Concept | Syntaxe | Usage |
|---------|---------|-------|
| Import module | `import module` | Tout le module |
| Import spécifique | `from module import x` | Seulement x |
| Alias | `import x as y` | Renommer |
| Import relatif | `from . import x` | Dans un package |
| Module exécutable | `if __name__ == "__main__"` | Code principal |
| Venv | `python -m venv` | Isoler les dépendances |
| Requirements | `pip freeze > requirements.txt` | Sauvegarder deps |
| Package | `pyproject.toml` | Distribuer son code |

---

## Prochain Chapitre

Tu sais organiser ton code en modules et packages ! Le chapitre suivant sur les **classes et objets** t'apprendra la programmation orientée objet pour créer des structures de données complexes.
