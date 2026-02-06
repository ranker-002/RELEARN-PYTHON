# Chapitre 14: Exceptions et Gestion des Erreurs

## Ce que vous allez apprendre

- Le concept d'exceptions
- try/except/else/finally
- Les exceptions内置
- Créer ses propres exceptions
- Hiérarchie des exceptions
- Propagation des exceptions
- Bonnes pratiques

---

## 1. Introduction aux Exceptions

### Qu'est-ce qu'une Exception?

Une exception est un événement qui interrompt le flux normal d'exécution:

```python
# Division par zéro
resultat = 10 / 0  # ZeroDivisionError

# Index invalide
liste = [1, 2, 3]
print(liste[10])  # IndexError

# Clé inexistante
dico = {"a": 1}
print(dico["z"])  # KeyError

# Type incorrect
"texte" + 5  # TypeError
```

### Pourquoi les Exceptions?

- Séparation du code normal et du code d'erreur
- Propagation automatique des erreurs
- Possibilité de récupération
- Messages d'erreur détaillés

---

## 2. Structure try/except

### Syntaxe de Base

```python
try:
    # Code qui peut lever une exception
    resultat = 10 / 0
except ZeroDivisionError:
    # Code de récupération
    resultat = float('inf')
    print("Division par zéro détectée!")

print(resultat)  # inf
```

### Capturer Plusieurs Exceptions

```python
try:
    x = int(input("Entrez un nombre: "))
    resultat = 100 / x
except ValueError:
    print("Ce n'est pas un nombre valide!")
except ZeroDivisionError:
    print("Impossible de diviser par zéro!")
except Exception as e:
    print(f"Erreur inattendue: {e}")
```

### Capturer avec Tuple

```python
try:
    # Plusieurs opérations risquées
    x = int(input())
    y = [1, 2, 3][x]
except (ValueError, IndexError) as e:
    print(f"Erreur: {e}")
```

### Else et Finally

```python
try:
    x = int("42")
except ValueError:
    print("Conversion échouée")
else:
    # S'exécute SEULEMENT si pas d'exception
    print(f"Conversion réussie: {x}")
finally:
    # S'exécute TOUJOURS (même avec return)
    print("Fin du bloc try")
```

---

## 3. Les Exceptions内置

### Hiérarchie des Exceptions

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── StopIteration
      ├── StopAsyncIteration
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── ConnectionError
      ├── ReferenceError
      ├── RuntimeError
      ├── SyntaxError
      │    └── IndentationError
      ├── TypeError
      └── ValueError
```

### Utiliser les Bonnes Exceptions

```python
# MAUVAIS: Trop générique
try:
    operation_risquee()
except:
    pass

# BON: Spécifique
try:
    operation_risquee()
except ValueError as e:
    print(f"Valeur invalide: {e}")
except FileNotFoundError:
    print("Fichier non trouvé")
```

---

## 4. Créer ses Propres Exceptions

### Exception Simple

```python
class MonException(Exception):
    pass

raise MonException("Un message d'erreur")
```

### Exception avec Détails

```python
class ValidationError(Exception):
    def __init__(self, champ, valeur, message):
        self.champ = champ
        self.valeur = valeur
        self.message = message
        super().__init__(self.message)

try:
    age = -5
    if age < 0:
        raise ValidationError("age", age, "L'âge ne peut pas être négatif")
except ValidationError as e:
    print(f"Erreur dans {e.champ}: {e.message}")
```

### Hiérarchie d'Exceptions

```python
class ApplicationError(Exception):
    """Exception de base pour l'application."""

class ValidationError(ApplicationError):
    """Erreur de validation des données."""

class DatabaseError(ApplicationError):
    """Erreur de base de données."""

class ConfigurationError(ApplicationError):
    """Erreur de configuration."""
```

---

## 5. Propagation des Exceptions

### Remonter une Exception

```python
def niveau3():
    raise ValueError("Erreur au niveau 3")

def niveau2():
    niveau3()

def niveau1():
    niveau2()

