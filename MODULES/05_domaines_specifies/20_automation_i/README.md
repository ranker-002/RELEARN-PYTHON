# Chapitre 20 : Automation I

## Pourquoi Automatiser ?

Imaginez que vous deviez renommer 500 fichiers un par un, ou envoyer le même email à 100 personnes, ou backupper vos documents tous les jours à 3h du matin. Faire ces tâches manuellement prendrait des heures, serait ennuyeux, et surtout... nous sommes humains, donc nous ferions des erreurs.

**L'automatisation**, c'est quand on demande à l'ordinateur de faire ces tâches répétitives pour nous. L'ordinateur ne se fatigue jamais, ne fait pas d'erreurs d'inattention, et peut travailler pendant que vous dormez.

Python est parfait pour l'automatisation parce que :
- La syntaxe est simple et lisible
- Il y a beaucoup de modules intégrés pour manipuler fichiers, dossiers, processus
- On peut créer des scripts qui s'exécutent à des moments précis

Ce chapitre vous montre les outils de base pour automatiser les tâches liées aux fichiers et dossiers.

---

## Le Module `os` : Votre Assistant Système

Le module `os` est comme une passerelle vers le système d'exploitation. Il vous permet de naviguer dans les dossiers, créer des fichiers, exécuter des commandes système, et bien plus encore.

### Lister les Fichiers et Dossiers

```python
import os

# Lister le contenu d'un dossier
contenu = os.listdir(".")
print(contenu)

# Lister avec plus de détails
for element in os.listdir("."):
    chemin = os.path.join(".", element)
    if os.path.isdir(chemin):
        print(f"[DIR]  {element}")
    else:
        taille = os.path.getsize(chemin)
        print(f"[FILE] {element} ({taille} octets)")
```

**Pourquoi utiliser `os.path.join` ?** Sur Windows, les chemins utilisent des `\` (backslashes), sur Mac et Linux, ce sont des `/` (slashes). `os.path.join` s'occupe de choisir le bon séparateur pour vous.

### Naviguer dans les Dossiers

```python
import os

# Dossier courant
print(os.getcwd())

# Changer de dossier
os.chdir("/home/utilisateur/documents")

# Remonter d'un niveau
os.chdir("..")

# Aller dans un sous-dossier
os.chdir("mon_projet")
```

### Créer et Supprimer

```python
import os

# Créer un dossier
os.mkdir("mon_nouveau_dossier")

# Créer des dossiers imbriqués
os.makedirs("dossier/sous_dossier/sous_sous_dossier")

# Supprimer un fichier
os.remove("fichier.txt")

# Supprimer un dossier (vide)
os.rmdir("dossier_vide")

# Supprimer un dossier et son contenu (dangereux !)
import shutil
shutil.rmtree("dossier_a_supprimer")
```

### Informations sur les Fichiers

```python
import os
from datetime import datetime

fichier = "mon_fichier.txt"

# Est-ce un fichier ? Un dossier ?
print(f"Est fichier: {os.path.isfile(fichier)}")
print(f"Est dossier: {os.path.isdir(fichier)}")

# Taille et dates
print(f"Taille: {os.path.getsize(fichier)} octets")

# Date de dernière modification (en timestamp)
timestamp = os.path.getmtime(fichier)
date_modif = datetime.fromtimestamp(timestamp)
print(f"Dernière modification: {date_modif}")

# Date de création (peut varier selon l'OS)
timestamp_creation = os.path.getctime(fichier)
date_creation = datetime.fromtimestamp(timestamp_creation)
print(f"Date de création: {date_creation}")
```

---

## `pathlib` : La Version Moderne (Recommandée)

Depuis Python 3.4, `pathlib` offre une approche orientée objet plus élégante. Au lieu de manipuler des chaînes de caractères, vous travaillez avec des objets `Path`.

```python
from pathlib import Path

# Créer un objet Path
p = Path(".")

