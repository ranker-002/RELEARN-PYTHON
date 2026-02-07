"""
Module Article - Représente un article de news.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class LuStatus(Enum):
    """Statut de lecture d'un article."""
    NON_LU = "non_lu"
    EN_COURS = "en_cours"
    LU = "lu"


@dataclass
class Article:
    """
    Représente un article de news.
    
    Attributes:
        titre: Titre de l'article
        description: Résumé ou contenu de l'article
        lien: URL de l'article
        date_publication: Date de publication
        source: Nom de la source (flux)
        categorie: Catégorie de l'article
        guid: Identifiant unique
        statut_lecture: Statut de lecture
        date_ajout: Date d'ajout à l'agrégateur
    """
    titre: str
    description: str
    lien: str
    date_publication: datetime
    source: str
    categorie: Optional[str] = None
    guid: Optional[str] = None
    statut_lecture: LuStatus = LuStatus.NON_LU
    date_ajout: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Initialise les valeurs par défaut."""
        if self.guid is None:
            self.guid = self.lien
        if self.date_ajout is None:
            self.date_ajout = datetime.now()
    
    def est_recent(self, jours: int = 7) -> bool:
        """
        Vérifie si l'article est récent.
        
        Args:
            jours: Nombre de jours pour définir "récent"
            
        Returns:
            True si l'article est récent
        """
        delta = datetime.now() - self.date_publication
        return delta.days < jours
    
    def est_lu(self) -> bool:
        """Vérifie si l'article a été lu."""
        return self.statut_lecture == LuStatus.LU
    
    def __str__(self) -> str:
        """Représentation textuelle de l'article."""
        statut = "✓" if self.est_lu() else "○"
        return f"[{statut}] {self.titre}"
    
    def __repr__(self) -> str:
        """Représentation technique."""
        return f"Article(titre='{self.titre[:30]}...', source='{self.source}')"
