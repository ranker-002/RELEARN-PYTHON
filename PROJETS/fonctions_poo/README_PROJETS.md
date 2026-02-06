# Module 2: Fonctions & POO - Projets

Projets pour maîtriser la programmation orientée objet et les fonctions avancées.

## Prérequis

**Module 2 requis** : Chapitres 08-13

## Projets Disponibles

| Projet | Difficulté | Description |
|--------|------------|-------------|
| [Système Bancaire](./projet_01_systeme_bancaire/README.md) | Intermédiaire | Gestion de comptes, transactions, intérêts |
| [Gestionnaire de Contacts](./projet_02_gestionnaire_contacts/README.md) | Intermédiaire | CRUD contacts avec recherche avancée |

## Structure

```
fonctions_poo/
├── projet_01_systeme_bancaire/
│   ├── README.md
│   ├── src/
│   │   ├── main.py
│   │   ├── compte.py
│   │   ├── client.py
│   │   └── transaction.py
│   └── solution/
└── projet_02_gestionnaire_contacts/
    ├── README.md
    ├── src/
    └── solution/
```

## Indications

### Système Bancaire
- Créez une classe `CompteBancaire` avec méthodes `deposer()`, `retirer()`, `solde()`
- Gérez les découverts avec une exception personnalisée
- Utilisez l'héritage pour `CompteEpargne` avec intérêts

### Gestionnaire de Contacts
- Créez une classe `Contact` avec attributs et `__str__`
- Gérez la persistance JSON
- Implémentez recherche par nom, email, téléphone

---

[Retour aux PROJETS](../README_GLOBAL.md)
