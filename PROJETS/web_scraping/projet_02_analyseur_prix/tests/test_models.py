"""Tests for models."""
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestPrix:
    """Test cases for Prix model."""
    
    def test_prix_creation(self):
        """Test Prix instantiation."""
        from src.models import Prix
        prix = Prix(montant=99.99, devise="EUR")
        assert prix.montant == 99.99
        assert prix.devise == "EUR"
        assert prix.date_collecte is not None
    
    def test_prix_formater(self):
        """Test Prix formatting."""
        from src.models import Prix
        prix = Prix(montant=99.99)
        assert "99.99" in prix.formater()
    
    def test_prix_vers_dict(self):
        """Test Prix serialization."""
        from src.models import Prix
        prix = Prix(montant=50.0, devise="EUR", site="amazon")
        data = prix.vers_dict()
        assert data["montant"] == 50.0
        assert data["site"] == "amazon"
    
    def test_prix_comparison(self):
        """Test Prix comparison."""
        from src.models import Prix
        p1 = Prix(montant=50.0)
        p2 = Prix(montant=100.0)
        assert p1 < p2
        assert p2 > p1


class TestProduit:
    """Test cases for Produit model."""
    
    def test_produit_creation(self):
        """Test Produit instantiation."""
        from src.models import Produit
        produit = Produit(
            id="test_001",
            nom="Test Product",
            url="https://example.com/product"
        )
        assert produit.id == "test_001"
        assert produit.nom == "Test Product"
        assert produit.prix_historique == []
    
    def test_produit_ajouter_prix(self):
        """Test adding price to product."""
        from src.models import Produit, Prix
        produit = Produit(id="test_001", nom="Test", url="https://example.com")
        prix = Prix(montant=75.0)
        produit.ajouter_prix(prix)
        assert produit.prix_actuel.montant == 75.0
        assert len(produit.prix_historique) == 1
    
    def test_produit_est_alerte(self):
        """Test product alert status."""
        from src.models import Produit, Prix
        produit = Produit(id="test_001", nom="Test", url="https://example.com", seuil_alerte=100.0)
        assert produit.est_alerte() is False
        produit.ajouter_prix(Prix(montant=50.0))
        assert produit.est_alerte() is True


class TestDisponibilite:
    """Test cases for Disponibilite enum."""
    
    def test_disponibilite_values(self):
        """Test Disponibilite enum values."""
        from src.models import Disponibilite
        assert Disponibilite.DISPONIBLE.value == "disponible"
        assert Disponibilite.INDISPONIBLE.value == "indisponible"
        assert Disponibilite.RUPTURE.value == "rupture"
        assert Disponibilite.PRECOMMANDE.value == "precommande"
