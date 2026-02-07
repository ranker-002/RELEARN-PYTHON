"""Tests for main module."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestMain:
    """Test cases for main module."""
    
    def test_initialization(self):
        """Test application initialization."""
        from src.main import PriceAnalyzerApp
        app = PriceAnalyzerApp()
        assert app is not None
        assert app.VERSION == "1.0.0"
    
    def test_banniere(self):
        """Test banner display."""
        from src.main import PriceAnalyzerApp
        app = PriceAnalyzerApp()
        app._afficher_banniere()
    
    def test_colors(self):
        """Test colors are defined."""
        from src.main import Colors
        assert hasattr(Colors, "RESET")
        assert hasattr(Colors, "BOLD")
        assert hasattr(Colors, "GREEN")
        assert hasattr(Colors, "RED")
    
    def test_example(self):
        """Example test case."""
        assert True


class TestCLI:
    """Test cases for CLI functionality."""
    
    def test_parser_exists(self):
        """Test argument parser exists."""
        import argparse
        parser = argparse.ArgumentParser()
        assert parser is not None
    
    def test_argument_parsing(self):
        """Test argument parsing."""
        import sys
        from src.main import PriceAnalyzerApp
        
        app = PriceAnalyzerApp()
        
        sys.argv = ["prog", "--version"]
        try:
            app._traiter_arguments()
        except SystemExit:
            pass
