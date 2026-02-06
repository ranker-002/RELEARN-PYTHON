# Projet: Sauvegarde Automatique avec Versioning

Créez un système de backup intelligent avec compression et historique.

## Objectif

Appliquer la gestion d'erreurs, la sérialisation, et shutil dans un système robuste.

## Difficulté

**Intermédiaire** - Durée estimée: 5-7 heures

## Prérequis

**Module 3 requis** : Chapitres 14-16

## Fonctionnalités Attendues

### Sauvegarde
- Copie récursive de dossiers
- Compression ZIP avec horodatage
- Exclusion de fichiers (patterns .gitignore-style)
- Vérification checksum SHA256

### Gestion des Versions
- Stockage horodaté (backup_2024-01-15_10-30-15.zip)
- Rotation automatique (garder N dernière versions)
- Nettoyage des backups anciens

### Restauration
- Lister les backups disponibles
- Restaurer une version spécifique
- Extraction sélective

---

[Retour au module](../README_PROJETS.md)
