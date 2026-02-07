#!/usr/bin/env python3
"""
Script pour enrichir les README.md des projets.
Version améliorée avec parsing plus robuste.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple


# Modèles spécifiques par type de projet
PROJECT_TEMPLATES = {
    "web_scraping": {
        "intro": "Le web scraping est l'art d'extraire automatiquement des données depuis les sites web.",
        "tools": ["requests", "BeautifulSoup", "lxml", "Selenium"],
        "concepts": ["HTML parsing", "CSS selectors", "XPath", "API discovery"],
        "skill1": "Requêtes HTTP avec requests",
    },
    "automation": {
        "intro": "L'automatisation permet de programmer des tâches répétitives pour gagner du temps.",
        "tools": ["schedule", "python-dotenv", "smtplib", "selenium"],
        "concepts": ["Planification", "Envoi d'emails", "Manipulation de fichiers", "APIs"],
        "skill1": "Planification de tâches avec schedule",
    },
    "data_science": {
        "intro": "La data science transforme les données brutes en insights actionnables.",
        "tools": ["pandas", "numpy", "scipy", "jupyter"],
        "concepts": ["Nettoyage de données", "Statistiques", "EDA", "Visualisation"],
        "skill1": "Manipulation de données avec pandas",
    },
    "visualisation": {
        "intro": "La visualisation de données communique efficacement les informations complexes.",
        "tools": ["matplotlib", "seaborn", "plotly", "bokeh"],
        "concepts": ["Graphiques", "Tableaux de bord", "Animations", "Cartographie"],
        "skill1": "Création de graphiques avec matplotlib",
    },
    "machine_learning": {
        "intro": "Le machine learning permet aux ordinateurs d'apprendre sans être explicitement programmés.",
        "tools": ["scikit-learn", "xgboost", "lightgbm", "pandas"],
        "concepts": ["Régression", "Classification", "Clustering", "Évaluation"],
        "skill1": "Entraînement de modèles avec scikit-learn",
    },
    "deep_learning": {
        "intro": "Le deep learning utilise des réseaux de neurones profonds pour résoudre des problèmes complexes.",
        "tools": ["torch", "tensorflow", "keras", "torchvision"],
        "concepts": ["Réseaux CNN", "RNN/LSTM", "Transfer Learning", "GPU Training"],
        "skill1": "Création de réseaux de neurones avec PyTorch",
    },
    "web_dev": {
        "intro": "Le développement web crée des applications accessibles via un navigateur.",
        "tools": ["fastapi", "flask", "jinja2", "sqlalchemy"],
        "concepts": ["API REST", "Bases de données", "Authentification", "Déploiement"],
        "skill1": "Création d'APIs REST avec FastAPI",
    },
    "robustesse_fichiers": {
        "intro": "La gestion robuste des fichiers garantit la fiabilité des applications.",
        "tools": ["pathlib", "json", "csv", "shutil"],
        "concepts": ["Lecture/écriture", "Gestion d'erreurs", "Sérialisation", "Permissions"],
        "skill1": "Manipulation de fichiers avec pathlib",
    },
    "concepts_avances": {
        "intro": "Les concepts avancés différencient le code amateur du code professionnel.",
        "tools": ["functools", "itertools", "typing", "asyncio"],
        "concepts": ["Décorateurs", "Générateurs", "Type hints", "Concurrence"],
        "skill1": "Création de décorateurs avancés",
    },
    "core_fondations": {
        "intro": "Les fondations core maîtrisent les bases essentielles de Python.",
        "tools": ["builtins", "dataclasses", "enum"],
        "concepts": ["Variables", "Boucles", "Fonctions", "POO"],
        "skill1": "Manipulation de variables et types",
    },
    "fonctions_poo": {
        "intro": "La programmation orientée objet modélise le monde réel en classes et objets.",
        "tools": ["dataclasses", "abc", "enum"],
        "concepts": ["Classes", "Héritage", "Polymorphisme", "Encapsulation"],
        "skill1": "Création de classes et objets",
    },
}


def get_module_info(module_name: str) -> Dict:
    """Récupère les infos pour un module."""
    return PROJECT_TEMPLATES.get(module_name, {
        "intro": "Ce projet vous permet d'appliquer vos connaissances Python.",
        "tools": ["requests", "python"],
        "concepts": ["Programmation"],
        "skill1": "Programmation Python",
    })


def extract_readme_info(readme_path: Path) -> Tuple[str, str, str]:
    """Extrait les infos du README existant."""
    content = readme_path.read_text(encoding='utf-8')
    
    # Titre
    title_match = re.search(r'^#\s*(?:Projet|Project):\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Project Name"
    
    # Difficulté
    diff_match = re.search(r'\*\*([^*]+)\*\*', content)
    difficulty = diff_match.group(1).strip() if diff_match else "Intermédiaire"
    
    # Heures
    hours_match = re.search(r'(\d+[-\d]*)\s*heures?', content)
    hours = hours_match.group(1) if hours_match else "8-12"
    
    return title, difficulty, hours


def extract_features(content: str) -> List[str]:
    """Extrait les fonctionnalités."""
    features = []
    
    # Chercher les sections avec -
    lines = content.split('\n')
    current_feature = None
    
    for line in lines:
        # Titre de feature (###)
        if line.startswith('### '):
            current_feature = line[4:].strip()
            # Nettoyer les préfixes comme "Core Features (Mandatory)"
            if '(' in current_feature:
                current_feature = current_feature.split('(')[0].strip()
        elif line.strip().startswith('- ') and current_feature:
            features.append(current_feature)
            current_feature = None
    
    return list(set(features[:6]))  # Max 6 features


def create_enriched_readme(
    project_path: Path,
    module_info: Dict,
    title: str,
    difficulty: str,
    hours: str,
    features: List[str]
) -> str:
    """Crée un README enrichi."""
    
    slug = project_path.name
    tools = module_info.get("tools", ["python"])
    concepts = module_info.get("concepts", ["programming"])
    skill1 = module_info.get("skill1", "Programmation")
    intro = module_info.get("intro", "Un projet Python complet.")
    
    features_section = ""
    for i, feature in enumerate(features[:5], 1):
        features_section += f"""
