"""
Exercice 22.5 - STATISTIQUES
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Calculer des statistiques."""
    donnees = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])

    print(f"Moyenne: {np.mean(donnees)}")
    print(f"Médiane: {np.median(donnees)}")
    print(f"Variance: {np.var(donnees)}")
    print(f"Écart-type: {np.std(donnees)}")
    print(f"Min: {np.min(donnees)}")
    print(f"Max: {np.max(donnees)}")


# Pour tests manuels
if __name__ == "__main__":
    run()
