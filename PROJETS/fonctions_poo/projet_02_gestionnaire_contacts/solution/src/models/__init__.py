#!/usr/bin/env python3
"""
Models for contact management system.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum
import uuid


class CategorieContact(Enum):
    """Contact categories."""
    FAMILLE = "famille"
    AMI = "ami"
    COLLEGUE = "collegue"
    CLIENT = "client"
    FOURNISSEUR = "fournisseur"
    AUTRE = "autre"


class StatutContact(Enum):
    """Contact status."""
    ACTIF = "actif"
    INACTIF = "inactif"
    FAVORI = "favori"


@dataclass
class Contact:
    """Represents a contact."""
    id: str
    nom: str
    prenom: str
    email: str
    telephone: str
    adresse: str = ""
    categorie: CategorieContact = CategorieContact.AUTRE
    statut: StatutContact = StatutContact.ACTIF
    notes: str = ""
    date_creation: datetime = field(default_factory=datetime.now)
    date_modification: Optional[datetime] = None
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

    @property
    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom}"

    def ajouter_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
            self.date_modification = datetime.now()

    def retirer_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
            self.date_modification = datetime.now()

    def mettre_a_jour(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.date_modification = datetime.now()


@dataclass
class Groupe:
    """Represents a contact group."""
    id: str
    nom: str
    description: str = ""
    contacts_ids: List[str] = field(default_factory=list)
    date_creation: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

    def ajouter_contact(self, contact_id: str):
        if contact_id not in self.contacts_ids:
            self.contacts_ids.append(contact_id)

    def retirer_contact(self, contact_id: str):
        if contact_id in self.contacts_ids:
            self.contacts_ids.remove(contact_id)

    @property
    def nombre_contacts(self) -> int:
        return len(self.contacts_ids)


@dataclass
class Interaction:
    """Represents an interaction with a contact."""
    id: str
    contact_id: str
    type_interaction: str  # "appel", "email", "reunion", "note"
    contenu: str
    date_interaction: datetime = field(default_factory=datetime.now)
    rappel: Optional[datetime] = None
    statut: str = "complete"  # "complete", "en_attente", "annule"

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


__all__ = [
    "Contact", "Groupe", "Interaction",
    "CategorieContact", "StatutContact"
]
