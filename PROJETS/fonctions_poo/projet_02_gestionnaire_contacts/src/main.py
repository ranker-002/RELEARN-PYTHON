#!/usr/bin/env python3
"""
Gestionnaire de Contacts CLI

Application de gestion de contacts avec:
- CRUD complet des contacts
- Organisation par groupes
- Suivi des interactions
- Recherche et filtres
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from models import Contact, CategorieContact, StatutContact
from services.gestionnaire_contacts import ServiceContacts


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"


class Projet02GestionnaireContacts:
    """Application principale."""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        """Initialise l'application."""
        self.service = ServiceContacts()
        self.logger = self._setup_logging()
        self.logger.info("Application initialisée")
    
    def _setup_logging(self):
        """Configure le logging."""
        import logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("gestionnaire_contacts")
    
    def _afficher_banniere(self):
        """Affiche la bannière."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print(f"╔══════════════════════════════════════════════════╗")
        print(f"║          GESTIONNAIRE DE CONTACTS v{self.VERSION}         ║")
        print(f"╚══════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
    
    def _afficher_menu(self):
        """Affiche le menu principal."""
        print(f"\n{Colors.BOLD}=== MENU PRINCIPAL ==={Colors.RESET}")
        print(f"{Colors.CYAN}1.{Colors.RESET} Gestion des contacts")
        print(f"{Colors.CYAN}2.{Colors.RESET} Gestion des groupes")
        print(f"{Colors.CYAN}3.{Colors.RESET} Interactions")
        print(f"{Colors.CYAN}4.{Colors.RESET} Recherche et filtres")
        print(f"{Colors.CYAN}5.{Colors.RESET} Statistiques")
        print(f"{Colors.CYAN}6.{Colors.RESET} Quitter")
        print()
    
    def creer_contact(self):
        """Crée un nouveau contact."""
        print(f"\n{Colors.BOLD}=== NOUVEAU CONTACT ==={Colors.RESET}")
        nom = input(f"{Colors.CYAN}Nom: {Colors.RESET}").strip()
        prenom = input(f"{Colors.CYAN}Prénom: {Colors.RESET}").strip()
        email = input(f"{Colors.CYAN}Email: {Colors.RESET}").strip()
        telephone = input(f"{Colors.CYAN}Téléphone: {Colors.RESET}").strip()
        adresse = input(f"{Colors.CYAN}Adresse (optionnel): {Colors.RESET}").strip()
        
        print(f"\n{Colors.CYAN}Catégories:{Colors.RESET}")
        for i, cat in enumerate(CategorieContact, 1):
            print(f"  {i}. {cat.value}")
        
        try:
            choix = int(input(f"\n{Colors.CYAN}Choix (1-{len(CategorieContact)}): {Colors.RESET}")) - 1
            categorie = list(CategorieContact)[choix]
        except (ValueError, IndexError):
            categorie = CategorieContact.AUTRE
        
        contact = self.service.creer_contact(nom, prenom, email, telephone, adresse, categorie)
        print(f"\n{Colors.GREEN}Contact créé avec succès!{Colors.RESET}")
        print(f"{Colors.CYAN}ID: {Colors.RESET}{contact.id[:8]}")
    
    def lister_contacts(self):
        """Liste tous les contacts."""
        contacts = self.service.get_all_contacts()
        if not contacts:
            print(f"\n{Colors.YELLOW}Aucun contact trouvé.{Colors.RESET}")
            return
        
        print(f"\n{Colors.BOLD}=== CONTACTS ({len(contacts)}) ==={Colors.RESET}")
        for contact in contacts:
            statut_icon = "★" if contact.statut == StatutContact.FAVORI else " "
            print(f"{Colors.CYAN}{statut_icon}{Colors.RESET} {contact.nom_complet} ({contact.categorie.value})")
            print(f"   📧 {contact.email} | 📱 {contact.telephone}")
            print(f"   ID: {contact.id[:8]}")
    
    def rechercher_contact(self):
        """Recherche un contact."""
        critere = input(f"\n{Colors.CYAN}Rechercher: {Colors.RESET}").strip()
        resultats = self.service.rechercher_contacts(critere)
        
        if not resultats:
            print(f"\n{Colors.YELLOW}Aucun résultat.{Colors.RESET}")
            return
        
        print(f"\n{Colors.BOLD}=== RÉSULTATS ({len(resultats)}) ==={Colors.RESET}")
        for contact in resultats:
            print(f"{Colors.CYAN}-{Colors.RESET} {contact.nom_complet} - {contact.email}")
    
    def creer_groupe(self):
        """Crée un nouveau groupe."""
        print(f"\n{Colors.BOLD}=== NOUVEAU GROUPE ==={Colors.RESET}")
        nom = input(f"{Colors.CYAN}Nom du groupe: {Colors.RESET}").strip()
        description = input(f"{Colors.CYAN}Description (optionnel): {Colors.RESET}").strip()
        
        groupe = self.service.creer_groupe(nom, description)
        print(f"\n{Colors.GREEN}Groupe créé avec succès!{Colors.RESET}")
        print(f"{Colors.CYAN}ID: {Colors.RESET}{groupe.id[:8]}")
    
    def lister_groupes(self):
        """Liste tous les groupes."""
        groupes = self.service.get_all_groupes()
        if not groupes:
            print(f"\n{Colors.YELLOW}Aucun groupe trouvé.{Colors.RESET}")
            return
        
        print(f"\n{Colors.BOLD}=== GROUPES ({len(groupes)}) ==={Colors.RESET}")
        for groupe in groupes:
            print(f"{Colors.CYAN}-{Colors.RESET} {groupe.nom} ({groupe.nombre_contacts} contacts)")
            print(f"   {groupe.description}")
    
    def ajouter_au_groupe(self):
        """Ajoute un contact à un groupe."""
        contact_id = input(f"\n{Colors.CYAN}ID Contact: {Colors.RESET}").strip()
        groupe_id = input(f"{Colors.CYAN}ID Groupe: {Colors.RESET}").strip()
        
        if self.service.ajouter_contact_au_groupe(contact_id, groupe_id):
            print(f"\n{Colors.GREEN}Contact ajouté au groupe!{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}Erreur: Contact ou groupe non trouvé.{Colors.RESET}")
    
    def ajouter_interaction(self):
        """Ajoute une interaction."""
        print(f"\n{Colors.BOLD}=== NOUVELLE INTERACTION ==={Colors.RESET}")
        contact_id = input(f"{Colors.CYAN}ID Contact: {Colors.RESET}").strip()
        
        print(f"\n{Colors.CYAN}Types:{Colors.RESET} appel, email, reunion, note")
        type_interaction = input(f"{Colors.CYAN}Type: {Colors.RESET}").strip()
        contenu = input(f"{Colors.CYAN}Contenu: {Colors.RESET}").strip()
        
        interaction = self.service.creer_interaction(contact_id, type_interaction, contenu)
        if interaction:
            print(f"\n{Colors.GREEN}Interaction ajoutée!{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}Contact non trouvé.{Colors.RESET}")
    
    def voir_statistiques(self):
        """Affiche les statistiques."""
        stats = self.service.get_statistiques()
        print(f"\n{Colors.BOLD}=== STATISTIQUES ==={Colors.RESET}")
        print(f"{Colors.CYAN}Total contacts:{Colors.RESET} {stats['total_contacts']}")
        print(f"{Colors.CYAN}Total groupes:{Colors.RESET} {stats['total_groupes']}")
        print(f"{Colors.CYAN}Total interactions:{Colors.RESET} {stats['total_interactions']}")
        print(f"{Colors.CYAN}Contacts favoris:{Colors.RESET} {stats['contacts_favoris']}")
        print(f"\n{Colors.CYAN}Par catégorie:{Colors.RESET}")
        for cat, count in stats['par_categorie'].items():
            print(f"  {cat}: {count}")
    
    def run(self):
        """Point d'entrée interactif."""
        self._afficher_banniere()
        
        while True:
            self._afficher_menu()
            choix = input(f"{Colors.CYAN}Choix: {Colors.RESET}").strip()
            
            if choix == "1":
                print(f"\n{Colors.BOLD}=== GESTION DES CONTACTS ==={Colors.RESET}")
                print(f"{Colors.CYAN}1.{Colors.RESET} Créer un contact")
                print(f"{Colors.CYAN}2.{Colors.RESET} Lister les contacts")
                print(f"{Colors.CYAN}3.{Colors.RESET} Rechercher")
                sub = input(f"{Colors.CYAN}Choix: {Colors.RESET}").strip()
                if sub == "1":
                    self.creer_contact()
                elif sub == "2":
                    self.lister_contacts()
                elif sub == "3":
                    self.rechercher_contact()
            
            elif choix == "2":
                print(f"\n{Colors.BOLD}=== GESTION DES GROUPES ==={Colors.RESET}")
                print(f"{Colors.CYAN}1.{Colors.RESET} Créer un groupe")
                print(f"{Colors.CYAN}2.{Colors.RESET} Lister les groupes")
                print(f"{Colors.CYAN}3.{Colors.RESET} Ajouter contact au groupe")
                sub = input(f"{Colors.CYAN}Choix: {Colors.RESET}").strip()
                if sub == "1":
                    self.creer_groupe()
                elif sub == "2":
                    self.lister_groupes()
                elif sub == "3":
                    self.ajouter_au_groupe()
            
            elif choix == "3":
                self.ajouter_interaction()
            
            elif choix == "4":
                self.rechercher_contact()
            
            elif choix == "5":
                self.voir_statistiques()
            
            elif choix == "6":
                print(f"\n{Colors.YELLOW}Au revoir!{Colors.RESET}")
                break


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description="Gestionnaire de Contacts")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    
    args = parser.parse_args()
    
    app = Projet02GestionnaireContacts()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir!")
    except Exception as e:
        print(f"\n{Colors.RED}Erreur: {e}{Colors.RESET}")


if __name__ == "__main__":
    main()
