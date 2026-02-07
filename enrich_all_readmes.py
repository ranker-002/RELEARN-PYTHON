#!/usr/bin/env python3
"""
Script pour enrichir les README.md avec un format spécifique par domaine.
Applique le même format que l'agrégateur RSS aux autres projets.
"""

import json
from pathlib import Path
from typing import Dict, List


# Templates par type de projet
TEMPLATES = {
    "automation": {
        "intro": "L'automatisation permet de programmer des tâches répétitives pour gagner du temps.",
        "concepts": ["Planification", "Envoi d'emails", "APIs", "Logs"],
        "features": [
            ("Génération de Rapports", ["Templates Jinja2", "Graphiques matplotlib", "Tableaux de données"]),
            ("Envoi Automatique", ["SMTP", "Emails HTML", "Pièces jointes"]),
            ("Planification", ["Cron/schedule", "Exécution programmée", "Logs d'exécution"]),
        ],
        "tools": ["jinja2", "matplotlib", "smtplib", "schedule"],
        "data_format": "JSON/YAML",
    },
    "web_scraping": {
        "intro": "Le web scraping extrait automatiquement des données depuis les sites web.",
        "concepts": ["Parsing HTML", "CSS Selectors", "APIs", "Rate Limiting"],
        "features": [
            ("Parsing RSS/Atom", ["Format XML", "Dates RFC 822", "Catégories"]),
            ("API REST", ["Endpoints", "Authentification", "Pagination"]),
            ("Notifications", ["Email", "Desktop", "Webhooks"]),
        ],
        "tools": ["requests", "BeautifulSoup", "lxml"],
        "data_format": "XML/JSON",
    },
    "data_science": {
        "intro": "La data science transforme les données brutes en insights actionnables.",
        "concepts": ["Nettoyage", "Statistiques", "Corrélations", "Visualisation"],
        "features": [
            ("Nettoyage", ["Valeurs manquantes", "Duplicatas", "Outliers"]),
            ("Analyse Statistique", ["Moyenne/Médiane", "Écart-type", "Corrélations"]),
            ("Visualisation", ["Distributions", "Scatter plots", "Heatmaps"]),
        ],
        "tools": ["pandas", "numpy", "matplotlib", "seaborn"],
        "data_format": "CSV/Pandas",
    },
    "visualisation": {
        "intro": "La visualisation de données communique efficacement les informations complexes.",
        "concepts": ["Graphiques", "Tableaux de bord", "Couleurs", "Accessibility"],
        "features": [
            ("Style", ["Themes matplotlib", "Polices professionnelles", "Haute résolution"]),
            ("Types de Graphiques", ["Line/Bar/Scatter", "Heatmaps", "Cartographies"]),
            ("Export", ["PNG/SVG", "Format académique", "Interactive plots"]),
        ],
        "tools": ["matplotlib", "seaborn", "plotly", "bokeh"],
        "data_format": "CSV/Pandas",
    },
    "machine_learning": {
        "intro": "Le machine learning permet aux ordinateurs d'apprendre sans être programmés explicitement.",
        "concepts": ["Régression", "Classification", "Feature Engineering", "Validation"],
        "features": [
            ("Prétraitement", ["Normalisation", "Encoding", "Split train/test"]),
            ("Modèles", ["Linear Regression", "Random Forest", "XGBoost"]),
            ("Évaluation", ["Cross-validation", "RMSE/MAE/R2", "Feature importance"]),
        ],
        "tools": ["scikit-learn", "pandas", "numpy", "xgboost"],
        "data_format": "CSV/Scikit-learn",
    },
    "deep_learning": {
        "intro": "Le deep learning utilise des réseaux de neurones profonds pour résoudre des problèmes complexes.",
        "concepts": ["Réseaux CNN", "Backpropagation", "Gradients", "GPU Training"],
        "features": [
            ("Architecture", ["Dense layers", "Dropout", "BatchNorm"]),
            ("Entraînement", ["Forward/backward pass", "Early stopping", "Learning rate"]),
            ("Données", ["MNIST/CIFAR", "Data augmentation", "Tensor loading"]),
        ],
        "tools": ["torch", "tensorflow", "keras", "torchvision"],
        "data_format": "Tensors/Images",
    },
    "web_dev": {
        "intro": "Le développement web crée des applications accessibles via un navigateur.",
        "concepts": ["API REST", "CRUD", "Authentification", "Base de données"],
        "features": [
            ("Endpoints CRUD", ["POST/GET/PUT/DELETE", "Pagination", "Filtres"]),
            ("Authentification", ["JWT", "OAuth", "Permissions"]),
            ("Documentation", ["Swagger/OpenAPI", "Tests automatisés"]),
        ],
        "tools": ["fastapi", "flask", "sqlalchemy", "uvicorn"],
        "data_format": "JSON/API",
    },
    "robustesse_fichiers": {
        "intro": "La gestion robuste des fichiers garantit la fiabilité des applications.",
        "concepts": ["Lecture/Écriture", "Gestion d'erreurs", "Permissions", "Chemins sécurisés"],
        "features": [
            ("Navigation", ["Lister fichiers", "Changer répertoire", "Recherche"]),
            ("Opérations", ["Copier/Déplacer", "Supprimer avec confirmation", "Créer dossiers"]),
            ("Sécurité", ["Validation des chemins", "Permissions", "Gestion d'erreurs"]),
        ],
        "tools": ["pathlib", "shutil", "os", "stat"],
        "data_format": "Multiples formats",
    },
    "concepts_avances": {
        "intro": "Les concepts avancés différencient le code amateur du code professionnel.",
        "concepts": ["Décorateurs", "Générateurs", "Type hints", "Concurrence"],
        "features": [
            ("Décorateurs", ["@log", "@validate", "@retry", "@cache"]),
            ("Générateurs", ["Streaming", "Yield", "Itertools"]),
            ("Pipeline", ["Extraction", "Transformation", "Génération rapport"]),
        ],
        "tools": ["functools", "itertools", "typing", "asyncio"],
        "data_format": "JSON/CSV",
    },
    "fonctions_poo": {
        "intro": "La programmation orientée objet modélise le monde réel en classes et objets.",
        "concepts": ["Classes", "Héritage", "Polymorphisme", "Encapsulation"],
        "features": [
            ("Classes", ["Attributs", "Méthodes", "Properties"]),
            ("Héritage", ["Super()", "Méthodes override", "Multiple inheritance"]),
            ("Exceptions", ["Custom exceptions", "Try/except", "Gestion gracieuse"]),
        ],
        "tools": ["dataclasses", "abc", "enum"],
        "data_format": "JSON/Objet",
    },
}


