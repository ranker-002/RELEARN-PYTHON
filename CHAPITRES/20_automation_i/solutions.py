# =============================================================================
# CHAPITRE 20: AUTOMATION I - SOLUTIONS
# =============================================================================

import os
from pathlib import Path
import shutil
import subprocess
import glob
from datetime import datetime


def exercice_20_1():
    """Lister les fichiers du dossier courant avec os."""
    fichiers = os.listdir(".")
    print("Fichiers dans le dossier courant:")
    for f in fichiers:
        print(f"  - {f}")


def exercice_20_2():
    """Utiliser pathlib pour lister les fichiers."""
    dossier = Path(".")
    for element in dossier.iterdir():
        if element.is_file():
            print(f"FICHIER: {element.name}")
        elif element.is_dir():
            print(f" DOSSIER: {element.name}/")


def exercice_20_3():
    """Créer une structure de dossiers."""
    structure = Path("test_folder/subfolder1/subfolder2")
    structure.mkdir(parents=True, exist_ok=True)
    print("Dossiers créés!")


def exercice_20_4():
    """Trouver tous les fichiers Python."""
    py_files = glob.glob("*.py")
    print(f"Fichiers Python trouvés: {py_files}")


def exercice_20_5():
    """Copier un fichier avec shutil."""
    test_file = Path("test_copy.txt")
    test_file.write_text("Contenu à copier")
    shutil.copy("test_copy.txt", "test_copy_backup.txt")
    print("Fichier copié!")


def exercice_20_6():
    """Afficher les informations d'un fichier."""
    fichier = Path("test_copy.txt")
    if fichier.exists():
        print(f"Nom: {fichier.name}")
        print(f"Taille: {fichier.stat().st_size} octets")
        mtime = datetime.fromtimestamp(fichier.stat().st_mtime)
        print(f"Modifié le: {mtime}")


def exercice_20_7():
    """Renommer un fichier."""
    original = Path("test_copy.txt")
    renomme = Path("test_renomme.txt")
    if original.exists():
        original.rename(renomme)
        print(f"Renommé en {renomme.name}")


def exercice_20_8():
    """Supprimer des fichiers de test."""
    fichiers = ["test_copy_backup.txt", "test_renomme.txt"]
    for f in fichiers:
        if Path(f).exists():
            Path(f).unlink()
            print(f"Supprimé: {f}")
    
    if Path("test_folder").exists():
        shutil.rmtree("test_folder")
        print("Dossier test_folder supprimé")


def exercice_20_9():
    """Rechercher récursivement tous les fichiers .py."""
    p = Path(".")
    py_files = list(p.rglob("*.py"))
    print(f"Fichiers Python: {len(py_files)} trouvés")
    for f in py_files[:5]:
        print(f"  {f}")


def exercice_20_10():
    """Exécuter une commande système."""
    resultat = subprocess.run(["echo", "Hello from subprocess!"], 
                              capture_output=True, text=True)
    print(resultat.stdout.strip())


def exercice_20_11():
    """Organiser les fichiers par extension."""
    dossier = Path(".")
    for element in dossier.iterdir():
        if element.is_file():
            ext = element.suffix.lower()[1:] if element.suffix else "autres"
            cible = dossier / ext
            cible.mkdir(exist_ok=True)
            element.rename(cible / element.name)
            print(f"{element.name} → {ext}/")


def exercice_20_12():
    """Nettoyer les fichiers temporaires."""
    temp_files = []
    for element in Path(".").iterdir():
        if element.is_file():
            if element.name.endswith((".tmp", ".log", "~")):
                temp_files.append(element)
    
    for f in temp_files:
        print(f"Nettoyé: {f.name}")


def exercice_20_13():
    """Créer une archive zip."""
    Path("archive_test").mkdir(exist_ok=True)
    Path("archive_test/fichier1.txt").write_text("Test 1")
    Path("archive_test/fichier2.txt").write_text("Test 2")
    
    shutil.make_archive("backup_test", "zip", "archive_test")
    print("Archive backup_test.zip créée")
    
    shutil.rmtree("archive_test")


def exercice_20_14():
    """Calculer la taille totale d'un dossier."""
    def taille_dossier(dossier):
        total = 0
        for element in Path(dossier).rglob("*"):
            if element.is_file():
                total += element.stat().st_size
        return total
    
    taille = taille_dossier(".")
    print(f"Taille totale: {taille} octets ({taille / 1024:.2f} Ko)")


def exercice_20_15():
    """Système de backup avec horodatage."""
    source = Path(".")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    
    print(f"Création du backup: {backup_name}")
    shutil.make_archive(backup_name, "zip", ".")
    print(f"Backup créé: {backup_name}.zip")
    print(f"Taille: {Path(f'{backup_name}.zip').stat().st_size} octets")


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 20: AUTOMATION I - SOLUTIONS")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Solution 20.{i} ---")
        try:
            eval(f"exercice_20_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
