"""
Exercice 20.14 - CALCUL TAILLE DOSSIER
======================================


"""


def run():
    """Fonction principale de l'exercice."""
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


# Pour tests manuels
if __name__ == "__main__":
    run()
