"""Article Filter Service - Filtre les articles."""
from typing import Dict, List
from models import Article


class ArticleFilter:
    """Filtre les articles par mots-clés."""
    
    def __init__(self, config: Dict):
        self.config = config or {}
        self.inclure = config.get("mots_cles_inclure", [])
        self.exclure = config.get("mots_cles_exclure", [])
    
    def appliquer(self, articles: List[Article]) -> List[Article]:
        """Applique les filtres."""
        if not self.inclure and not self.exclure:
            return articles
        
        resultat = []
        for article in articles:
            texte = (article.titre + " " + article.description).lower()
            
            doit_inclure = not self.inclure or any(m in texte for m in self.inclure)
            doit_exclure = any(m in texte for m in self.exclure)
            
            if doit_inclure and not doit_exclure:
                resultat.append(article)
        
        return resultat
