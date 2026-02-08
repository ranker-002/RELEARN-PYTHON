#!/usr/bin/env python3
"""
Modèles de données pour l'analyseur de prix.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum


class Disponibilite(Enum):
    DISPONIBLE = "disponible"
    INDISPONIBLE = "indisponible"
    RUPTURE = "rupture"
    PRECOMMANDE = "precommande"


@dataclass
class Prix:
    montant: float
    devise: str = "EUR"
    date_collecte: datetime = None
    url_source: str = ""
    site: str = ""
    
    def __post_init__(self):
        if self.date_collecte is None:
            self.date_collecte = datetime.now()
    
    def formater(self) -> str:
        return f"{self.montant:.2f} {self.devise}"
    
    def vers_dict(self) -> dict:
        return {
            "montant": self.montant,
            "devise": self.devise,
            "date_collecte": self.date_collecte.isoformat(),
            "url_source": self.url_source,
            "site": self.site,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Prix":
        return cls(
            montant=data.get("montant", 0.0),
            devise=data.get("devise", "EUR"),
            date_collecte=datetime.fromisoformat(data["date_collecte"]) if "date_collecte" in data else None,
            url_source=data.get("url_source", ""),
            site=data.get("site", ""),
        )


@dataclass
class Produit:
    id: str
    nom: str
    url: str
    categorie: str = ""
    prix_actuel: Optional[Prix] = None
    prix_historique: List[Prix] = field(default_factory=list)
    seuil_alerte: Optional[float] = None
    disponible: Disponibilite = Disponibilite.DISPONIBLE
    
    def __post_init__(self):
        if self.prix_historique is None:
            self.prix_historique = []
    
    def ajouter_prix(self, prix: Prix):
        self.prix_actuel = prix
        self.prix_historique.append(prix)
    
    @property
    def variation_pourcentage(self) -> Optional[float]:
        if len(self.prix_historique) < 2:
            return None
        premier = self.prix_historique[0].montant
        dernier = self.prix_historique[-1].montant
        return ((dernier - premier) / premier) * 100
    
    def est_alerte(self) -> bool:
        if self.prix_actuel is None or self.seuil_alerte is None:
            return False
        return self.prix_actuel.montant <= self.seuil_alerte
    
    def vers_dict(self) -> dict:
        return {
            "id": self.id,
            "nom": self.nom,
            "url": self.url,
            "categorie": self.categorie,
            "prix_actuel": self.prix_actuel.vers_dict() if self.prix_actuel else None,
            "prix_historique": [p.vers_dict() for p in self.prix_historique],
            "seuil_alerte": self.seuil_alerte,
            "disponible": self.disponible.value,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Produit":
        prix_actuel = None
        if data.get("prix_actuel"):
            prix_actuel = Prix.depuis_dict(data["prix_actuel"])
        
        historique = [Prix.depuis_dict(p) for p in data.get("prix_historique", [])]
        
        disponible = Disponibilite.DISPONIBLE
        if data.get("disponible"):
            try:
                disponible = Disponibilite(data["disponible"])
            except ValueError:
                pass
        
        return cls(
            id=data["id"],
            nom=data["nom"],
            url=data["url"],
            categorie=data.get("categorie", ""),
            prix_actuel=prix_actuel,
            prix_historique=historique,
            seuil_alerte=data.get("seuil_alerte"),
            disponible=disponible,
        )
