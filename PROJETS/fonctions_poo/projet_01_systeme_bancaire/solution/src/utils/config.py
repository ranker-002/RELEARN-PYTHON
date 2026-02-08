#!/usr/bin/env python3
"""
Configuration utilities.
"""

from pathlib import Path
from typing import Optional
import json


class Config:
    """Configuration management."""
    
    DEFAULT_CONFIG = {
        "devise": "EUR",
        "frais_tenue_compte": 2.0,
        "taux_interet_epargne": 0.5,
        "plafond_depot_espèces": 3000,
        "langue": "fr"
    }
    
    def __init__(self, fichier_config: Optional[str] = None):
        self.config = self.DEFAULT_CONFIG.copy()
        if fichier_config:
            self._charger_config(fichier_config)
    
    def _charger_config(self, fichier: str):
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
                self.config.update(donnees)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    def get(self, cle: str, default=None):
        return self.config.get(cle, default)
    
    def set(self, cle: str, valeur):
        self.config[cle] = valeur
    
    @property
    def devise(self) -> str:
        return self.config.get("devise", "EUR")
    
    @property
    def frais_tenue_compte(self) -> float:
        return self.config.get("frais_tenue_compte", 2.0)
