# Projet: Système Bancaire

Créez un système complet de gestion de comptes bancaires avec transactions et intérêts.

## Objectif

Maîtriser la programmation orientée objet (classes, héritage, encapsulation) avec un projet réaliste.

## Difficulté

**Intermédiaire** - Durée estimée: 6-8 heures

## Prérequis

**Module 2 requis** : Chapitres 08-11

## Fonctionnalités Attendues

### Classes à Implémenter

1. **CompteBancaire** (classe de base)
   - Propriétés: numero_compte, solde, titulaire, date_creation
   - Méthodes: deposer(), retirer(), consulter_solde()
   - Gestion du découvert avec exception

2. **CompteCourant** (hérite de CompteBancaire)
   - Frais de transaction mensuels
   - Découvert autorisé configurable

3. **CompteEpargne** (hérite de CompteBancaire)
   - Taux d'intérêt annuel
   - Méthode calculer_interets()

4. **Transaction**
   - Type: depot, retrait, virement
   - Montant, date, description

5. **Client**
   - Informations personnelles
   - Liste de comptes
   - Historique de transactions global

### Fonctionnalités Système
- Création de clients et comptes
- Dépôts et retraits sécurisés
- Virements entre comptes
- Génération de relevés mensuels
- Calcul d'intérêts pour comptes épargne
- Historique des transactions complet

## Structure Suggérée

```
projet_01_systeme_bancaire/
├── README.md
├── src/
│   ├── main.py              # Application CLI
│   ├── models/
│   │   ├── __init__.py
│   │   ├── compte.py        # CompteBancaire, CompteCourant, CompteEpargne
│   │   ├── client.py        # Client
│   │   └── transaction.py   # Transaction
│   ├── services/
│   │   ├── banque.py        # Service de gestion
│   │   └── historique.py    # Gestion de l'historique
│   └── utils/
│       ├── validateurs.py   # Validation des entrées
│       └── formateurs.py    # Formatage des relevés
├── solution/
│   └── (fichiers complets)
├── data/
│   └── banque.json          # Sauvegarde
└── tests/
    ├── test_compte.py
    └── test_transaction.py
```

## Diagramme de Classes

```
Client
├── 1 compte * (liste de comptes)
    │
    ├── CompteBancaire (classe abstraite)
    │   ├── CompteCourant
    │   │   - frais_mensuels
    │   │   - plafond_decouvert
    │   │
    │   └── CompteEpargne
    │       - taux_interet
    │       - calculer_interets()
    │
    └── * transactions (historique)
```

## Indications

### Niveau 1: Classe de base
```python
class CompteBancaire:
    def __init__(self, numero: str, titulaire: str, solde_initial: float = 0):
        self._numero = numero
        self._titulaire = titulaire
        self._solde = solde_initial
        self._historique = []

    def deposer(self, montant: float) -> None:
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._solde += montant
        self._enregistrer_transaction("dépôt", montant)
```

### Niveau 2: Héritage
```python
class CompteEpargne(CompteBancaire):
    def __init__(self, numero: str, titulaire: str, taux_interet: float = 0.02):
        super().__init__(numero, titulaire)
        self._taux_interet = taux_interet

    def calculer_interets(self) -> float:
        return self._solde * self._taux_interet
```

### Niveau 3: Gestion des exceptions
```python
class DecouvertAutoriseException(Exception):
    """Levée quand le retrait dépasse le découvert autorisé."""

class CompteBancaire:
    def retirer(self, montant: float) -> None:
        if montant > self._solde:
            raise DecouvertAutoriseException(
                f"Solde insuffisant. Solde: {self._solde}, Demande: {montant}"
            )
```

## Exemple d'Exécution

```
=== SYSTÈME BANCAIRE ===

1. Créer un client
2. Créer un compte
3. Déposer de l'argent
4. Retirer de l'argent
5. Virer entre comptes
6. Afficher un compte
7. Calculer intérêts (épargne)
8. Quitter

>>> 1

Nom du client: Jean Dupont
Email: jean.dupont@email.com
✓ Client créé! ID: CLI001

>>> 3

Numéro de compte: COM001
Montant: 1000
✓ Dépôt effectué! Nouveau solde: 1500.00 €

>>> 6

=== COMPTE COM001 ===
Titulaire: Jean Dupont
Type: Compte Courant
Solde: 1500.00 €
Découvert autorisé: 500.00 €

=== HISTORIQUE ===
[2024-01-15 10:30] Dépôt: +1000.00 €
[2024-01-15 10:32] Dépôt: +500.00 €
```

## Critères de Validation

- [ ] Héritage correctement implémenté
- [ ] Encapsulation (attributs protégés/privés)
- [ ] Exceptions personnalisées pour erreurs métier
- [ ] Persistance des données
- [ ] Code documenté avec docstrings

---

[Retour au module](../README_PROJETS.md)