def get_project_info(project_dir: Path) -> Dict:
    """Récupère les infos du projet."""
    readme_path = project_dir / "README.md"
    if not readme_path.exists():
        return {}
    
    content = readme_path.read_text(encoding='utf-8')
    
    # Extraire le titre
    import re
    title_match = re.search(r'^#\s*(?:Projet|Project):\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else project_dir.name
    
    # Difficulté et heures
    diff_match = re.search(r'\*\*([^*]+)\*\*', content)
    difficulty = diff_match.group(1).strip() if diff_match else "Intermédiaire"
    
    hours_match = re.search(r'(\d+[-\d]*)\s*heures?', content)
    hours = hours_match.group(1) if hours_match else "8-12"
    
    return {"title": title, "difficulty": difficulty, "hours": hours}


def create_enriched_readme(project_dir: Path, module_info: Dict) -> str:
    """Crée un README enrichi."""
    
    project_name = project_dir.name
    title = module_info.get("title", project_name)
    difficulty = module_info.get("difficulty", "Intermédiaire")
    hours = module_info.get("hours", "8-12")
    
    intro = module_info.get("intro", "Un projet Python complet.")
    concepts = module_info.get("concepts", ["Concept 1", "Concept 2"])
    features = module_info.get("features", [])
    tools = module_info.get("tools", ["python"])
    data_format = module_info.get("data_format", "JSON")
    
    # Générer la section fonctionnalités
    features_section = ""
    for i, (feature_name, items) in enumerate(features[:4], 1):
        items_html = "\n".join(f"  - {item}" for item in items[:4])
        features_section += f"""
### {i}. {feature_name}

{items_html}
"""
    
    # Créer le README complet
    readme = f'''# {title}

{intro}

---

## Introduction

Ce projet vous permet d'appliquer les concepts clés de {concepts[0].lower()} dans un projet réel et professionnel.

**Concepts clés:** {', '.join(concepts[:4])}

**Outils utilisés:** {', '.join(tools[:4])}

**Format de données:** {data_format}

```
┌─────────────────────────────────────────────────────────┐
│                    {title[:40]:^40} │
├─────────────────────────────────────────────────────────┤
│  🎯 Objectif: Appliquer {concepts[0].lower()}           │
│  📚 Outils: {tools[0]:<15}                             │
│  ⏱️  Durée: {hours} heures                            │
└─────────────────────────────────────────────────────────┘
```

---

## Prérequis

- **Module recommandé**: [Web Scraping](../../05_domaines_specifies/21_web_scraping/README_MODULE.md)
- Compétences nécessaires:
'''
    
    # Compétences spécifiques
    skills_map = {
        "requests": "  - Requêtes HTTP avec requests",
        "BeautifulSoup": "  - Parsing HTML avec BeautifulSoup",
        "pandas": "  - Manipulation de données avec pandas",
        "fastapi": "  - Création d'APIs REST avec FastAPI",
        "torch": "  - Réseaux de neurones avec PyTorch",
        "scikit-learn": "  - Machine learning avec scikit-learn",
        "matplotlib": "  - Visualisation avec matplotlib",
        "selenium": "  - Automatisation de navigateur avec Selenium",
        "jinja2": "  - Templates avec Jinja2",
        "pathlib": "  - Manipulation de fichiers avec pathlib",
    }
    
    for tool in tools[:3]:
        tool_lower = tool.lower()
        if tool_lower in skills_map:
            readme += skills_map[tool_lower] + "\n"
    
    readme += """
---

## Structure du Projet

```
"""
    readme += f'''{project_name}/
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
    \"\"\"Description du modèle.\"\"\"
    id: str
    name: str
    status: Status = Status.PENDING
    created_at: datetime = None
    data: Optional[dict] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def is_valid(self) -> bool:
        \"\"\"Valide le modèle.\"\"\"
        return bool(self.id and self.name)
```

---

## Indications Progressives

### Niveau 1 - Découverte

**Objectif:** Comprendre la structure de base

```python
# Structure de base à implémenter
class Project:
    def __init__(self, config: dict):
        self.config = config
        self.data = []
    
    def load(self) -> bool:
        \"\"\"Charge les données.\"\"\"
        # TODO: Implémenter
        pass
    
    def process(self) -> list:
        \"\"\"Traite les données.\"\"\"
        # TODO: Implémenter
        pass
```

**Indice:** Commencez par identifier les entités principales et leurs relations.

---

### Niveau 2 - Approfondissement

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
        \"\"\"Exécute le traitement avec validation.\"\"\"
        if not data:
            logger.error("Aucune donnée fournie")
            return None
        
        required = self.config.get("required_fields", [])
        for field in required:
            if field not in data:
                logger.error(f"Champ manquant: {{field}}")
                return None
        
        return self._process(data)
    
    def _process(self, data: dict) -> dict:
        \"\"\"Logique de traitement.\"\"\"
        pass
```

---

### Niveau 3 - Expert

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
        \"\"\"Exécute le pipeline complet.\"\"\"
        for item in inputs:
            result = self._process_with_retry(item)
            self.results.append(result)
        return self.results
    
    def _process_with_retry(self, item: dict) -> Result:
        \"\"\"Traitement avec retry automatique.\"\"\"
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
        \"\"\"Exporte les résultats.\"\"\"
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
- [Documentation {tool}](https://docs.python.org/)

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
        module_info = TEMPLATES.get(module_name, TEMPLATES["automation"])
        
        for project_dir in sorted(module_dir.iterdir()):
            if not project_dir.is_dir():
                continue
            
            # Skip le projet déjà enrichi manuellement
            if "aggregateur_actualites" in project_dir.name:
                print(f"⏭️  {module_name}/{project_dir.name} (déjà enrichi)")
                continue
            
            project_info = get_project_info(project_dir)
            new_readme = create_enriched_readme(project_dir, {**module_info, **project_info})
            
            readme_path = project_dir / "README.md"
            if readme_path.exists():
                readme_path.write_text(new_readme, encoding='utf-8')
                enriched += 1
                print(f"✅ {module_name}/{project_dir.name}")
    
    print(f"\n=== {enriched} README.md enrichis ===\n")


if __name__ == "__main__":
    enrich_all_readmes()
