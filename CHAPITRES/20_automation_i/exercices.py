# =============================================================================
# CHAPITRE 20: AUTOMATION I - EXERCICES
# =============================================================================

# =============================================================================
# EXERCICE 20.1 - LISTER LES FICHIERS
# =============================================================================
def exercice_20_1():
    """Lister les fichiers du dossier courant avec os."""
    import os
    
    fichiers = os.listdir(".")
    print("Fichiers dans le dossier courant:")
    for f in fichiers:
        print(f"  - {f}")


# =============================================================================
# EXERCICE 20.2 - PATHLIB BASIQUE
# =============================================================================
def exercice_20_2():
    """Utiliser pathlib pour lister les fichiers."""
    from pathlib import Path
    
    dossier = Path(".")
    for element in dossier.iterdir():
        if element.is_file():
            print(f"FICHIER: {element.name}")
        elif element.is_dir():
            print(f" DOSSIER: {element.name}/")


# =============================================================================
# EXERCICE 20.3 - CRÉER DOSSIERS
# =============================================================================
def exercice_20_3():
    """Créer une structure de dossiers."""
    from pathlib import Path
    
    structure = Path("test_folder/subfolder1/subfolder2")
    structure.mkdir(parents=True, exist_ok=True)
    print("Dossiers créés!")


# =============================================================================
# EXERCICE 20.4 - CHERCHER AVEC GLOB
# =============================================================================
def exercice_20_4():
    """Trouver tous les fichiers Python."""
    import glob
    
    py_files = glob.glob("*.py")
    print(f"Fichiers Python trouvés: {py_files}")


# =============================================================================
# EXERCICE 20.5 - COPIER FICHIER
# =============================================================================
def exercice_20_5():
    """Copier un fichier avec shutil."""
    import shutil
    from pathlib import Path
    
    test_file = Path("test_copy.txt")
    test_file.write_text("Contenu à copier")
    
    shutil.copy("test_copy.txt", "test_copy_backup.txt")
    print("Fichier copié!")


# =============================================================================
# EXERCICE 20.6 - INFOS FICHIER
# =============================================================================
def exercice_20_6():
    """Afficher les informations d'un fichier."""
    from pathlib import Path
    from datetime import datetime
    
    fichier = Path("test_copy.txt")
    if fichier.exists():
        print(f"Nom: {fichier.name}")
        print(f"Taille: {fichier.stat().st_size} octets")
        mtime = datetime.fromtimestamp(fichier.stat().st_mtime)
        print(f"Modifié le: {mtime}")


# =============================================================================
# EXERCICE 20.7 - RENOMMAGE SIMPLE
# =============================================================================
def exercice_20_7():
    """Renommer un fichier."""
    from pathlib import Path
    
    original = Path("test_copy.txt")
    renomme = Path("test_renomme.txt")
    if original.exists():
        original.rename(renomme)
        print(f"Renommé en {renomme.name}")


# =============================================================================
# EXERCICE 20.8 - SUPPRESSION
# =============================================================================
def exercice_20_8():
    """Supprimer des fichiers de test."""
    import os
    from pathlib import Path
    
    fichiers = ["test_copy_backup.txt", "test_renomme.txt"]
    for f in fichiers:
        if Path(f).exists():
            Path(f).unlink()
            print(f"Supprimé: {f}")
    
    # Supprimer le dossier de test
    if Path("test_folder").exists():
        import shutil
        shutil.rmtree("test_folder")
        print("Dossier test_folder supprimé")


# =============================================================================
# EXERCICE 20.9 - RECHERCHE RÉCURSIVE
# =============================================================================
def exercice_20_9():
    """Rechercher récursivement tous les fichiers .py."""
    from pathlib import Path
    
    p = Path(".")
    py_files = list(p.rglob("*.py"))
    print(f"Fichiers Python: {len(py_files)} trouvés")
    for f in py_files[:5]:
        print(f"  {f}")


# =============================================================================
# EXERCICE 20.10 - COMMANDES SYSTÈME
# =============================================================================
def exercice_20_10():
    """Exécuter une commande système."""
    import subprocess
    
    resultat = subprocess.run(["echo", "Hello from subprocess!"], 
                              capture_output=True, text=True)
    print(resultat.stdout.strip())


# =============================================================================
# EXERCICE 20.11 - ORGANISATEUR SIMPLE
# =============================================================================
def exercice_20_11():
    """Organiser les fichiers par extension."""
    from pathlib import Path
    import os
    
    dossier = Path(".")
    for element in dossier.iterdir():
        if element.is_file():
            ext = element.suffix.lower()[1:] if element.suffix else "autres"
            cible = dossier / ext
            cible.mkdir(exist_ok=True)
            element.rename(cible / element.name)
            print(f"{element.name} → {ext}/")


# =============================================================================
# EXERCICE 20.12 - NETTOYAGE DOSSIER
# =============================================================================
def exercice_20_12():
    """Nettoyer les fichiers temporaires."""
    from pathlib import Path
    
    temp_files = []
    for element in Path(".").iterdir():
        if element.is_file():
            if element.name.endswith((".tmp", ".log", "~")):
                temp_files.append(element)
    
    for f in temp_files:
        print(f"Nettoyé: {f.name}")


# =============================================================================
# EXERCICE 20.13 - COMPRESSION
# =============================================================================
def exercice_20_13():
    """Créer une archive zip."""
    import shutil
    from pathlib import Path
    
    # Créer un dossier à archiver
    Path("archive_test").mkdir(exist_ok=True)
    Path("archive_test/fichier1.txt").write_text("Test 1")
    Path("archive_test/fichier2.txt").write_text("Test 2")
    
    shutil.make_archive("backup_test", "zip", "archive_test")
    print("Archive backup_test.zip créée")
    
    # Nettoyer
    shutil.rmtree("archive_test")


# =============================================================================
# EXERCICE 20.14 - CALCUL TAILLE DOSSIER
# =============================================================================
def exercice_20_14():
    """Calculer la taille totale d'un dossier."""
    from pathlib import Path
    
    def taille_dossier(dossier):
        total = 0
        for element in Path(dossier).rglob("*"):
            if element.is_file():
                total += element.stat().st_size
        return total
    
    # Calculer pour le dossier courant
    taille = taille_dossier(".")
    print(f"Taille totale: {taille} octets ({taille / 1024:.2f} Ko)")


# =============================================================================
# EXERCICE 20.15 - SYSTÈME DE BACKUP COMPLET
# =============================================================================
def exercice_20_15():
    """Système de backup avec horodatage."""
    import shutil
    from pathlib import Path
    from datetime import datetime
    import os
    
    source = Path(".")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    
    print(f"Création du backup: {backup_name}")
    
    # Créer l'archive
    shutil.make_archive(backup_name, "zip", ".")
    
    print(f"Backup créé: {backup_name}.zip")
    print(f"Taille: {Path(f'{backup_name}.zip').stat().st_size} octets")


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 20: AUTOMATION I")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Exercice 20.{i} ---")
        try:
            eval(f"exercice_20_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
