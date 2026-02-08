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
class Classificateur:
    """Represents a classificateur."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


@dataclass
class Donnees:
    """Represents a donnees."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


@dataclass
class Classe:
    """Represents a classe."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


@dataclass
class Evaluation:
    """Represents a evaluation."""
    id: str
    nom: str
    statut: Statut = Statut.ACTIF
    date_creation: datetime = field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


__all__ = ["Statut", "Classificateur", "Donnees", "Classe", "Evaluation"]
