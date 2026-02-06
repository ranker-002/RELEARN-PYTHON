# Module 4: Concepts Avancés - Projets

Projets pour appliquer décorateurs, générateurs et type hinting.

## Prérequis

**Module 4 requis** : Chapitres 17-19

## Projets Disponibles

| Projet | Difficulté | Description |
|--------|------------|-------------|
| [Générateur de Rapports](./projet_01_generateur_rapports/README.md) | Avancé | Pipeline avec décorateurs et types |
| [Pipeline de Données](./projet_02_pipeline_donnees/README.md) | Avancé | Traitement concurrent haute performance |

## Structure

```
concepts_avances/
├── projet_01_generateur_rapports/
│   ├── README.md
│   ├── src/
│   └── solution/
└── projet_02_pipeline_donnees/
    ├── README.md
    ├── src/
    └── solution/
```

## Indications

### Générateur de Rapports
- Créez des décorateurs pour logger, mesurer le temps, valider les entrées
- Utilisez des générateurs pour traiter les données par batches
- Ajoutez des type hints à toutes les fonctions

### Pipeline de Données
- Utilisez asyncio ou threading pour le traitement parallèle
- Implémentez un générateur pour streamer les données
- Gérez les erreurs avec retry automatique

---

[Retour aux PROJETS](../README_GLOBAL.md)
