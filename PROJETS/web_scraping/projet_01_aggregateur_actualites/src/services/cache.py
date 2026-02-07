"""Cache Manager - Met en cache les flux."""
from typing import Tuple, Optional
from datetime import datetime, timedelta


class CacheManager:
    """Gestionnaire de cache simple."""
    
    def __init__(self, duree_max: int = 3600):
        self.cache = {}
        self.duree_max = duree_max
    
    def set(self, url: str, contenu: str):
        """Met en cache un flux."""
        self.cache[url] = (contenu, datetime.now())
    
    def get(self, url: str) -> Optional[Tuple[str, int]]:
        """Récupère un flux du cache."""
        if url not in self.cache:
            return None
        
        contenu, date = self.cache[url]
        age = (datetime.now() - date).seconds
        
        if age > self.duree_max:
            del self.cache[url]
            return None
        
        return contenu, age
    
    def exists(self, url: str) -> bool:
        """Vérifie si un flux est en cache."""
        return self.get(url) is not None
    
    def clear(self):
        """Vide le cache."""
        self.cache.clear()
