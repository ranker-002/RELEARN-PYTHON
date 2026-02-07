#!/usr/bin/env python3
"""
Module de prix pour l'analyseur.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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
    
    def formater(self, format: str = "standard") -> str:
        if format == "compact":
            if self.montant >= 1000:
                return f"{self.montant/1000:.1f}k {self.devise}"
            return f"{self.montant:.2f} {self.devise}"
        return f"{self.montant:.2f} {self.devise}"
    
    def __str__(self) -> str:
        return self.formater()
    
    def __repr__(self) -> str:
        return f"Prix({self.montant} {self.devise}, {self.site})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Prix):
            return False
        return (
            self.montant == other.montant and
            self.devise == other.devise and
            self.site == other.site
        )
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Prix):
            return NotImplemented
        return self.montant < other.montant
    
    def __le__(self, other: object) -> bool:
        return self == other or self < other
    
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Prix):
            return NotImplemented
        return self.montant > other.montant
    
    def __ge__(self, other: object) -> bool:
        return self == other or self > other
