"""Feed Fetcher Service - Télécharge les flux RSS."""
from typing import Optional
import requests


class FeedFetcher:
    """Télécharge les flux RSS."""
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
    
    def telecharger(self, url: str) -> Optional[str]:
        """Télécharge un flux RSS."""
        try:
            reponse = requests.get(url, timeout=self.timeout)
            reponse.raise_for_status()
            return reponse.text
        except requests.RequestException as e:
            print(f"Erreur: {e}")
            return None
