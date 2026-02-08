#!/usr/bin/env python3
"""
Configuration du gestionnaire de tâches.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional


class Config:
    """Gestionnaire de configuration."""
    
    DEFAULTS = {
        "theme": "clair",
        "format_date": "%d/%m/%Y",
        "format_heure": "%H:%M",
        "afficher_priorites": True,
        "afficher_projets": True,
        "afficher_tags": True,
        "taches_par_page": 10,
        "sauvegarde_auto": True,
    }
    
    def __init__(self, fichier: str = "data/config.json"):
        self.fichier = Path(fichier)
        self.config: Dict[str, Any] = {}
        self._charger()
    
    def _charger(self):
        if self.fichier.exists():
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except (json.JSONDecodeError, KeyError):
                self.config = self.DEFAULTS.copy()
        else:
            self.config = self.DEFAULTS.copy()
    
    def _sauvegarder(self):
        self.fichier.parent.mkdir(parents=True, exist_ok=True)
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, cle: str, default: Any = None) -> Any:
        return self.config.get(cle, default)
    
    def set(self, cle: str, valeur: Any):
        self.config[cle] = valeur
        self._sauvegarder()
    
    def reset(self):
        self.config = self.DEFAULTS.copy()
        self._sauvegarder()
    
    def get_theme(self) -> str:
        return self.config.get("theme", "clair")
    
    def set_theme(self, theme: str):
        if theme in ["clair", "sombre"]:
            self.config["theme"] = theme
            self._sauvegarder()
    
    def get_format_date(self) -> str:
        return self.config.get("format_date", "%d/%m/%Y")
    
    def get_format_heure(self) -> str:
        return self.config.get("format_heure", "%H:%M")
    
    def get_taches_par_page(self) -> int:
        return self.config.get("taches_par_page", 10)
    
    def set_taches_par_page(self, nombre: int):
        self.config["taches_par_page"] = max(1, min(nombre, 100))
        self._sauvegarder()
    
    def exporter(self, chemin: str):
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2)
    
    def importer(self, chemin: str):
        with open(chemin, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self._sauvegarder()
