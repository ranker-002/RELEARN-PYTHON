"""Tests for main module."""
import pytest
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestMain:
    """Test cases for main module."""
    
    def test_initialization(self):
        """Test application initialization."""
        from src.main import Projet01ApiRestApplication
        app = Projet01ApiRestApplication()
        assert app is not None
    
    def test_example(self):
        """Example test case."""
        assert True
