#!/usr/bin/env python3
"""
Évaluateur d'expressions mathématiques.
"""

import re
from typing import Optional, Dict
from .calculateur import Calculateur


class Evaluateur:
    """Évalue des expressions mathématiques complexes."""
    
    def __init__(self):
        self.calculateur = Calculateur()
        self.variables: Dict[str, float] = {}
    
    def evaluer(self, expression: str) -> tuple[float, bool, Optional[str]]:
        """
        Évalue une expression et retourne le résultat.
        
        Args:
            expression: Expression à évaluer
            
        Returns:
            Tuple (résultat, est_valide, message_erreur)
        """
        expression = expression.strip()
        
        if not expression:
            return 0.0, False, "Expression vide"
        
        try:
            expression = self._substituer_variables(expression)
            expression = self._normaliser(expression)
            
            resultat = self._evaluer_recursive(expression)
            
            return resultat, True, None
            
        except ValueError as e:
            return 0.0, False, str(e)
        except Exception as e:
            return 0.0, False, f"Erreur: {e}"
    
    def _substituer_variables(self, expression: str) -> str:
        """Remplace les variables par leurs valeurs."""
        for nom in sorted(self.variables.keys(), key=len, reverse=True):
            expression = re.sub(r'\b' + re.escape(nom) + r'\b', 
                             str(self.variables[nom]), expression)
        return expression
    
    def _normaliser(self, expression: str) -> str:
        """Normalise l'expression pour l'évaluation."""
        expression = expression.lower()
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('−', '-')
        expression = re.sub(r'\^(\d+)', r'**\1', expression)
        expression = re.sub(r'(\d+)\s*%', r'\1/100', expression)
        return expression
    
    def _evaluer_recursive(self, expression: str) -> float:
        """Évalue récursivement l'expression."""
        expression = expression.strip()
        
        if '(' in expression:
            resultat = self._evaluer_parentheses(expression)
        elif '+' in expression and not self._est_operateur_unaire(expression, '+'):
            return self._evaluer_gauche(expression, '+')
        elif '-' in expression and not self._est_operateur_unaire(expression, '-'):
            return self._evaluer_gauche(expression, '-')
        elif '*' in expression or '×' in expression:
            return self._evaluer_gauche(expression.replace('×', '*'), '*')
        elif '/' in expression:
            return self._evaluer_gauche(expression, '/')
        elif '^' in expression:
            return self._evaluer_gauche(expression, '^')
        elif '%' in expression:
            return self._evaluer_gauche(expression, '%')
        else:
            return self._parser_nombre(expression)
    
    def _est_operateur_unaire(self, expression: str, operateur: str) -> bool:
        """Vérifie si l'opérateur est unaire (au début ou après un autre opérateur)."""
        idx = expression.find(operateur)
        if idx == -1:
            return False
        if idx == 0:
            return True
        return expression[idx - 1] in '+-*/^%('
    
    def _evaluer_parentheses(self, expression: str) -> float:
        """Évalue les expressions entre parenthèses."""
        profondeur = 0
        debut = 0
        
        for i, char in enumerate(expression):
            if char == '(':
                if profondeur == 0:
                    debut = i + 1
                profondeur += 1
            elif char == ')':
                profondeur -= 1
                if profondeur == 0:
                    contenu = expression[debut:i]
                    return self._evaluer_recursive(contenu)
        
        raise ValueError("Parenthèses non équilibrées")
    
    def _evaluer_gauche(self, expression: str, operateur: str) -> float:
        """Évalue en séparant par l'opérateur de gauche à droite."""
        parties = []
        profondeur = 0
        debut = 0
        
        for i, char in enumerate(expression):
            if char in '([':
                profondeur += 1
            elif char in ')]':
                profondeur -= 1
            elif char == operateur and profondeur == 0 and not self._est_operateur_unaire(expression, operateur):
                parties.append(expression[debut:i])
                debut = i + 1
        
        parties.append(expression[debut:])
        
        resultat = self._parser_nombre(parties[0])
        
        for partie in parties[1:]:
            if operateur == '+':
                resultat += self._parser_nombre(partie)
            elif operateur == '-':
                resultat -= self._parser_nombre(partie)
            elif operateur == '*':
                resultat *= self._parser_nombre(partie)
            elif operateur == '/':
                diviseur = self._parser_nombre(partie)
                if diviseur == 0:
                    raise ValueError("Division par zéro")
                resultat /= diviseur
            elif operateur == '^':
                resultat **= self._parser_nombre(partie)
            elif operateur == '%':
                resultat %= self._parser_nombre(partie)
        
        return resultat
    
    def _parser_nombre(self, texte: str) -> float:
        """Convertit un texte en nombre."""
        texte = texte.strip()
        
        if not texte:
            raise ValueError("Nombre attendu")
        
        if texte.startswith('-'):
            return -self._parser_nombre(texte[1:])
        
        fonctions = {
            'sqrt': lambda x: x ** 0.5,
            'abs': abs,
            'floor': lambda x: int(x // 1),
            'ceil': lambda x: int(-(-x // 1)),
            'round': round,
            'sin': lambda x: __import__('math').sin(__import__('math').radians(x)),
            'cos': lambda x: __import__('math').cos(__import__('math').radians(x)),
            'tan': lambda x: __import__('math').tan(__import__('math').radians(x)),
            'log': lambda x: __import__('math').log10(x),
            'ln': lambda x: __import__('math').log(x),
            'exp': __import__('math').exp,
        }
        
        for nom, fonction in fonctions.items():
            if texte.startswith(nom + '(') and texte.endswith(')'):
                try:
                    arg = float(texte[len(nom) + 1:-1])
                    return fonction(arg)
                except (ValueError, TypeError):
                    pass
        
        try:
            return float(texte)
        except ValueError:
            raise ValueError(f"Impossible de parser: {texte}")
    
    def ajouter_variable(self, nom: str, valeur: float):
        """Ajoute une variable."""
        self.variables[nom] = float(valeur)
    
    def supprimer_variable(self, nom: str) -> bool:
        """Supprime une variable."""
        if nom in self.variables:
            del self.variables[nom]
            return True
        return False
    
    def get_variables(self) -> Dict[str, float]:
        """Retourne toutes les variables."""
        return self.variables.copy()
