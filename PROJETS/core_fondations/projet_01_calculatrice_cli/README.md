# Projet 1 : Calculatrice CLI

Créez une calculatrice interactive en ligne de commande qui prend en charge les opérations de base, avancées et les conversions d'unités.

---

## Introduction : Qu'est-ce qu'une Calculatrice CLI ?

Une calculatrice CLI est un outil qui :
- **Effectue** des opérations mathématiques de base (addition, soustraction, multiplication, division)
- **Calcule** des opérations avancées (puissance, racine carrée, factorielle, logarithmes)
- **Convertit** des unités de mesure (longueur, masse, température, devises)
- **Mémorise** les résultats pour les utiliser dans des calculs ultérieurs

**Exemples d'utilisation réelle :**
- **bc** : Calculatrice Unix en ligne de commande
- **calc** : Calculatrice sur Windows
- **Python REPL** : Interpréteur Python interactif

**Architecture du système :**
```
┌─────────────────────────────────────────────────────────┐
│                 CALCULATRICE CLI                       │
├─────────────────────────────────────────────────────────┤
│  OPÉRATIONS:           │  FONCTIONNALITÉS:           │
│  - Addition (+)       │  ✓ Calcul interactif         │
│  - Soustraction (-)   │  ✓ Historique des calculs    │
│  - Multiplication (×) │  ✓ Variables personnalisées  │
│  - Division (÷)      │  ✓ Conversion d'unités       │
│  - Puissance (^2)     │  ✓ Mode scientifique         │
│  - Racine (√)        │  ✓ Sauvegarde/restauration  │
└─────────────────────────────────────────────────────────┘
```

---

## Prérequis

- **Module 1 requis** : [Core Fondations](../../01_core_fondations/)
- Compétences nécessaires :
  - Opérateurs arithmétiques
  - Fonctions et modularité
  - Structures de données (listes, dictionnaires)
  - Gestion des erreurs

---

## Structure du Projet

```
projet_01_calculatrice_cli/
├── src/
│   ├── main.py              # Point d'entrée CLI
│   ├── models/
│   │   ├── operation.py     # Classe Operation
│   │   ├── historique.py     # Classe Historique
│   │   └── variable.py      # Classe Variable
│   ├── services/
│   │   ├── calculateur.py   # Service de calculs
│   │   ├── convertisseur.py # Conversion d'unités
│   │   └── evaluateur.py    # Évaluation d'expressions
│   └── utils/
│       ├── config.py        # Configuration
│       └── formatter.py     # Formatage des résultats
├── tests/
│   ├── test_calculateur.py
│   ├── test_convertisseur.py
│   └── test_main.py
├── data/
│   └── historique.json     # Sauvegarde de l'historique
├── README.md
└── requirements.txt
```

---

## Fonctionnalités

### 1. Opérations de Base

```python
class Calculateur:
    def additionner(self, a: float, b: float) -> float:
        return a + b
    
    def soustraire(self, a: float, b: float) -> float:
        return a - b
    
    def multiplier(self, a: float, b: float) -> float:
        return a * b
    
    def diviser(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division par zéro impossible")
        return a / b
```

### 2. Opérations Avancées

```python
class CalculateurAvance:
    def puissance(self, base: float, exposant: float) -> float:
        return base ** exposant
    
    def racine_carree(self, nombre: float) -> float:
        if nombre < 0:
            raise ValueError("Racine carrée d'un nombre négatif")
        return nombre ** 0.5
    
    def factorielle(self, n: int) -> int:
        if n < 0:
            raise ValueError("Factorielle d'un nombre négatif")
        if n == 0 or n == 1:
            return 1
        return n * self.factorielle(n - 1)
    
    def logarithme(self, n: float, base: float = 10) -> float:
        import math
        return math.log(n, base)
```

### 3. Conversion d'Unités

```python
class Convertisseur:
    UNITES = {
        'longueur': {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'ft': 0.3048,
            'in': 0.0254,
        },
        'masse': {
            'kg': 1.0,
            'g': 0.001,
            'lb': 0.453592,
            'oz': 0.0283495,
        },
        'temperature': {
            'C': 'celsius',
            'F': 'fahrenheit',
            'K': 'kelvin',
        },
    }
    
    def convertir(self, valeur: float, unite_source: str, 
                 unite_cible: str, categorie: str) -> float:
        if categorie == 'temperature':
            return self._convertir_temperature(valeur, unite_source, unite_cible)
        facteur_source = self.UNITES[categorie][unite_source]
        facteur_cible = self.UNITES[categorie][unite_cible]
        return valeur * facteur_source / facteur_cible
```

### 4. Historique des Calculs

```python
class Historique:
    def __init__(self):
        self.calculs = []
    
    def ajouter(self, expression: str, resultat: float):
        self.calculs.append({
            'expression': expression,
            'resultat': resultat,
            'timestamp': datetime.now(),
        })
    
    def afficher(self, n: int = 10):
        for calc in self.calculs[-n:]:
            print(f"  {calc['expression']} = {calc['resultat']}")
    
    def sauvegarder(self, fichier: str = "data/historique.json"):
        import json
        with open(fichier, 'w') as f:
            json.dump(self.calculs, f)
```

### 5. Interface CLI Interactive

```
╔══════════════════════════════════════════════════╗
║              CALCULATRICE CLI                    ║
╠══════════════════════════════════════════════════╣
║  1. Calcul simple       2. Calcul scientifique ║
║  3. Conversion          4. Historique          ║
║  5. Variables           6. Sauvegarder         ║
║  7. Quitter                                    ║
╚══════════════════════════════════════════════════╝
```

