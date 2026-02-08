# Gestionnaire de Contacts

Application complète de gestion de contacts avec organisation par groupes et suivi des interactions.

---

## 🎯 Objectif du Projet

Créer une application de gestion de contacts professionnelle permettant de :
- Stocker et organiser des contacts (nom, email, téléphone, adresse)
- Classer les contacts par catégories (famille, amis, collègues, clients...)
- Créer des groupes personnalisés de contacts
- Suivre l'historique des interactions (appels, emails, rendez-vous)
- Rechercher et filtrer les contacts

Ce projet vous permettra de mettre en pratique :
- La conception orientée objet avancée (dataclasses, enums, propriétés)
- La persistance de données JSON
- La gestion des relations entre entités (contact-groupe)
- Les filtres et recherches
- L'interface CLI interactive

---

## 📋 Fonctionnalités à Implémenter

1. **Gestion des contacts**
   - Création de contacts avec toutes les informations
   - Modification et suppression
   - Recherche par nom, email ou téléphone
   - Marquage comme favori

2. **Organisation par catégories**
   - Famille, Amis, Collègues, Clients, Fournisseurs, Autre
   - Filtrage par catégorie

3. **Groupes de contacts**
   - Création de groupes personnalisés
   - Ajout/retrait de contacts aux groupes
   - Liste des contacts par groupe

4. **Suivi des interactions**
   - Enregistrement des appels, emails, réunions, notes
   - Historique par contact
   - Rappels de suivi

5. **Statistiques**
   - Nombre total de contacts
   - Répartition par catégorie
   - Nombre de favoris

---

## 🗂️ Modèles de Données

### Contact
```python
@dataclass
class Contact:
    id: str                    # UUID auto-généré
    nom: str
    prenom: str
    email: str
    telephone: str
    adresse: str = ""
    categorie: CategorieContact = CategorieContact.AUTRE
    statut: StatutContact = StatutContact.ACTIF
    notes: str = ""
    date_creation: datetime
    date_modification: Optional[datetime]
    tags: List[str]
    
    # Méthodes à implémenter :
    - __post_init__() : génération de l'ID UUID
    - nom_complet (property) : retourne "Prénom Nom"
    - ajouter_tag(tag: str)
    - retirer_tag(tag: str)
    - mettre_a_jour(**kwargs)
```

### CategorieContact (Enum)
```python
class CategorieContact(Enum):
    FAMILLE = "famille"
    AMI = "ami"
    COLLEGUE = "collegue"
    CLIENT = "client"
    FOURNISSEUR = "fournisseur"
    AUTRE = "autre"
```

### StatutContact (Enum)
```python
class StatutContact(Enum):
    ACTIF = "actif"
    INACTIF = "inactif"
    FAVORI = "favori"
```

### Groupe
```python
@dataclass
class Groupe:
    id: str                    # UUID auto-généré
    nom: str
    description: str = ""
    contacts_ids: List[str]    # IDs des contacts membres
    date_creation: datetime
    
    # Méthodes à implémenter :
    - __post_init__() : génération de l'ID
    - ajouter_contact(contact_id: str)
    - retirer_contact(contact_id: str)
    - nombre_contacts (property)
```

### Interaction
```python
@dataclass
class Interaction:
    id: str                    # UUID auto-généré
    contact_id: str            # Référence vers le contact
    type_interaction: str      # "appel", "email", "reunion", "note"
    contenu: str
    date_interaction: datetime
    rappel: Optional[datetime]
    statut: str                # "complete", "en_attente", "annule"
    
    # Méthodes à implémenter :
    - __post_init__() : génération de l'ID
```

---

## ⚙️ Service à Développer

### ServiceContacts
**Fichier :** `src/services/gestionnaire_contacts.py`

**Responsabilités :**
- Gérer la persistance JSON de tous les contacts, groupes et interactions
- Fournir les opérations CRUD
- Implémenter la recherche et le filtrage

**Méthodes principales :**

```python
class ServiceContacts:
    def __init__(self, repertoire_donnees: str = "data")
    
    # Gestion des contacts
    def creer_contact(self, nom, prenom, email, telephone, 
                      adresse="", categorie=CategorieContact.AUTRE) -> Contact
    def get_contact(self, contact_id: str) -> Optional[Contact]
    def get_all_contacts(self) -> List[Contact]
    def rechercher_contacts(self, critere: str) -> List[Contact]
    def filtrer_par_categorie(self, categorie: CategorieContact) -> List[Contact]
    def filtrer_par_statut(self, statut: StatutContact) -> List[Contact]
    def supprimer_contact(self, contact_id: str) -> bool
    
    # Gestion des groupes
    def creer_groupe(self, nom: str, description: str = "") -> Groupe
    def get_groupe(self, groupe_id: str) -> Optional[Groupe]
    def get_all_groupes(self) -> List[Groupe]
    def ajouter_contact_au_groupe(self, contact_id: str, groupe_id: str) -> bool
    
    # Gestion des interactions
    def creer_interaction(self, contact_id: str, type_interaction: str,
                          contenu: str, rappel: Optional[datetime] = None) -> Optional[Interaction]
    def get_interactions_contact(self, contact_id: str) -> List[Interaction]
    
    # Statistiques
    def get_statistiques(self) -> Dict
```

**Persistance :**
- Sauvegarder dans `data/contacts.json`
- Sauvegarder dans `data/groupes.json`
- Sauvegarder dans `data/interactions.json`
- Charger automatiquement au démarrage

---

## 🚀 Workflow de Développement

