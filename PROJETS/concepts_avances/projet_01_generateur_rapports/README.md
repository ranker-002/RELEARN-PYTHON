# Projet: Générateur de Rapports avec Décorateurs

Créez un pipeline de génération de rapports avec logging et validation.

## Objectif

Appliquer décorateurs, générateurs, et type hinting dans un système professionnel.

## Difficulté

**Avancé** - Durée estimée: 8-10 heures

## Prérequis

**Module 4 requis** : Chapitres 17-19

## Fonctionnalités Attendues

### Pipeline
- Extraction données (fichiers CSV/JSON/database)
- Transformation (agrégation, filtrage)
- Génération rapport (PDF/HTML/Markdown)

### Décorateurs
- @log_execution: Log durée et étapes
- @validate_input: Valider types et contraintes
- @retry: Retry sur erreur temporaire
- @cache: Mettre en cache les résultats coûteux

### Générateurs
- Streaming de grandes quantités de données
- Processing par batches
- Yield pour étapes intermédiaires

### Type Hinting
- Toutes les fonctions typées
- Utilisation de mypy pour vérification

---

[Retour au module](../README_PROJETS.md)
