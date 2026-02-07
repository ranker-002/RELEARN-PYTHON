"""
Exercice 16.8 - MESSAGE JSON
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Serialiser messages."""
    import json

    messages = [
        {"type": "text", "contenu": "Hello"},
        {"type": "image", "url": "img.png"}
    ]

    with open("messages.json", "w") as f:
        json.dump(messages, f)


# Pour tests manuels
if __name__ == "__main__":
    run()
