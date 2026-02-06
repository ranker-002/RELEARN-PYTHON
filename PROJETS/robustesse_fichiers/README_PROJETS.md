# Module 3: Robustesse & Fichiers - Projets

Projets pour maîtriser la gestion d'erreurs et la manipulation de fichiers.

## Prérequis

**Module 3 requis** : Chapitres 14-16

## Projets Disponibles

| Projet | Difficulté | Description |
|--------|------------|-------------|
| [Gestionnaire de Fichiers](./projet_01_gestionnaire_fichiers/README.md) | Intermédiaire | Explorateur CLI avec opérations sécurisées |
| [Sauvegarde Automatique](./projet_02_sauvegarde_automatique/README.md) | Intermédiaire | Backup avec versioning et compression |

## Structure

```
robustesse_fichiers/
├── projet_01_gestionnaire_fichiers/
│   ├── README.md
│   ├── src/
│   └── solution/
└── projet_02_sauvegarde_automatique/
    ├── README.md
    ├── src/
    └── solution/
```

## Indications

### Gestionnaire de Fichiers
- Utilisez pathlib pour la manipulation de chemins
- Gérez les exceptions pour chaque opération (copier, déplacer, supprimer)
- Validez les chemins pour éviter les injections

### Sauvegarde Automatique
- Utilisez shutil pour la copie et compression
- Implémentez un système de versioning avec timestamps
- Gérez les erreurs de permission et de fichier manquant

---

[Retour aux PROJETS](../README_GLOBAL.md)
