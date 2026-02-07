"""
Exercice 20.9 - RECHERCHE RÉCURSIVE
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Rechercher récursivement tous les fichiers .py."""
    from pathlib import Path

    p = Path(".")
    py_files = list(p.rglob("*.py"))
    print(f"Fichiers Python: {len(py_files)} trouvés")
    for f in py_files[:5]:
        print(f"  {f}")


# Pour tests manuels
if __name__ == "__main__":
    run()
