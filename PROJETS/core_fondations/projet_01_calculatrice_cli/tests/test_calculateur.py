"""Tests for calculateur service."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestCalculateur:
    """Test cases for Calculateur."""
    
    def test_addition(self):
        """Test addition."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.additionner(2, 3) == 5
        assert calc.additionner(-1, 1) == 0
        assert calc.additionner(0, 0) == 0
    
    def test_soustraction(self):
        """Test soustraction."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.soustraire(5, 3) == 2
        assert calc.soustraire(3, 5) == -2
        assert calc.soustraire(0, 0) == 0
    
    def test_multiplication(self):
        """Test multiplication."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.multiplier(4, 5) == 20
        assert calc.multiplier(-2, 3) == -6
        assert calc.multiplier(0, 100) == 0
    
    def test_division(self):
        """Test division."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.diviser(10, 2) == 5
        assert calc.diviser(7, 2) == 3.5
    
    def test_division_par_zero(self):
        """Test division by zero."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        try:
            calc.diviser(10, 0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
    
    def test_puissance(self):
        """Test power operation."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.calculer(2, '^', 3) == 8
        assert calc.calculer(5, '^', 0) == 1
        assert calc.calculer(10, '^', -1) == 0.1
    
    def test_racine_carree(self):
        """Test square root."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.calculer(16, 'sqrt') == 4
        assert calc.calculer(0, 'sqrt') == 0
    
    def test_factorielle(self):
        """Test factorial."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.calculer(5, 'fact') == 120
        assert calc.calculer(0, 'fact') == 1
    
    def test_moyenne(self):
        """Test average."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        assert calc.moyenne([1, 2, 3, 4, 5]) == 3
        assert calc.moyenne([10, 20]) == 15
    
    def test_moyenne_liste_vide(self):
        """Test average with empty list."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        try:
            calc.moyenne([])
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
    
    def test_get_operateurs(self):
        """Test get operators."""
        from src.services.calculateur import Calculateur
        calc = Calculateur()
        operateurs = calc.get_operateurs()
        assert '+' in operateurs
        assert '*' in operateurs
        assert 'sqrt' in operateurs
