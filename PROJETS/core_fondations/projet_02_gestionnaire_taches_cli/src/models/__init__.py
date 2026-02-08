"""Models package - Tâche, Projet, Tag."""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Tache:
    """Représente une tâche."""
    id: str
    titre: str
    description: str = ""
    statut: str = "todo"
    priorite: str = "moyenne"
    projet_id: str = ""
    tags: List[str] = None
    date_echeance: Optional[datetime] = None
    date_creation: datetime = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.date_creation is None:
            self.date_creation = datetime.now()
        if not self.id:
            import uuid
            self.id = str(uuid.uuid4())[:8]


@dataclass
class Projet:
    """Représente un projet."""
    id: str
    nom: str
    description: str = ""
    couleur: str = "bleu"
    date_creation: datetime = None

    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now()
        if not self.id:
            import uuid
            self.id = str(uuid.uuid4())[:8]


@dataclass
class Tag:
    """Représente un tag."""
    id: str
    nom: str
    couleur: str = "gris"

    def __post_init__(self):
        if not self.id:
            import uuid
            self.id = str(uuid.uuid4())[:8]


__all__ = ["Tache", "Projet", "Tag"]
