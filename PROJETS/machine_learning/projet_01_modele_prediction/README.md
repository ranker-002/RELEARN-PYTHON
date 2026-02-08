# Modèle de Prédiction

Système de prédiction basé sur le machine learning

---

## 🎯 Objectif du Projet

Créer un système pour entraîner des modèles prédictifs sur des données tabulaires

Ce projet vous permettra de mettre en pratique :
- La conception orientée objet (classes, héritage, encapsulation)
- La persistance de données (JSON)
- Les services et la séparation des responsabilités
- L'interface en ligne de commande (CLI)

---

## 📋 Fonctionnalités à Implémenter

1. **Import et préparation des datasets**
2. **Sélection des features et target**
3. **Choix d'algorithmes (régression linéaire, random forest, etc.)**
4. **Entraînement et validation du modèle**
5. **Évaluation des performances (MSE, R², MAE)**
6. **Prédiction sur de nouvelles données**

---

## 🗂️ Modèles de Données

Vous devez créer les classes suivantes dans `src/models/` :

### Modele
```python
@dataclass
class Modele:
    id, nom, algorithme, hyperparametres, date_entrainement
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

### Dataset
```python
@dataclass
class Dataset:
    id, nom, chemin, features, target, train_test_split
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

### Feature
```python
@dataclass
class Feature:
    id, dataset_id, nom, type, importance
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

### Prediction
```python
@dataclass
class Prediction:
    id, modele_id, entrees, sortie, confiance
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

---

## ⚙️ Services à Développer

Créez les services suivants dans `src/services/` :

### Entraineur
**Description :** Entraîne les modèles

**Fichier :** `src/services/entraineur.py`

**Méthodes principales :**
- `preparer_donnees()`
- `entrainer()`
- `valider()`

### Predicteur
**Description :** Fait des prédictions

**Fichier :** `src/services/predicteur.py`

**Méthodes principales :**
- `predire()`
- `evaluer_performance()`
- `expliquer()`

---

## 🚀 Workflow de Développement

### Étape 1 : Analyse du scaffold
Le projet contient une structure de base dans `src/` :
```
src/
├── __init__.py
├── main.py              ← Point d'entrée (squelette fourni)
├── models/
│   └── __init__.py      ← À compléter avec vos classes
├── services/
│   └── __init__.py      ← À compléter avec vos services
└── utils/
    └── __init__.py      ← Utilitaires optionnels
```

### Étape 2 : Implémentation
1. **Commencez par les modèles** dans `src/models/__init__.py`
   - Définissez vos dataclasses avec leurs attributs
   - Ajoutez les méthodes `__post_init__`, validation, etc.

2. **Développez les services** dans `src/services/`
   - Implémentez la logique métier
   - Gérez la persistance JSON
   - Ajoutez les méthodes CRUD

3. **Complétez l'interface** dans `src/main.py`
   - Ajoutez les menus interactifs
   - Connectez les services à l'UI

### Étape 3 : Vérification

#### Option A : Vérification en ligne de commande
```bash
python verification.py
```
Cela vérifiera :
- ✅ Structure du projet
- ✅ Imports fonctionnels
- ✅ Exécution sans erreur

#### Option B : Interface Web de Vérification
```bash
python verify_server.py
```
Puis ouvrez votre navigateur sur `http://localhost:8000`

L'interface web permet de :
- Voir le statut de chaque test
- Comparer votre code avec la solution
- Visualiser les différences
- Obtenir des indications

#### Option C : Comparaison manuelle avec la solution
La solution complète est disponible dans `solution/src/` :
```bash
# Comparez votre code avec la solution
diff src/models/__init__.py solution/src/models/__init__.py
diff src/services/ solution/src/services/
```

### Étape 4 : Tests
```bash
pytest tests/
```

---

## 📁 Structure Finale Attendue

```
projet_XX_nom/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application CLI complète
│   ├── models/
│   │   ├── __init__.py      # Toutes vos classes
│   │   └── [fichiers supplémentaires]
│   ├── services/
│   │   ├── __init__.py
│   │   └── [vos_services].py
│   └── utils/
│       ├── __init__.py
│       └── [utilitaires].py
├── solution/                # Solution de référence
│   └── src/                 # (Ne regardez que si bloqué !)
├── tests/                   # Tests à compléter
├── data/                    # Données JSON générées
├── README.md               # Ce fichier
├── requirements.txt        # Dépendances
└── verification.py         # Script de vérification
```

---

## 🎓 Conseils de Développement

### Niveau 1 - Découverte
- Commencez par implémenter un seul modèle
- Testez la création et la persistance JSON
- Utilisez `print()` pour déboguer

### Niveau 2 - Approfondissement
- Ajoutez la validation des données
- Implémentez les relations entre modèles
- Créez un service simple

### Niveau 3 - Expert
- Gérez les erreurs avec try/except
- Ajoutez des logs
- Optimisez les performances
- Écrivez des tests unitaires

---

## ⚠️ Erreurs Courantes

1. **ImportError** : Vérifiez que tous les `__init__.py` sont présents
2. **JSON serialization** : Convertissez les enums et dates en string
3. **Attributs manquants** : Utilisez `field(default_factory=list)` pour les listes
4. **ID unique** : Générez les UUID dans `__post_init__`

---

## 📖 Ressources Utiles

- [Documentation Python - dataclasses](https://docs.python.org/fr/3/library/dataclasses.html)
- [Documentation Python - Pathlib](https://docs.python.org/fr/3/library/pathlib.html)
- [Documentation Python - JSON](https://docs.python.org/fr/3/library/json.html)

---

## ✅ Checklist de Validation

Avant de passer à la vérification, assurez-vous que :

- [ ] Les modèles sont créés avec tous les attributs
- [ ] Les méthodes `__post_init__` génèrent les IDs
- [ ] Les services implémentent toutes les méthodes requises
- [ ] La persistance JSON fonctionne
- [ ] L'application CLI démarre sans erreur
- [ ] Les tests unitaires passent (si écrits)

---

## 🏆 Critères de Réussite

Le projet est réussi si :
1. ✅ `python verification.py` affiche "Projet valide!"
2. ✅ L'interface web montre tous les tests en vert
3. ✅ Vous pouvez créer, lire, mettre à jour et supprimer des données
4. ✅ Les données persistent après redémarrage
5. ✅ L'interface CLI est fonctionnelle et intuitive

---

**Bonne chance ! N'oubliez pas : la solution est là pour vous aider si vous êtes bloqué.**

*Durée estimée: 4-8 heures | Difficulté: Intermédiaire*

---

[Retour au module](../README_PROJETS.md)
