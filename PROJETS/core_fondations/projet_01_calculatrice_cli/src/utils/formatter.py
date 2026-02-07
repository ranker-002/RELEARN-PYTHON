#!/usr/bin/env python3
"""
Formatage des résultats.
"""

from typing import Union
import locale


class ResultFormatter:
    """Formate les résultats des calculs."""
    
    SYMBOLES_DEVISE = {
        "EUR": "€",
        "USD": "$",
        "GBP": "£",
        "JPY": "¥",
        "CHF": "CHF",
        "CNY": "¥",
    }
    
    @staticmethod
    def formater_nombre(valeur: Union[int, float], precision: int = 10) -> str:
        """Formate un nombre avec la précision spécifiée."""
        if isinstance(valeur, int):
            return str(valeur)
        
        if precision <= 0:
            return str(int(round(valeur)))
        
        valeur_arrondie = round(valeur, precision)
        
        if valeur_arrondie == int(valeur_arrondie):
            return str(int(valeur_arrondie))
        
        return f"{valeur_arrondie:.{precision}f}".rstrip('0').rstrip('.')
    
    @staticmethod
    def formater_scientifique(valeur: Union[int, float]) -> str:
        """Formate un nombre en notation scientifique."""
        return f"{valeur:.6e}"
    
    @staticmethod
    def formater_engineering(valeur: float) -> str:
        """Formate un nombre en notation engineering."""
        import math
        exp = int(math.floor(math.log10(abs(valeur))))
        exp = (exp // 3) * 3
        
        if exp != 0:
            mantisse = valeur / (10 ** exp)
            prefixe = {3: "k", 6: "M", 9: "G", 12: "T", -3: "m", -6: "µ", -9: "n"}
            sym = prefixe.get(exp, f"e{exp}")
            return f"{mantisse:.3f}{sym}"
        return str(valeur)
    
    @staticmethod
    def formater_pourcentage(valeur: float, precision: int = 2) -> str:
        """Formate un pourcentage."""
        return f"{valeur:.{precision}f}%"
    
    @staticmethod
    def formater_devise(valeur: float, devise: str = "EUR") -> str:
        """Formate une valeur en devise."""
        symbole = ResultFormatter.SYMBOLES_DEVISE.get(devise, devise)
        return f"{valeur:,.2f} {symbole}"
    
    @staticmethod
    def formater_monetaire(valeur: float, symbole: str = "€") -> str:
        """Formate une valeur monétaire."""
        return f"{symbole}{valeur:,.2f}"
    
    @staticmethod
    def formater_entier(valeur: float) -> str:
        """Formate un entier avec des séparateurs de milliers."""
        return f"{int(valeur):,}"
    
    @staticmethod
    def formater_fraction(valeur: float) -> str:
        """Formate une fraction approximative."""
        if abs(valeur) < 0.01 or abs(valeur) > 1000:
            return ResultFormatter.formater_nombre(valeur)
        
        fractions = {
            0.125: "1/8", 0.25: "1/4", 0.333: "1/3", 0.5: "1/2",
            0.666: "2/3", 0.75: "3/4", 0.875: "7/8",
        }
        
        partie_entiere = int(valeur)
        reste = abs(valeur) - partie_entiere
        
        meilleure_frac = None
        meilleure_diff = float('inf')
        
        for frac, val in fractions.items():
            diff = abs(reste - val)
            if diff < meilleure_diff:
                meilleure_diff = diff
                meilleure_frac = frac
        
        if meilleure_diff < 0.05:
            if partie_entiere != 0:
                return f"{partie_entiere} {meilleure_frac}"
            return meilleure_frac
        
        return ResultFormatter.formater_nombre(valeur)
    
    @staticmethod
    def formater_temps(secondes: float) -> str:
        """Formate une durée en secondes."""
        if secondes < 60:
            return f"{secondes:.2f}s"
        elif secondes < 3600:
            minutes = secondes // 60
            secs = secondes % 60
            return f"{int(minutes)}min {secs:.0f}s"
        elif secondes < 86400:
            heures = secondes // 3600
            mins = (secondes % 3600) // 60
            return f"{int(heures)}h {int(mins)}min"
        else:
            jours = secondes // 86400
            heures = (secondes % 86400) // 3600
            return f"{int(jours)}j {int(heures)}h"
    
    @staticmethod
    def formater_taille_octets(octets: float) -> str:
        """Formate une taille en octets."""
        if octets < 1024:
            return f"{octets:.0f} B"
        elif octets < 1024 ** 2:
            return f"{octets / 1024:.1f} KB"
        elif octets < 1024 ** 3:
            return f"{octets / (1024 ** 2):.1f} MB"
        elif octets < 1024 ** 4:
            return f"{octets / (1024 ** 3):.1f} GB"
        else:
            return f"{octets / (1024 ** 4):.1f} TB"
