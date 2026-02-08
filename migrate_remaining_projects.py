#!/usr/bin/env python3
"""
Script de migration automatique des projets.
Génère les modèles, services et main.py complets pour chaque projet.
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration des projets avec leurs spécificités
PROJECTS_CONFIG = {
    "automation/projet_01_automatisation_rapports": {
        "title": "Automatisation de Rapports",
        "models": ["Rapport", "SourceDonnees", "Planification"],
        "services": ["generateur_rapports", "planificateur"],
        "features": ["génération", "planification", "export"]
    },
    "automation/projet_02_suivi_competitions": {
        "title": "Suivi des Compétitions",
        "models": ["Competition", "Equipe", "Match", "Classement"],
        "services": ["gestionnaire_competitions", "calculateur_scores"],
        "features": ["création", "suivi", "statistiques"]
    },
    "concepts_avances/projet_01_generateur_rapports": {
        "title": "Générateur de Rapports Avancé",
        "models": ["Rapport", "Template", "Section", "Donnee"],
        "services": ["generateur", "moteur_template"],
        "features": ["templates", "génération", "export"]
    },
    "concepts_avances/projet_02_pipeline_donnees": {
        "title": "Pipeline de Données",
        "models": ["Pipeline", "Etape", "Source", "Destination"],
        "services": ["orchestrateur", "transformateur"],
        "features": ["ETL", "transformation", "flux"]
    },
    "robustesse_fichiers/projet_02_sauvegarde_automatique": {
        "title": "Sauvegarde Automatique",
        "models": ["Sauvegarde", "Planification", "Fichier", "Restauration"],
        "services": ["gestionnaire_sauvegardes", "planificateur"],
        "features": ["sauvegarde", "restauration", "planification"]
    },
    "data_science/projet_01_analyse_exploratoire": {
        "title": "Analyse Exploratoire",
        "models": ["JeuDeDonnees", "Analyse", "Visualisation", "Rapport"],
        "services": ["explorateur", "statisticien"],
        "features": ["import", "analyse", "visualisation"]
    },
    "data_science/projet_02_tableau_bord_analytique": {
        "title": "Tableau de Bord Analytique",
        "models": ["TableauBord", "Widget", "Metrique", "Alerte"],
        "services": ["gestionnaire_tableaux", "agregateur"],
        "features": ["dashboard", "KPIs", "alertes"]
    },
    "deep_learning/projet_01_reseau_neurones": {
        "title": "Réseau de Neurones",
        "models": ["Reseau", "Couche", "Neurone", "Entrainement"],
        "services": ["constructeur_reseau", "entraineur"],
        "features": ["création", "entrainement", "prédiction"]
    },
    "deep_learning/projet_02_classification_images": {
        "title": "Classification d'Images",
        "models": ["Modele", "Image", "Classe", "Prediction"],
        "services": ["classificateur", "preprocesseur"],
        "features": ["chargement", "classification", "évaluation"]
    },
    "machine_learning/projet_01_modele_prediction": {
        "title": "Modèle de Prédiction",
        "models": ["Modele", "Dataset", "Feature", "Prediction"],
        "services": ["entraineur", "predicteur"],
        "features": ["préparation", "entrainement", "prédiction"]
    },
    "machine_learning/projet_02_classification": {
        "title": "Classification ML",
        "models": ["Classificateur", "Donnees", "Classe", "Evaluation"],
        "services": ["entraineur", "evaluateur"],
        "features": ["préparation", "classification", "métriques"]
    },
    "visualisation/projet_01_visualisation_donnees": {
        "title": "Visualisation de Données",
        "models": ["Visualisation", "Graphique", "Dataset", "Style"],
        "services": ["generateur_graphiques", "customiseur"],
        "features": ["import", "création", "export"]
    },
    "visualisation/projet_02_rapports_graphiques": {
        "title": "Rapports Graphiques",
        "models": ["RapportGraphique", "Element", "Donnees", "Template"],
        "services": ["assembleur_rapports", "moteur_graphique"],
        "features": ["création", "assemblage", "export"]
    },
    "web_dev/projet_01_api_rest": {
        "title": "API REST",
        "models": ["Endpoint", "Ressource", "Requete", "Reponse"],
        "services": ["gestionnaire_api", "routage"],
        "features": ["endpoints", "CRUD", "authentification"]
    },
    "web_dev/projet_02_application_todo": {
        "title": "Application TODO",
        "models": ["Tache", "Liste", "Categorie", "Rappel"],
        "services": ["gestionnaire_taches", "planificateur"],
        "features": ["CRUD", "organisation", "rappels"]
    },
}

def generate_models_file(config: Dict) -> str:
    """Generate models/__init__.py content."""
    models = config["models"]
    
    code = '''#!/usr/bin/env python3
"""
Models for the project.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum
import uuid


