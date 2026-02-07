"""Date Utilities - Fonctions de manipulation de dates."""
from datetime import datetime
from typing import Optional


class DateUtils:
    """Utilitaires pour les dates."""
    
    @staticmethod
    def parser_date_rss(date_str: str) -> Optional[datetime]:
        """Parse une date au format RSS."""
        formats = [
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S GMT",
            "%Y-%m-%dT%H:%M:%SZ",
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue
        return None
    
    @staticmethod
    def formater_relative(date: datetime) -> str:
        """Formate une date en temps relatif."""
        maintenant = datetime.now()
        delta = maintenant - date
        
        if delta.days > 0:
            return f"il y a {delta.days} jour(s)"
        elif delta.seconds > 3600:
            return f"il y a {delta.seconds // 3600} heure(s)"
        elif delta.seconds > 60:
            return f"il y a {delta.seconds // 60} minute(s)"
        else:
            return "à l'instant"
    
    @staticmethod
    def formater(date: datetime, fmt: str = "%d/%m/%Y %H:%M") -> str:
        """Formate une date."""
        return date.strftime(fmt)
