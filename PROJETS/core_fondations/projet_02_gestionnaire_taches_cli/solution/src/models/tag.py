#!/usr/bin/env python3
"""
Modèle de données pour les tags.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
import uuid


@dataclass
class Tag:
    id: str
    nom: str
    couleur: str = "#95a5a6"
    icone: str = "🏷️"
    description: str = ""
    cree_le: datetime = field(default_factory=datetime.now)
    nb_utilisations: int = 0
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())[:8]
    
    def incrementer_utilisations(self):
        self.nb_utilisations += 1
    
    def get_couleur_html(self) -> str:
        return self.couleur
    
    def mettre_a_jour(self, **kwargs):
        for cle, valeur in kwargs.items():
            if hasattr(self, cle) and cle not in ["id", "cree_le", "nb_utilisations"]:
                setattr(self, cle, valeur)
    
    def vers_dict(self) -> dict:
        return {
            "id": self.id,
            "nom": self.nom,
            "couleur": self.couleur,
            "icone": self.icone,
            "description": self.description,
            "cree_le": self.cree_le.isoformat(),
            "nb_utilisations": self.nb_utilisations,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Tag":
        return cls(
            id=data["id"],
            nom=data["nom"],
            couleur=data.get("couleur", "#95a5a6"),
            icone=data.get("icone", "🏷️"),
            description=data.get("description", ""),
            cree_le=datetime.fromisoformat(data["cree_le"]),
            nb_utilisations=data.get("nb_utilisations", 0),
        )
    
    def __str__(self) -> str:
        return f"{self.icone} {self.nom}"
    
    def __repr__(self) -> str:
        return f"Tag({self.nom!r}, {self.nb_utilisations} utilisations)"


TAG_COLORS = [
    "#e74c3c", "#e67e22", "#f1c40f", "#2ecc71",
    "#1abc9c", "#3498db", "#9b59b6", "#e91e63",
    "#34495e", "#95a5a6",
]


def get_couleur_aleatoire() -> str:
    import random
    return random.choice(TAG_COLORS)


def get_couleur_depuis_nom(nom: str) -> str:
    import hashlib
    hash_value = int(hashlib.md5(nom.encode()).hexdigest(), 16)
    return TAG_COLORS[hash_value % len(TAG_COLORS)]
