#!/usr/bin/env python3
"""
Utilitaires de formatage.
"""

from typing import Union
import locale


class PriceFormatter:
    """Formateur de prix."""
    
    DEVISE_SYMBOLES = {
        "EUR": "€",
        "USD": "$",
        "GBP": "£",
        "JPY": "¥",
    }
    
    @staticmethod
    def formater(montant: Union[float, int], devise: str = "EUR", 
                  format: str = "standard") -> str:
        """
        Formate un prix.
        
        Args:
            montant: Montant numérique
            devise: Code de devise
            format: Format (standard, compact, with_symbol)
            
        Returns:
            Prix formaté
        """
        if montant is None:
            return "N/A"
        
        symbole = PriceFormatter.DEVISE_SYMBOLES.get(devise, devise)
        
        try:
            montant = float(montant)
        except (ValueError, TypeError):
            return "N/A"
        
        if format == "compact":
            if montant >= 1000000:
                return f"{montant/1000000:.1f}M {symbole}"
            elif montant >= 1000:
                return f"{montant/1000:.1f}k {symbole}"
            else:
                return f"{montant:.2f} {symbole}"
        elif format == "with_symbol":
            return f"{montant:,.2f} {symbole}"
        else:
            return f"{montant:,.2f} {symbole}"
    
    @staticmethod
    def parser(prix_str: str) -> tuple[Union[float, None], str]:
        """
        Parse un prix formaté.
        
        Args:
            prix_str: Prix formaté
            
        Returns:
            Tuple (montant, devise)
        """
        if not prix_str:
            return None, "EUR"
        
        devise = "EUR"
        for code, symbole in PriceFormatter.DEVISE_SYMBOLES.items():
            if symbole in prix_str or code in prix_str.upper():
                devise = code
                break
        
        import re
        chiffres = re.sub(r"[^\d.,]", "", prix_str)
        
        if "," in chiffres and "." in chiffres:
            if chiffres.index(",") > chiffres.index("."):
                chiffres = chiffres.replace(",", "")
            else:
                chiffres = chiffres.replace(",", ".")
        elif "," in chiffres:
            chiffres = chiffres.replace(",", ".")
        
        try:
            montant = float(chiffres) if chiffres else None
            return montant, devise
        except ValueError:
            return None, devise
    
    @staticmethod
    def comparer(prix1: Union[float, int], prix2: Union[float, int]) -> int:
        """
        Compare deux prix.
        
        Args:
            prix1: Premier prix
            prix2: Deuxième prix
            
        Returns:
            -1 si prix1 < prix2, 0 si égal, 1 si prix1 > prix2
        """
        try:
            p1 = float(prix1)
            p2 = float(prix2)
        except (ValueError, TypeError):
            return 0
        
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
        return 0
    
    @staticmethod
    def calculer_pourcentage(ancien: Union[float, int], 
                             nouveau: Union[float, int]) -> float:
        """
        Calcule le pourcentage de changement.
        
        Args:
            ancien: Ancien prix
            nouveau: Nouveau prix
            
        Returns:
            Pourcentage de changement
        """
        try:
            ancien = float(ancien)
            nouveau = float(nouveau)
        except (ValueError, TypeError):
            return 0.0
        
        if ancien == 0:
            return 0.0
        
        return ((nouveau - ancien) / ancien) * 100
    
    @staticmethod
    def formater_pourcentage(valeur: float, include_sign: bool = True) -> str:
        """
        Formate un pourcentage.
        
        Args:
            valeur: Valeur numérique
            include_sign: Inclure le signe
            
        Returns:
            Pourcentage formaté
        """
        if include_sign:
            if valeur > 0:
                return f"+{valeur:.1f}%"
            elif valeur < 0:
                return f"{valeur:.1f}%"
            return "0%"
        return f"{valeur:.1f}%"
