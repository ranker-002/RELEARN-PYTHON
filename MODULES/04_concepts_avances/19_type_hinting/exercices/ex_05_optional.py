"""
Exercice 19.5 - OPTIONAL
========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Optional pour valeurs possibles None."""
    # Crée une fonction qui prend un nom optionnel

    def saluer(nom: Optional[str]) -> str:
        if nom is None:
            return "Bonjour, inconnu!"
        return f"Bonjour, {nom}!"

    print(saluer("Alice"))
    print(saluer(None))


# Pour tests manuels
if __name__ == "__main__":
    run()
