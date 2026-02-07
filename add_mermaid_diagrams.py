#!/usr/bin/env python3
"""
Script pour ajouter des diagrammes Mermaid aux README.md des projets.
"""

from pathlib import Path


DIAGRAMS_SECTION = '''
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
'''


def add_diagrams_to_readme(readme_path: Path, project_name: str = None):
    """Ajoute les diagrammes Mermaid à un README.md"""
    
    if not readme_path.exists():
        print(f"❌ README non trouvé: {readme_path}")
        return False
    
    content = readme_path.read_text(encoding='utf-8')
    
    if "## Architecture et Diagrammes" in content:
        print(f"⚠️  Diagrammes déjà présents: {readme_path}")
        return False
    
    sections_to_check = [
        ("## Installation", 150),
        ("## Ressources", 150),
        ("## Prérequis", 200),
        ("## Fonctionnalités", 200),
    ]
    
    insertion_point = None
    for section, min_offset in sections_to_check:
        idx = content.find(section)
        if idx != -1 and idx > min_offset:
            insertion_point = idx
            break
    
    if insertion_point is None:
        for i, line in enumerate(content.split('\n')):
            if line.startswith('---') and i > 20:
                insertion_point = content.find(line, i)
                break
    
    if insertion_point is None:
        insertion_point = len(content) - 100
    
    new_content = content[:insertion_point] + DIAGRAMS_SECTION + content[insertion_point:]
    
    readme_path.write_text(new_content, encoding='utf-8')
    print(f"✅ Diagrammes ajoutés: {readme_path}")
    return True


def main():
    base_path = Path("/home/ranker/DEV/RELEARN-PYTHON/PROJETS")
    
    readmes_updated = 0
    
    for module_path in sorted(base_path.iterdir()):
        if not module_path.is_dir():
            continue
        
        for project_path in sorted(module_path.glob("projet_*")):
            if not project_path.is_dir():
                continue
            
            readme_path = project_path / "README.md"
            if readme_path.exists():
                if add_diagrams_to_readme(readme_path):
                    readmes_updated += 1
    
    print(f"\n🎉 Total: {readmes_updated} README.md mis à jour avec diagrammes Mermaid")


if __name__ == "__main__":
    main()
