"""
Exercice 20.13 - COMPRESSION
============================


"""


def run():
    """Fonction principale de l'exercice."""
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


# Pour tests manuels
if __name__ == "__main__":
    run()
