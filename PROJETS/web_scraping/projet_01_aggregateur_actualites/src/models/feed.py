"""
Module Feed - Représente un flux RSS.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

from .article import Article


@dataclass
class FluxRSS:
    """
    Représente un flux RSS.
    
    Attributes:
        nom: Nom du flux
        url: URL du flux
        categorie: Catégorie du flux
        articles: Liste des articles
        date_derniere_mise_a_jour: Date de dernière mise à jour
    """
    nom: str
    url: str
    categorie: str
    articles: List[Article] = field(default_factory=list)
    date_derniere_mise_a_jour: Optional[datetime] = None
    
    def __post_init__(self):
        """Initialise les valeurs par défaut."""
        if self.articles is None:
            self.articles = []
        if self.date_derniere_mise_a_jour is None:
            self.date_derniere_mise_a_jour = datetime.now()
    
    @property
    def nb_articles(self) -> int:
        """Retourne le nombre d'articles."""
        return len(self.articles)
    
    @property
    def nb_articles_non_lus(self) -> int:
        """Retourne le nombre d'articles non lus."""
        return sum(1 for a in self.articles if not a.est_lu())
    
    def articles_recents(self, jours: int = 7) -> List[Article]:
        """Retourne les articles récents."""
        return [a for a in self.articles if a.est_recent(jours)]
    
    def ajouter_article(self, article: Article):
        """Ajoute un article au flux."""
        self.articles.append(article)
    
    def __str__(self) -> str:
        """Représentation textuelle."""
        return f"{self.nom} ({self.nb_articles} articles)"
    
    def __repr__(self) -> str:
        """Représentation technique."""
        return f"FluxRSS(nom='{self.nom}', url='{self.url}', articles={self.nb_articles})"