### {i}. {feature.capitalize()}

- Implémentation de {feature.lower()}
- Tests unitaires associés
- Documentation du code
"""
    
    readme = f'''# {title}

{intro}

---

## Introduction

{intro}

**Outils utilisés:** {', '.join(tools)}

**Concepts clés:** {', '.join(concepts)}

### {title} en action

```
┌─────────────────────────────────────────────────────────┐
│                    {title[:40]:^40} │
├─────────────────────────────────────────────────────────┤
│  🎯 Objectif: Appliquer {concepts[0].lower()}          │
│  📚 Outils: {tools[0]:<15}                             │
│  ⏱️  Durée: {hours} heures                            │
└─────────────────────────────────────────────────────────┘
```

---

## Prérequis

- **Module recommandé**: [Web Scraping](../../05_domaines_specifies/21_web_scraping/README_MODULE.md)
- Compétences requises:
  - {skill1}
'''

    # Ajouter skills spécifiques
    skills_map = {
        "requests": "  - Requêtes HTTP avec requests",
        "BeautifulSoup": "  - Parsing HTML avec BeautifulSoup",
        "pandas": "  - Manipulation de données avec pandas",
        "fastapi": "  - Création d'APIs REST avec FastAPI",
        "torch": "  - Réseaux de neurones avec PyTorch",
        "scikit-learn": "  - Machine learning avec scikit-learn",
        "matplotlib": "  - Visualisation avec matplotlib",
        "selenium": "  - Automatisation de navigateur avec Selenium",
    }
    
    for tool in tools[:3]:
        tool_lower = tool.lower()
        if tool_lower in skills_map and skills_map[tool_lower] not in readme:
            readme += skills_map[tool_lower] + "\n"
    
    readme += """
