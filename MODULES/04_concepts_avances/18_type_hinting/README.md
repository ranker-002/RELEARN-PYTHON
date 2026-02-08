# Chapitre 18 : Le Type Hinting - Documenter les Types en Python

## Introduction : À quoi servent les types explicites ?

Imagine que tu reçus une lettre de la poste, mais l'expéditeur n'a pas écrit son adresse de retour. Si la lettre n'arrive pas, tu ne pourras jamais savoir qui l'a envoyée !

C'est exactement ce qui se passe avec du code sans types : quand quelque chose ne fonctionne pas, c'est difficile de trouver d'où vient le problème.

Le **Type Hinting** (ou "annotations de types") est comme ajouter des adresses de retour à ton code. Tu dis explicitement à Python :
- "Cette fonction attend un texte"
- "Cette variable doit contenir un nombre"
- "Cette liste ne peut contenir que des entiers"

Python ne t'oblige pas à respecter ces indications, mais :
1. Ton code est **mieux documenté**
2. Les **éditeurs intelligents** peuvent t'aider
3. Les **outils comme mypy** peuvent détecter des erreurs avant l'exécution

---

## 1. Les Bases du Type Hinting

### annotation simple

Regarde ce code sans types :

```python
# Code sans types - difficile de comprendre !
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

moyenne = calculer_moyenne([15, 12, 18, 14])
```

Maintenant avec les types :

```python
# Code avec types - tout est clair !
from typing import List

def calculer_moyenne(notes: List[float]) -> float:
    """Calcule la moyenne d'une liste de notes.
    
    Args:
        notes: Liste des notes (entre 0 et 20)
    
    Returns:
        La moyenne calculée
    """
    return sum(notes) / len(notes)

moyenne: float = calculer_moyenne([15, 12, 18, 14])
```

C'est beaucoup plus clair ! En un coup d'œil, tu sais que :
- `notes` doit être une liste de nombres
- La fonction retourne un nombre (float)

### Les types de base

```python
# Types primitifs
nom: str = "Alice"              # Texte
age: int = 25                   # Nombre entier
taille: float = 1.75            # Nombre décimal
est_actif: bool = True          # Vrai ou Faux

# Pas besoin d'annotation si le type est évident
prenom = "Bob"  # Python comprend que c'est un str
```

---

## 2. Les Types pour les Collections

Les listes, dictionnaires et autres collections ont besoin de préciser **ce qu'ils contiennent**.

```python
from typing import List, Dict, Set, Tuple

# Liste de textes
noms: List[str] = ["Alice", "Bob", "Charlie"]

# Dictionnaire : Clé -> Valeur
ages: Dict[str, int] = {
    "Alice": 25,
    "Bob": 30,
}

# Ensemble (pas d'ordre, pas de doublons)
primes: Set[int] = {2, 3, 5, 7, 11}

# Tuple (liste de taille fixe)
coordonnees: Tuple[float, float] = (48.8566, 2.3522)  # Paris

# Tuple avec types différents
personne: Tuple[str, int, str] = ("Alice", 25, "Paris")
```

### Les types optionnels

Parfois, une variable peut avoir une valeur OU être "vide" (None).

```python
from typing import Optional

# Soit un texte, soit None
nom: Optional[str] = None
prenom: Optional[str] = "Alice"

# Équivalent à :
# nom: Union[str, None] = None
```

---

## 3. Les Types pour les Fonctions

Tu peux aussi typer les fonctions !

```python
from typing import Callable, List

# Fonction qui prend un entier et retourne un entier
def doubler(x: int) -> int:
    return x * 2

# Fonction comme paramètre
def appliquer(fonction: Callable[[int], int], valeur: int) -> int:
    """Applique une fonction à une valeur."""
    return fonction(valeur)

# Appeler avec une fonction typée
resultat = appliquer(doubler, 5)  # 10
```

---

## 4. Les Types Personalisés avec `TypeVar`

