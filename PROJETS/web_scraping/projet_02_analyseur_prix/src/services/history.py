#!/usr/bin/env python3
"""
Service d'historique des prix.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional


class PriceHistory:
    """Gère l'historique des prix collectés."""
    
    def __init__(self, repertoire: str = "data/history"):
        """
        Initialise l'historique.
        
        Args:
            repertoire: Répertoire de stockage
        """
        self.repertoire = Path(repertoire)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        self.historique: Dict[str, List[Dict[str, Any]]] = {}
    
    def ajouter(self, url: str, resultat: Dict[str, Any]):
        """
        Ajoute une entrée à l'historique.
        
        Args:
            url: URL du produit
            resultat: Résultat du scraping
        """
        if url not in self.historique:
            self.historique[url] = []
        
        entree = {
            "date_collecte": datetime.now().isoformat(),
            "prix": resultat.get("prix"),
            "titre": resultat.get("titre"),
            "site": resultat.get("site"),
            "disponible": resultat.get("disponible"),
        }
        
        self.historique[url].append(entree)
    
    def obtenir_historique(self, url: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Obtient l'historique pour une URL ou toutes les URLs.
        
        Args:
            url: URL optionnelle
            
        Returns:
            Liste des entrées d'historique
        """
        if url:
            return self.historique.get(url, [])
        all_history = []
        for url_entries in self.historique.values():
            all_history.extend(url_entries)
        return sorted(all_history, key=lambda x: x.get("date_collecte", ""))
    
    def obtenir_tout(self) -> Dict[str, List[Dict[str, Any]]]:
        """Retourne tout l'historique."""
        return self.historique
    
    def effacer(self, url: Optional[str] = None):
        """
        Efface l'historique.
        
        Args:
            url: URL optionnelle (sinon tout effacer)
        """
        if url:
            if url in self.historique:
                del self.historique[url]
        else:
            self.historique.clear()
    
    def exporter_json(self, chemin: Optional[str] = None) -> str:
        """
        Exporte l'historique en JSON.
        
        Args:
            chemin: Chemin du fichier (auto-généré si non fourni)
            
        Returns:
            Chemin du fichier exporté
        """
        if chemin is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            chemin = str(self.repertoire / f"historique_{timestamp}.json")
        
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(self.historique, f, indent=2, ensure_ascii=False)
        
        return chemin
    
    def exporter_csv(self, chemin: Optional[str] = None) -> str:
        """
        Exporte l'historique en CSV.
        
        Args:
            chemin: Chemin du fichier (auto-généré si non fourni)
            
        Returns:
            Chemin du fichier exporté
        """
        if chemin is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            chemin = str(self.repertoire / f"historique_{timestamp}.csv")
        
        lignes = ["date_collecte,titre,prix,site,disponible,url"]
        
        for url, entrees in self.historique.items():
            for entree in entrees:
                ligne = f"{entree.get('date_collecte', '')}," \
                        f"\"{entree.get('titre', '').replace('\"', '\"\"')}\"," \
                        f"{entree.get('prix', '')}," \
                        f"{entree.get('site', '')}," \
                        f"{entree.get('disponible', '')}," \
                        f"{url}"
                lignes.append(ligne)
        
        with open(chemin, "w", encoding="utf-8") as f:
            f.write("\n".join(lignes))
        
        return chemin
    
    def importer_json(self, chemin: str):
        """
        Importe un historique depuis JSON.
        
        Args:
            chemin: Chemin du fichier JSON
        """
        with open(chemin, "r", encoding="utf-8") as f:
            self.historique = json.load(f)
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Retourne les statistiques de l'historique.
        
        Returns:
            Dictionnaire de statistiques
        """
        total_collectes = sum(len(v) for v in self.historique.values())
        sites = set()
        prix_totaux = []
        
        for entrees in self.historique.values():
            for entree in entrees:
                if entree.get("site"):
                    sites.add(entree["site"])
                if entree.get("prix") is not None:
                    prix_totaux.append(entree["prix"])
        
        return {
            "nb_produits_suivis": len(self.historique),
            "total_collectes": total_collectes,
            "nb_sites": len(sites),
            "prix_moyen": sum(prix_totaux) / len(prix_totaux) if prix_totaux else 0,
            "prix_min": min(prix_totaux) if prix_totaux else 0,
            "prix_max": max(prix_totaux) if prix_totaux else 0,
        }
