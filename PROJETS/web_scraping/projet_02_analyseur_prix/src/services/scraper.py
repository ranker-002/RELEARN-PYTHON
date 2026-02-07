#!/usr/bin/env python3
"""
Service de scraping pour récupérer les prix des sites e-commerce.
"""

import re
from typing import Optional, Dict, Any
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError


class PriceScraper:
    """Scraper pour récupérer les prix depuis différents sites e-commerce."""
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    
    TIMEOUT = 10
    
    SITES_CONFIG = {
        "amazon": {
            "domain": "amazon",
            "selecteur_titre": ["#productTitle", ".product-title"],
            "selecteur_prix": [".a-price .a-offscreen", ".a-price-price span", "#priceblock_ourprice"],
            "selecteur_prix_fraction": [".a-price-fraction", ".a-price-fraction"],
            "selecteur_dispo": ["#availability span", ".a-stock-status"],
        },
        "cdiscount": {
            "domain": "cdiscount",
            "selecteur_titre": [".fpProdName", ".productTitle"],
            "selecteur_prix": [".fpPrice.price", ".price", "#fpPrice"],
            "selecteur_prix_fraction": [],
            "selecteur_dispo": [".fpStock", ".stock", "#availability"],
        },
        "fnac": {
            "domain": "fnac",
            "selecteur_titre": [".fnacProductTitle", ".title"],
            "selecteur_prix": [".fnacPrice", ".price", ".userPrice"],
            "selecteur_prix_fraction": [],
            "selecteur_dispo": [".fnacStockStatus", ".stock"],
        },
        "rue_du_commerce": {
            "domain": "rue du commerce",
            "selecteur_titre": [".product-title", ".title"],
            "selecteur_prix": [".price", ".current-price", ".productPrice"],
            "selecteur_prix_fraction": [],
            "selecteur_dispo": [".availability", ".in-stock"],
        },
    }
    
    def __init__(self, timeout: int = TIMEOUT):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
    
    def detecter_site(self, url: str) -> str:
        """Détecte le site à partir de l'URL."""
        url_lower = url.lower()
        for site_name, config in self.SITES_CONFIG.items():
            if config["domain"] in url_lower:
                return site_name
        return "generic"
    
    def scraper_produit(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Scrappe un produit et retourne ses informations.
        
        Args:
            url: URL du produit
            
        Returns:
            Dict avec les informations du produit ou None en cas d'erreur
        """
        site = self.detecter_site(url)
        self.logger.info(f"Scraping {url} (site: {site})")
        
        try:
            response = self._fetch(url)
            if response is None:
                return None
            
            soup = BeautifulSoup(response.content, "html.parser")
            
            titre = self._extract_title(soup, site)
            prix = self._extract_price(soup, site)
            disponible = self._extract_availability(soup, site)
            
            resultat = {
                "url": url,
                "site": site,
                "titre": titre,
                "prix": prix,
                "disponible": disponible,
            }
            
            self.logger.info(f"Produit scrapé: {titre[:30]}... - {prix}€")
            return resultat
            
        except Exception as e:
            self.logger.error(f"Erreur lors du scraping: {e}")
            return None
    
    def _fetch(self, url: str) -> Optional[requests.Response]:
        """Récupère le contenu d'une URL."""
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response
        except Timeout:
            self.logger.error(f"Timeout lors de la requête: {url}")
        except ConnectionError:
            self.logger.error(f"Erreur de connexion: {url}")
        except RequestException as e:
            self.logger.error(f"Erreur de requête: {e}")
        return None
    
    def _extract_title(self, soup: BeautifulSoup, site: str) -> str:
        """Extrait le titre du produit."""
        config = self.SITES_CONFIG.get(site, {})
        selecteurs = config.get("selecteur_titre", [])
        
        for sel in selecteurs:
            elem = soup.select_one(sel)
            if elem:
                return elem.get_text(strip=True)
        
        h1 = soup.find("h1")
        if h1:
            return h1.get_text(strip=True)
        
        return "Produit inconnu"
    
    def _extract_price(self, soup: BeautifulSoup, site: str) -> Optional[float]:
        """Extrait le prix du produit."""
        config = self.SITES_CONFIG.get(site, {})
        selecteurs = config.get("selecteur_prix", [])
        
        for sel in selecteurs:
            elem = soup.select_one(sel)
            if elem:
                prix_str = elem.get_text(strip=True)
                prix = self._parse_price(prix_str)
                if prix is not None:
                    return prix
        
        return None
    
    def _parse_price(self, price_str: str) -> Optional[float]:
        """
        Convertit une chaîne de prix en float.
        
        Exemples:
            "99,99 €" -> 99.99
            "99.99€" -> 99.99
            "1 299,00 €" -> 1299.00
        """
        if not price_str:
            return None
        
        price_str = price_str.strip()
        
        prix = re.sub(r"[^\d,\.]", "", price_str)
        
        if "," in prix and "." in prix:
            if prix.index(",") > prix.index("."):
                prix = prix.replace(",", "").replace(".", "")
            else:
                prix = prix.replace(",", "")
        elif "," in prix:
            prix = prix.replace(",", ".")
        
        try:
            return float(prix) if prix else None
        except ValueError:
            return None
    
    def _extract_availability(self, soup: BeautifulSoup, site: str) -> str:
        """Extrait la disponibilité du produit."""
        config = self.SITES_CONFIG.get(site, {})
        selecteurs = config.get("selecteur_dispo", [])
        
        for sel in selecteurs:
            elem = soup.select_one(sel)
            if elem:
                texte = elem.get_text(strip=True).lower()
                if "indisponible" in texte or "rupture" in texte:
                    return "indisponible"
                elif "précommande" in texte:
                    return "precommande"
                elif "disponible" in texte or "en stock" in texte:
                    return "disponible"
        
        return "disponible"
    
    @property
    def logger(self):
        import logging
        return logging.getLogger("PriceScraper")
