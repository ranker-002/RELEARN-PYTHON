#!/usr/bin/env python3
"""
Modèles de données pour le gestionnaire de tâches.
"""

from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional, List
from enum import Enum
import uuid


class StatutTache(Enum):
    A_FAIRE = "a_faire"
    EN_COURS = "en_cours"
    TERMINEE = "terminee"
    ANNULEE = "annulee"


class PrioriteTache(Enum):
    CRITIQUE = 1
    HAUTE = 2
    NORMALE = 3
    BASSE = 4
    TRES_BASSE = 5


class NiveauPriorite(Enum):
    CRITIQUE = ("Critique", "🔴")
    HAUTE = ("Haute", "🟠")
    NORMALE = ("Normale", "🟡")
    BASSE = ("Basse", "🟢")
    TRES_BASSE = ("Très basse", "⚪")
    
    def __init__(self, nom, emoji):
        self.nom = nom
        self.emoji = emoji


@dataclass
class Tache:
    id: str
    titre: str
    description: str = ""
    statut: StatutTache = StatutTache.A_FAIRE
    priorite: int = 3
    projet: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    echeance: Optional[datetime] = None
    cree_le: datetime = field(default_factory=datetime.now)
    modifie_le: datetime = field(default_factory=datetime.now)
    terminee_le: Optional[datetime] = None
    temps_passe: int = 0
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())[:8]
    
    def est_en_retard(self) -> bool:
        if self.echeance and self.statut != StatutTache.TERMINEE:
            return datetime.now() > self.echeance
        return False
    
    def jours_jusqu_echeance(self) -> Optional[int]:
        if not self.echeance:
            return None
        delta = self.echeance - datetime.now()
        return delta.days
    
    def marquer_terminee(self):
        self.statut = StatutTache.TERMINEE
        self.terminee_le = datetime.now()
        self.modifie_le = datetime.now()
    
    def marquer_en_cours(self):
        self.statut = StatutTache.EN_COURS
        self.modifie_le = datetime.now()
    
    def marquer_annulee(self):
        self.statut = StatutTache.ANNULEE
        self.modifie_le = datetime.now()
    
    def ajouter_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
            self.modifie_le = datetime.now()
    
    def supprimer_tag(self, tag: str) -> bool:
        if tag in self.tags:
            self.tags.remove(tag)
            self.modifie_le = datetime.now()
            return True
        return False
    
    def changer_projet(self, projet: Optional[str]):
        self.projet = projet
        self.modifie_le = datetime.now()
    
    def changer_priorite(self, priorite: int):
        if 1 <= priorite <= 5:
            self.priorite = priorite
            self.modifie_le = datetime.now()
    
    def changer_echeance(self, echeance: Optional[datetime]):
        self.echeance = echeance
        self.modifie_le = datetime.now()
    
    def get_emoji_priorite(self) -> str:
        emojis = {1: "🔴", 2: "🟠", 3: "🟡", 4: "🟢", 5: "⚪"}
        return emojis.get(self.priorite, "⚪")
    
    def get_statut_emoji(self) -> str:
        emojis = {
            StatutTache.A_FAIRE: "📋",
            StatutTache.EN_COURS: "🔄",
            StatutTache.TERMINEE: "✅",
            StatutTache.ANNULEE: "❌",
        }
        return emojis.get(self.statut, "📋")
    
    def vers_dict(self) -> dict:
        return {
            "id": self.id,
            "titre": self.titre,
            "description": self.description,
            "statut": self.statut.value,
            "priorite": self.priorite,
            "projet": self.projet,
            "tags": self.tags,
            "echeance": self.echeance.isoformat() if self.echeance else None,
            "cree_le": self.cree_le.isoformat(),
            "modifie_le": self.modifie_le.isoformat(),
            "terminee_le": self.terminee_le.isoformat() if self.terminee_le else None,
            "temps_passe": self.temps_passe,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Tache":
        echeance = None
        if data.get("echeance"):
            echeance = datetime.fromisoformat(data["echeance"])
        
        terminee_le = None
        if data.get("terminee_le"):
            terminee_le = datetime.fromisoformat(data["terminee_le"])
        
        return cls(
            id=data["id"],
            titre=data["titre"],
            description=data.get("description", ""),
            statut=StatutTache(data.get("statut", "a_faire")),
            priorite=data.get("priorite", 3),
            projet=data.get("projet"),
            tags=data.get("tags", []),
            echeance=echeance,
            cree_le=datetime.fromisoformat(data["cree_le"]),
            modifie_le=datetime.fromisoformat(data["modifie_le"]),
            terminee_le=terminee_le,
            temps_passe=data.get("temps_passe", 0),
        )
    
    def __str__(self) -> str:
        emoji = self.get_statut_emoji()
        priorite_emoji = self.get_emoji_priorite()
        projet_str = f" [{self.projet}]" if self.projet else ""
        tags_str = f" #{self.tags}" if self.tags else ""
        echeance_str = f" 📅 {self.echeance.strftime('%d/%m/%Y')}" if self.echeance else ""
        return f"{emoji} {priorite_emoji} {self.titre}{projet_str}{tags_str}{echeance_str}"
    
    def __repr__(self) -> str:
        return f"Tache({self.titre!r}, {self.statut.value}, priorite={self.priorite})"
    
    def __lt__(self, other: "Tache") -> bool:
        if self.priorite != other.priorite:
            return self.priorite > other.priorite
        if self.echeance and other.echeance:
            if self.echeance != other.echeance:
                return self.echeance < other.echeance
        return self.cree_le < other.cree_le


@dataclass
class TacheRecurrente(Tache):
    recurrence: str = ""  # daily, weekly, monthly
    prochaine_echeance: Optional[datetime] = None
    
    def creer_suivante(self) -> Optional["TacheRecurrente"]:
        if not self.prochaine_echeance:
            return None
        
        import datetime as dt
        delta_map = {
            "daily": dt.timedelta(days=1),
            "weekly": dt.timedelta(weeks=1),
            "monthly": dt.timedelta(days=30),
        }
        delta = delta_map.get(self.recurrence)
        if not delta:
            return None
        
        nouvelle = TacheRecurrente(
            id=str(uuid.uuid4())[:8],
            titre=self.titre,
            description=self.description,
            priorite=self.priorite,
            projet=self.projet,
            tags=self.tags.copy(),
            recurrence=self.recurrence,
            prochaine_echeance=self.prochaine_echeance + delta,
        )
        return nouvelle
