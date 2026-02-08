# Projet 2 : Gestionnaire de Tâches CLI

Créez un gestionnaire de tâches en ligne de commande pour organiser et suivre vos activités quotidiennes.

---

## Introduction : Qu'est-ce qu'un Gestionnaire de Tâches ?

Un gestionnaire de tâches est un outil qui :
- **Crée** et organise des tâches avec priorités et échéances
- **Catégorise** les tâches par projets et contextes
- **Suivi** le temps passé sur chaque tâche
- **Filtre** et recherche des tâches efficacement
- **Sauvegarde** l'historique des tâches accomplies

**Exemples d'utilisation réelle :**
- **Todoist** : Gestionnaire de tâches populaire
- **Taskwarrior** : Gestionnaire CLI avancé
- **Microsoft Todo** : Application Windows

---

## Prérequis

- **Module 1 requis** : [Core Fondations](../../01_core_fondations/)
- Compétences nécessaires :
  - Listes et dictionnaires
  - Dates et heures
  - Fichiers JSON
  - Structures de données

---

## Structure du Projet

```
projet_02_gestionnaire_taches_cli/
├── src/
│   ├── main.py              # Point d'entrée CLI
│   ├── models/
│   │   ├── tache.py        # Classe Tache
│   │   ├── projet.py       # Classe projet
│   │   └── tag.py         # Classe Tag
│   ├── services/
│   │   ├── gestionnaire.py  # Gestion des tâches
│   │   ├── filtre.py       # Filtrage avancé
│   │   └── exporteur.py    # Export CSV/JSON
│   └── utils/
│       ├── config.py       # Configuration
│       └── date_utils.py   # Manipulation dates
├── tests/
├── data/
│   └── taches.json        # Sauvegarde
├── README.md
└── requirements.txt
```

---

## Fonctionnalités

### 1. CRUD des Tâches

```python
class GestionnaireTaches:
    def creer_tache(self, titre: str, description: str = "", 
                   priorite: int = 3, echeance: datetime = None) -> Tache:
        tache = Tache(
            id=self._generer_id(),
            titre=titre,
            description=description,
            priorite=priorite,
            echeance=echeance,
            statut=StatutTache.A_FAIRE
        )
        self.taches.append(tache)
        return tache
    
    def lister_taches(self, filtre: FiltreTache = None) -> list[Tache]:
        resultat = self.taches
        if filtre:
            resultat = self.filtre.appliquer(resultat, filtre)
        return sorted(resultat, key=lambda t: t.priorite, reverse=True)
```

### 2. Système de Priorités

```python
PRIORITES = {
    1: ("Critique", "🔴"),
    2: ("Haute", "🟠"),
    3: ("Normale", "🟡"),
    4: ("Basse", "🟢"),
    5: ("Très basse", "⚪"),
}
```

### 3. Filtrage Avancé

```python
class FiltreTache:
    def appliquer(self, taches: list[Tache], criteres: dict) -> list[Tache]:
        resultat = taches
        
        if "statut" in criteres:
            resultat = [t for t in resultat if t.statut == criteres["statut"]]
        
        if "priorite_min" in criteres:
            resultat = [t for t in resultat if t.priorite >= criteres["priorite_min"]]
        
        if "projet" in criteres:
            resultat = [t for t in resultat if t.projet == criteres["projet"]]
        
        return resultat
```

### 4. Interface CLI

```
╔══════════════════════════════════════════════════╗
║           GESTIONNAIRE DE TÂCHES               ║
╠══════════════════════════════════════════════════╣
║  1. Lister tâches    2. Créer tâche          ║
║  3. Modifier tâche   4. Supprimer tâche      ║
║  5. Marquer fait    6. Filtrer             ║
║  7. Projets         8. Statistiques         ║
║  9. Exporter        10. Quitter            ║
╚══════════════════════════════════════════════════╝
```

---

## Modèle de Données

```python
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional, List
from enum import Enum
from uuid import uuid4


class StatutTache(Enum):
    A_FAIRE = "a_faire"
    EN_COURS = "en_cours"
    TERMINEE = "terminee"
    ANNULEE = "annulee"


class PrioriteTache(Enum):
    CRITIQUE = 1
    HAUTE = 2
    NORMALE = 3
    BASSE = 4
    TRES_BASSE = 5


@dataclass
class Tache:
    id: str
    titre: str
    description: str = ""
    statut: StatutTache = StatutTache.A_FAIRE
    priorite: int = 3
    projet: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    echeance: Optional[datetime] = None
    cree_le: datetime = field(default_factory=datetime.now)
    modifie_le: datetime = field(default_factory=datetime.now)
    terminee_le: Optional[datetime] = None
    
    def est_en_retard(self) -> bool:
        if self.echeance and self.statut != StatutTache.TERMINEE:
            return datetime.now() > self.echeance
        return False


@dataclass
class Projet:
    id: str
    nom: str
    description: str = ""
    couleur: str = "bleu"
    cree_le: datetime = field(default_factory=datetime.now)
    actif: bool = True
```

---

## Indications Progressives

### Niveau 1 - CRUD de Base

```python
class GestionnaireSimple:
    def __init__(self):
        self.taches = []
    
    def ajouter(self, titre: str):
        self.taches.append({"titre": titre, "terminee": False})
    
    def lister(self):
        for i, tache in enumerate(self.taches):
            etat = "✓" if tache["terminee"] else " "
            print(f"[{etat}] {tache['titre']}")
    
    def marquer_terminee(self, index: int):
        self.taches[index]["terminee"] = True
```

### Niveau 2 - Classes et Persistence

```python
class GestionnaireAvance:
    def __init__(self, fichier="data/taches.json"):
        self.fichier = fichier
        self.taches = self._charger()
    
    def _charger(self) -> list[dict]:
        import json
        if os.path.exists(self.fichier):
            with open(self.fichier) as f:
                return json.load(f)
        return []
    
    def _sauvegarder(self):
        import json
        with open(self.fichier, 'w') as f:
            json.dump(self.taches, f, indent=2)
```

---

## Configuration

Créez `data/taches.json` :

```json
[]
```

---

## Critères de Validation

- [ ] CRUD complet des tâches
- [ ] Système de priorités
- [ ] Échéances fonctionnelles
- [ ] Catégorisation (projets/tags)
- [ ] Filtrage avancé
- [ ] Sauvegarde JSON
- [ ] Export CSV

---

## Pièges Courants

### 1. Dates Mal Comparées
```python
if tache.echeance and datetime.now() > tache.echeance:
    print("En retard!")
```

### 2. Index Invalide
```python
try:
    self.taches[index]
except IndexError:
    print("Tache inexistante")
```

### 3. Fichier Non Trouvé
```python
try:
    self._charger()
except FileNotFoundError:
    self.taches = []
```

---

## Installation et Utilisation

```bash
python src/main.py
pytest tests/
python verification.py
```

---

## Ressources

- [Documentation Python datetime](https://docs.python.org/fr/3/library/datetime.html)
- [Module json](https://docs.python.org/fr/3/library/json.html)

---

## Objectifs d'Apprentissage

- Classes et instances
- Dates et heures
- Fichiers JSON
- Listes et dictionnaires
- CLI interactive

---

*Durée estimée : 6-8 heures | Difficulté : Intermédiaire*

---

[Retour au module](../README_PROJETS.md)
