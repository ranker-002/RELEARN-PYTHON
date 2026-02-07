"""
Exercice 19.12 - PROTOCOL
=========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Protocol pour interfaces."""
    def afficher(objet: Rendu) -> None:
        print(objet.render())

    img = Image(b"data")
    txt = Texte("Bonjour")

    afficher(img)
    afficher(txt)


# Pour tests manuels
if __name__ == "__main__":
    run()
