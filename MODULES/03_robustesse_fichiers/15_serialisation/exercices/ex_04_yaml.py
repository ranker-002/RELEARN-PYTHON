"""
Exercice 16.4 - YAML
====================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lire et ecrire YAML."""
    import yaml

    data = {
        "serveur": {
            "host": "localhost",
            "port": 8080
        },
        "debug": True
    }

    with open("config.yaml", "w") as f:
        yaml.dump(data, f)

    with open("config.yaml", "r") as f:
        print(yaml.safe_load(f))


# Pour tests manuels
if __name__ == "__main__":
    run()
