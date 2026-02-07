"""Tests for models."""
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestModels:
    """Test cases for models."""
    
    def test_model_creation(self):
        """Test model instantiation."""
        from src.models import *
        # TODO: Add tests
        assert True