---

## Structure du Projet

```
"""
    readme += f"""{slug}/
├── src/
│   ├── main.py              # Point d'entrée CLI/API
│   ├── models/
│   │   └── *.py             # Classes métier
│   ├── services/
│   │   └── *.py             # Logique métier
│   └── utils/
│       └── *.py             # Helpers
├── tests/
│   └── test_*.py            # Tests unitaires
├── data/
│   ├── sample/              # Données d'exemple
│   │   └── *.csv/json/xml
│   └── input/              # Données de test
├── README.md
└── requirements.txt
```
"""
    
    readme += """
---

## Fonctionnalités

"""
    readme += features_section
    
    readme += """
---

## Modèle de Données

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Model:
    """Description du modèle."""
    id: str
    name: str
    status: Status = Status.PENDING
    created_at: datetime = None
    data: Optional[dict] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def is_valid(self) -> bool:
        """Valide le modèle."""
        return bool(self.id and self.name)
```

---

## Indications Progressives

### 🚦 Niveau 1 - Découverte

**Objectif:** Comprendre la structure de base

```python
# Structure de base à implémenter
class Project:
    def __init__(self, config: dict):
        self.config = config
        self.data = []
    
    def load(self) -> bool:
        """Charge les données."""
        pass
    
    def process(self) -> list:
        """Traite les données."""
        pass
```

**Indice:** Commencez par identifier les entités principales et leurs relations.

---

### 🚦🚦 Niveau 2 - Approfondissement

**Objectif:** Implémenter la logique métier

```python
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class Processor:
    def __init__(self, config: dict):
        self.config = config
        self.results = []
    
    def run(self, data: dict) -> Optional[dict]:
        """Exécute le traitement avec validation."""
        if not data:
            logger.error("Aucune donnée fournie")
            return None
        
        required = self.config.get("required_fields", [])
        for field in required:
            if field not in data:
                logger.error(f"Champ manquant: {field}")
                return None
        
        return self._process(data)
    
    def _process(self, data: dict) -> dict:
        """Logique de traitement."""
        pass
```

---

### 🚦🚦🚦 Niveau 3 - Expert

**Objectif:** Production-ready avec robustesse

```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
import json

@dataclass
class Result:
    id: str
    data: Dict
    timestamp: datetime
    success: bool
    error: Optional[str] = None

class ExpertProcessor:
    def __init__(self, config: dict, max_retries: int = 3):
        self.config = config
        self.max_retries = max_retries
        self.results: List[Result] = []
    
    def pipeline(self, inputs: List[dict]) -> List[Result]:
        """Exécute le pipeline complet."""
        for item in inputs:
            result = self._process_with_retry(item)
            self.results.append(result)
        return self.results
    
    def _process_with_retry(self, item: dict) -> Result:
        """Traitement avec retry automatique."""
        for attempt in range(self.max_retries):
            try:
                result = self._execute(item)
                return Result(
                    id=str(uuid.uuid4()),
                    data=item,
                    timestamp=datetime.now(),
                    success=True,
                    result=result
                )
            except Exception as e:
                if attempt == self.max_retries - 1:
                    return Result(
                        id=str(uuid.uuid4()),
                        data=item,
                        timestamp=datetime.now(),
                        success=False,
                        error=str(e)
                    )
        return Result(
            id=str(uuid.uuid4()),
            data=item,
            timestamp=datetime.now(),
            success=False
        )
    
    def _execute(self, item: dict) -> dict:
        pass
    
    def export(self, filepath: str):
        """Exporte les résultats."""
        with open(filepath, 'w') as f:
            json.dump([r.__dict__ for r in self.results], f, default=str)
