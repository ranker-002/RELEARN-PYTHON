# Chapitre 15: Fichiers I/O

## Ce que vous allez apprendre

- Ouvrir et fermer des fichiers
- Lire des fichiers (read, readline, readlines)
- Écrire dans des fichiers (write, writelines)
- Modes d'ouverture (r, w, a, r+, b)
- Gestion contextuelle (with)
- Parcours de fichiers
- Chemins et os.path
- Fichiers temporaires
- Encodages

---

## 1. Ouvrir et Fermer des Fichiers

### Ouvrir un Fichier

```python
# Mode lecture (read)
fichier = open("mon_fichier.txt", "r", encoding="utf-8")
contenu = fichier.read()
fichier.close()
```

### Modes d'Ouverture

| Mode | Description |
|------|-------------|
| `r` | Lecture seule (défaut) |
| `w` | Écriture (écrase) |
| `a` | Ajout (append) |
| `r+` | Lecture et écriture |
| `rb` | Lecture binaire |
| `wb` | Écriture binaire |
| `x` | Création exclusive |

---

## 2. Gestion Contextuelle (with)

```python
# AVEC with - recommande!
with open("fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
# Le fichier se ferme automatiquement

# SANS with (a eviter)
f = open("fichier.txt", "r")
try:
    contenu = f.read()
finally:
    f.close()  # Obligatoire!
```

---

## 3. Lire des Fichiers

### read() - Tout Lire

```python
with open("fichier.txt", "r") as f:
    contenu = f.read()
print(contenu)
```

### readline() - Ligne par Ligne

```python
with open("fichier.txt", "r") as f:
    ligne1 = f.readline()
    ligne2 = f.readline()
```

### readlines() - Liste de Lignes

```python
with open("fichier.txt", "r") as f:
    lignes = f.readlines()
    
for ligne in lignes:
    print(ligne.strip())
```

### Parcours Direct

```python
with open("fichier.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
```

---

## 4. Écrire dans des Fichiers

### write() - Écrire du Texte

```python
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")
```

### writelines() - Écrire une Liste

```python
lignes = ["Ligne 1\n", "Ligne 2\n", "Ligne 3\n"]

with open("sortie.txt", "w") as f:
    f.writelines(lignes)
```

### Ajout avec 'a'

```python
with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(f"[{datetime.now()}] Nouvelle entrée\n")
```

---

## 5. Encodages

```python
# UTF-8 (recommande)
with open("fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

# UTF-8 avec BOM
with open("fichier.txt", "r", encoding="utf-8-sig") as f:
    contenu = f.read()

# Latin-1 (ISO-8859-1)
with open("fichier.txt", "r", encoding="latin-1") as f:
    contenu = f.read()
```

---

## 6. Chemins et os.path

```python
import os

# Chemins absolus et relatifs
chemin = "dossier/sous-dossier/fichier.txt"
absolu = os.path.abspath(chemin)
print(absolu)

# Joindre des chemins
chemin_complet = os.path.join("dossier", "fichier.txt")
print(chemin_complet)

# Explorer le repertoire
print(os.listdir("."))
for elem in os.listdir("."):
    print(elem)

# Verifier le type
os.path.isfile("fichier.txt")  # True
os.path.isdir("dossier")        # True
os.path.exists("fichier.txt")   # True
```

---

## 7. Parcours Récursif

```python
import os

def parcours_repertoire(chemin, niveau=0):
    """Parcours recursif avec indentation."""
    for elem in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, elem)
        print("  " * niveau + elem)
        if os.path.isdir(chemin_complet):
            parcours_repertoire(chemin_complet, niveau + 1)

parcours_repertoire(".")
```

---

## 8. Fichiers Temporaires

```python
import tempfile

# Fichier temporaire auto-supprime
with tempfile.NamedTemporaryFile(mode="w", delete=True) as f:
    f.write("Données temporaires\n")
    f.flush()
    print(f"Fichier temporaire: {f.name}")

# Repertoire temporaire
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Repertoire: {tmpdir}")
    # Le repertoire est supprime a la sortie du bloc
```

---

## 9. Exemples Pratiques

### Compteur de Lignes

```python
def compter_lignes(fichier):
    with open(fichier, "r") as f:
        return sum(1 for _ in f)

print(f"Nombre de lignes: {compter_lignes('fichier.txt')}")
```

### Copier un Fichier

```python
def copier_fichier(source, destination):
    with open(source, "rb") as src:
        with open(destination, "wb") as dst:
            dst.write(src.read())

copier_fichier("source.txt", "destination.txt")
```

### Filtrer des Lignes

```python
def filtrer_lignes(fichier_entree, fichier_sortie, mot):
    with open(fichier_entree, "r") as entree:
        with open(fichier_sortie, "w") as sortie:
            for ligne in entree:
                if mot in ligne:
                    sortie.write(ligne)
```

---

## 10. CSV

```python
import csv

# Lire du CSV
with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Ecrire du CSV
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Age", "Ville"])
    writer.writerow(["Alice", 30, "Paris"])
    writer.writerow(["Bob", 25, "Lyon"])
```

### CSV avec Dictionnaires

```python
import csv

# Lecture
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Nom"], row["Age"])

# Ecriture
with open("output.csv", "w", encoding="utf-8") as f:
    fieldnames = ["Nom", "Age", "Ville"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Nom": "Alice", "Age": 30, "Ville": "Paris"})
```

---

## 11. JSON

```python
import json

# Lire JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)

# Ecrire JSON
data = {"nom": "Alice", "age": 30, "villes": ["Paris", "Lyon"]}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

---

## Points Clés à Retenir

| Fonction | Usage |
|----------|-------|
| `open()` | Ouvrir un fichier |
| `read()` | Lire tout |
| `readline()` | Lire une ligne |
| `readlines()` | Liste de lignes |
| `write()` | Ecrire du texte |
| `writelines()` | Ecrire liste |
| `with` | Context manager |
| `encoding` | UTF-8 par defaut |

---

## Erreurs Courantes

```python
# ERREUR: Oublier de fermer
f = open("fichier.txt", "r")
contenu = f.read()
f.close()  # Obliger!

# ERREUR: Mauvais encodage
with open("fichier.txt", "r") as f:  # Pas d'encoding specifie!
    pass

# ERREUR: Lire fichier binaire en mode texte
with open("image.png", "r") as f:  # ERREUR!
    pass
# CORRECT:
with open("image.png", "rb") as f:
    data = f.read()
```
