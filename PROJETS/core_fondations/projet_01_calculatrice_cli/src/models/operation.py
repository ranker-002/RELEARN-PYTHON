#!/usr/bin/env python3
"""
Modèles de données pour la calculatrice.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union
from enum import Enum


class TypeOperation(Enum):
    BASIQUE = "basique"
    AVANCEE = "avancee"
    CONVERSION = "conversion"
    VARIABLE = "variable"


@dataclass
class Operation:
    type: TypeOperation
    expression: str
    operande1: Optional[float] = None
    operande2: Optional[float] = None
    unite_source: Optional[str] = None
    unite_cible: Optional[str] = None
    categorie: Optional[str] = None
    resultat: Optional[float] = None
    
    def executer(self) -> float:
        if self.type == TypeOperation.BASIQUE:
            return self._executer_basique()
        elif self.type == TypeOperation.AVANCEE:
            return self._executer_avancee()
        elif self.type == TypeOperation.CONVERSION:
            return self._executer_conversion()
        return 0.0
    
    def _executer_basique(self) -> float:
        expr = self.expression.lower()
        if expr in ['+', 'add', 'addition']:
            return (self.operande1 or 0) + (self.operande2 or 0)
        elif expr in ['-', 'sub', 'soustraction']:
            return (self.operande1 or 0) - (self.operande2 or 0)
        elif expr in ['*', 'x', 'mul', 'multiplication']:
            return (self.operande1 or 0) * (self.operande2 or 0)
        elif expr in ['/', 'div', 'division']:
            if (self.operande2 or 0) == 0:
                raise ValueError("Division par zéro")
            return (self.operande1 or 0) / (self.operande2 or 1)
        elif expr == '%' or expr == 'mod':
            return (self.operande1 or 0) % (self.operande2 or 1)
        return 0.0
    
    def _executer_avancee(self) -> float:
        import math
        expr = self.expression.lower()
        a = self.operande1 or 0
        b = self.operande2 or 0
        
        if expr in ['^', 'pow', 'puissance']:
            return a ** b
        elif expr in ['sqrt', 'racine', 'racine_carree']:
            if a < 0:
                raise ValueError("Racine carrée d'un nombre négatif")
            return math.sqrt(a)
        elif expr in ['fact', 'factorielle']:
            n = int(a)
            if n < 0:
                raise ValueError("Factorielle d'un nombre négatif")
            return math.factorial(n)
        elif expr == 'log':
            if a <= 0:
                raise ValueError("Logarithme d'un nombre non positif")
            return math.log10(a) if b == 0 else math.log(a, b)
        elif expr == 'ln':
            if a <= 0:
                raise ValueError("Logarithme d'un nombre non positif")
            return math.log(a)
        elif expr == 'abs':
            return abs(a)
        elif expr == 'floor':
            return math.floor(a)
        elif expr == 'ceil':
            return math.ceil(a)
        elif expr == '%':
            return a % b
        return 0.0
    
    def _executer_conversion(self) -> float:
        return self.operande1 or 0.0


@dataclass
class Calcul:
    expression: str
    resultat: float
    timestamp: datetime = None
    valide: bool = True
    erreur: Optional[str] = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def vers_dict(self) -> dict:
        return {
            "expression": self.expression,
            "resultat": self.resultat,
            "timestamp": self.timestamp.isoformat(),
            "valide": self.valide,
            "erreur": self.erreur,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Calcul":
        return cls(
            expression=data["expression"],
            resultat=data["resultat"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            valide=data.get("valide", True),
            erreur=data.get("erreur"),
        )


@dataclass
class Variable:
    nom: str
    valeur: float
    description: str = ""
    
    def __post_init__(self):
        if not self.nom:
            self.nom = f"var_{id(self)}"
    
    def __str__(self) -> str:
        return f"{self.nom} = {self.valeur}"
    
    def __repr__(self) -> str:
        return f"Variable({self.nom}, {self.valeur})"
    
    def vers_dict(self) -> dict:
        return {
            "nom": self.nom,
            "valeur": self.valeur,
            "description": self.description,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Variable":
        return cls(
            nom=data["nom"],
            valeur=data["valeur"],
            description=data.get("description", ""),
        )
