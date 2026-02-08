#!/usr/bin/env python3
"""
Service for managing contacts.
"""

from typing import Optional, List, Dict
from datetime import datetime
from pathlib import Path
import json
import uuid

from models import Contact, Groupe, Interaction, CategorieContact, StatutContact


class ServiceContacts:
    """Manages contacts and groups."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.repertoire = Path(repertoire_donnees)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        self.contacts: Dict[str, Contact] = {}
        self.groupes: Dict[str, Groupe] = {}
        self.interactions: Dict[str, Interaction] = {}
        self._charger_donnees()
    
    def _chemin_fichier(self, nom: str) -> Path:
        return self.repertoire / f"{nom}.json"
    
    def _charger_donnees(self):
        """Load data from files."""
        for fichier in self.repertoire.glob("*.json"):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    if fichier.stem == "contacts":
                        for c in donnees:
                            contact = Contact(**c)
                            self.contacts[contact.id] = contact
                    elif fichier.stem == "groupes":
                        for g in donnees:
                            groupe = Groupe(**g)
                            self.groupes[groupe.id] = groupe
                    elif fichier.stem == "interactions":
                        for i in donnees:
                            interaction = Interaction(**i)
                            self.interactions[interaction.id] = interaction
            except (json.JSONDecodeError, FileNotFoundError):
                pass
    
    def _sauvegarder_donnees(self):
        """Save data to files."""
        contacts_data = [vars(c) for c in self.contacts.values()]
        groupes_data = [vars(g) for g in self.groupes.values()]
        interactions_data = [vars(i) for i in self.interactions.values()]
        
        with open(self._chemin_fichier("contacts"), 'w', encoding='utf-8') as f:
            json.dump(contacts_data, f, indent=2, default=str)
        with open(self._chemin_fichier("groupes"), 'w', encoding='utf-8') as f:
            json.dump(groupes_data, f, indent=2, default=str)
        with open(self._chemin_fichier("interactions"), 'w', encoding='utf-8') as f:
            json.dump(interactions_data, f, indent=2, default=str)
    
    def creer_contact(self, nom: str, prenom: str, email: str,
                      telephone: str, adresse: str = "",
                      categorie: CategorieContact = CategorieContact.AUTRE) -> Contact:
        """Create a new contact."""
        contact = Contact(
            id="",
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            adresse=adresse,
            categorie=categorie
        )
        self.contacts[contact.id] = contact
        self._sauvegarder_donnees()
        return contact
    
    def get_contact(self, contact_id: str) -> Optional[Contact]:
        return self.contacts.get(contact_id)
    
    def get_all_contacts(self) -> List[Contact]:
        return list(self.contacts.values())
    
    def rechercher_contacts(self, critere: str) -> List[Contact]:
        """Search contacts by name, email, or phone."""
        critere = critere.lower()
        return [c for c in self.contacts.values()
                if critere in c.nom.lower() or critere in c.prenom.lower()
                or critere in c.email.lower() or critere in c.telephone]
    
    def filtrer_par_categorie(self, categorie: CategorieContact) -> List[Contact]:
        return [c for c in self.contacts.values() if c.categorie == categorie]
    
    def filtrer_par_statut(self, statut: StatutContact) -> List[Contact]:
        return [c for c in self.contacts.values() if c.statut == statut]
    
    def supprimer_contact(self, contact_id: str) -> bool:
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self._sauvegarder_donnees()
            return True
        return False
    
    def creer_groupe(self, nom: str, description: str = "") -> Groupe:
        """Create a new group."""
        groupe = Groupe(
            id="",
            nom=nom,
            description=description
        )
        self.groupes[groupe.id] = groupe
        self._sauvegarder_donnees()
        return groupe
    
    def get_groupe(self, groupe_id: str) -> Optional[Groupe]:
        return self.groupes.get(groupe_id)
    
    def get_all_groupes(self) -> List[Groupe]:
        return list(self.groupes.values())
    
    def ajouter_contact_au_groupe(self, contact_id: str, groupe_id: str) -> bool:
        groupe = self.get_groupe(groupe_id)
        if groupe and contact_id in self.contacts:
            groupe.ajouter_contact(contact_id)
            self._sauvegarder_donnees()
            return True
        return False
    
    def creer_interaction(self, contact_id: str, type_interaction: str,
                          contenu: str, rappel: Optional[datetime] = None) -> Optional[Interaction]:
        """Create a new interaction."""
        if contact_id not in self.contacts:
            return None
        
        interaction = Interaction(
            id="",
            contact_id=contact_id,
            type_interaction=type_interaction,
            contenu=contenu,
            rappel=rappel
        )
        self.interactions[interaction.id] = interaction
        self._sauvegarder_donnees()
        return interaction
    
    def get_interactions_contact(self, contact_id: str) -> List[Interaction]:
        return [i for i in self.interactions.values() if i.contact_id == contact_id]
    
    def get_statistiques(self) -> Dict:
        """Get contact statistics."""
        return {
            "total_contacts": len(self.contacts),
            "total_groupes": len(self.groupes),
            "total_interactions": len(self.interactions),
            "contacts_favoris": len([c for c in self.contacts.values() if c.statut == StatutContact.FAVORI]),
            "par_categorie": {
                cat.value: len([c for c in self.contacts.values() if c.categorie == cat])
                for cat in CategorieContact
            }
        }
