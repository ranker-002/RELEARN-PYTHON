"""
Exercice 19.14 - TYPE CHECKING SIMULE
=====================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Démontrer les types avec mypy."""
    # Ces déclarations seraient vérifiées par mypy

    def calculer_tva(prix: float, taux: float = 0.20) -> float:
        return prix * taux

    # mypy détecterait ces erreurs:
    # resultat: str = calculer_tva(100)  # ERREUR: float au lieu de str

    resultat: float = calculer_tva(100)
    print(f"TVA: {resultat}€")


# Pour tests manuels
if __name__ == "__main__":
    run()