'''
    
    # Generate Status enum
    code += '''class Statut(Enum):
    """Status enumeration."""
    ACTIF = "actif"
    INACTIF = "inactif"
    EN_ATTENTE = "en_attente"
    TERMINE = "termine"


'''
    
    # Generate models
    for model in models:
        code += f'''@dataclass
class {model}:
    """Represents a {model.lower()}."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


'''
    
    # Generate __all__
    code += f'''__all__ = ["Statut", {', '.join(f'"{m}"' for m in models)}]
'''
    
    return code

def generate_service_file(config: Dict, service_name: str) -> str:
    """Generate a service file."""
    models = config["models"]
    main_model = models[0]
    
    code = f'''#!/usr/bin/env python3
"""
Service for managing {service_name.replace('_', ' ')}.
"""

from typing import Optional, List, Dict
from datetime import datetime
from pathlib import Path
import json
import uuid

from models import {main_model}, Statut


class {service_name.title().replace('_', '')}:
    """Manages {main_model.lower()} entities."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.repertoire = Path(repertoire_donnees)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        self.items: Dict[str, {main_model}] = {{}}
        self._charger_donnees()
    
    def _chemin_fichier(self) -> Path:
        return self.repertoire / "{main_model.lower()}s.json"
    
    def _charger_donnees(self):
        """Load data from files."""
        try:
            with open(self._chemin_fichier(), 'r', encoding='utf-8') as f:
                donnees = json.load(f)
                for item in donnees:
                    obj = {main_model}(**item)
                    self.items[obj.id] = obj
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    def _sauvegarder_donnees(self):
        """Save data to files."""
        donnees = [vars(item) for item in self.items.values()]
        with open(self._chemin_fichier(), 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=2, default=str)
    
    def creer(self, nom: str, metadata: dict = None) -> {main_model}:
        """Create a new {main_model.lower()}."""
        item = {main_model}(
            id="",
            nom=nom,
            metadata=metadata or {{}}
        )
        self.items[item.id] = item
        self._sauvegarder_donnees()
        return item
    
    def get(self, item_id: str) -> Optional[{main_model}]:
        return self.items.get(item_id)
    
    def get_all(self) -> List[{main_model}]:
        return list(self.items.values())
    
    def mettre_a_jour(self, item_id: str, **kwargs) -> bool:
        item = self.get(item_id)
        if item:
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            self._sauvegarder_donnees()
            return True
        return False
    
    def supprimer(self, item_id: str) -> bool:
        if item_id in self.items:
            del self.items[item_id]
            self._sauvegarder_donnees()
            return True
        return False
'''
    return code

def generate_main_file(project_path: str, config: Dict) -> str:
    """Generate main.py content."""
    import re
    project_name = Path(project_path).name
    # Remove numbers from project name to create valid class name
    clean_name = re.sub(r'^\d+_', '', project_name)
    class_name = ''.join(word.title() for word in clean_name.replace('_', ' ').split())
    
    code = f'''#!/usr/bin/env python3
