"""Gestionnaire de tâches."""

from typing import List, Optional
from models import Tache, Projet, Tag


class GestionnaireTaches:
    """Gère les tâches."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.taches: List[Tache] = []
        self.projets: List[Projet] = []
        self.tags: List[Tag] = []
    
    def ajouter_tache(self, titre: str) -> Tache:
        """Ajouter une tâche."""
        raise NotImplementedError
    
    def lister_taches(self, filtre: str = None) -> List[Tache]:
        """Lister les tâches."""
        raise NotImplementedError
    
    def marquer_terminee(self, tache_id: str) -> bool:
        """Marquer comme terminée."""
        raise NotImplementedError
    
    def supprimer_tache(self, tache_id: str) -> bool:
        """Supprimer une tâche."""
        raise NotImplementedError
    
    def get_statistiques(self) -> dict:
        """Retourner les statistiques."""
        raise NotImplementedError
