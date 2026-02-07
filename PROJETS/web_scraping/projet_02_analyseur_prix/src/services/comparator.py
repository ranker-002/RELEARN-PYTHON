#!/usr/bin/env python3
"""
Service de comparaison de prix.
"""

from typing import List, Dict, Any, Optional


class PriceComparator:
    """Compare les prix de plusieurs produits."""
    
    def comparer(self, produits: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Compare une liste de produits et retourne les résultats triés par prix.
        
        Args:
            produits: Liste de dictionnaires contenant les informations des produits
            
        Returns:
            Liste triée avec les comparaisons
        """
        if not produits:
            return []
        
        resultats = []
        seen_titres = {}
        
        for produit in produits:
            titre = produit.get("titre", "Produit inconnu")
            prix = produit.get("prix")
            
            if prix is None:
                continue
            
            if titre not in seen_titres:
                seen_titres[titre] = []
            seen_titres[titre].append(produit)
        
        for titre, items in seen_titres.items():
            prix_valides = [p.get("prix", 0) for p in items if p.get("prix") is not None]
            
            if not prix_valides:
                continue
            
            prix_min = min(prix_valides)
            prix_max = max(prix_valides)
            moyenne = sum(prix_valides) / len(prix_valides)
            
            meilleur_site = min(items, key=lambda x: x.get("prix", float("inf")))
            
            resultats.append({
                "titre": titre,
                "prix_min": prix_min,
                "prix_max": prix_max,
                "moyenne": moyenne,
                "nb_offres": len(prix_valides),
                "meilleur_site": meilleur_site.get("site", "N/A"),
                "meilleur_url": meilleur_site.get("url", ""),
                "produits": items,
            })
        
        return sorted(resultats, key=lambda x: x.get("prix_min", float("inf")))
    
    def trouver_meilleur_prix(self, produits: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Trouve le produit au meilleur prix.
        
        Args:
            produits: Liste de dictionnaires des produits
            
        Returns:
            Le produit au meilleur prix ou None
        """
        if not produits:
            return None
        
        produits_avec_prix = [p for p in produits if p.get("prix") is not None]
        
        if not produits_avec_prix:
            return None
        
        return min(produits_avec_prix, key=lambda x: x.get("prix", float("inf")))
    
    def calculer_economie(self, produits: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calcule les économies potentielles.
        
        Args:
            produits: Liste de dictionnaires des produits
            
        Returns:
            Dictionnaire avec les économies
        """
        comparaisons = self.comparer(produits)
        
        if not comparaisons:
            return {"economies": [], "total_economies": 0}
        
        economies = []
        total_economies = 0
        
        for comp in comparaisons:
            if comp.get("nb_offres", 0) > 1:
                eco = comp["prix_max"] - comp["prix_min"]
                total_economies += eco
                economies.append({
                    "titre": comp["titre"][:50],
                    "economie": eco,
                    "pourcentage": (eco / comp["prix_max"]) * 100 if comp["prix_max"] > 0 else 0,
                })
        
        return {
            "economies": sorted(economies, key=lambda x: x["economie"], reverse=True),
            "total_economies": total_economies,
        }
