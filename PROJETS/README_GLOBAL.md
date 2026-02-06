# PROJETS - Projets Concrets et Utilitaires

Appliquez vos connaissances Python avec des projets réels, complets et utiles pour votre portfolio.

## Philosophie des Projets

Chaque projet dans ce dossier est conçu pour :
- **Regrouper plusieurs compétences** d'un ou plusieurs modules
- **Produire un livrable concret** que vous pouvez utiliser au quotidien
- **Demontrer votre expertise** auprès d'éventuels employeurs
- **Construire votre portfolio** de développeur Python

## Structure des Projets

Chaque projet suit cette structure :

```
projet_xx_nom/
├── README.md              # Énoncé, objectifs, prérequis
├── src/
│   ├── main.py            # Point d'entrée
│   ├── core/               # Logique métier
│   ├── utils/             # Fonctions utilitaires
│   └── models/            # Modèles de données (si applicable)
├── tests/                 # Tests unitaires
├── data/                  # Données exemple (si applicable)
├── requirements.txt       # Dépendances spécifiques
├── solution/              # Solution complète commentée
│   └── *.py
└── .env.example           # Variables d'environnement (template)
```

## Niveaux de Difficulté

| Niveau | Description |
|--------|-------------|
| Débutant | 1-2 modules requis, guidée, solution fournie |
| Intermédiaire | 2-3 modules requis, autonomie croissante |
| Avancé | 3+ modules requis, recherche personnelle |
| Expert | Parcours complet, défi réel |

## Prérequis par Projet

Chaque projet indique explicitement les modules requis :

```markdown
**Prérequis**: Module 1 (Fondations Core) - Chapitres 01-07
```

---

## Index des Projets

### Module 1: Fondations Core

| Projet | Difficulté | Pages | Description |
|--------|------------|-------|-------------|
| [Calculatrice CLI](./core_fondations/projet_01_calculatrice_cli/README.md) | Débutant | 01-04 | Calculatrice interactive en ligne de commande |
| [Gestionnaire de Tâches CLI](./core_fondations/projet_02_gestionnaire_taches_cli/README.md) | Intermédiaire | 01-07 | Todo list persistante en CLI |

### Module 2: Fonctions & POO

| Projet | Difficulté | Chapitres | Description |
|--------|------------|-----------|-------------|
| [Système Bancaire](./fonctions_poo/projet_01_systeme_bancaire/README.md) | Intermédiaire | 08-11 | Gestion complète de comptes bancaires |
| [Gestionnaire de Contacts](./fonctions_poo/projet_02_gestionnaire_contacts/README.md) | Intermédiaire | 08-13 | CRM léger avec persistance JSON |

### Module 3: Robustesse & Fichiers

| Projet | Difficulté | Chapitres | Description |
|--------|------------|-----------|-------------|
| [Gestionnaire de Fichiers](./robustesse_fichiers/projet_01_gestionnaire_fichiers/README.md) | Intermédiaire | 14-15 | Explorateur CLI sécurisé |
| [Sauvegarde Automatique](./robustesse_fichiers/projet_02_sauvegarde_automatique/README.md) | Intermédiaire | 14-16 | Système de backup avec versioning |

### Module 4: Concepts Avancés

| Projet | Difficulté | Chapitres | Description |
|--------|------------|-----------|-------------|
| [Générateur de Rapports](./concepts_avances/projet_01_generateur_rapports/README.md) | Avancé | 17-19 | Pipeline avec décorateurs et types |
| [Pipeline de Données](./concepts_avances/projet_02_pipeline_donnees/README.md) | Avancé | 17-19 | Traitement concurrent haute performance |

### Module 5: Domaines Spécialisés

#### Automation
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [Automatisation Rapports](./automation/projet_01_automatisation_rapports/README.md) | Avancé | 20 | Génération et envoi automatique |
| [Suivi Compétitions](./automation/projet_02_suivi_competitions/README.md) | Avancé | 20 | Surveillance sites e-sport |

#### Web Scraping
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [Agrégateur d'Actualités](./web_scraping/projet_01_aggregateur_actualites/README.md) | Avancé | 21 | Agrégation de flux RSS multiples |
| [Analyseur de Prix](./web_scraping/projet_02_analyseur_prix/README.md) | Avancé | 21 | Suivi de prix e-commerce |

#### Data Science
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [Analyse Exploratoire](./data_science/projet_01_analyse_exploratoire/README.md) | Avancé | 22 | EDA sur dataset Kaggle |
| [Dashboard Analytique](./data_science/projet_02_tableau_bord_analytique/README.md) | Expert | 22-23 | Visualisation interactive |

#### Visualisation
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [Visualisation de Données](./visualisation/projet_01_visualisation_donnees/README.md) | Avancé | 23 | Graphiques publication-ready |
| [Rapports Graphiques](./visualisation/projet_02_rapports_graphiques/README.md) | Expert | 23 | Génération automatique de rapports |

#### Web Development
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [API REST](./web_dev/projet_01_api_rest/README.md) | Avancé | 24 | CRUD complet avec FastAPI |
| [Application Todo](./web_dev/projet_02_application_todo/README.md) | Intermédiaire | 24 | Todo list full-stack |

#### Machine Learning
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [Modèle Prédiction](./machine_learning/projet_01_modele_prediction/README.md) | Expert | 25 | Prédiction房价/prix |
| [Classification](./machine_learning/projet_02_classification/README.md) | Expert | 25 | Classification multi-classes |

#### Deep Learning
| Projet | Difficulté | Chapitre | Description |
|--------|------------|----------|-------------|
| [Réseau Neurones](./deep_learning/projet_01_reseau_neurones/README.md) | Expert | 26 | Architecture personalisée |
| [Classification Images](./deep_learning/projet_02_classification_images/README.md) | Expert | 26 | CNN pour CIFAR-10 |

---

## Comment Utiliser Ces Projets

### 1. Complétez d'abord les Modules Recommandés

Chaque projet liste ses prérequis. Assurez-vous d'avoir complété les modules correspondants avant de commencer.

### 2. Lisez le README du Projet

Chaque projet contient :
- Une description détaillée
- Les objectifs d'apprentissage
- Les fonctionnalités attendues
- Les contraintes techniques
- Des indices progressifs

### 3. Commencez par le Starter Code

Un squelette est fourni pour vous aider à démarrer sans partir de zéro.

### 4. Vérifiez avec les Tests

Des tests unitaires sont inclus pour valider votre implémentation.

### 5. Comparez avec la Solution

La solution complète commentée vous permet de comprendre les bonnes pratiques.

---

## Ajouter un Nouveau Projet

Si vous souhaitez contribuer un nouveau projet :

1. Créez un dossier dans le thème approprié
2. Suivez la structure standard
3. Rédigez un README complet
4. Incluez au moins 3 niveaux d'indices
5. Ajoutez des tests unitaires

---

## Progression

Utilisez `progres_apprentissage.md` à la racine pour suivre votre avancement dans les projets.

Bon coding ! 🚀
