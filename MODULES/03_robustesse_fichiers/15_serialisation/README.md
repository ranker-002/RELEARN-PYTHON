# Chapitre 15 : Sérialisation - Sauvegarder et Partager des Données

## Introduction : Pourquoi Sérialiser ?

Imagine que tu créées un jeu vidéo. Le joueur a passé 3 heures à avancer, a débloqué des niveaux, accumulé des points. Si tu éteins l'ordinateur, tout est perdu ! 😱

La **sérialisation** est la solution : elle transforme les objets Python (listes, dictionnaires, objets complexes) en un format qui peut être :
- **Sauvegardé** sur disque
- **Transmis** via réseau
- **Partagé** entre programmes
- **Stocké** dans une base de données

Le processus inverse s'appelle la **désérialisation** : on lit le format stocké et on recrée les objets Python.

**Exemple concret :**
```python
# Tu as cette donnée en mémoire
game_state = {
    "joueur": "Alice",
    "niveau": 5,
    "score": 12500,
    "inventaire": ["épée", "bouclier", "potion"]
}

# Sérialisation → Fichier sauvegardé
# Désérialisation → Objet recréé en mémoire
```

---

## 1. JSON - Le Format Universel

### Pourquoi JSON ?

**JSON** (JavaScript Object Notation) est le format le plus utilisé car :
- ✅ Lisible par les humains
- ✅ Supporté par tous les langages
- ✅ Léger et textuel
- ✅ Parfait pour les APIs web

### Sauvegarder en JSON

```python
import json

# Données à sauvegarder
utilisateur = {
    "nom": "Alice Martin",
    "age": 28,
    "email": "alice@email.com",
    "competences": ["Python", "JavaScript", "SQL"],
    "adresse": {
        "rue": "123 Rue de Paris",
        "ville": "Paris",
        "code_postal": "75001"
    },
    "est_actif": True
}

# Méthode 1 : Sauvegarder dans un fichier
with open("utilisateur.json", "w", encoding="utf-8") as f:
    json.dump(utilisateur, f, ensure_ascii=False, indent=2)

# Méthode 2 : Obtenir une chaîne JSON
texte_json = json.dumps(utilisateur, ensure_ascii=False, indent=2)
print(texte_json)
```

**Résultat dans le fichier :**
```json
{
  "nom": "Alice Martin",
  "age": 28,
  "email": "alice@email.com",
  "competences": [
    "Python",
    "JavaScript",
    "SQL"
  ],
  "adresse": {
    "rue": "123 Rue de Paris",
    "ville": "Paris",
    "code_postal": "75001"
  },
  "est_actif": true
}
```

### Charger depuis JSON

```python
import json

# Lire depuis un fichier
with open("utilisateur.json", "r", encoding="utf-8") as f:
    donnees = json.load(f)

print(donnees["nom"])  # Alice Martin
print(donnees["competences"])  # ['Python', 'JavaScript', 'SQL']

# Depuis une chaîne JSON
texte = '{"temperature": 25, "unite": "Celsius"}'
data = json.loads(texte)
print(data["temperature"])  # 25
```

### Options Importantes de json.dump()

```python
import json

donnees = {"nom": " café ", "prix": 19.99}

# Format compact (une seule ligne)
json_compact = json.dumps(donnees)  # {"nom": "caf\u00e9", "prix": 19.99}

# Format lisible avec indentation
json_beau = json.dumps(donnees, indent=2, ensure_ascii=False)

# Trier les clés
json_trie = json.dumps(donnees, indent=2, sort_keys=True)

# Personnaliser le séparateur (défaut: ", ")
json_custom = json.dumps(donnees, separators=(",", ":"))
```

### Types Supportés par JSON

