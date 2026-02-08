"""
Exercice 16.10 - VALIDATION JSON
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Valider JSON avec schema."""
    import json

    schema = {
        "type": "object",
        "properties": {
            "nom": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["nom"]
    }

    data = {"nom": "Alice", "age": 30}
    # Validation simplifiee
    for key in schema["required"]:
        if key not in data:
            print(f"Erreur: {key} requis")
            return
    print("Valide!")


# Pour tests manuels
if __name__ == "__main__":
    run()