---

## Modèle de Données

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union
from enum import Enum


class TypeOperation(Enum):
    BASIQUE = "basique"
    AVANCEE = "avancee"
    CONVERSION = "conversion"
    VARIABLE = "variable"


@dataclass
class Operation:
    type: TypeOperation
    expression: str
   operande1: Optional[float]
    operande2: Optional[float] = None
    unite_source: Optional[str] = None
    unite_cible: Optional[str] = None
    categorie: Optional[str] = None
    
    def executer(self) -> float:
        if self.type == TypeOperation.BASIQUE:
            return self._executer_basique()
        elif self.type == TypeOperation.AVANCEE:
            return self._executer_avancee()
        elif self.type == TypeOperation.CONVERSION:
            return self._executer_conversion()
    
    def _executer_basique(self) -> float:
        if self.expression == '+':
            return self.operande1 + self.operande2
        elif self.expression == '-':
            return self.operande1 - self.operande2
        elif self.expression == '*':
            return self.operande1 * self.operande2
        elif self.expression == '/':
            if self.operande2 == 0:
                raise ValueError("Division par zéro")
            return self.operande1 / self.operande2


@dataclass
class Variable:
    nom: str
    valeur: float
    description: str = ""
    
    def __str__(self):
        return f"{self.nom} = {self.valeur}"


@dataclass
class Calcul:
    expression: str
    resultat: float
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
```

---

## Indications Progressives

### Niveau 1 - Découverte

**Objectif:** Implémenter les quatre opérations de base

```python
class CalculatriceBasic:
    def calculer(self, a: float, b: float, operateur: str) -> float:
        if operateur == '+':
            return a + b
        elif operateur == '-':
            return a - b
        elif operateur == '*':
            return a * b
        elif operateur == '/':
            if b == 0:
                raise ValueError("Division par zéro")
            return a / b
        else:
            raise ValueError(f"Opérateur inconnu: {operateur}")
```

---

### Niveau 2 - Approfondissement

**Objectif:** Ajouter les opérations avancées et les conversions

```python
class CalculatriceAvancee(CalculatriceBasic):
    OPERATIONS_AVANCEES = {
        '^': lambda a, b: a ** b,
        'sqrt': lambda a, _: a ** 0.5,
        'fact': lambda a, _: self._factorielle(int(a)),
        'log': lambda a, _: __import__('math').log(a),
    }
    
    def _factorielle(self, n: int) -> int:
        if n < 0:
            raise ValueError("Factorielle négative")
        resultat = 1
        for i in range(2, n + 1):
            resultat *= i
        return resultat
```

---

### Niveau 3 - Expert

**Objectif:** Application CLI complète avec historique et variables

```python
class CalculatriceExpert:
    def __init__(self):
        self.historique = []
        self.variables = {}
        self.calc = CalculatriceAvancee()
    
    def evaluer(self, expression: str) -> float:
        expression = self._substituer_variables(expression)
        resultat = self.calc.evaluer(expression)
        self.historique.append(Calcul(expression, resultat))
        return resultat
    
    def _substituer_variables(self, expression: str) -> str:
        for nom, valeur in self.variables.items():
            expression = expression.replace(nom, str(valeur))
        return expression
```

---

## Configuration

Créez `data/historique.json` :

```json
[]
```

---

## Critères de Validation

- [ ] Les 4 opérations de base fonctionnent
- [ ] Les opérations avancées (puissance, racine, factorielle)
- [ ] La conversion d'unités (longueur, masse, température)
- [ ] L'historique des calculs
- [ ] Les variables personnalisées
- [ ] La sauvegarde/restauration de l'historique
- [ ] La gestion des erreurs (division par zéro, etc.)

---

## Pièges Courants

### 1. Division par zéro
```python
def diviser(self, a, b):
    if b == 0:
        raise ValueError("Division par zéro!")
    return a / b
```

### 2. Factorielle de nombres négatifs
```python
if n < 0:
    raise ValueError("Factorielle non définie pour les nombres négatifs")
```

### 3. Expressions mal formées
```python
try:
    resultat = eval(expression)
except (SyntaxError, NameError) as e:
    print(f"Erreur: Expression invalide - {e}")
```

### 4. Précision des flottants
```python
resultat = round(a / b, 10)  # Arrondir à 10 décimales
```

---

## Installation et Utilisation

```bash
python src/main.py
pytest tests/ -v
python verification.py
```

**Mode d'emploi :**
- Tapez une expression (ex: `2 + 3 * 4`)
- Utilisez `sqrt(16)` pour la racine carrée
- Utilisez `2^3` pour les puissances
- Tapez `help` pour l'aide
- Tapez `quit` pour quitter

---

## Ressources

- [Documentation Python](https://docs.python.org/fr/3/)
- [Module math](https://docs.python.org/fr/3/library/math.html)
- [F-strings](https://docs.python.org/fr/3/tutorial/inputoutput.html#formatted-string-literals)

---

## Objectifs d'Apprentissage

- Utiliser les opérateurs arithmétiques
- Implémenter des fonctions avec gestion d'erreurs
- Manipuler des listes et dictionnaires
- Créer une CLI interactive
- Gérer la sérialisation JSON
- Utiliser les dataclasses

---

*Durée estimée : 4-6 heures | Difficulté : Débutant*

---

[Retour au module](../README_PROJETS.md)
