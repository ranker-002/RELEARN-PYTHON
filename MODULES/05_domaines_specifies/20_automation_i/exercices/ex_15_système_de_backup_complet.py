"""
Exercice 20.15 - SYSTÈME DE BACKUP COMPLET
==========================================


"""


def run():
    """Fonction principale de l'exercice."""
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


# Pour tests manuels
if __name__ == "__main__":
    run()
