#!/usr/bin/env python3
"""
Service de calculs mathématiques.
"""

import math
from typing import Optional, Union


class Calculateur:
    """Effectue des calculs mathématiques de base et avancés."""
    
    OPERATEURS_BASIQUES = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        'x': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else float('inf'),
        '%': lambda a, b: a % b,
        'mod': lambda a, b: a % b,
    }
    
    OPERATEURS_AVANCES = {
        '^': lambda a, b: a ** b,
        'pow': lambda a, b: a ** b,
        'puissance': lambda a, b: a ** b,
        'sqrt': lambda a, _: math.sqrt(a) if a >= 0 else float('nan'),
        'racine': lambda a, _: math.sqrt(a) if a >= 0 else float('nan'),
        'racine_carree': lambda a, _: math.sqrt(a) if a >= 0 else float('nan'),
        'fact': lambda a, _: math.factorial(int(a)) if a >= 0 and a == int(a) else float('nan'),
        'factorielle': lambda a, _: math.factorial(int(a)) if a >= 0 and a == int(a) else float('nan'),
        'log': lambda a, b: math.log(a, b) if a > 0 and b > 0 and b != 1 else float('nan'),
        'log10': lambda a, _: math.log10(a) if a > 0 else float('nan'),
        'ln': lambda a, _: math.log(a) if a > 0 else float('nan'),
        'abs': lambda a, _: abs(a),
        'floor': lambda a, _: math.floor(a),
        'ceil': lambda a, _: math.ceil(a),
        'round': lambda a, _: round(a),
        'sin': lambda a, _: math.sin(math.radians(a)),
        'cos': lambda a, _: math.cos(math.radians(a)),
        'tan': lambda a, _: math.tan(math.radians(a)),
        'deg2rad': lambda a, _: math.radians(a),
        'rad2deg': lambda a, _: math.degrees(a),
    }
    
    def __init__(self):
        self.derniere_operation: Optional[str] = None
        self.derniere_erreur: Optional[str] = None
    
    def additionner(self, a: float, b: float) -> float:
        """Additionne deux nombres."""
        self.derniere_operation = f"{a} + {b}"
        return a + b
    
    def soustraire(self, a: float, b: float) -> float:
        """Soustrait deux nombres."""
        self.derniere_operation = f"{a} - {b}"
        return a - b
    
    def multiplier(self, a: float, b: float) -> float:
        """Multiplie deux nombres."""
        self.derniere_operation = f"{a} × {b}"
        return a * b
    
    def diviser(self, a: float, b: float) -> float:
        """Divise deux nombres."""
        if b == 0:
            self.derniere_erreur = "Division par zéro"
            raise ValueError("Division par zéro")
        self.derniere_operation = f"{a} ÷ {b}"
        return a / b
    
    def calculer(self, a: float, operateur: str, b: Optional[float] = None) -> float:
        """
        Effectue un calcul avec un opérateur.
        
        Args:
            a: Premier opérande
            operateur: Opérateur (+, -, *, /, ^, sqrt, etc.)
            b: Second opérande (requis pour les opérateurs binaires)
            
        Returns:
            Résultat du calcul
        """
        self.derniere_erreur = None
        
        operateur = operateur.lower().strip()
        
        if operateur in self.OPERATEURS_BASIQUES:
            if b is None:
                self.derniere_erreur = f"Opérateur '{operateur}' nécessite deux opérandes"
                raise ValueError(self.derniere_erreur)
            return self.OPERATEURS_BASIQUES[operateur](a, b)
        
        elif operateur in self.OPERATEURS_AVANCES:
            fonction = self.OPERATEURS_AVANCES[operateur]
            if operateur in ['log'] and b is None:
                b = 10
            return fonction(a, b if b is not None else 0)
        
        else:
            self.derniere_erreur = f"Opérateur inconnu: {operateur}"
            raise ValueError(self.derniere_erreur)
    
    def evaluer_expression(self, expression: str) -> float:
        """
        Évalue une expression mathématique simple.
        
        Args:
            expression: Expression (ex: "2 + 3 * 4")
            
        Returns:
            Résultat de l'évaluation
        """
        self.derniere_erreur = None
        
        expression = expression.strip()
        
        try:
            resultat = eval(expression, {"__builtins__": {}}, {})
            if isinstance(resultat, (int, float)):
                self.derniere_operation = expression
                return float(resultat)
            else:
                self.derniere_erreur = "L'expression ne retourne pas un nombre"
                raise ValueError(self.derniere_erreur)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            self.derniere_erreur = str(e)
            raise ValueError(f"Erreur d'évaluation: {e}")
    
    def pourcentage(self, valeur: float, total: float) -> float:
        """Calcule le pourcentage."""
        if total == 0:
            self.derniere_erreur = "Total nul pour le pourcentage"
            raise ValueError("Total nul pour le pourcentage")
        self.derniere_operation = f"{valeur} / {total} × 100%"
        return (valeur / total) * 100
    
    def moyenne(self, nombres: list) -> float:
        """Calcule la moyenne d'une liste de nombres."""
        if not nombres:
            self.derniere_erreur = "Liste vide"
            raise ValueError("Liste vide")
        self.derniere_operation = f"moyenne({len(nombres)} nombres)"
        return sum(nombres) / len(nombres)
    
    def mediane(self, nombres: list) -> float:
        """Calcule la médiane d'une liste de nombres."""
        if not nombres:
            self.derniere_erreur = "Liste vide"
            raise ValueError("Liste vide")
        self.derniere_operation = f"mediane({len(nombres)} nombres)"
        tri = sorted(nombres)
        n = len(tri)
        mid = n // 2
        if n % 2 == 0:
            return (tri[mid - 1] + tri[mid]) / 2
        return tri[mid]
    
    def minimum(self, nombres: list) -> float:
        """Retourne le minimum d'une liste."""
        if not nombres:
            self.derniere_erreur = "Liste vide"
            raise ValueError("Liste vide")
        self.derniere_operation = f"min({len(nombres)} nombres)"
        return min(nombres)
    
    def maximum(self, nombres: list) -> float:
        """Retourne le maximum d'une liste."""
        if not nombres:
            self.derniere_erreur = "Liste vide"
            raise ValueError("Liste vide")
        self.derniere_operation = f"max({len(nombres)} nombres)"
        return max(nombres)
    
    def sommer(self, nombres: list) -> float:
        """Calcule la somme d'une liste."""
        if not nombres:
            self.derniere_erreur = "Liste vide"
            raise ValueError("Liste vide")
        self.derniere_operation = f"somme({len(nombres)} nombres)"
        return sum(nombres)
    
    def get_operateurs(self) -> list:
        """Liste tous les opérateurs disponibles."""
        return list(self.OPERATEURS_BASIQUES.keys()) + list(self.OPERATEURS_AVANCES.keys())
