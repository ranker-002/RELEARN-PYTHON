# Projet: Gestionnaire de Tâches CLI

Créez une todo list persistante en ligne de commande avec catégories et priorités.

## Objectif

Consolider les bases (variables, listes, dictionnaires, fichiers) dans un projet utile au quotidien.

## Difficulté

**Intermédiaire** - Durée estimée: 4-6 heures

## Prérequis

**Module 1 requis** : Chapitres 01-07

## Fonctionnalités Attendues

### CRUD Complet
1. **Créer** une tâche avec:
   - Titre (obligatoire)
   - Description (optionnelle)
   - Priorité (haute, moyenne, basse)
   - Catégorie (travail, personnel, urgent)
   - Date d'échéance (optionnelle)

2. **Lister** les tâches avec:
   - Filtre par statut (toutes, en cours, terminées)
   - Filtre par priorité
   - Tri par date ou priorité

3. **Modifier** une tâche:
   - Marquer comme terminée/non terminée
   - Modifier le contenu

4. **Supprimer** une tâche (individuelle ou toutes terminées)

### Fonctionnalités Supplémentaires
- Persistance JSON (les tâches survivent au redémarrage)
- Recherche par mot-clé
- Statistiques (nombre de tâches, % terminées)
- Export JSON

## Structure Suggérée

```
projet_02_gestionnaire_taches_cli/
├── README.md
├── src/
│   ├── main.py           # Point d'entrée + boucle CLI
│   ├── task.py           # Classe Task
│   ├── storage.py        # Sauvegarde/chargement JSON
│   └── cli.py            # Fonctions CLI
├── solution/
│   ├── main.py
│   ├── task.py
│   ├── storage.py
│   └── cli.py
├── data/
│   └── tasks.json        # Base de données
└── tests/
    └── test_task.py
```

## Modèle de Données

```python
class Task:
    id: int
    titre: str
    description: str
    priorite: str  # "haute", "moyenne", "basse"
    categorie: str
    date_echeance: Optional[str]
    completed: bool
    date_creation: str
```

## Indications

### Indice 1: Structure de tâche
```python
tache = {
    "id": 1,
    "titre": "Apprendre Python",
    "description": "Finir le chapitre 7",
    "priorite": "haute",
    "categorie": "apprentissage",
    "completed": False,
    "date_creation": "2024-01-15"
}
```

### Indice 2: Sauvegarde JSON
```python
import json

def sauvegarder(taches, fichier="data/tasks.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(taches, f, indent=2, ensure_ascii=False)
```

### Indice 3: Menu CLI
```python
while True:
    afficher_menu()
    choix = input(">>> ")
    if choix == "1":
        creer_tache()
    elif choix == "2":
        lister_taches()
    # ... autres options
```

## Exemple d'Exécution

```
=== GESTIONNAIRE DE TÂCHES ===

1. Ajouter une tâche
2. Lister les tâches
3. Modifier une tâche
4. Supprimer une tâche
5. Rechercher
6. Statistiques
7. Quitter

>>> 1

Titre: Apprendre les classes Python
Description (enter pour none): Finir le module 2
Priorité (haute/moyenne/basse): haute
Catégorie: Apprentissage
Date d'échéance (YYYY-MM-DD, enter pour none): 2024-02-01

✓ Tâche ajoutée!

>>> 2

=== TÂCHES ===
[1] [HAUTE] Apprendre les classes Python (Apprentissage)
     Finir le module 2 | Échéance: 2024-02-01
     ❌ En cours

[2] [BASSE] Acheter du lait (Personnel)
     ❌ En cours

```

## Critères de Validation

- [ ] CRUD complet fonctionne
- [ ] Données persistées entre les sessions
- [ ] Filtres et tris fonctionnels
- [ ] Validation des entrées
- [ ] Code structuré et documenté

---

[Retour au module](../README_PROJETS.md)