```

---

## Configuration

```json
{
  "settings": {
    "input_file": "data/sample/input.csv",
    "output_file": "results/output.json",
    "log_level": "INFO"
  },
  "processing": {
    "batch_size": 100,
    "max_retries": 3,
    "timeout": 30
  }
}
```

---

## Critères de Validation

- [ ] **Structure**: Code organisé selon la structure recommandée
- [ ] **Fonctionnalités core**: Toutes les fonctionnalités obligatoires implémentées
- [ ] **Gestion erreurs**: Erreurs gérées gracieusement
- [ ] **Type hints**: Code utilise des annotations de type
- [ ] **Documentation**: Fonctions publiques avec docstrings
- [ ] **Tests**: Tests passent avec pytest
- [ ] **Exécution**: Projet s'exécute sans erreurs

---

## Pièges Courants

1. **Validation des entrées**: Toujours valider avant de traiter
   - **Solution**: Utilisez try/except et vérification de types

2. **Gestion de la mémoire**: Gros volumes peuvent saturer la RAM
   - **Solution**: Utilisez des générateurs pour les grands fichiers

3. **Récupération d'erreurs**: Gérez les échecs partiels
   - **Solution**: Implémentez des checkpoints et retry logic

---

## Installation et Utilisation

```bash
# Installer les dépendances
uv sync --extra web-scraping

# Lancer le projet
python src/main.py

# Exécuter les tests
pytest tests/ -v

# Valider votre implémentation
python verification.py
```

---

## Ressources

### Documentation
- [Documentation Python](https://docs.python.org/fr/3/)
- [Documentation {tool}](https://docs.python-requests.org/)

### Tutoriels
- [Real Python](https://realpython.com/)
- [Official Tutorials](https://docs.python.org/fr/3/tutorial/)

### Outils
- [PyPI](https://pypi.org/)
- [Python Weekly](https://pythonweekly.com/)

---

## Objectifs d'Apprentissage

À la fin de ce projet, vous serez capables de:
- ✅ Appliquer {concept1} dans un projet réel
- ✅ Structurer un projet Python professionnel
- ✅ Implémenter une gestion d'erreurs robuste
- ✅ Écrire du code maintenable et testable

---

*Durée estimée: {hours} heures | Difficulté: {difficulty}*

---

[Retour au module](../README_PROJETS.md)
"""
    
    # Remplacer les placeholders
    readme = readme.replace("{tool}", tools[0] if tools else "python")
    readme = readme.replace("{concept1}", concepts[0].lower() if concepts else "programming")
    readme = readme.replace("{hours}", hours)
    readme = readme.replace("{difficulty}", difficulty)
    
    return readme


def enrich_all_readmes():
    """Enrichit tous les README.md des projets."""
    base_path = Path(__file__).parent / "PROJETS"
    
    print("\n=== Enrichissement des README.md ===\n")
    
    enriched = 0
    
    for module_dir in sorted(base_path.iterdir()):
        if not module_dir.is_dir():
            continue
        
        module_name = module_dir.name
        module_info = get_module_info(module_name)
        
        for project_dir in sorted(module_dir.iterdir()):
            if not project_dir.is_dir():
                continue
            
            readme_path = project_dir / "README.md"
            if not readme_path.exists():
                continue
            
            # Extraire les infos
            title, difficulty, hours = extract_readme_info(readme_path)
            
            # Extraire les fonctionnalités
            content = readme_path.read_text(encoding='utf-8')
            features = extract_features(content)
            
            # Créer le nouveau README
            new_readme = create_enriched_readme(
                project_dir, module_info, title, difficulty, hours, features
            )
            
            # Sauvegarder
            readme_path.write_text(new_readme, encoding='utf-8')
            enriched += 1
            print(f"✅ {module_name}/{project_dir.name}")
    
    print(f"\n=== {enriched} README.md enrichis ===\n")


if __name__ == "__main__":
    enrich_all_readmes()