```python
import json

# ✅ Types qui fonctionnent naturellement
data = {
    "chaine": "texte",           # str
    "entier": 42,                # int
    "decimal": 3.14,             # float
    "booleen": True,             # bool (attention: true en JSON)
    "null": None,                # None (attention: null en JSON)
    "liste": [1, 2, 3],          # list
    "dictionnaire": {"a": 1},    # dict
}

# ❌ Types qui ne fonctionnent PAS directement
data_probleme = {
    "tuple": (1, 2, 3),          # Tuple → converti en liste
    "ensemble": {1, 2, 3},       # Set → ERREUR !
    "bytes": b"hello",           # Bytes → ERREUR !
    "date": datetime.now(),      # DateTime → ERREUR !
}
```

### Gérer les Types Non-Supportés

**Solution 1 : Convertir avant sérialisation**
```python
import json
from datetime import datetime

data = {
    "nom": "Projet Alpha",
    "date_creation": datetime.now(),  # Problème !
    "tags": {"python", "web", "api"}  # Problème !
}

# Convertir manuellement
data_converti = {
    "nom": data["nom"],
    "date_creation": data["date_creation"].isoformat(),  # "2024-01-15T10:30:00"
    "tags": list(data["tags"])  # Convertir set en list
}

with open("projet.json", "w") as f:
    json.dump(data_converti, f, indent=2)
```

**Solution 2 : Utiliser un encodeur personnalisé**
```python
import json
from datetime import datetime
from decimal import Decimal

class MonEncodeur(json.JSONEncoder):
    """Encodeur personnalisé pour types spéciaux."""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, bytes):
            return obj.decode('utf-8')
        return super().default(obj)

# Utilisation
data = {
    "date": datetime.now(),
    "prix": Decimal("19.99"),
    "tags": {"python", "web"}
}

json_str = json.dumps(data, cls=MonEncodeur, indent=2)
```

### Exemple Pratique : Sauvegarde de Jeu

```python
import json
from datetime import datetime

class SauvegardeJeu:
    """Gère la sauvegarde et chargement d'une partie."""
    
    def __init__(self, fichier="sauvegarde.json"):
        self.fichier = fichier
    
    def sauvegarder(self, etat_jeu):
        """Sauvegarde l'état du jeu en JSON."""
        sauvegarde = {
            "version": "1.0",
            "date": datetime.now().isoformat(),
            "donnees": etat_jeu
        }
        
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(sauvegarde, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Partie sauvegardée dans {self.fichier}")
    
    def charger(self):
        """Charge une partie sauvegardée."""
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                sauvegarde = json.load(f)
            
            print(f"✅ Partie chargée (sauvegardée le {sauvegarde['date']})")
            return sauvegarde["donnees"]
            
        except FileNotFoundError:
            print("❌ Aucune sauvegarde trouvée")
            return None
        except json.JSONDecodeError:
            print("❌ Fichier de sauvegarde corrompu")
            return None

# Utilisation
sauvegarde = SauvegardeJeu()

# Sauvegarder
etat = {
    "joueur": "Alice",
    "niveau": 5,
    "points_de_vie": 85,
    "position": {"x": 100, "y": 200}
}
sauvegarde.sauvegarder(etat)

# Charger
ancien_etat = sauvegarde.charger()
```

---

## 2. Pickle - Sérialisation Binaire Python

### Pourquoi Pickle ?

**Pickle** est spécifique à Python mais permet de sérialiser :
- ✅ N'importe quel objet Python (presque tout !)
- ✅ Objets personnalisés
- ✅ Fonctions (avec limitations)
- ✅ Format binaire compact

**⚠️ ATTENTION :** Pickle n'est PAS sécurisé ! Ne chargez jamais un fichier pickle provenant d'une source non fiable.

### Sauvegarder avec Pickle

```python
import pickle

# Données complexes
joueur = {
    "nom": "Alice",
    "inventaire": ["épée", "bouclier", "potion"],
    "position": (100, 200),  # Tuple préservé !
    "competences": {"force": 15, "agilite": 12}
}

# Sauvegarder en binaire
with open("joueur.pkl", "wb") as f:  # 'wb' = write binary
    pickle.dump(joueur, f)

print("✅ Données sauvegardées")
```

### Charger avec Pickle

