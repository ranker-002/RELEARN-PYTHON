"""
Exercice 20.8 - SUPPRESSION
===========================


"""


def run():
    """Fonction principale de l'exercice."""
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


# Pour tests manuels
if __name__ == "__main__":
    run()