niveau1()  # ValueError remonté jusqu'au sommet
```

### Relancer une Exception

```python
def diviser_securise(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Division par zéro!")
        raise  # Relance l'exception

try:
    diviser_securise(10, 0)
except ZeroDivisionError:
    print("Exception gérée ici")
```

### Chainer des Exceptions

```python
try:
    raise ValueError("Erreur initiale")
except ValueError as e:
    raise RuntimeError("Erreur secondaire") from e

# Output: RuntimeError: Erreur secondaire
# Caused by: ValueError: Erreur initiale
```

---

## 6. Patterns Avancés

### Context Manager pour les Ressources

```python
class ResourceManager:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"Acquisition de {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Libération de {self.name}")
        if exc_type:
            print(f"Exception: {exc_type.__name__}")
        return False  # Propager l'exception

with ResourceManager("database") as r:
    print(f"Utilisation de {r.name}")
    # raise RuntimeError("Erreur!")
```

### Retry Pattern

```python
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Tentative {attempt} échouée: {e}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def operation_risquee():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Connexion refusée")
    return "Succès!"
```

### Validation avec Exceptions

```python
class Validator:
    @staticmethod
    def required(value, field_name):
        if value is None or value == "":
            raise ValueError(f"{field_name} est requis")
    
    @staticmethod
    def min_length(value, min_len, field_name):
        if len(value) < min_len:
            raise ValueError(f"{field_name} doit avoir au moins {min_len} caractères")
    
    @staticmethod
    def max_length(value, max_len, field_name):
        if len(value) > max_len:
            raise ValueError(f"{field_name} ne peut pas dépasser {max_len} caractères")
    
    @staticmethod
    def in_range(value, min_val, max_val, field_name):
        if not (min_val <= value <= max_val):
            raise ValueError(f"{field_name} doit être entre {min_val} et {max_val}")

def validate_user(data):
    Validator.required(data.get('name'), 'name')
    Validator.min_length(data.get('name', ''), 2, 'name')
    Validator.in_range(data.get('age', 0), 0, 150, 'age')
```

---

## 7. Bonnes Pratiques

### Ne Pas Utiliser try/except pour le Flux Normal

```python
# MAUVAIS
try:
    dico["cle"]
except KeyError:
    dico["cle"] = "valeur par défaut"

# BON
dico = {}
cle = "nouvelle"
dico[cle] = dico.get(cle, "valeur par défaut")
```

### Lever des Exceptions Précoces

```python
def traiter_utilisateur(user_id):
    # Validation précoce
    if not user_id:
        raise ValueError("ID utilisateur requis")
    
    if user_id < 0:
        raise ValueError("ID utilisateur invalide")
    
    # Suite du traitement...
```

### Logging des Exceptions

```python
import logging

try:
    operation_complexe()
except Exception as e:
    logging.error(f"Erreur lors de l'opération: {e}", exc_info=True)
    # Affiche la trace complète
```

---

## Points Clés à Retenir

| Mot-clé | Usage |
|---------|-------|
| `try` | Bloc de code à surveiller |
| `except` | Attraper une exception |
| `else` | Si pas d'exception |
| `finally` | Toujours exécuter |
| `raise` | Lever une exception |
| `as` | Stocker l'exception |

---

## Erreurs Courantes

```python
# ERREUR: Avaler toutes les exceptions
try:
    operation()
except:  # MAUVAIS!
    pass

# ERREUR: Renvoyer un résultat après une exception
try:
    return 1
except:
    return 2
finally:
    return 3  # Retourne toujours 3!

# ERREUR: Comparer le type d'exception
try:
    raise ValueError()
except Exception as e:
    if type(e) == ValueError:  # MAUVAIS!
        pass

# ERREUR: Oublier de propager
try:
    operation()
except Exception:
    print("Erreur!")  # Oubli de raise
```

---

## Prochain Chapitre

Dans le chapitre suivant, vous apprendrez la **manipulation de fichiers** pour lire et écrire des données sur le disque.
