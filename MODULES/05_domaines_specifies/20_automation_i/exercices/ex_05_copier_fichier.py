"""
Exercice 20.5 - COPIER FICHIER
==============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Copier un fichier avec shutil."""
    import shutil
    from pathlib import Path

    test_file = Path("test_copy.txt")
    test_file.write_text("Contenu à copier")

    shutil.copy("test_copy.txt", "test_copy_backup.txt")
    print("Fichier copié!")


# Pour tests manuels
if __name__ == "__main__":
    run()
