#!/usr/bin/env python3
"""
Service de gestion des alertes de prix.
"""

from typing import Dict, List, Any


class PriceAlerter:
    """Gère les alertes de prix."""
    
    def __init__(self, seuil_default: float = 0.1):
        """
        Initialise l'alerteur.
        
        Args:
            seuil_default: Pourcentage de baisse par défaut pour les alertes
        """
        self.seuils: Dict[str, float] = {}
        self.seuil_default = seuil_default
        self.historique_alertes: List[Dict[str, Any]] = []
    
    def ajouter_alerte(self, url: str, seuil: float):
        """
        Ajoute une alerte pour une URL.
        
        Args:
            url: URL du produit
            seuil: Seuil de prix pour l'alerte
        """
        self.seuils[url] = seuil
    
    def supprimer_alerte(self, url: str):
        """Supprime une alerte."""
        if url in self.seuils:
            del self.seuils[url]
    
    def lister_alertes(self) -> List[Dict[str, Any]]:
        """Liste toutes les alertes."""
        return [
            {"url": url, "seuil": seuil}
            for url, seuil in self.seuils.items()
        ]
    
    def verifier(self, produit: Dict[str, Any]) -> List[str]:
        """
        Vérifie si un produit déclenche une alerte.
        
        Args:
            produit: Dictionnaire avec les informations du produit
            
        Returns:
            Liste des messages d'alerte
        """
        alertes = []
        url = produit.get("url", "")
        prix = produit.get("prix")
        
        if prix is None:
            return alertes
        
        if url in self.seuils:
            seuil = self.seuils[url]
            if prix <= seuil:
                message = self._creer_message_alerte(produit, seuil)
                alertes.append(message)
                self._enregistrer_alerte(produit, seuil)
        
        if prix <= 50:
            message = f"💰 BON PLAN: {produit.get('titre', 'N/A')[:40]}... à {prix}€!"
            alertes.append(message)
        
        return alertes
    
    def verifier_toutes(self, produits: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        Vérifie toutes les alertes pour une liste de produits.
        
        Args:
            produits: Liste de produits
            
        Returns:
            Dictionnaire URL -> liste d'alertes
        """
        resultats = {}
        
        for produit in produits:
            url = produit.get("url", "")
            alertes = self.verifier(produit)
            
            if alertes:
                resultats[url] = alertes
        
        return resultats
    
    def _creer_message_alerte(self, produit: Dict[str, Any], seuil: float) -> str:
        """Crée un message d'alerte."""
        titre = produit.get("titre", "N/A")[:40]
        prix = produit.get("prix", 0)
        site = produit.get("site", "N/A")
        
        reduction = ((produit.get("prix_precedent", prix) - prix) / produit.get("prix_precedent", 1)) * 100 if produit.get("prix_precedent") else 0
        
        return f"🚨 ALERTE PRIX: {titre}... est à {prix}€ sur {site} (seuil: {seuil}€) - réduction: {reduction:.1f}%"
    
    def _enregistrer_alerte(self, produit: Dict[str, Any], seuil: float):
        """Enregistre une alerte dans l'historique."""
        self.historique_alertes.append({
            "url": produit.get("url", ""),
            "titre": produit.get("titre", ""),
            "prix": produit.get("prix", 0),
            "seuil": seuil,
            "site": produit.get("site", ""),
        })
    
    def get_historique(self) -> List[Dict[str, Any]]:
        """Retourne l'historique des alertes."""
        return self.historique_alertes
