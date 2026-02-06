# Chapitre 10 : Modules et Packages - Organiser ton Code

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

## 5. Installer des packages avec pip

```bash
# Installer un package
pip install requests

# Utiliser le package installé
import requests
```

---

## Exercices

1. Crée ton propre module avec quelques fonctions
2. Importe et utilise ce module dans un autre fichier
