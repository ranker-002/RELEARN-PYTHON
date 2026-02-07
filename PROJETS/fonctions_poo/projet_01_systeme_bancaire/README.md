# projet_01_systeme_bancaire

L'automatisation permet de programmer des tâches répétitives.

---

## Introduction

Ce projet vous permet d'appliquer planification dans un projet réel et professionnel.

**Concepts clés:** Planification, Emails, APIs, Logs

**Outils:** jinja2, matplotlib, smtplib

---

## Prérequis

- Module recommandé: Chapitres 20-26

---

## Structure

```
projet_01_systeme_bancaire/
├── src/
│   ├── main.py
│   ├── models/
│   ├── services/
│   └── utils/
├── tests/
├── data/
└── README.md
```

---

## Fonctionnalités

### 1. Fonctionnalité principale

- Implémentation de base
- Tests associés
- Documentation

---

## Modèle de Données

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Item:
    id: str
    name: str
    status: Status = Status.PENDING
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
```

---

## Indications

### Niveau 1

```python
class Project:
    def __init__(self):
        self.data = []
    
    def run(self):
        pass
```

---

## Critères de Validation

- [ ] Structure du projet
- [ ] Fonctionnalités implémentées
- [ ] Tests passent
- [ ] Code documenté

---


---

## Architecture et Diagrammes

### Architecture du Projet

```mermaid
graph TD
    subgraph src/
        A[main.py] --> B[Services]
        B --> C[Parser]
        B --> D[Fetcher]
        B --> E[Filter]
        A --> F[Models]
        F --> G[DataModel]
        A --> H[Utils]
    end
    
    subgraph data/
        I[sample/data.csv] --> A
    end
    
    subgraph tests/
        J[test_*.py] --> A
    end
```

### Flux de Données

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant C as CLI
    participant S as Services
    participant M as Models
    participant D as Data
    
    U->>C: Lancer l'application
    C->>S: Initialiser services
    S->>M: Charger modèles
    M->>D: Lire données
    D-->>M: Retourner données
    M-->>S: Modèles prêts
    S-->>C: Services prêts
    C->>U: Afficher menu
```

### Modèle de Données

```mermaid
classDiagram
    class DataModel {
        +str id
        +str name
        +created_at: datetime
        +save(): bool
        +load(): bool
    }
    
    class Service {
        +process(data: DataModel): dict
        +validate(input: dict): bool
    }
    
    Service --> DataModel: utilise
```

### Architecture Fonctionnelle

```mermaid
flowchart LR
    subgraph Input
        A[CLI Arguments]
        B[Config File]
        C[User Input]
    end
    
    subgraph Processing
        D[Main App]
        E[Services Layer]
        F[Models Layer]
    end
    
    subgraph Output
        G[Console Display]
        H[File Export]
        I[Log Results]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    F --> G
    F --> H
    F --> I
```
## Installation

```bash
python src/main.py
pytest tests/
python verification.py
```

---

## Ressources

- Documentation Python: https://docs.python.org/fr/3/

---

*Durée estimée: 8-12 heures | Difficulté: Outils:*

---

[Retour au module](../README_PROJETS.md)
