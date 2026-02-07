"""
Exercice 22.14 - TEST STATISTIQUE
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Faire un test statistique."""
    np.random.seed(42)
    echantillon1 = np.random.normal(100, 10, 50)
    echantillon2 = np.random.normal(105, 10, 50)

    # Test t
    t_stat, p_value = stats.ttest_ind(echantillon1, echantillon2)

    print(f"Échantillon 1: {np.mean(echantillon1):.2f}")
    print(f"Échantillon 2: {np.mean(echantillon2):.2f}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significatif: {'Oui' if p_value < 0.05 else 'Non'}")


# Pour tests manuels
if __name__ == "__main__":
    run()