Quand tu crées des classes ou des structures complexes, tu peux créer tes propres types.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')  # T est un type générique

class Pile(Generic[T]):
    """Une pile (LIFO - Last In, First Out)."""
    
    def __init__(self) -> None:
        self.elements: List[T] = []
    
    def push(self, element: T) -> None:
        self.elements.append(element)
    
    def pop(self) -> T:
        return self.elements.pop()

# Utiliser la pile avec des types spécifiques
pile_entiers: Pile[int] = Pile()
pile_entiers.push(1)
pile_entiers.push(2)
pile_entiers.push(3)

print(pile_entiers.pop())  # 3
```

---

## 5. Les Literal Types

Parfois, tu veux limiter une variable à certaines valeurs précises.

```python
from typing import Literal

# La direction ne peut être que ces 3 valeurs
Direction = Literal["nord", "sud", "est", "ouest"]

def deplacer(direction: Direction, distance: int) -> str:
    return f"Direction {direction}, distance {distance}"

# OK
deplacer("nord", 10)

# ERREUR (détectée par mypy)
# deplacer("diagonale", 10)  # Type checker!
```

---

## 6. TypedDict - Dictionnaires avec Types

Pour les dictionnaires dont tu connais la structure :

```python
from typing import TypedDict

class Personne(TypedDict):
    """Dictionnaire structuré pour une personne."""
    nom: str
    age: int
    ville: str

# Créer une personne
alice: Personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès comme un dictionnaire normal
print(alice["nom"])  # "Alice"
```

---

## 7. Protocol - Interfaces Strukturelles

Parfois, tu ne veux pas hériter d'une classe, mais simplement dire "cet objet a ces méthodes".

```python
from typing import Protocol

class Rendu(Protocol):
    """Quelque chose qui peut être rendu (affiché)."""
    
    def render(self) -> str:
        ...

class Image:
    def __init__(self, data: bytes):
        self.data = data
    
    def render(self) -> str:
        return f"[Image de {len(self.data)} octets]"

class Texte:
    def __init__(self, contenu: str):
        self.contenu = contenu
    
    def render(self) -> str:
        return self.contenu

# Fonction qui accepte n'importe quel objet avec render()
def afficher_objet(objet: Rendu) -> None:
    print(objet.render())

# Les deux fonctionnent !
afficher_objet(Image(b"données"))
afficher_objet(Texte("Bonjour !"))
```

---

## 8. Utiliser mypy pour Vérifier les Types

**mypy** est un outil qui analyse ton code et détecte les erreurs de types AVANT l'exécution.

### Installer mypy

```bash
pip install mypy
```

### Exemple de code avec erreurs

```python
# fichier: exemple.py
from typing import List

def saluer(nom: str) -> str:
    return f"Bonjour {nom}!"

def calculer_somme(a: int, b: int) -> int:
    return a + b

# Utilisation
print(saluer("Alice"))  # OK

# Erreurs intentionnelles pour démontrer mypy
resultat: int = calculer_somme("pas", "des nombres")  # ERREUR mypy!
```

### Lancer mypy

```bash
$ mypy exemple.py

exemple.py:10: error: Argument 1 to "calculer_somme" has incompatible type "str"; expected "int"
exemple.py:10: error: Argument 2 to "calculer_somme" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)
```

mypy a détecté que tu passes des textes ("pas", "des nombres") alors que la fonction attend des entiers !

---

## 9. Configuration de mypy

Créer un fichier `mypy.ini` ou `pyproject.toml` pour configurer mypy :

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.mypy.plugins."numpy"]
enabled = true
```

---

## 10. Exemple Complet : Module Typé

Voici un module bien typé pour gérer des utilisateurs :

