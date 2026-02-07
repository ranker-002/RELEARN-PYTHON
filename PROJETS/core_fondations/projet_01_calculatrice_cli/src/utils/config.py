#!/usr/bin/env python3
"""
Configuration de la calculatrice.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional


class Config:
    """Gestionnaire de configuration."""
    
    DEFAULTS = {
        "precision": 10,
        "notation": "standard",
        "mode": "interactif",
        "theme": "clair",
        "historique_max": 100,
        "sauvegarde_auto": True,
        "operateurs_favoris": ["+", "-", "*", "/"],
    }
    
    def __init__(self, fichier: str = "data/config.json"):
        self.fichier = Path(fichier)
        self.config: Dict[str, Any] = {}
        self._charger()
    
    def _charger(self):
        """Charge la configuration depuis le fichier."""
        if self.fichier.exists():
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except (json.JSONDecodeError, KeyError):
                self.config = self.DEFAULTS.copy()
        else:
            self.config = self.DEFAULTS.copy()
    
    def _sauvegarder(self):
        """Sauvegarde la configuration dans le fichier."""
        self.fichier.parent.mkdir(parents=True, exist_ok=True)
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, cle: str, default: Any = None) -> Any:
        """Obtient une valeur de configuration."""
        return self.config.get(cle, default)
    
    def set(self, cle: str, valeur: Any):
        """Définit une valeur de configuration."""
        self.config[cle] = valeur
        self._sauvegarder()
    
    def reset(self):
        """Réinitialise la configuration par défaut."""
        self.config = self.DEFAULTS.copy()
        self._sauvegarder()
    
    def get_precision(self) -> int:
        """Retourne la précision des décimales."""
        return self.config.get("precision", 10)
    
    def set_precision(self, precision: int):
        """Définit la précision des décimales."""
        self.config["precision"] = max(0, min(precision, 20))
        self._sauvegarder()
    
    def get_notation(self) -> str:
        """Retourne la notation (standard, scientifique, engineering)."""
        return self.config.get("notation", "standard")
    
    def set_notation(self, notation: str):
        """Définit la notation."""
        if notation in ["standard", "scientifique", "engineering"]:
            self.config["notation"] = notation
            self._sauvegarder()
    
    def get_mode(self) -> str:
        """Retourne le mode (interactif, batch)."""
        return self.config.get("mode", "interactif")
    
    def set_mode(self, mode: str):
        """Définit le mode."""
        if mode in ["interactif", "batch"]:
            self.config["mode"] = mode
            self._sauvegarder()
    
    def get_theme(self) -> str:
        """Retourne le thème (clair, sombre)."""
        return self.config.get("theme", "clair")
    
    def set_theme(self, theme: str):
        """Définit le thème."""
        if theme in ["clair", "sombre"]:
            self.config["theme"] = theme
            self._sauvegarder()
    
    def exporter(self, chemin: str):
        """Exporte la configuration vers un fichier."""
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def importer(self, chemin: str):
        """Importe la configuration depuis un fichier."""
        with open(chemin, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self._sauvegarder()
