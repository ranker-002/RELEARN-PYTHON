"""Date utilities."""

from datetime import datetime
from typing import Optional


class DateUtils:
    """Utilitaires de date."""
    
    @staticmethod
    def formatter_date(dt: datetime, fmt: str = "%d/%m/%Y") -> str:
        return dt.strftime(fmt)
    
    @staticmethod
    def parser_date(texte: str) -> Optional[datetime]:
        for fmt in ["%d/%m/%Y", "%Y-%m-%d"]:
            try:
                return datetime.strptime(texte, fmt)
            except ValueError:
                continue
        return None
