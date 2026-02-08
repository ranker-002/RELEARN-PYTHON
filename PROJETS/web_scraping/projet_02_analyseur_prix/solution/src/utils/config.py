#!/usr/bin/env python3
"""
Gestion de la configuration.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional, List


class Config:
    """Gestionnaire de configuration."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialise la configuration.
        
        Args:
            config_path: Chemin du fichier de configuration
        """
        self.config: Dict[str, Any] = {}
        self.config_path = config_path
        
        if config_path and Path(config_path).exists():
            self.load(config_path)
        else:
            self._defaults()
    
    def _defaults(self):
        """Définit les valeurs par défaut."""
        self.config = {
            "produits": [],
            "alertes": {
                "email": "",
                "notification": False,
            },
            "scraper": {
                "timeout": 10,
                "retry": 3,
            },
            "export": {
                "format": "csv",
                "repertoire": "data/exports",
            },
        }
    
    def load(self, config_path: str) -> "Config":
        """
        Charge la configuration depuis un fichier.
        
        Args:
            config_path: Chemin du fichier JSON
            
        Returns:
            self
        """
        path = Path(config_path)
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
            self.config_path = config_path
        else:
            self._defaults()
        return self
    
    def save(self, config_path: Optional[str] = None) -> str:
        """
        Sauvegarde la configuration.
        
        Args:
            config_path: Chemin du fichier (utilise le chemin actuel si non fourni)
            
        Returns:
            Chemin du fichier sauvegardé
        """
        path = config_path or self.config_path
        if path is None:
            path = "config.json"
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
        
        return path
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Obtient une valeur de configuration.
        
        Args:
            key: Clé (peut utiliser des points pour les sous-clés)
            default: Valeur par défaut
            
        Returns:
            La valeur ou default
        """
        keys = key.split(".")
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """
        Définit une valeur de configuration.
        
        Args:
            key: Clé (peut utiliser des points pour les sous-clés)
            value: Valeur à définir
        """
        keys = key.split(".")
        
        if len(keys) == 1:
            self.config[keys[0]] = value
        else:
            current = self.config
            for k in keys[:-1]:
                if k not in current:
                    current[k] = {}
                current = current[k]
            current[keys[-1]] = value
    
    def ajouter_produit(self, produit: Dict[str, Any]):
        """
        Ajoute un produit à suivre.
        
        Args:
            produit: Dictionnaire avec les informations du produit
        """
        produits = self.config.setdefault("produits", [])
        produits.append(produit)
    
    def supprimer_produit(self, produit_id: str) -> bool:
        """
        Supprime un produit.
        
        Args:
            produit_id: ID du produit
            
        Returns:
            True si supprimé, False sinon
        """
        produits = self.config.get("produits", [])
        
        for i, p in enumerate(produits):
            if p.get("id") == produit_id:
                del produits[i]
                return True
        
        return False
    
    def lister_produits(self) -> List[Dict[str, Any]]:
        """Liste les produits suivis."""
        return self.config.get("produits", [])
