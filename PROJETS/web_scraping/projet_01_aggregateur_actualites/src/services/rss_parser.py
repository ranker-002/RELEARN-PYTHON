"""RSS Parser Service - Parse les flux RSS/Atom."""
from datetime import datetime
from typing import Optional, Dict, List
from xml.etree import ElementTree as ET
from models import Article, FluxRSS


class RSSParser:
    """Parser pour flux RSS 2.0 et Atom."""
    
    DATE_FORMATS = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S%z",
    ]
    
    def parser_date(self, date_str: str) -> Optional[datetime]:
        """Convertit une date RSS en datetime."""
        for fmt in self.DATE_FORMATS:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue
        return None
    
    def parser_flux(self, contenu_xml: str, subscription: Dict) -> FluxRSS:
        """Parse un flux RSS."""
        try:
            root = ET.fromstring(contenu_xml)
        except ET.ParseError:
            raise ValueError("XML invalide")
        
        nom = subscription.get("nom", "Inconnu")
        url = subscription.get("url", "")
        categorie = subscription.get("categorie", "général")
        
        flux = FluxRSS(nom=nom, url=url, categorie=categorie)
        
        # Parser les items (RSS 2.0)
        for item in root.findall(".//item"):
            article = self._parser_item(item, nom)
            if article:
                flux.articles.append(article)
        
        return flux
    
    def _parser_item(self, item, source: str) -> Optional[Article]:
        """Parse un item RSS."""
        try:
            titre = self._get_text(item, "title") or "Sans titre"
            description = self._get_text(item, "description") or ""
            lien = self._get_text(item, "link") or ""
            date_str = self._get_text(item, "pubDate") or ""
            categorie = self._get_text(item, "category")
            guid = self._get_text(item, "guid") or lien
            
            date_pub = self.parser_date(date_str) or datetime.now()
            
            return Article(
                titre=titre,
                description=description,
                lien=lien,
                date_publication=date_pub,
                source=source,
                categorie=categorie,
                guid=guid
            )
        except Exception:
            return None
    
    def _get_text(self, parent, tag: str) -> Optional[str]:
        """Récupère le texte d'un élément."""
        elem = parent.find(tag)
        return elem.text.strip() if elem is not None and elem.text else None
