# Projet: Pipeline de Données Concurrent

Créez un système de traitement de données haute performance.

## Objectif

Maîtriser la programmation concurrente avec threading/asyncio et les générateurs.

## Difficulté

**Avancé** - Durée estimée: 10-12 heures

## Prérequis

**Module 4 requis** : Chapitres 17-19

## Fonctionnalités Attendues

### Traitement Parallèle
- Threading pour I/O bound (lecture fichiers, API calls)
- asyncio pour opérations network
- Pool de workers configurable

### Architecture Pipeline
- Stage 1: Extraction (générateur)
- Stage 2: Transformation (parallèle)
- Stage 3: Chargement (batch)

### Robustesse
- Retry automatique avec exponential backoff
- Circuit breaker pour services externes
- Dead letter queue pour erreurs

---

[Retour au module](../README_PROJETS.md)
