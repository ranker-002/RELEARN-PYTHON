"""Tests for convertisseur service."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestConvertisseur:
    """Test cases for Convertisseur."""
    
    def test_longueur_km_vers_m(self):
        """Test conversion kilometers to meters."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        assert conv.convertir(1, 'km', 'm', 'longueur') == 1000
    
    def test_longueur_m_vers_km(self):
        """Test conversion meters to kilometers."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        assert conv.convertir(1000, 'm', 'km', 'longueur') == 1
    
    def test_longueur_pied_vers_metre(self):
        """Test conversion feet to meters."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        result = conv.convertir(1, 'ft', 'm', 'longueur')
        assert abs(result - 0.3048) < 0.001
    
    def test_temperature_c_vers_f(self):
        """Test conversion Celsius to Fahrenheit."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        assert conv.convertir(0, 'C', 'F', 'temperature') == 32
        assert conv.convertir(100, 'C', 'F', 'temperature') == 212
    
    def test_temperature_f_vers_c(self):
        """Test conversion Fahrenheit to Celsius."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        assert conv.convertir(32, 'F', 'C', 'temperature') == 0
        assert conv.convertir(212, 'F', 'C', 'temperature') == 100
    
    def test_temperature_c_vers_k(self):
        """Test conversion Celsius to Kelvin."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        assert conv.convertir(0, 'C', 'K', 'temperature') == 273.15
    
    def test_masse_kg_vers_g(self):
        """Test conversion kilograms to grams."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        assert conv.convertir(1, 'kg', 'g', 'masse') == 1000
    
    def test_categories(self):
        """Test get categories."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        cats = conv.get_categories()
        assert 'longueur' in cats
        assert 'masse' in cats
        assert 'temperature' in cats
    
    def test_unites_longueur(self):
        """Test get unites for longueur."""
        from src.services.convertisseur import Convertisseur
        conv = Convertisseur()
        unites = conv.get_unites('longueur')
        assert 'm' in unites
        assert 'km' in unites
