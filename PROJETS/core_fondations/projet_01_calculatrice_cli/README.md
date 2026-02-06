# Projet 1: Calculatrice CLI

Créez une calculatrice interactive en ligne de commande avec opérations de base et avancée.

## Objectif

Appliquer les fondamentaux de Python (variables, types, opérateurs, conditions) dans un projet concret et utile.

## Difficulté

**Débutant** - Durée estimée: 2-3 heures

## Prérequis

**Module 1 requis** : Chapitres 01-04

## Fonctionnalités Attendues

### Opérations de Base
- Addition `+`
- Soustraction `-`
- Multiplication `*`
- Division `/`
- Division entière `//`
- Modulo `%`
- Puissance `**`

### Fonctionnalités
1. Menu interactif en boucle
2. Validation des entrées utilisateur
3. Gestion des erreurs (division par zéro, entrée invalide)
4. Affichage formaté des résultats
5. Option pour continuer ou quitter

### Bonus (Optionnel)
- Historique des calculs
- Fonctions mathématiques avancées (racine carrée, sinus, cosinus)
- Conversion d'unités

## Structure Suggérée

```
projet_01_calculatrice_cli/
├── README.md
├── src/
│   ├── main.py           # Point d'entrée
│   ├── operations.py     # Fonctions mathématiques
│   └── interface.py      # Interactions utilisateur
├── solution/
│   ├── main.py
│   ├── operations.py
│   └── interface.py
└── tests/
    └── test_operations.py
```

## Indications

### Niveau 1 - Indice
Commencez par créer les fonctions pour chaque opération:
```python
def addition(a: float, b: float) -> float:
    return a + b
```

### Niveau 2 - Indice
Créez un menu avec une boucle `while`:
```python
while True:
    print_menu()
    choix = input("Votre choix: ")
    if choix == "q":
        break
    # traiter le choix
```

### Niveau 3 - Indice
Gérez les erreurs avec try/except:
```python
try:
    resultat = a / b
except ZeroDivisionError:
    print("Erreur: division par zéro!")
```

## Exemple d'Exécution

```
=== CALCULATRICE CLI ===

1. Addition
2. Soustraction
3. Multiplication
4. Division
5. Quitter

Votre choix: 1
Entrez le premier nombre: 10
Entrez le deuxième nombre: 5

Résultat: 10 + 5 = 15

Voulez-vous continuer? (o/n): o

=== CALCULATRICE CLI ===
...
```

## Critères de Validation

- [ ] Le programme accepte les nombres décimaux
- [ ] La division par zéro est gérée
- [ ] Les entrées non numériques sont validées
- [ ] L'utilisateur peut quitter proprement
- [ ] Le code est lisible et commenté

## Ressources

- [Documentation Python - float](https://docs.python.org/fr/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Gestion des exceptions](https://docs.python.org/fr/3/tutorial/errors.html)

---

[Retour au module](../README_PROJETS.md)
