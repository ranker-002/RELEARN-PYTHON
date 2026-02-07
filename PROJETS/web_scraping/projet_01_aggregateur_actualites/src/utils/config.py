"""Configuration Utility - Gère la configuration."""
from typing import Dict, Any, Optional
from pathlib import Path
import json


class Config:
    """Gestionnaire de configuration."""
    
    def __init__(self, data: Optional[Dict] = None):
        self.data = data or {}
    
    @classmethod
    def load(cls, filepath: Optional[str] = None) -> "Config":
        """Charge la configuration depuis un fichier."""
        if filepath is None:
            filepath = "data/subscriptions.json"
        
        path = Path(filepath)
        if path.exists():
            try:
                data = json.loads(path.read_text())
                return cls(data)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        return cls()
    
    def get(self, key: str, default: Any = None) -> Any:
        """Récupère une valeur."""
        return self.data.get(key, default)
    
    def set(self, key: str, value: Any):
        """Définit une valeur."""
        self.data[key] = value
    
    def save(self, filepath: str = "config.json"):
        """Sauvegarde la configuration."""
        Path(filepath).write_text(json.dumps(self.data, indent=2))
