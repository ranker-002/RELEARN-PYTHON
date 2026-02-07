"""
Exercice 15.14 - FICHIER TEMPORAIRE
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser un fichier temporaire."""
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("Donnees temporaires\n")
        print(f"Fichier: {f.name}")

    print("Fichier temporaire cree")


# Pour tests manuels
if __name__ == "__main__":
    run()
