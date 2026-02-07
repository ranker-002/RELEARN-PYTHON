#!/usr/bin/env python3
"""
Utilitaires de manipulation de dates.
"""

from datetime import datetime, timedelta
from typing import Union, Optional
import re


class DateUtils:
    """Utilitaires pour les dates."""
    
    @staticmethod
    def formater(date: Union[datetime, str], format: str = "%d/%m/%Y %H:%M") -> str:
        """
        Formate une date.
        
        Args:
            date: Date ou chaîne ISO
            format: Format de sortie
            
        Returns:
            Date formatée
        """
        if isinstance(date, str):
            try:
                date = datetime.fromisoformat(date)
            except ValueError:
                return date
        
        if date is None:
            return ""
        
        return date.strftime(format)
    
    @staticmethod
    def parser(date_str: str, formats: Optional[list] = None) -> Optional[datetime]:
        """
        Parse une chaîne de date.
        
        Args:
            date_str: Chaîne de date
            formats: Formats à essayer
            
        Returns:
            datetime ou None
        """
        if formats is None:
            formats = [
                "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%dT%H:%M:%SZ",
                "%Y-%m-%d %H:%M:%S",
                "%d/%m/%Y %H:%M",
                "%d/%m/%Y",
                "%Y-%m-%d",
            ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        
        return None
    
    @staticmethod
    def relative(date: Union[datetime, str]) -> str:
        """
        Retourne une représentation relative de la date.
        
        Args:
            date: Date ou chaîne ISO
            
        Returns:
            Chaîne relative (ex: "il y a 2 heures")
        """
        if isinstance(date, str):
            date = datetime.fromisoformat(date)
        
        if date is None:
            return ""
        
        now = datetime.now()
        delta = now - date
        
        if delta.days < 0:
            return "dans le futur"
        elif delta.days == 0:
            if delta.seconds < 60:
                return "à l'instant"
            elif delta.seconds < 3600:
                minutes = delta.seconds // 60
                return f"il y a {minutes} minute{'s' if minutes > 1 else ''}"
            else:
                hours = delta.seconds // 3600
                return f"il y a {hours} heure{'s' if hours > 1 else ''}"
        elif delta.days == 1:
            return "hier"
        elif delta.days < 7:
            return f"il y a {delta.days} jours"
        elif delta.days < 30:
            weeks = delta.days // 7
            return f"il y a {weeks} semaine{'s' if weeks > 1 else ''}"
        elif delta.days < 365:
            months = delta.days // 30
            return f"il y a {months} mois"
        else:
            years = delta.days // 365
            return f"il y a {years} an{'s' if years > 1 else ''}"
    
    @staticmethod
    def creer_date(days: int = 0, hours: int = 0) -> datetime:
        """
        Crée une date avec un offset.
        
        Args:
            days: Nombre de jours à ajouter
            hours: Nombre d'heures à ajouter
            
        Returns:
            datetime
        """
        return datetime.now() + timedelta(days=days, hours=hours)
    
    @staticmethod
    def est_recente(date: Union[datetime, str], jours: int = 7) -> bool:
        """
        Vérifie si une date est récente.
        
        Args:
            date: Date ou chaîne ISO
            jours: Nombre de jours maximum
            
        Returns:
            True si récente
        """
        if isinstance(date, str):
            date = datetime.fromisoformat(date)
        
        if date is None:
            return False
        
        delta = datetime.now() - date
        return delta.days < jours
