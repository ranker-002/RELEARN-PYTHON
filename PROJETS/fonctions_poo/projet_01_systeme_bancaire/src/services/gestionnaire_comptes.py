#!/usr/bin/env python3
"""
Service for managing bank accounts.
"""

from typing import Optional, List, Dict
from datetime import datetime
from pathlib import Path
import json
import uuid

from models import Client, Compte, TypeCompte, StatutCompte


class GestionnaireComptes:
    """Manages bank accounts and clients."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.repertoire = Path(repertoire_donnees)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        self.clients: Dict[str, Client] = {}
        self.comptes: Dict[str, Compte] = {}
        self._charger_donnees()
    
    def _chemin_fichier(self, nom: str) -> Path:
        return self.repertoire / f"{nom}.json"
    
    def _charger_donnees(self):
        """Load data from files."""
        for fichier in self.repertoire.glob("*.json"):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    if fichier.stem.startswith("client"):
                        for c in donnees:
                            client = Client(**c)
                            self.clients[client.id] = client
                    elif fichier.stem.startswith("compte"):
                        for c in donnees:
                            compte = Compte(**c)
                            self.comptes[compte.id] = compte
            except (json.JSONDecodeError, FileNotFoundError):
                pass
    
    def _sauvegarder_donnees(self):
        """Save data to files."""
        clients_data = [vars(c) for c in self.clients.values()]
        comptes_data = [vars(c) for c in self.comptes.values()]
        
        with open(self._chemin_fichier("clients"), 'w', encoding='utf-8') as f:
            json.dump(clients_data, f, indent=2, default=str)
        with open(self._chemin_fichier("comptes"), 'w', encoding='utf-8') as f:
            json.dump(comptes_data, f, indent=2, default=str)
    
    def creer_client(self, nom: str, prenom: str, email: str, 
                     telephone: str, adresse: str = "") -> Client:
        """Create a new client."""
        client = Client(
            id="",
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            adresse=adresse
        )
        self.clients[client.id] = client
        self._sauvegarder_donnees()
        return client
    
    def creer_compte(self, client_id: str, type_compte: TypeCompte,
                     decouvert_autorise: float = 0.0, taux_interet: float = 0.0) -> Optional[Compte]:
        """Create a new account for a client."""
        if client_id not in self.clients:
            return None
        
        compte = Compte(
            id="",
            numero="",
            client_id=client_id,
            type_compte=type_compte,
            decouvert_autorise=decouvert_autorise,
            taux_interet=taux_interet
        )
        self.comptes[compte.id] = compte
        self._sauvegarder_donnees()
        return compte
    
    def get_client(self, client_id: str) -> Optional[Client]:
        return self.clients.get(client_id)
    
    def get_compte(self, compte_id: str) -> Optional[Compte]:
        return self.comptes.get(compte_id)
    
    def get_comptes_client(self, client_id: str) -> List[Compte]:
        return [c for c in self.comptes.values() if c.client_id == client_id]
    
    def get_all_clients(self) -> List[Client]:
        return list(self.clients.values())
    
    def get_all_comptes(self) -> List[Compte]:
        return list(self.comptes.values())
    
    def bloquer_compte(self, compte_id: str) -> bool:
        compte = self.get_compte(compte_id)
        if compte:
            compte.statut = StatutCompte.BLOQUE
            self._sauvegarder_donnees()
            return True
        return False
    
    def reactiver_compte(self, compte_id: str) -> bool:
        compte = self.get_compte(compte_id)
        if compte:
            compte.statut = StatutCompte.ACTIF
            self._sauvegarder_donnees()
            return True
        return False
    
    def rechercher_clients(self, critere: str) -> List[Client]:
        critere = critere.lower()
        return [c for c in self.clients.values() 
                if critere in c.nom.lower() or critere in c.prenom.lower() 
                or critere in c.email.lower()]