```python
# user_manager.py
from typing import List, Optional, Dict
from dataclasses import dataclass

@dataclass
class Utilisateur:
    """Représente un utilisateur du système."""
    id: int
    nom: str
    email: str
    actif: bool = True

class GestionnaireUtilisateurs:
    """Gère une collection d'utilisateurs."""
    
    def __init__(self) -> None:
        self._utilisateurs: Dict[int, Utilisateur] = {}
        self._next_id: int = 1
    
    def ajouter_utilisateur(self, nom: str, email: str) -> Utilisateur:
        """Crée et ajoute un nouvel utilisateur."""
        user = Utilisateur(
            id=self._next_id,
            nom=nom,
            email=email,
            actif=True
        )
        self._utilisateurs[user.id] = user
        self._next_id += 1
        return user
    
    def get_utilisateur(self, id: int) -> Optional[Utilisateur]:
        """Récupère un utilisateur par son ID."""
        return self._utilisateurs.get(id)
    
    def desactiver_utilisateur(self, id: int) -> bool:
        """Désactive un utilisateur. Retourne True si trouvé."""
        user = self._utilisateurs.get(id)
        if user:
            user.actif = False
            return True
        return False
    
    def lister_actifs(self) -> List[Utilisateur]:
        """Liste tous les utilisateurs actifs."""
        return [u for u in self._utilisateurs.values() if u.actif]
```

---

## Résumé des Types

| Type | Usage | Exemple |
|------|-------|---------|
| `str` | Texte | `nom: str = "Alice"` |
| `int` | Entier | `age: int = 25` |
| `float` | Décimal | `prix: float = 19.99` |
| `bool` | Booléen | `actif: bool = True` |
| `List[T]` | Liste de T | `notes: List[int] = [1, 2, 3]` |
| `Dict[K, V]` | Dictionnaire | `ages: Dict[str, int] = {}` |
| `Set[T]` | Ensemble | `primes: Set[int] = {2, 3}` |
| `Tuple[T1, T2]` | Tuple | `coords: Tuple[float, float]` |
| `Optional[T]` | T ou None | `nom: Optional[str] = None` |
| `Callable[[A], R]` | Fonction | `f: Callable[[int], int]` |
| `Union[T1, T2]` | T1 ou T2 | `nombre: Union[int, float]` |

---

## Quand Utiliser le Type Hinting ?

### Utile pour :
- **Projets en équipe** - everyone understands the expected types
- **Bibliothèques publiques** - documentation automatique
- **Code complexe** - éviter les erreurs subtiles
- **Grande base de code** - maintenance facilitée

### Optionnel pour :
- Petits scripts personnels
- Prototypes rapides
- Exploration de données (pandas, notebooks)

---

## Erreurs Courantes

### 1. Oublier d'importer les types

```python
# MAUVAIS - List n'est pas défini !
def foo(notes: List) -> List:
    return notes

# CORRECT
from typing import List
def foo(notes: List[float]) -> List[float]:
    return notes
```

### 2. Utiliser des types trop génériques

```python
# MAUVAIS - Trop vague !
def traiter(data: dict) -> dict:
    pass

# CORRECT - Précis !
from typing import TypedDict

class UserData(TypedDict):
    nom: str
    age: int

def traiter(data: UserData) -> UserData:
    return data
```

### 3. Ignorer les erreurs mypy

```bash
# Les erreurs mypy sont là pour t'aider !
# Ne les ignore pas sans bonne raison
```

---

## Exercice : Module de Gestion de Bibliothèque

Crée un module entièrement typé pour gérer une bibliothèque avec :
- Classe `Livre` (titre, auteur, année)
- Classe `Bibliotheque` (ajouter, emprunter, retourner)
- Utilise les types appropriés (`List`, `Optional`, etc.)

---

## Outils Connexes

- **mypy** - Vérification statique des types
- **pyright** - Alternative à mypy (Microsoft)
- **pyre** - Alternative à mypy (Facebook)
- **VS Code** - Support natif du type checking

---

## Prochain Chapitre

Dans le chapitre suivant, tu apprendras à créer ton **premier projet complet** en appliquant tout ce que tu as appris : architecture, tests, documentation, et déploiment !

---

*Le type hinting peut sembler fastidieux au début, mais il t'économise des heures de débogage !*