```python
import pickle

# Charger depuis le fichier binaire
with open("joueur.pkl", "rb") as f:  # 'rb' = read binary
    joueur_charge = pickle.load(f)

print(joueur_charge)
# {'nom': 'Alice', 'inventaire': ['épée', 'bouclier', 'potion'], 
#  'position': (100, 200), 'competences': {'force': 15, 'agilite': 12}}

# Note : Le tuple est conservé (pas converti en liste comme avec JSON)
print(type(joueur_charge["position"]))  # <class 'tuple'>
```

### Sérialiser des Objets Personnalisés

```python
import pickle

class Personnage:
    """Personnage de jeu avec méthodes."""
    
    def __init__(self, nom, niveau=1):
        self.nom = nom
        self.niveau = niveau
        self.points_de_vie = 100
        self.inventaire = []
    
    def monter_niveau(self):
        self.niveau += 1
        self.points_de_vie += 20
        print(f"{self.nom} passe au niveau {self.niveau}!")
    
    def __repr__(self):
        return f"Personnage({self.nom}, niveau={self.niveau})"

# Créer un personnage
hero = Personnage("Aragorn", niveau=5)
hero.inventaire = ["Anduril", "Armure"]

# Sauvegarder l'objet complet (données + méthodes)
with open("hero.pkl", "wb") as f:
    pickle.dump(hero, f)

# Charger - l'objet est recréé avec toutes ses méthodes
with open("hero.pkl", "rb") as f:
    hero_charge = pickle.load(f)

print(hero_charge)  # Personnage(Aragorn, niveau=5)
hero_charge.monter_niveau()  # Aragorn passe au niveau 6!
```

### Protocoles Pickle

```python
import pickle

# Différents protocoles (versions)
# 0 : ASCII, lisible (déprécié)
# 1 : Binaire ancien
# 2 : Python 2.3+
# 3 : Python 3.0+ (défaut)
# 4 : Python 3.4+ (meilleur pour gros objets)
# 5 : Python 3.8+ (optimisé)

data = {"test": "valeur"}

# Utiliser un protocole spécifique
with open("data.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

# Vérifier le protocole utilisé
print(pickle.HIGHEST_PROTOCOL)  # Généralement 5
```

### Compression avec Pickle

```python
import pickle
import gzip  # Compression

data_gros = {"cles": list(range(10000))}

# Sauvegarder compressé
with gzip.open("data.pkl.gz", "wb") as f:
    pickle.dump(data_gros, f)

# Charger depuis fichier compressé
with gzip.open("data.pkl.gz", "rb") as f:
    data_charge = pickle.load(f)

print(f"Taille originale: {len(str(data_gros))} octets")
# Le fichier compressé est beaucoup plus petit !
```

---

## 3. CSV - Données Tabulaires

### Pourquoi CSV ?

**CSV** (Comma-Separated Values) est parfait pour :
- ✅ Tableaux de données
- ✅ Export vers Excel
- ✅ Bases de données simples
- ✅ Interopérabilité maximale

### Écrire un CSV

```python
import csv

# Données à écrire
csv_sauvegarde = [
    ["Nom", "Age", "Ville"],  # En-tête
    ["Alice", 25, "Paris"],
    ["Bob", 30, "Lyon"],
    ["Charlie", 35, "Marseille"]
]

# Méthode 1 : Écrire ligne par ligne
with open("contacts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for ligne in csv_sauvegarde:
        writer.writerow(ligne)

# Méthode 2 : Écrire tout d'un coup
with open("contacts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(csv_sauvegarde)
```

### Lire un CSV

```python
import csv

# Lire tout le fichier
with open("contacts.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for ligne in reader:
        print(ligne)
# ['Nom', 'Age', 'Ville']
# ['Alice', '25', 'Paris']
# ...

# Convertir en liste
donnees = list(csv.reader(open("contacts.csv", "r", encoding="utf-8")))
```

### CSV avec Dictionnaires (DictReader/DictWriter)

