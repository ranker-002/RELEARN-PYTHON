#!/usr/bin/env python3
"""
Gestionnaire de Tâches CLI - Projet d'apprentissage.

ÉNONCÉ:
--------
Implémentez un gestionnaire de tâches en ligne de commande avec:
- CRUD des tâches (créer, lister, modifier, supprimer)
- Projets et tags pour organisation
- Filtrage et recherche avancée
- Export (JSON, CSV, Markdown)
- Persistance des données

TODO: Implémenter la logique du projet.
"""

import argparse
from typing import List, Optional


class Tache:
    """Tâche à implémenter."""
    
    def __init__(self, titre: str):
        self.id = ""
        self.titre = titre
        self.description = ""
        self.statut = "todo"
        self.priorite = "moyenne"
        self.projet = ""
        self.tags = []
        self.date_echeance = None
        self.date_creation = None


class GestionnaireTaches:
    """Gestionnaire à implémenter."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.taches = []
        self.projets = []
        self.tags = []
    
    def ajouter_tache(self, titre: str) -> Tache:
        """Ajouter une tâche."""
        raise NotImplementedError
    
    def lister_taches(self, filtre: str = None) -> List[Tache]:
        """Lister les tâches."""
        raise NotImplementedError
    
    def marquer_terminee(self, tache_id: str) -> bool:
        """Marquer une tâche comme terminée."""
        raise NotImplementedError
    
    def supprimer_tache(self, tache_id: str) -> bool:
        """Supprimer une tâche."""
        raise NotImplementedError
    
    def get_statistiques(self) -> dict:
        """Retourner les statistiques."""
        raise NotImplementedError


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description="Gestionnaire de Tâches CLI")
    parser.add_argument("--list", action="store_true", help="Lister les tâches")
    parser.add_argument("--add", metavar="TACHE", help="Ajouter une tâche")
    parser.add_argument("--done", metavar="ID", help="Marquer comme terminée")
    parser.add_argument("--stats", action="store_true", help="Afficher les statistiques")
    
    args = parser.parse_args()
    
    print("=== Gestionnaire de Tâches CLI ===")
    print("TODO: Implémenter la logique")
    
    if args.list:
        print("Liste des tâches...")
    elif args.add:
        print(f"Ajouter: {args.add}")
    elif args.done:
        print(f"Marquer comme faite: {args.done}")
    elif args.stats:
        print("Statistiques...")
    else:
        print("\nUtiliser --help pour voir les options")


if __name__ == "__main__":
    main()
