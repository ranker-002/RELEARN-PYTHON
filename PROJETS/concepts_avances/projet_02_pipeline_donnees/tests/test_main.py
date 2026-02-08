"""Tests for main module."""
import sys
import pytest
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestMain:
    """Test cases for main module."""
    
    def test_initialization(self):
        """Test application initialization."""
        from src.main import Projet02PipelineDonnees
        app = Projet02PipelineDonnees()
        assert app is not None
    
    def test_example(self):
        """Example test case."""
        assert True
