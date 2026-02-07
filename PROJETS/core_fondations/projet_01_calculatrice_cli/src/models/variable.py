#!/usr/bin/env python3
"""
Gestion des variables personnalisées.
"""

import json
from pathlib import Path
from typing import Optional, Dict


class Variable:
    """Représente une variable avec un nom et une valeur."""
    
    def __init__(self, nom: str, valeur: float, description: str = ""):
        self.nom = nom
        self.valeur = float(valeur)
        self.description = description
    
    def __str__(self) -> str:
        return f"{self.nom} = {self.valeur}"
    
    def __repr__(self) -> str:
        return f"Variable({self.nom!r}, {self.valeur!r})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Variable):
            return False
        return self.nom == other.nom and self.valeur == other.valeur
    
    def __hash__(self) -> int:
        return hash((self.nom, self.valeur))
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Variable):
            return NotImplemented
        return self.nom < other.nom
    
    def mise_a_jour(self, nouvelle_valeur: float):
        """Met à jour la valeur de la variable."""
        self.valeur = float(nouvelle_valeur)
    
    def vers_dict(self) -> dict:
        return {
            "nom": self.nom,
            "valeur": self.valeur,
            "description": self.description,
        }
    
    @classmethod
    def depuis_dict(cls, data: dict) -> "Variable":
        return cls(
            nom=data["nom"],
            valeur=data["valeur"],
            description=data.get("description", ""),
        )


class GestionnaireVariables:
    """Gère un ensemble de variables."""
    
    def __init__(self, fichier: str = "data/variables.json"):
        self.variables: Dict[str, Variable] = {}
        self.fichier = Path(fichier)
        self._charger()
    
    def _charger(self):
        """Charge les variables depuis le fichier."""
        if self.fichier.exists():
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for nom, valeur in data.items():
                        if isinstance(valeur, dict):
                            self.variables[nom] = Variable.depuis_dict(valeur)
                        else:
                            self.variables[nom] = Variable(nom, valeur)
            except (json.JSONDecodeError, KeyError):
                self.variables = {}
    
    def _sauvegarder(self):
        """Sauvegarde les variables dans le fichier."""
        self.fichier.parent.mkdir(parents=True, exist_ok=True)
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump({nom: var.vers_dict() for nom, var in self.variables.items()}, 
                     f, indent=2, ensure_ascii=False)
    
    def ajouter(self, nom: str, valeur: float, description: str = "") -> Variable:
        """
        Ajoute ou met à jour une variable.
        
        Args:
            nom: Nom de la variable
            valeur: Valeur de la variable
            description: Description optionnelle
            
        Returns:
            La variable créée ou mise à jour
        """
        variable = Variable(nom, valeur, description)
        self.variables[nom] = variable
        self._sauvegarder()
        return variable
    
    def supprimer(self, nom: str) -> bool:
        """
        Supprime une variable.
        
        Args:
            nom: Nom de la variable
            
        Returns:
            True si supprimée, False sinon
        """
        if nom in self.variables:
            del self.variables[nom]
            self._sauvegarder()
            return True
        return False
    
    def obtenir(self, nom: str) -> Optional[Variable]:
        """
        Obtient une variable par son nom.
        
        Args:
            nom: Nom de la variable
            
        Returns:
            La variable ou None
        """
        return self.variables.get(nom)
    
    def valeur(self, nom: str) -> Optional[float]:
        """
        Obtient la valeur d'une variable.
        
        Args:
            nom: Nom de la variable
            
        Returns:
            La valeur ou None
        """
        variable = self.obtenir(nom)
        return variable.valeur if variable else None
    
    def lister(self) -> List[Variable]:
        """Liste toutes les variables."""
        return sorted(self.variables.values(), key=lambda v: v.nom)
    
    def exister(self, nom: str) -> bool:
        """Vérifie si une variable existe."""
        return nom in self.variables
    
    def effacer(self):
        """Efface toutes les variables."""
        self.variables = {}
        self._sauvegarder()
    
    def importer_json(self, chemin: str):
        """
        Importe des variables depuis un fichier JSON.
        
        Args:
            chemin: Chemin du fichier JSON
        """
        with open(chemin, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for nom, valeur in data.items():
            if isinstance(valeur, dict):
                self.variables[nom] = Variable.depuis_dict(valeur)
            else:
                self.variables[nom] = Variable(nom, valeur)
        self._sauvegarder()
    
    def exporter_json(self, chemin: Optional[str] = None) -> str:
        """
        Exporte les variables vers un fichier JSON.
        
        Args:
            chemin: Chemin du fichier (auto-généré si None)
            
        Returns:
            Chemin du fichier
        """
        if chemin is None:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            chemin = f"data/variables_export_{timestamp}.json"
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump({nom: var.vers_dict() for nom, var in self.variables.items()}, 
                     f, indent=2, ensure_ascii=False)
        
        return chemin
    
    def substituer(self, texte: str) -> str:
        """
        Substitue les variables dans une expression.
        
        Args:
            texte: Expression contenant des variables
            
        Returns:
            Expression avec les valeurs substituées
        """
        resultat = texte
        for nom, variable in sorted(self.variables.items(), key=lambda x: -len(x[0])):
            resultat = resultat.replace(nom, str(variable.valeur))
        return resultat
    
    def compter(self) -> int:
        """Retourne le nombre de variables."""
        return len(self.variables)