```python
import csv

# Écrire avec des en-têtes automatiques
champs = ["nom", "age", "ville"]
donnees = [
    {"nom": "Alice", "age": 25, "ville": "Paris"},
    {"nom": "Bob", "age": 30, "ville": "Lyon"},
    {"nom": "Charlie", "age": 35, "ville": "Marseille"}
]

with open("contacts_dict.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=champs)
    writer.writeheader()  # Écrit les noms de colonnes
    writer.writerows(donnees)

# Lire comme dictionnaires
with open("contacts_dict.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for ligne in reader:
        print(f"{ligne['nom']} habite à {ligne['ville']}")
# Alice habite à Paris
# Bob habite à Lyon
```

### Personnaliser le Format CSV

```python
import csv

# Utiliser ; au lieu de , (format européen)
with open("data_europe.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Prix", "Quantité"])
    writer.writerow(["19,99", "5"])  # 19,99 avec virgule

# Gérer les guillemets
with open("data_quoted.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(["Texte avec, virgule", "Normal"])
    # "Texte avec, virgule","Normal"

# Lire avec dialecte personnalisé
csv.register_dialect("excel_eu", delimiter=";", quotechar='"')
with open("data_europe.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, dialect="excel_eu")
    for ligne in reader:
        print(ligne)
```

---

## 4. YAML - Configuration Lisible

### Pourquoi YAML ?