# Lister le contenu (avec des objets Path, pas des strings)
for element in p.iterdir():
    if element.is_dir():
        print(f"[DIR]  {element.name}")
    elif element.is_file():
        print(f"[FILE] {element.name}")

# Lister les fichiers seulement
fichiers = [f for f in p.iterdir() if f.is_file()]
print(fichiers)

# Lister les fichiers avec un motif
py_files = list(p.glob("*.py"))
print(f"Fichiers Python: {py_files}")

# Rechercher récursivement
all_py = list(p.rglob("*.py"))
print(f"Tous les Python: {all_py}")

# Créer des chemins (plus lisible !)
nouveau = p / "dossier" / "sous_dossier" / "fichier.txt"
print(nouveau)  # Affiche: dossier/sous_dossier/fichier.txt

# Propriétés utiles
print(f"Nom: {p.name}")
print(f"Extension: {p.suffix}")
print(f"Parent: {p.parent}")
print(f"Stem (sans extension): {p.stem}")

# Vérifications
print(f"Existe: {p.exists()}")
print(f"Est fichier: {p.is_file()}")
```

### Créer et Supprimer avec pathlib

```python
from pathlib import Path

# Créer un dossier
dossier = Path("nouveau_dossier")
dossier.mkdir(exist_ok=True)  # exist_ok=True: ne pas lever d'erreur si existe déjà

# Créer des dossiers imbriqués
Path("a/b/c").mkdir(parents=True, exist_ok=True)

# Créer un fichier (ne fait rien si existe déjà)
fichier = Path("test.txt")
fichier.touch()

# Supprimer un fichier
fichier.unlink()

# Supprimer un dossier vide
dossier.rmdir()

# Lire et écrire (méthodes pratiques !)
contenu = fichier.read_text()
print(contenu)

fichier.write_text("Bonjour le monde!")
```

---

## `glob` : Recherche par Motif

Le module `glob`寻找 les fichiers qui correspondent à un motif, comme dans un terminal.

```python
import glob

# Rechercher dans le dossier courant
print(glob.glob("*.py"))  # Tous les fichiers .py

# Rechercher récursivement
print(glob.glob("**/*.txt", recursive=True))

# Caractères spéciaux :
# *        = n'importe quelle séquence de caractères
# ?        = un caractère cualquiera
# [abc]    = un caractère parmi a, b, ou c
# [0-9]    = un chiffre cualquiera

# Exemples
glob.glob("*.py")           # Fichiers .py
glob.glob("file?.txt")      # file1.txt, file2.txt, mais pas file10.txt
glob.glob("file[0-9].txt")  # file0.txt à file9.txt
glob.glob("**/*.py")        # Tous les .py récursivement
```

---

## `shutil` : Opérations Avancées sur les Fichiers

`shutil` (shell utilities) offre des opérations de haut niveau, souvent utilisées avec `os`.

```python
import shutil
import os
from pathlib import Path

# Copier un fichier
shutil.copy("source.txt", "destination.txt")           # Contenu seulement
shutil.copy2("source.txt", "destination.txt")          # Contenu + métadonnées

# Copier un dossier entier (comme cp -r)
shutil.copytree("mon_dossier", "mon_dossier_backup")

# Déplacer/renommer
shutil.move("ancien_nom.txt", "nouveau_nom.txt")

# Compression
shutil.make_archive("backup", "zip", "dossier_a_sauvegarder")

# Décompression
shutil.unpack_archive("backup.zip", "dossier_extraction")
```

---

## `subprocess` : Lancer des Commandes Système

Parfois, le moyen le plus simple est de laisser le système faire le travail. `subprocess` permet de lancer des commandes comme dans un terminal.

```python
import subprocess

# Lancer une commande simple (retourne le code de sortie)
resultat = subprocess.run(["ls", "-la"])
print(f"Code de sortie: {resultat.returncode}")

# Capturer la sortie
resultat = subprocess.run(
    ["ls", "-la"],
    capture_output=True,
    text=True
)
print(resultat.stdout)
print(resultat.stderr)

