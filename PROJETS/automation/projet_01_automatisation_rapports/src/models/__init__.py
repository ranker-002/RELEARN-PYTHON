#!/usr/bin/env python3
"""
Models for the project.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum
import uuid


class Statut(Enum):
    """Status enumeration."""
    ACTIF = "actif"
    INACTIF = "inactif"
    EN_ATTENTE = "en_attente"
    TERMINE = "termine"


@dataclass
class Rapport:
    """Represents a rapport."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


@dataclass
class SourceDonnees:
    """Represents a sourcedonnees."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


@dataclass
class Planification:
    """Represents a planification."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


__all__ = ["Statut", "Rapport", "SourceDonnees", "Planification"]
