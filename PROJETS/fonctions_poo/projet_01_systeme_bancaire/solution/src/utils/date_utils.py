#!/usr/bin/env python3
"""
Date utilities for the banking system.
"""

from datetime import datetime, date, timedelta
from typing import Optional


class DateUtils:
    """Utilities for date manipulation."""
    
    @staticmethod
    def formatter_date(dt, fmt: str = "%d/%m/%Y") -> str:
        if isinstance(dt, datetime):
            return dt.strftime(fmt)
        elif isinstance(dt, date):
            return dt.strftime(fmt)
        return str(dt)
    
    @staticmethod
    def formatter_datetime(dt: datetime, fmt: str = "%d/%m/%Y %H:%M") -> str:
        return dt.strftime(fmt)
    
    @staticmethod
    def formatter_montant(montant: float, devise: str = "EUR") -> str:
        return f"{montant:,.2f} {devise}".replace(",", " ").replace(".", ",")
    
    @staticmethod
    def parser_date(texte: str) -> Optional[date]:
        formats = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]
        for fmt in formats:
            try:
                return datetime.strptime(texte, fmt).date()
            except ValueError:
                continue
        return None
    
    @staticmethod
    def get_age(date_naissance: date) -> int:
        aujourd_hui = date.today()
        age = aujourd_hui.year - date_naissance.year
        if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
            age -= 1
        return age