### Étape 1 : Analyse du scaffold
Le projet contient une structure de base :
```
src/
├── __init__.py
├── main.py              ← Squelette avec menu CLI
├── models/
│   └── __init__.py      ← À compléter avec Contact, Groupe, Interaction
├── services/
│   └── __init__.py      ← À compléter avec ServiceContacts
└── utils/
    └── __init__.py
```

### Étape 2 : Implémentation des modèles
1. Créez les enums `CategorieContact` et `StatutContact`
2. Implémentez la classe `Contact` avec toutes ses méthodes
3. Implémentez la classe `Groupe`
4. Implémentez la classe `Interaction`
5. Testez la création d'objets et la génération d'UUID

### Étape 3 : Développement du service
1. Créez le `ServiceContacts` avec le constructeur
2. Implémentez `_charger_donnees()` pour lire les JSON
3. Implémentez `_sauvegarder_donnees()` pour écrire les JSON
4. Ajoutez les méthodes CRUD pour les contacts
5. Ajoutez les méthodes pour les groupes
6. Ajoutez les méthodes pour les interactions
7. Ajoutez les méthodes de recherche et filtrage

### Étape 4 : Interface CLI
Complétez `main.py` avec :
- Menu principal avec sous-menus
- Formulaires de création (contact, groupe)
- Affichage des listes avec formatage
- Recherche interactive
- Affichage des statistiques

### Étape 5 : Vérification

#### Option A : Vérification en ligne de commande
```bash
python verification.py
```

#### Option B : Interface Web de Vérification
```bash
python verify_server.py
```
Ouvrez votre navigateur sur `http://localhost:8000`

#### Option C : Comparaison avec la solution
```bash
# Comparez votre code
diff src/models/__init__.py solution/src/models/__init__.py
diff src/services/gestionnaire_contacts.py solution/src/services/gestionnaire_contacts.py
```

---

## 📁 Structure Finale Attendue

```
projet_02_gestionnaire_contacts/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application CLI complète
│   ├── models/
│   │   └── __init__.py      # Contact, Groupe, Interaction, Enums
│   ├── services/
│   │   └── gestionnaire_contacts.py  # ServiceContacts
│   └── utils/
│       └── __init__.py
├── solution/                # Solution de référence
│   └── src/
├── tests/
├── data/                    # JSON générés automatiquement
│   ├── contacts.json
│   ├── groupes.json
│   └── interactions.json
├── README.md               # Ce fichier
├── requirements.txt
└── verification.py
```

---

## 🎓 Conseils de Développement

### Niveau 1 - Commencez simple
```python
# 1. Créez d'abord le Contact basique
contact = Contact(id="", nom="Dupont", prenom="Jean", 
                  email="jean@email.com", telephone="0612345678")
# Vérifiez que l'ID se génère automatiquement
print(contact.id)  # Doit afficher un UUID
```

### Niveau 2 - Ajoutez la persistance
```python
# Testez la sauvegarde JSON
service = ServiceContacts()
contact = service.creer_contact("Dupont", "Jean", "jean@email.com", "0612345678")
# Vérifiez que data/contacts.json est créé
```

### Niveau 3 - Interface complète
- Ajoutez les couleurs dans l'affichage
- Gérez les erreurs (contact non trouvé, etc.)
- Ajoutez la confirmation avant suppression

---

## ⚠️ Erreurs Courantes

1. **UUID non généré** : Assurez-vous que `__post_init__` vérifie `if not self.id`
2. **JSON non sérialisable** : Convertissez les enums avec `.value` avant sauvegarde
3. **Import circulaire** : Importez les modèles au début du fichier service
4. **Date mal formatée** : Utilisez `default=str` dans `json.dump()`

---

## ✅ Checklist de Validation

- [ ] Les modèles `Contact`, `Groupe`, `Interaction` sont créés
- [ ] Les enums `CategorieContact` et `StatutContact` fonctionnent
- [ ] Les UUID se génèrent automatiquement
- [ ] Le service sauvegarde et charge les données JSON
- [ ] On peut créer, lire, modifier, supprimer des contacts
- [ ] On peut créer des groupes et y ajouter des contacts
- [ ] On peut enregistrer des interactions
- [ ] La recherche et le filtrage fonctionnent
- [ ] L'interface CLI est fonctionnelle
- [ ] `python verification.py` affiche "Projet valide!"

---

## 🏆 Critères de Réussite

1. ✅ Création d'un contact avec toutes les informations
2. ✅ Recherche de contacts fonctionnelle
3. ✅ Création de groupes et ajout de contacts
4. ✅ Persistance des données (redémarrage conservé)
5. ✅ Interface utilisateur intuitive et colorée
6. ✅ Tous les tests de verification.py passent

---

## 💡 Exemple d'Utilisation

```python
# Exemple d'utilisation programmatique
from src.services.gestionnaire_contacts import ServiceContacts
from src.models import CategorieContact

# Créer le service
service = ServiceContacts()

# Créer un contact
contact = service.creer_contact(
    nom="Dupont",
    prenom="Marie",
    email="marie.dupont@email.com",
    telephone="0612345678",
    categorie=CategorieContact.CLIENT
)

# Créer un groupe
groupe = service.creer_groupe("Clients VIP", "Meilleurs clients")

# Ajouter le contact au groupe
service.ajouter_contact_au_groupe(contact.id, groupe.id)

# Créer une interaction
service.creer_interaction(
    contact_id=contact.id,
    type_interaction="appel",
    contenu="Discussion projet X"
)

# Voir les statistiques
stats = service.get_statistiques()
print(f"Total contacts: {stats['total_contacts']}")
```

---

**Bonne chance ! N'hésitez pas à consulter la solution si vous êtes bloqué.**

*Durée estimée: 4-6 heures | Difficulté: Intermédiaire*

---

[Retour au module](../README_PROJETS.md)