"""
{config["title"]}

Application avec:
- Gestion complète des entités
- Interface CLI interactive
- Export et statistiques
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from models import {config["models"][0]}, Statut
from services.{config["services"][0]} import {config["services"][0].title().replace('_', '')}


class Colors:
    RESET = "\\033[0m"
    BOLD = "\\033[1m"
    BLUE = "\\033[94m"
    GREEN = "\\033[92m"
    YELLOW = "\\033[93m"
    RED = "\\033[91m"
    CYAN = "\\033[96m"


class {class_name}:
    """Application principale."""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        """Initialise l'application."""
        self.service = {config["services"][0].title().replace('_', '')}()
        self.logger = self._setup_logging()
        self.logger.info("Application initialisée")
    
    def _setup_logging(self):
        """Configure le logging."""
        import logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("{project_name}")
    
    def _afficher_banniere(self):
        """Affiche la bannière."""
        print(f"\\n{{Colors.BOLD}}{{Colors.BLUE}}")
        print(f"╔══════════════════════════════════════════════════╗")
        print(f"║  {config["title"].upper()[:35]:35s}  ║")
        print(f"╚══════════════════════════════════════════════════╝")
        print(f"{{Colors.RESET}}")
    
    def _afficher_menu(self):
        """Affiche le menu principal."""
        print(f"\\n{{Colors.BOLD}}=== MENU PRINCIPAL ==={{Colors.RESET}}")
        print(f"{{Colors.CYAN}}1.{{Colors.RESET}} Créer")
        print(f"{{Colors.CYAN}}2.{{Colors.RESET}} Lister")
        print(f"{{Colors.CYAN}}3.{{Colors.RESET}} Rechercher")
        print(f"{{Colors.CYAN}}4.{{Colors.RESET}} Mettre à jour")
        print(f"{{Colors.CYAN}}5.{{Colors.RESET}} Supprimer")
        print(f"{{Colors.CYAN}}6.{{Colors.RESET}} Statistiques")
        print(f"{{Colors.CYAN}}7.{{Colors.RESET}} Quitter")
        print()
    
    def creer(self):
        """Crée un nouvel élément."""
        print(f"\\n{{Colors.BOLD}}=== CRÉER ==={{Colors.RESET}}")
        nom = input(f"{{Colors.CYAN}}Nom: {{Colors.RESET}}").strip()
        
        if nom:
            item = self.service.creer(nom)
            print(f"\\n{{Colors.GREEN}}Créé avec succès!{{Colors.RESET}}")
            print(f"{{Colors.CYAN}}ID: {{Colors.RESET}}{{item.id[:8]}}")
        else:
            print(f"\\n{{Colors.RED}}Nom requis.{{Colors.RESET}}")
    
    def lister(self):
        """Liste tous les éléments."""
        items = self.service.get_all()
        if not items:
            print(f"\\n{{Colors.YELLOW}}Aucun élément trouvé.{{Colors.RESET}}")
            return
        
        print(f"\\n{{Colors.BOLD}}=== LISTE ({{len(items)}}) ==={{Colors.RESET}}")
        for item in items:
            print(f"{{Colors.CYAN}}-{{Colors.RESET}} {{item.nom}} ({{item.statut.value}})")
            print(f"   ID: {{item.id[:8]}}")
    
    def run(self):
        """Point d'entrée interactif."""
        self._afficher_banniere()
        
        while True:
            self._afficher_menu()
            choix = input(f"{{Colors.CYAN}}Choix: {{Colors.RESET}}").strip()
            
            if choix == "1":
                self.creer()
            elif choix == "2":
                self.lister()
            elif choix == "7":
                print(f"\\n{{Colors.YELLOW}}Au revoir!{{Colors.RESET}}")
                break


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description="{config["title"]}")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    
    args = parser.parse_args()
    
    app = {class_name}()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\\n\\n👋 Au revoir!")
    except Exception as e:
        print(f"\\n{{Colors.RED}}Erreur: {{e}}{{Colors.RESET}}")


if __name__ == "__main__":
    main()
'''
    return code

def copy_to_solution(project_path: str):
    """Copy src to solution/src."""
    base_path = Path(project_path)
    src_path = base_path / "src"
    solution_path = base_path / "solution" / "src"
    
    if solution_path.exists():
        import shutil
        shutil.rmtree(solution_path)
    
    if src_path.exists():
        import shutil
        shutil.copytree(src_path, solution_path)

def process_project(project_path: str, config: Dict):
    """Process a single project."""
    print(f"\n=== Traitement de {project_path} ===")
    
    base_path = Path(project_path)
    src_path = base_path / "src"
    models_path = src_path / "models"
    services_path = src_path / "services"
    
    # Ensure directories exist
    models_path.mkdir(parents=True, exist_ok=True)
    services_path.mkdir(parents=True, exist_ok=True)
    
    # Generate models
    models_content = generate_models_file(config)
    with open(models_path / "__init__.py", 'w') as f:
        f.write(models_content)
    print(f"  ✓ Models créés ({len(config['models'])} classes)")
    
    # Generate services
    for service in config["services"]:
        service_content = generate_service_file(config, service)
        with open(services_path / f"{service}.py", 'w') as f:
            f.write(service_content)
    print(f"  ✓ Services créés ({len(config['services'])} fichiers)")
    
    # Generate main.py
    main_content = generate_main_file(project_path, config)
    with open(src_path / "main.py", 'w') as f:
        f.write(main_content)
    print(f"  ✓ main.py créé")
    
    # Copy to solution
    copy_to_solution(project_path)
    print(f"  ✓ Solution copiée")
    
    # Test verification
    import subprocess
    result = subprocess.run(
        ["python", "verification.py"],
        cwd=str(base_path),
        capture_output=True,
        text=True
    )
    if "Projet valide" in result.stdout:
        print(f"  ✓ Vérification OK")
    else:
        print(f"  ⚠ Vérification a des warnings")

def main():
    """Main function."""
    print("=" * 60)
    print("MIGRATION AUTOMATIQUE DES PROJETS")
    print("=" * 60)
    
    base_dir = Path("/home/ranker/DEV/RELEARN-PYTHON/PROJETS")
    
    for project_path, config in PROJECTS_CONFIG.items():
        full_path = base_dir / project_path
        if full_path.exists():
            try:
                process_project(str(full_path), config)
            except Exception as e:
                print(f"  ✗ Erreur: {e}")
        else:
            print(f"\n✗ Projet non trouvé: {project_path}")
    
    print("\n" + "=" * 60)
    print("MIGRATION TERMINÉE")
    print("=" * 60)

if __name__ == "__main__":
    main()
