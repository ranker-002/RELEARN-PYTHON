"""
Exercice 19.6 - UNION
=====================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Union pour plusieurs types possibles."""
    # Crée une fonction qui accepte int ou str

    def afficher(valeur: Union[int, str]) -> str:
        return f"Valeur: {valeur}"

    print(afficher(42))
    print(afficher("texte"))


# Pour tests manuels
if __name__ == "__main__":
    run()
