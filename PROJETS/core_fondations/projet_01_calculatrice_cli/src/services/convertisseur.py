#!/usr/bin/env python3
"""
Service de conversion d'unités.
"""

from typing import Dict, Optional


class Convertisseur:
    """Convertit des valeurs entre différentes unités."""
    
    FACTEURS_LONGUEUR: Dict[str, float] = {
        'm': 1.0,
        'meter': 1.0,
        'meters': 1.0,
        'km': 1000.0,
        'kilometer': 1000.0,
        'kilometers': 1000.0,
        'cm': 0.01,
        'centimeter': 0.01,
        'centimeters': 0.01,
        'mm': 0.001,
        'millimeter': 0.001,
        'millimeters': 0.001,
        'ft': 0.3048,
        'feet': 0.3048,
        'foot': 0.3048,
        'in': 0.0254,
        'inch': 0.0254,
        'inches': 0.0254,
        'mi': 1609.344,
        'mile': 1609.344,
        'miles': 1609.344,
        'yd': 0.9144,
        'yard': 0.9144,
        'yards': 0.9144,
    }
    
    FACTEURS_MASSE: Dict[str, float] = {
        'kg': 1.0,
        'kilogram': 1.0,
        'kilograms': 1.0,
        'g': 0.001,
        'gram': 0.001,
        'grams': 0.001,
        'mg': 0.000001,
        'milligram': 0.000001,
        'milligrams': 0.000001,
        'lb': 0.453592,
        'lbs': 0.453592,
        'pound': 0.453592,
        'pounds': 0.453592,
        'oz': 0.0283495,
        'ounce': 0.0283495,
        'ounces': 0.0283495,
        't': 1000.0,
        'ton': 1000.0,
        'tons': 1000.0,
        'tonne': 1000.0,
        'tonnes': 1000.0,
    }
    
    CATEGORIES = {
        'longueur': ['m', 'km', 'cm', 'mm', 'ft', 'in', 'mi', 'yd'],
        'masse': ['kg', 'g', 'mg', 'lb', 'oz', 't'],
        'volume': ['l', 'ml', 'gal', 'qt', 'pt', 'cup', 'fl_oz'],
        'surface': ['m2', 'km2', 'cm2', 'mm2', 'ft2', 'in2', 'acre', 'hectare'],
        'vitesse': ['m/s', 'km/h', 'mph', 'ft/s', 'knot', 'mach'],
        'temps': ['s', 'ms', 'min', 'h', 'd', 'wk', 'mo', 'y'],
        'donnees': ['b', 'kb', 'mb', 'gb', 'tb', 'pb'],
    }
    
    def __init__(self):
        self.derniere_conversion: Optional[str] = None
        self.derniere_erreur: Optional[str] = None
    
    def convertir(self, valeur: float, unite_source: str, unite_cible: str,
                  categorie: str = 'longueur') -> float:
        """
        Convertit une valeur d'une unité vers une autre.
        
        Args:
            valeur: Valeur à convertir
            unite_source: Unité source
            unite_cible: Unité cible
            categorie: Catégorie d'unités
            
        Returns:
            Valeur convertie
        """
        self.derniere_erreur = None
        unite_source = unite_source.lower().strip()
        unite_cible = unite_cible.lower().strip()
        
        try:
            if categorie == 'longueur':
                return self._convertir_longueur(valeur, unite_source, unite_cible)
            elif categorie == 'masse':
                return self._convertir_masse(valeur, unite_source, unite_cible)
            elif categorie == 'temperature':
                return self._convertir_temperature(valeur, unite_source, unite_cible)
            elif categorie == 'volume':
                return self._convertir_volume(valeur, unite_source, unite_cible)
            elif categorie == 'temps':
                return self._convertir_temps(valeur, unite_source, unite_cible)
            elif categorie == 'donnees':
                return self._convertir_donnees(valeur, unite_source, unite_cible)
            elif categorie == 'devise':
                return self._convertir_devise(valeur, unite_source, unite_cible)
            else:
                self.derniere_erreur = f"Catégorie inconnue: {categorie}"
                raise ValueError(self.derniere_erreur)
        except KeyError as e:
            self.derniere_erreur = f"Unité inconnue: {e}"
            raise ValueError(self.derniere_erreur)
    
    def _convertir_longueur(self, valeur: float, source: str, cible: str) -> float:
        if source not in self.FACTEURS_LONGUEUR or cible not in self.FACTEURS_LONGUEUR:
            raise KeyError(source if source not in self.FACTEURS_LONGUEUR else cible)
        
        en_metres = valeur * self.FACTEURS_LONGUEUR[source]
        resultat = en_metres / self.FACTEURS_LONGUEUR[cible]
        
        self.derniere_conversion = f"{valeur} {source} = {resultat} {cible}"
        return resultat
    
    def _convertir_masse(self, valeur: float, source: str, cible: str) -> float:
        facteurs = self.FACTEURS_MASSE
        if source not in facteurs or cible not in facteurs:
            raise KeyError(source if source not in facteurs else cible)
        
        en_kg = valeur * facteurs[source]
        resultat = en_kg / facteurs[cible]
        
        self.derniere_conversion = f"{valeur} {source} = {resultat} {cible}"
        return resultat
    
    def _convertir_temperature(self, valeur: float, source: str, cible: str) -> float:
        source = source.upper().replace('°', '')
        cible = cible.upper().replace('°', '')
        
        if source == cible:
            return valeur
        
        if source == 'C':
            en_celsius = valeur
        elif source == 'F':
            en_celsius = (valeur - 32) * 5/9
        elif source == 'K':
            en_celsius = valeur - 273.15
        else:
            raise KeyError(source)
        
        if cible == 'C':
            resultat = en_celsius
        elif cible == 'F':
            resultat = en_celsius * 9/5 + 32
        elif cible == 'K':
            resultat = en_celsius + 273.15
        else:
            raise KeyError(cible)
        
        self.derniere_conversion = f"{valeur}°{source} = {resultat}°{cible}"
        return resultat
    
    def _convertir_volume(self, valeur: float, source: str, cible: str) -> float:
        facteurs = {
            'l': 1.0, 'liter': 1.0, 'liters': 1.0,
            'ml': 0.001, 'milliliter': 0.001, 'milliliters': 0.001,
            'gal': 3.78541, 'gallon': 3.78541, 'gallons': 3.78541,
            'qt': 0.946353, 'quart': 0.946353, 'quarts': 0.946353,
            'pt': 0.473176, 'pint': 0.473176, 'pints': 0.473176,
            'cup': 0.236588, 'cups': 0.236588,
            'fl_oz': 0.0295735, 'fluid_oz': 0.0295735,
        }
        
        if source not in facteurs or cible not in facteurs:
            raise KeyError(source if source not in facteurs else cible)
        
        en_litres = valeur * facteurs[source]
        resultat = en_litres / facteurs[cible]
        
        self.derniere_conversion = f"{valeur} {source} = {resultat} {cible}"
        return resultat
    
    def _convertir_temps(self, valeur: float, source: str, cible: str) -> float:
        facteurs = {
            's': 1.0, 'sec': 1.0, 'second': 1.0, 'seconds': 1.0,
            'ms': 0.001, 'millisec': 0.001, 'millisecond': 0.001,
            'min': 60.0, 'minute': 60.0, 'minutes': 60.0,
            'h': 3600.0, 'hour': 3600.0, 'hours': 3600.0,
            'd': 86400.0, 'day': 86400.0, 'days': 86400.0,
            'wk': 604800.0, 'week': 604800.0, 'weeks': 604800.0,
        }
        
        if source not in facteurs or cible not in facteurs:
            raise KeyError(source if source not in facteurs else cible)
        
        en_secondes = valeur * facteurs[source]
        resultat = en_secondes / facteurs[cible]
        
        self.derniere_conversion = f"{valeur} {source} = {resultat} {cible}"
        return resultat
    
    def _convertir_donnees(self, valeur: float, source: str, cible: str) -> float:
        facteurs = {
            'b': 1.0, 'bit': 1.0, 'bits': 1.0,
            'kb': 1000.0, 'kbit': 1000.0,
            'mb': 1000000.0, 'mbit': 1000000.0,
            'gb': 1000000000.0, 'gbit': 1000000000.0,
            'tb': 1000000000000.0, 'tbit': 1000000000000.0,
            'B': 8.0, 'byte': 8.0, 'bytes': 8.0,
            'KB': 8000.0, 'KByte': 8000.0,
            'MB': 8000000.0, 'MByte': 8000000.0,
            'GB': 8000000000.0, 'GByte': 8000000000.0,
        }
        
        if source not in facteurs or cible not in facteurs:
            raise KeyError(source if source not in facteurs else cible)
        
        en_bits = valeur * facteurs[source]
        resultat = en_bits / facteurs[cible]
        
        self.derniere_conversion = f"{valeur} {source} = {resultat} {cible}"
        return resultat
    
    def _convertir_devise(self, valeur: float, source: str, cible: str) -> float:
        taux = {
            ('EUR', 'USD'): 1.10,
            ('EUR', 'GBP'): 0.85,
            ('EUR', 'JPY'): 163.0,
            ('USD', 'EUR'): 0.91,
            ('USD', 'GBP'): 0.77,
            ('USD', 'JPY'): 148.0,
            ('GBP', 'EUR'): 1.18,
            ('GBP', 'USD'): 1.30,
            ('GBP', 'JPY'): 192.0,
            ('JPY', 'EUR'): 0.0061,
            ('JPY', 'USD'): 0.0068,
            ('JPY', 'GBP'): 0.0052,
        }
        
        source = source.upper()
        cible = cible.upper()
        
        if (source, cible) in taux:
            resultat = valeur * taux[(source, cible)]
        elif source == cible:
            resultat = valeur
        else:
            raise KeyError(f"Taux de change non disponible: {source} -> {cible}")
        
        self.derniere_conversion = f"{valeur} {source} = {resultat} {cible}"
        return resultat
    
    def get_categories(self) -> list:
        """Liste les catégories d'unités disponibles."""
        return list(self.CATEGORIES.keys())
    
    def get_unites(self, categorie: str) -> list:
        """Liste les unités d'une catégorie."""
        return self.CATEGORIES.get(categorie, [])
