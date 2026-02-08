#!/usr/bin/env python3
"""
Utilitaires de manipulation de dates.
"""

from datetime import datetime, date, timedelta
from typing import Union, Optional
import re


class DateUtils:
    """Utilitaires pour les dates."""
    
    FORMATS_DATE = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
        "%d %B %Y",
        "%d %b %Y",
    ]
    
    FORMATS_HEURE = [
        "%H:%M",
        "%H:%M:%S",
        "%I:%M",
        "%I:%M %p",
    ]
    
    FORMATS_DATETIME = [
        "%d/%m/%Y %H:%M",
        "%d/%m/%Y %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
    ]
    
    @staticmethod
    def parser_date(texte: str) -> Optional[date]:
        texte = texte.strip()
        
        for fmt in DateUtils.FORMATS_DATE:
            try:
                return datetime.strptime(texte, fmt).date()
            except ValueError:
                continue
        
        try:
            if texte.lower() == "aujourd'hui":
                return date.today()
            elif texte.lower() == "demain":
                return date.today() + timedelta(days=1)
            elif texte.lower() == "hier":
                return date.today() - timedelta(days=1)
        except:
            pass
        
        return None
    
    @staticmethod
    def parser_datetime(texte: str) -> Optional[datetime]:
        texte = texte.strip()
        
        for fmt in DateUtils.FORMATS_DATETIME:
            try:
                return datetime.strptime(texte, fmt)
            except ValueError:
                continue
        
        for fmt in DateUtils.FORMATS_DATE:
            try:
                return datetime.strptime(texte, fmt)
            except ValueError:
                continue
        
        return None
    
    @staticmethod
    def formatter_date(dt: Union[datetime, date], fmt: str = "%d/%m/%Y") -> str:
        if isinstance(dt, datetime):
            return dt.strftime(fmt)
        elif isinstance(dt, date):
            return dt.strftime(fmt)
        return str(dt)
    
    @staticmethod
    def formatter_datetime(dt: datetime, fmt: str = "%d/%m/%Y %H:%M") -> str:
        return dt.strftime(fmt)
    
    @staticmethod
    def formatter_relative(dt: Union[datetime, date]) -> str:
        maintenant = datetime.now()
        cible = datetime.combine(dt, datetime.min.time()) if isinstance(dt, date) else dt
        
        delta = cible - maintenant
        
        if delta.days < 0:
            if delta.days == -1:
                return "hier"
            elif delta.days > -7:
                return f"il y a {-delta.days} jours"
            elif delta.days > -30:
                semaines = -delta.days // 7
                return f"il y a {semaines} semaine{'s' if semaines > 1 else ''}"
            else:
                mois = -delta.days // 30
                return f"il y a {mois} mois"
        elif delta.days == 0:
            return "aujourd'hui"
        elif delta.days == 1:
            return "demain"
        elif delta.days < 7:
            return f"dans {delta.days} jours"
        elif delta.days < 30:
            semaines = delta.days // 7
            return f"dans {semaines} semaine{'s' if semaines > 1 else ''}"
        else:
            mois = delta.days // 30
            return f"dans {mois} mois"
    
    @staticmethod
    def get_debut_semaine(dt: datetime = None) -> datetime:
        if dt is None:
            dt = datetime.now()
        debut = dt - timedelta(days=dt.weekday())
        return debut.replace(hour=0, minute=0, second=0, microsecond=0)
    
    @staticmethod
    def get_fin_semaine(dt: datetime = None) -> datetime:
        debut = DateUtils.get_debut_semaine(dt)
        return debut + timedelta(days=6, hours=23, minutes=59, seconds=59)
    
    @staticmethod
    def get_debut_mois(dt: datetime = None) -> datetime:
        if dt is None:
            dt = datetime.now()
        return dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    @staticmethod
    def get_fin_mois(dt: datetime = None) -> datetime:
        debut = DateUtils.get_debut_mois(dt)
        if debut.month == 12:
            return debut.replace(month=1, year=debut.year + 1) - timedelta(seconds=1)
        return debut.replace(month=debut.month + 1) - timedelta(seconds=1)
    
    @staticmethod
    def parser_intervalle(texte: str) -> tuple[Optional[datetime], Optional[datetime]]:
        texte = texte.lower().strip()
        
        maintenant = datetime.now()
        
        if "aujourd'hui" in texte:
            debut = maintenant.replace(hour=0, minute=0, second=0, microsecond=0)
            fin = maintenant.replace(hour=23, minute=59, second=59, microsecond=999999)
            return debut, fin
        
        if "cette semaine" in texte:
            return DateUtils.get_debut_semaine(), DateUtils.get_fin_semaine()
        
        if "ce mois" in texte:
            return DateUtils.get_debut_mois(), DateUtils.get_fin_mois()
        
        match = re.search(r"(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?", texte)
        if match:
            try:
                jour, mois, annee = int(match.group(1)), int(match.group(2)), int(match.group(3)) if match.group(3) else maintenant.year
                if annee < 100:
                    annee += 2000
                return datetime(annee, mois, jour, 0, 0, 0), datetime(annee, mois, jour, 23, 59, 59)
            except ValueError:
                pass
        
        return None, None
    
    @staticmethod
    def est_aujourd_hui(dt: datetime) -> bool:
        aujourd_hui = date.today()
        return dt.date() == aujourd_hui
    
    @staticmethod
    def est_cette_semaine(dt: datetime) -> bool:
        maintenant = datetime.now()
        debut = DateUtils.get_debut_semaine(maintenant)
        fin = DateUtils.get_fin_semaine(maintenant)
        return debut <= dt <= fin
    
    @staticmethod
    def est_ce_mois(dt: datetime) -> bool:
        maintenant = datetime.now()
        return dt.month == maintenant.month and dt.year == maintenant.year
    
    @staticmethod
    def ajouter_jours(dt: datetime, jours: int) -> datetime:
        return dt + timedelta(days=jours)
    
    @staticmethod
    def ajouter_heures(dt: datetime, heures: int) -> datetime:
        return dt + timedelta(hours=heures)
    
    @staticmethod
    def calculer_age(date_naissance: date) -> int:
        aujourd_hui = date.today()
        age = aujourd_hui.year - date_naissance.year
        if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
            age -= 1
        return age