# Lancer et attendre
resultat = subprocess.run(["python", "--version"], capture_output=True)
print(resultat.stdout.strip())

# Avec des arguments dynamiques (attention aux injections !)
fichier = "mon_fichier.txt"
resultat = subprocess.run(["wc", "-l", fichier], capture_output=True, text=True)
print(f"Lignes: {resultat.stdout.strip()}")

# Utiliser shell=True (dangereux si entrée utilisateur !)
# NE FAITES JAMAIS : subprocess.run(f"rm -rf {entree_utilisateur}", shell=True)
```

---

## Exemple Complet : Nettoyeur de Téléchargements

```python
from pathlib import Path
import shutil
import os
from datetime import datetime, timedelta

DOSSIER_TELECHARGEMENTS = Path.home() / "Downloads"
DOSSIER_ARCHIVE = DOSSIER_TELECHARGEMENTS / "Archive"
AGE_MAX = timedelta(days=30)

def organiser_telechargements():
    DOSSIER_TELECHARGEMENTS.mkdir(exist_ok=True)
    DOSSIER_ARCHIVE.mkdir(exist_ok=True)
    
    # Catégories de fichiers
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx"],
        "Archives": [".zip", ".tar", ".gz", ".rar"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Scripts": [".py", ".sh", ".js"],
    }
    
    for fichier in DOSSIER_TELECHARGEMENTS.iterdir():
        if fichier.is_file():
            deplace = False
            
            # Vérifier l'âge
            age = datetime.now() - datetime.fromtimestamp(fichier.stat().st_mtime)
            if age < AGE_MAX:
                continue  # Fichier récent, on garde
            
            # Catégoriser
            for categorie, extensions in categories.items():
                if fichier.suffix.lower() in extensions:
                    cat_folder = DOSSIER_TELECHARGEMENTS / categorie
                    cat_folder.mkdir(exist_ok=True)
                    fichier.rename(cat_folder / fichier.name)
                    print(f"→ {categorie}: {fichier.name}")
                    deplace = True
                    break
            
            # Fichier non catégorisé → Archive
            if not deplace:
                fichier.rename(DOSSIER_ARCHIVE / fichier.name)
                print(f"→ Archive: {fichier.name}")

if __name__ == "__main__":
    organiser_telechargements()
```

---

## Erreurs Courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| `FileNotFoundError` | Le fichier/dossier n'existe pas | Vérifier avec `os.path.exists()` |
| `PermissionError` | Pas les droits nécessaires | Vérifier les permissions du fichier |
| `IsADirectoryError` | Essayer de supprimer un dossier comme un fichier | Utiliser `os.rmdir()` ou `shutil.rmtree()` |
| `FileExistsError` | Trying to create a file that already exists | Utiliser `exist_ok=True` avec `mkdir()` |
| `WindowsError` | Opération non supportée sur Windows | Vérifier les caractères spéciaux dans les noms |

---

## Résumé

| Module | Usage Principal |
|--------|-----------------|
| `os` | Opérations système de base |
| `pathlib` | Manipulation orientée objet des chemins |
| `glob` | Recherche par motif |
| `shutil` | Opérations de haut niveau (copie, move, archive) |
| `subprocess` | Lancer des commandes système |

---

## Exercices Pratiques

1. **Nettoyeur de bureau** : Créer un script qui organise les fichiers du bureau par type (images, documents, etc.)

2. **Sauvegarde automatique** : Créer un système de backup qui copie des dossiers importants vers un autre emplacement avec horodatage

3. **Renommeur intelligent** : Un script qui renomme les fichiers en minuscule, remplace les espaces par des tirets, et ajoute un préfixe date

4. **监控系统** : Surveiller un dossier et alerter quand de nouveaux fichiers apparaissent

---

## Chapitre Suivant

Maintenant que vous savez manipuler les fichiers et dossiers automatiquement, passons au [Chapitre 21: Web Scraping](21_web_scraping/README.md) où nous apprendrons à extraire des données du web automatiquement.
