#!/usr/bin/env python3
"""
Système Bancaire CLI - Projet d'apprentissage.

ÉNONCÉ:
--------
Implémentez un système bancaire complet avec:
- Gestion des clients (création, recherche)
- Gestion des comptes (courant, épargne, professionnel)
- Transactions (dépôt, retrait, virement)
- Historique et relevés
- Frais et intérêts

TODO: Implémenter la logique du projet.
"""

import argparse
from typing import List, Optional


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"


class Client:
    """Client bancaire à implémenter."""
    
    def __init__(self, nom: str, prenom: str, email: str):
        self.id = ""
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = ""
        self.adresse = ""


class Compte:
    """Compte bancaire à implémenter."""
    
    def __init__(self, client_id: str, type_compte: str):
        self.id = ""
        self.numero = ""
        self.client_id = client_id
        self.type_compte = type_compte
        self.solde = 0.0
        self.decouvert_autorise = 0.0


class GestionnaireComptes:
    """Gestionnaire de comptes à implémenter."""
    
    def __init__(self):
        self.clients = []
        self.comptes = []
    
    def creer_client(self, nom: str, prenom: str, email: str) -> Client:
        """Créer un client."""
        raise NotImplementedError
    
    def creer_compte(self, client_id: str, type_compte: str) -> Compte:
        """Créer un compte."""
        raise NotImplementedError
    
    def deposer(self, compte_id: str, montant: float) -> bool:
        """Déposer de l'argent."""
        raise NotImplementedError
    
    def retirer(self, compte_id: str, montant: float) -> bool:
        """Retirer de l'argent."""
        raise NotImplementedError


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description="Système Bancaire CLI")
    parser.add_argument("--clients", action="store_true", help="Lister les clients")
    parser.add_argument("--comptes", action="store_true", help="Lister les comptes")
    parser.add_argument("--stats", action="store_true", help="Afficher les statistiques")
    
    args = parser.parse_args()
    
    print("=== Système Bancaire CLI ===")
    print("TODO: Implémenter la logique")
    
    if args.clients:
        print("Liste des clients...")
    elif args.comptes:
        print("Liste des comptes...")
    elif args.stats:
        print("Statistiques...")
    else:
        print("\nUtiliser --help pour voir les options")


if __name__ == "__main__":
    main()
