# Module 5 : Domaines Spécialisés

Appliquez Python dans des domaines professionnels : Automation, Data Science, Web, et Intelligence Artificielle.

## Contenu du Module

| Chapitre | Domaine | Contenu |
|----------|---------|---------|
| 20 | Automation | Selenium, APIs, emails, scripts système |
| 21 | Web Scraping | BeautifulSoup, Scrapy, extraction de données |
| 22 | Data Science | NumPy, Pandas, analyse de données |
| 23 | Visualisation | Matplotlib, Seaborn, graphiques |
| 24 | Web Dev | Flask, FastAPI, développement REST |
| 25 | Machine Learning | Scikit-learn, modèles prédictifs |
| 26 | Deep Learning | PyTorch, réseaux de neurones |

## Prérequis

Modules 1-4 complétés (fortement recommandé).

## Durée Estimée

6-8 semaines (1-2 semaines par domaine).

## Objectifs d'Apprentissage

À la fin de ce module, vous serez capable de :
- **Automation** : Automatiser des tâches répétitives (browser, emails, fichiers)
- **Web Scraping** : Extraire des données de sites web
- **Data Science** : Analyser et transformer des données avec Pandas
- **Visualisation** : Créer des graphiques professionnels
- **Web Dev** : Construire des APIs REST avec Flask/FastAPI
- **Machine Learning** : Construire et évaluer des modèles prédictifs
- **Deep Learning** : Concevoir des réseaux de neurones avec PyTorch

## Installation des Dépendances

```bash
# Automation + Web Scraping
uv sync --extra automation

# Data Science + Visualisation
uv sync --extra core

# Web Development
uv sync --extra web

# Machine Learning + Deep Learning
uv sync --extra ai

# Tout installer
uv sync --extra core --extra web --extra automation --extra data --extra ai
```

## Projets par Domaine

### Automation
| Projet | Difficulté | Prérequis | Description |
|--------|------------|-----------|-------------|
| Automatisation Rapports | Avancé | Chapitre 20 | Génération et envoi automatique de rapports |
| Suivi Compétitions | Avancé | Chapitre 20 | Surveillance de sites e-sport |

### Web Scraping
| Projet | Difficulté | Prérequis | Description |
|--------|------------|-----------|-------------|
| Agrégateur d'Actualités | Avancé | Chapitre 21 | Aggregation de flux multiples |
| Analyseur de Prix | Avancé | Chapitre 21 | Suivi de prix e-commerce |

### Data Science
| Projet | Difficulté | Prérequis | Description |
|--------|------------|-----------|-------------|
| Analyse Exploratoire | Avancé | Chapitre 22 | EDA sur dataset réel |
| Dashboard Analytique | Expert | Chapitres 22-23 | Visualisation interactive |

### Web Development
| Projet | Difficulté | Prérequis | Description |
|--------|------------|-----------|-------------|
| API REST | Avancé | Chapitre 24 | CRUD complet avec FastAPI |
| Application Todo | Intermédiaire | Chapitre 24 | Todo list avec backend REST |

### Machine Learning
| Projet | Difficulté | Prérequis | Description |
|--------|------------|-----------|-------------|
| Modèle Prédiction | Expert | Chapitre 25 | Prédiction sur données réelles |
| Classification | Expert | Chapitre 25 | Classification multi-classes |

### Deep Learning
| Projet | Difficulté | Prérequis | Description |
|--------|------------|-----------|-------------|
| Réseau Neurones | Expert | Chapitre 26 | Architecture personnalisée |
| Classification Images | Expert | Chapitre 26 | CNN pour images |

Voir [PROJETS/](../../PROJETS/README_GLOBAL.md)

## Chapitre Précédent

[Module 4 : Concepts Avancés](../04_concepts_avances/README_MODULE.md)

## Fin du Parcours

Félicitations ! Vous avez complété le parcours Python complet.
