# Projet: Gestionnaire de Contacts CRM

Créez un système de gestion de contacts avec recherche avancée et export.

## Objectif

Appliquer les classes, l'héritage, et la manipulation de fichiers dans un CRM léger.

## Difficulté

**Intermédiaire** - Durée estimée: 5-7 heures

## Prérequis

**Module 2 requis** : Chapitres 08-13

## Fonctionnalités Attendues

### Classe Contact
- Attributs: nom, prénom, email, téléphone, entreprise, poste, notes
- Méthodes: __str__, __eq__, to_dict(), from_dict()

### Types de Contacts
- **ContactPro**: entreprise, site web, LinkedIn
- **ContactPerso**: adresse, anniversaire, réseaux sociaux

### Fonctionnalités CRUD
- Ajouter un contact
- Lister avec filtres (par entreprise, par tag)
- Rechercher (nom, email, téléphone)
- Modifier et supprimer
- Importer/exporter JSON et CSV

## Structure

```
projet_02_gestionnaire_contacts/
├── README.md
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── contact.py
│   │   ├── contact_pro.py
│   │   └── contact_perso.py
│   ├── storage.py
│   └── cli.py
└── solution/
```

---

[Retour au module](../README_PROJETS.md)
