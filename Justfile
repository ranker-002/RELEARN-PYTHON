# Installation des dépendances
install:
    uv sync

# Installation avec outils de développement
install-dev:
    uv sync --extra dev

# Lancer les tests
test:
    uv run pytest

# Formatter le code
format:
    uv run black .

# Vérifier le code
lint:
    uv run flake8 .
    uv run mypy .

# Vérification complète (format + lint + test)
check: format lint test
    @echo "✅ Tout est OK!"

# Exécuter un fichier Python
run file:
    uv run python {{file}}

# Ouvrir un shell dans l'environnement virtuel
shell:
    uv run --with ipython ipython

# Lister les dépendances
deps:
    uv tree

# Mettre à jour les dépendances
update:
    uv sync --upgrade

# Nettoyer les caches
clean:
    rm -rf .venv __pycache__ .pytest_cache .ruff_cache build dist *.egg-info
