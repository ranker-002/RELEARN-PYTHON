#!/usr/bin/env python3
"""
Modèle de données pour les projets.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
import uuid


@dataclass
class Projet:
    id: str
    nom: str
    description: str = ""
    couleur: str = "#3498db"
    icone: str = "📁"
    cree_le: datetime = field(default_factory=datetime.now)
    modifie_le: datetime = field(default_factory=datetime.now)
    actif: bool = True
    taches: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())[:8]
    
    def ajouter_tache(self, tache_id: str):
        if tache_id not in self.taches:
            self.taches.append(tache_id)
            self.modifie_le = datetime.now()
    
    def supprimer_tache(self, tache_id: str) -> bool:
        if tache_id in self.taches:
            self.taches.remove(tache_id)
            self.modifie_le = datetime.now()
            return True
        return False
    
    def get_nb_taches(self) -> int:
        return len(self.taches)
    
    def get_couleur_html(self) -> str:
        return self.couleur
    
    def desactiver(self):
        self.actif = False
        self.modifie_le = datetime.now()
    
    def reactiver(self):
        self.actif = True
        self.modifie_le = datetime.now()
    
    def mettre_a_jour(self, **kwargs):
        for cle, valeur in kwargs.items():
            if hasattr(self, cle) and cle not in ["id", "cree_le", "taches"]:
                setattr(self, cle, valeur)
                self.modifie_le = datetime.now()
    
    def vers_dict(self) -> dict:
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "couleur": self.couleur,
            "icone": self.icone,
            "cree_le": self.cree_le.isoformat(),
            "modifie_le": self.modifie_le.isoformat(),
            "actif": self.actif,
            "taches": self.taches,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Projet":
        return cls(
            id=data["id"],
            nom=data["nom"],
            description=data.get("description", ""),
            couleur=data.get("couleur", "#3498db"),
            icone=data.get("icone", "📁"),
            cree_le=datetime.fromisoformat(data["cree_le"]),
            modifie_le=datetime.fromisoformat(data["modifie_le"]),
            actif=data.get("actif", True),
            taches=data.get("taches", []),
        )
    
    def __str__(self) -> str:
        etat = "" if self.actif else " [Désactivé]"
        return f"{self.icone} {self.nom}{etat}"
    
    def __repr__(self) -> str:
        return f"Projet({self.nom!r}, {len(self.taches)} tâches)"


COLORS = {
    "rouge": "#e74c3c",
    "orange": "#e67e22",
    "jaune": "#f1c40f",
    "vert": "#2ecc71",
    "bleu": "#3498db",
    "violet": "#9b59b6",
    "rose": "#e91e63",
    "gris": "#95a5a6",
    "noir": "#2c3e50",
}


def get_couleur_par_nom(nom: str) -> str:
    return COLORS.get(nom.lower(), "#3498db")
