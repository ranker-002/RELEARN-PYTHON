#!/usr/bin/env python3
"""
Gestion de l'historique des calculs.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import List, Optional
from .operation import Calcul


class Historique:
    """Gère l'historique des calculs effectués."""
    
    def __init__(self, fichier: str = "data/historique.json"):
        """
        Initialise l'historique.
        
        Args:
            fichier: Chemin du fichier de sauvegarde
        """
        self.fichier = Path(fichier)
        self.calculs: List[Calcul] = []
        self._charger()
    
    def _charger(self):
        """Charge l'historique depuis le fichier."""
        if self.fichier.exists():
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.calculs = [Calcul.depuis_dict(d) for d in data]
            except (json.JSONDecodeError, KeyError):
                self.calculs = []
    
    def _sauvegarder(self):
        """Sauvegarde l'historique dans le fichier."""
        self.fichier.parent.mkdir(parents=True, exist_ok=True)
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump([c.vers_dict() for c in self.calculs], f, indent=2, ensure_ascii=False)
    
    def ajouter(self, calcul: Calcul):
        """
        Ajoute un calcul à l'historique.
        
        Args:
            calcul: Calcul à ajouter
        """
        self.calculs.append(calcul)
        if len(self.calculs) > 1000:
            self.calculs = self.calculs[-1000:]
        self._sauvegarder()
    
    def ajouter_expression(self, expression: str, resultat: float, 
                          valide: bool = True, erreur: Optional[str] = None):
        """
        Ajoute une expression à l'historique.
        
        Args:
            expression: Expression mathématique
            resultat: Résultat du calcul
            valide: Si le calcul est valide
            erreur: Message d'erreur si invalide
        """
        calcul = Calcul(expression=expression, resultat=resultat, 
                       valide=valide, erreur=erreur)
        self.ajouter(calcul)
    
    def afficher(self, n: int = 10) -> str:
        """
        Retourne les derniers calculs formatés.
        
        Args:
            n: Nombre de calculs à afficher
            
        Returns:
            Chaîne formatée
        """
        if not self.calculs:
            return "Aucun calcul dans l'historique."
        
        resultat = []
        for calcul in self.calculs[-n:]:
            if calcul.valide:
                resultat.append(f"  {calcul.expression} = {calcul.resultat}")
            else:
                resultat.append(f"  {calcul.expression} = ERREUR: {calcul.erreur}")
        
        return "\n".join(resultat)
    
    def tout_afficher(self) -> List[Calcul]:
        """Retourne tous les calculs."""
        return self.calculs.copy()
    
    def effacer(self):
        """Efface l'historique."""
        self.calculs = []
        self._sauvegarder()
    
    def effacer_anciens(self, jours: int = 7):
        """
        Efface les calculs anciens.
        
        Args:
            jours: Âge minimum en jours
        """
        maintenant = datetime.now()
        self.calculs = [
            c for c in self.calculs
            if (maintenant - c.timestamp).days < jours
        ]
        self._sauvegarder()
    
    def compter(self) -> int:
        """Retourne le nombre de calculs."""
        return len(self.calculs)
    
    def dernier(self) -> Optional[Calcul]:
        """Retourne le dernier calcul."""
        return self.calculs[-1] if self.calculs else None
    
    def exporter_json(self, chemin: Optional[str] = None) -> str:
        """
        Exporte l'historique en JSON.
        
        Args:
            chemin: Chemin du fichier (auto-généré si None)
            
        Returns:
            Chemin du fichier
        """
        if chemin is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            chemin = f"data/historique_export_{timestamp}.json"
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump([c.vers_dict() for c in self.calculs], f, indent=2, ensure_ascii=False)
        
        return chemin
    
    def get_statistiques(self) -> dict:
        """
        Retourne les statistiques de l'historique.
        
        Returns:
            Dictionnaire de statistiques
        """
        if not self.calculs:
            return {"total": 0, "valides": 0, "erreurs": 0, "moyenne": 0}
        
        valides = [c.resultat for c in self.calculs if c.valide]
        
        return {
            "total": len(self.calculs),
            "valides": len(valides),
            "erreurs": len(self.calculs) - len(valides),
            "moyenne": sum(valides) / len(valides) if valides else 0,
        }
