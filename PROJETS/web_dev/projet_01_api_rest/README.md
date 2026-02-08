# API RESTful

Création d'une API REST complète avec FastAPI/Flask

---

## 🎯 Objectif du Projet

Développer une API REST avec opérations CRUD et authentification

Ce projet vous permettra de mettre en pratique :
- La conception orientée objet (classes, héritage, encapsulation)
- La persistance de données (JSON)
- Les services et la séparation des responsabilités
- L'interface en ligne de commande (CLI)

---

## 📋 Fonctionnalités à Implémenter

1. **Endpoints RESTful pour ressources multiples**
2. **Opérations CRUD complètes (GET, POST, PUT, DELETE)**
3. **Authentification JWT**
4. **Validation des données avec Pydantic**
5. **Documentation automatique (Swagger/OpenAPI)**
6. **Gestion des erreurs et codes HTTP**

---

## 🗂️ Modèles de Données

Vous devez créer les classes suivantes dans `src/models/` :

### Endpoint
```python
@dataclass
class Endpoint:
    id, chemin, methode, handler, description
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

### Ressource
```python
@dataclass
class Ressource:
    id, nom, schema, endpoints_ids
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

### Requete
```python
@dataclass
class Requete:
    id, endpoint_id, parametres, headers, body
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

### Reponse
```python
@dataclass
class Reponse:
    id, requete_id, status_code, body, temps_execution
    
    # Méthodes à implémenter :
    # - __post_init__() : initialisation automatique
    # - validation des données
    # - conversion vers/depuis dict pour JSON
```

---

## ⚙️ Services à Développer

Créez les services suivants dans `src/services/` :

### Gestionnaire Api
**Description :** Gère l'API

**Fichier :** `src/services/gestionnaire_api.py`

**Méthodes principales :**
- `enregistrer_endpoint()`
- `router()`
- `valider()`

### Routage
**Description :** Route les requêtes

**Fichier :** `src/services/routage.py`

**Méthodes principales :**
- `matcher()`
- `executer_handler()`
- `formatter_reponse()`

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