**YAML** est idéal pour :
- ✅ Fichiers de configuration
- ✅ Données hiérarchiques complexes
- ✅ Lisibilité maximale (pas de {} ni de ")
- ✅ Commentaires supportés

**Installation :**
```bash
pip install pyyaml
```

### Écrire en YAML

```python
import yaml

config = {
    "application": {
        "nom": "Mon Super App",
        "version": "2.0.1",
        "debug": False
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "nom": "ma_base",
        "utilisateur": "admin"
    },
    "features": [
        "authentification",
        "notifications",
        "export_pdf"
    ]
}

# Sauvegarder
with open("config.yaml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
```

**Résultat (config.yaml) :**
```yaml
application:
  nom: Mon Super App
  version: 2.0.1
  debug: false
database:
  host: localhost
  port: 5432
  nom: ma_base
  utilisateur: admin
features:
- authentification
- notifications
- export_pdf
```

### Lire du YAML

```python
import yaml

# Charger la configuration
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print(config["application"]["nom"])  # Mon Super App
print(config["database"]["host"])    # localhost
```

### YAML avec Commentaires

```python
import yaml

# YAML avec commentaires (impossible en JSON !)
yaml_content = """
# Configuration principale
application:
  nom: Mon App
  version: 1.0  # Version initiale
  
# Paramètres base de données
database:
  host: localhost  # Serveur local
  port: 5432       # Port PostgreSQL standard
"""

config = yaml.safe_load(yaml_content)
```

---

## 5. Comparaison des Formats

| Format | Lisible | Taille | Types | Usage Principal | Sécurité |
|--------|---------|--------|-------|-----------------|----------|
| **JSON** | ✅ Oui | Moyenne | Limités | APIs, Web, Config | ✅ Sûr |
| **Pickle** | ❌ Non | Compacte | Tous | Objets Python | ⚠️ Risqué |
| **CSV** | ✅ Oui | Légère | Texte/Num | Tableaux, Excel | ✅ Sûr |
| **YAML** | ✅ Oui | Légère | Types riches | Configuration | ✅ Sûr |

### Quand Utiliser Quoi ?

```python
# 🌐 API Web / Partage → JSON
import json
donnees_api = {"status": "ok", "data": []}
json.dumps(donnees_api)

# 🎮 Jeu vidéo / Objets complexes → Pickle
import pickle
sauvegarde_partie = {"joueur": Personnage("Hero")}
pickle.dump(sauvegarde_partie, f)

# 📊 Export Excel / Tableau → CSV
import csv
donnees_tableau = [["Nom", "Valeur"], ["A", 100]]
csv.writer(f).writerows(donnees_tableau)

# ⚙️ Configuration → YAML
import yaml
config_app = {"debug": False, "port": 8080}
yaml.dump(config_app, f)
```

---

## 6. Exemple Complet : Système de Sauvegarde Multi-Format

```python
import json
import pickle
import csv
import yaml
from datetime import datetime
from pathlib import Path

class GestionnaireSauvegarde:
    """Système de sauvegarde supportant plusieurs formats."""
    
    def __init__(self, dossier="sauvegardes"):
        self.dossier = Path(dossier)
        self.dossier.mkdir(exist_ok=True)
    
    def sauvegarder(self, donnees, nom, format="json"):
        """
        Sauvegarde les données dans le format spécifié.
        
        Args:
            donnees: Données à sauvegarder
            nom: Nom du fichier (sans extension)
            format: 'json', 'pickle', 'csv', ou 'yaml'
        """
        chemin = self.dossier / f"{nom}.{format}"
        
        if format == "json":
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)
        
        elif format == "pickle":
            with open(chemin, "wb") as f:
                pickle.dump(donnees, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        elif format == "csv":
            # Nécessite une liste de dictionnaires
            if donnees and isinstance(donnees[0], dict):
                with open(chemin, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=donnees[0].keys())
                    writer.writeheader()
                    writer.writerows(donnees)
            else:
                raise ValueError("CSV nécessite une liste de dictionnaires")
        
        elif format == "yaml":
            with open(chemin, "w", encoding="utf-8") as f:
                yaml.dump(donnees, f, default_flow_style=False)
        
        else:
            raise ValueError(f"Format '{format}' non supporté")
        
        print(f"✅ Sauvegardé: {chemin}")
        return chemin
    
    def charger(self, nom, format="json"):
        """Charge des données depuis un fichier."""
        chemin = self.dossier / f"{nom}.{format}"
        
        if not chemin.exists():
            raise FileNotFoundError(f"Fichier non trouvé: {chemin}")
        
        if format == "json":
            with open(chemin, "r", encoding="utf-8") as f:
                return json.load(f)
        
        elif format == "pickle":
            with open(chemin, "rb") as f:
                return pickle.load(f)
        
        elif format == "csv":
            with open(chemin, "r", encoding="utf-8") as f:
                return list(csv.DictReader(f))
        
        elif format == "yaml":
            with open(chemin, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        
        else:
            raise ValueError(f"Format '{format}' non supporté")

# Démonstration
gestionnaire = GestionnaireSauvegarde()

# Données de test
joueurs = [
    {"nom": "Alice", "score": 1250, "niveau": 5},
    {"nom": "Bob", "score": 980, "niveau": 4},
    {"nom": "Charlie", "score": 1500, "niveau": 6}
]

# Sauvegarder dans différents formats
gestionnaire.sauvegarder(joueurs, "classement", format="json")
gestionnaire.sauvegarder(joueurs, "classement", format="csv")
gestionnaire.sauvegarder(joueurs, "classement", format="yaml")

# Charger depuis JSON
classement_json = gestionnaire.charger("classement", format="json")
print(f"Chargé depuis JSON: {len(classement_json)} joueurs")
```

---

## 7. Bonnes Pratiques

### 1. Gestion des Erreurs

```python
import json

def charger_securise(chemin):
    """Charge un fichier JSON avec gestion d'erreurs."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Fichier non trouvé: {chemin}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON invalide: {e}")
        return None
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return None
```

### 2. Versioning des Données

```python
import json

def sauvegarder_versionnee(donnees, chemin, version="1.0"):
    """Sauvegarde avec métadonnées de version."""
    
    sauvegarde = {
        "_meta": {
            "version": version,
            "format": "json",
            "date": datetime.now().isoformat()
        },
        "data": donnees
    }
    
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(sauvegarde, f, indent=2)

def charger_versionnee(chemin, version_attendue="1.0"):
    """Charge en vérifiant la version."""
    
    with open(chemin, "r", encoding="utf-8") as f:
        sauvegarde = json.load(f)
    
    if sauvegarde.get("_meta", {}).get("version") != version_attendue:
        print("⚠️ Version différente de l'attendue")
    
    return sauvegarde["data"]
```

### 3. Sauvegardes Multiples

```python
import json
import shutil
from datetime import datetime
from pathlib import Path

def sauvegarder_avec_backup(donnees, chemin, max_backups=3):
    """Sauvegarde en gardant des versions de backup."""
    
    chemin = Path(chemin)
    
    # Renommer les anciennes sauvegardes
    for i in range(max_backups - 1, 0, -1):
        ancien = chemin.parent / f"{chemin.stem}.backup{i}{chemin.suffix}"
        nouveau = chemin.parent / f"{chemin.stem}.backup{i+1}{chemin.suffix}"
        if ancien.exists():
            if i == max_backups - 1:
                ancien.unlink()  # Supprimer le plus vieux
            else:
                shutil.move(ancien, nouveau)
    
    # Déplacer la sauvegarde actuelle en backup 1
    if chemin.exists():
        backup = chemin.parent / f"{chemin.stem}.backup1{chemin.suffix}"
        shutil.move(chemin, backup)
    
    # Sauvegarder les nouvelles données
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2)
    
    print(f"✅ Sauvegardé avec {max_backups} backups conservés")
```

---

## 8. Erreurs Courantes à Éviter

### 1. Oublier l'encodage UTF-8

```python
# ❌ MAUVAIS - Problèmes avec les accents
with open("data.json", "w") as f:
    json.dump({"nom": "café"}, f)

# ✅ CORRECT - Toujours spécifier UTF-8
with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"nom": "café"}, f, ensure_ascii=False)
```

### 2. Confondre dump() et dumps()

```python
import json

# ❌ ERREUR - dumps() retourne une chaîne, pas écrit dans fichier
json.dumps(data, open("fichier.json", "w"))

# ✅ CORRECT - dump() écrit directement dans le fichier
json.dump(data, open("fichier.json", "w", encoding="utf-8"))

# ✅ CORRECT - dumps() puis écriture manuelle
texte = json.dumps(data)
with open("fichier.json", "w", encoding="utf-8") as f:
    f.write(texte)
```

### 3. Charger du Pickle Non Fiable

```python
import pickle

# ⚠️ DANGEREUX - Ne jamais faire ça avec des fichiers inconnus
with open("fichier_inconnu.pkl", "rb") as f:
    data = pickle.load(f)  # Pourrait exécuter du code malveillant !

# ✅ SÛR - Vérifier la source ou utiliser JSON
```

### 4. Oublier newline="" en CSV

```python
import csv

# ❌ MAUVAIS - Lignes vides sur Windows
with open("data.csv", "w") as f:
    writer = csv.writer(f)

# ✅ CORRECT - Empêche les doubles retours à la ligne
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
```

---

## 9. Exercices Pratiques

### Exercice 1 : Sauvegarde de Configuration
Crée un système qui sauvegarde et charge la configuration d'une application (thème, langue, notifications) en JSON.

### Exercice 2 : Export de Données
Crée une fonction qui exporte une liste de contacts (dictionnaires) vers JSON, CSV et YAML.

### Exercice 3 : Sauvegarde de Partie
Implémente un système de sauvegarde pour un jeu simple avec pickle, incluant la date de sauvegarde.

### Exercice 4 : Conversion de Formats
Crée un programme qui lit un fichier JSON et l'exporte en CSV (pour tableaux de données).

---

## Résumé

| Format | Méthode Écriture | Méthode Lecture | Usage |
|--------|------------------|-----------------|-------|
| **JSON** | `json.dump()` / `dumps()` | `json.load()` / `loads()` | APIs, Web |
| **Pickle** | `pickle.dump()` | `pickle.load()` | Objets Python |
| **CSV** | `csv.writer()` / `DictWriter()` | `csv.reader()` / `DictReader()` | Tableaux |
| **YAML** | `yaml.dump()` | `yaml.safe_load()` | Configuration |

---

## Prochain Chapitre

Tu maîtrises maintenant la sérialisation ! Dans le chapitre suivant, tu découvriras les **décorateurs et générateurs**, des outils puissants pour écrire du code Python plus élégant et efficace.

---

*💡 Astuce : Pour la plupart des projets, commence par JSON. Il est sûr, universel, et suffisant dans 80% des cas !*
