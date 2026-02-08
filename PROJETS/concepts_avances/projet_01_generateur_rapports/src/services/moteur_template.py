#!/usr/bin/env python3
"""
Service for managing moteur template.
"""

from typing import Optional, List, Dict
from datetime import datetime
from pathlib import Path
import json
import uuid

from models import Rapport, Statut


class MoteurTemplate:
    """Manages rapport entities."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.repertoire = Path(repertoire_donnees)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        self.items: Dict[str, Rapport] = {}
        self._charger_donnees()
    
    def _chemin_fichier(self) -> Path:
        return self.repertoire / "rapports.json"
    
    def _charger_donnees(self):
        """Load data from files."""
        try:
            with open(self._chemin_fichier(), 'r', encoding='utf-8') as f:
                donnees = json.load(f)
                for item in donnees:
                    obj = Rapport(**item)
                    self.items[obj.id] = obj
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    def _sauvegarder_donnees(self):
        """Save data to files."""
        donnees = [vars(item) for item in self.items.values()]
        with open(self._chemin_fichier(), 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=2, default=str)
    
    def creer(self, nom: str, metadata: dict = None) -> Rapport:
        """Create a new rapport."""
        item = Rapport(
            id="",
            nom=nom,
            metadata=metadata or {}
        )
        self.items[item.id] = item
        self._sauvegarder_donnees()
        return item
    
    def get(self, item_id: str) -> Optional[Rapport]:
        return self.items.get(item_id)
    
    def get_all(self) -> List[Rapport]:
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
