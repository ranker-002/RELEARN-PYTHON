# =============================================================================
# CHAPITRE 24: WEB DEVELOPMENT - SOLUTIONS
# =============================================================================
# Niveau: INTERMÉDIAIRE
# Corrections commentées pour chaque exercice
# =============================================================================

# =============================================================================
# EXERCICE 24.1 - PREMIÈRE APPLICATION FLASK
# =============================================================================
def exercice_24_1():
    """
    Solution de l'exercice 24.1
    Première application Flask basique.
    """
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Bonjour Flask!'

    print("Application créée. Lancez avec: uv run python app.py")
    print(" puis ouvrez http://localhost:5000")


# =============================================================================
# EXERCICE 24.2 - ROUTES AVEC PARAMÈTRES
# =============================================================================
def exercice_24_2():
    """
    Solution de l'exercice 24.2
    Routes avec paramètres dynamiques.
    """
    from flask import Flask

    app = Flask(__name__)

    @app.route('/bonjour/<nom>')
    def bonjour(nom):
        return f'Bonjour {nom}!'

    @app.route('/au-revoir/<nom>')
    def aurevoir(nom):
        return f'Au revoir {nom}!'

    print("Routes créées.")


# =============================================================================
# EXERCICE 24.3 - ROUTES MULTIPLES
# =============================================================================
def exercice_24_3():
    """
    Solution de l'exercice 24.3
    Calculatrice simple.
    """
    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route('/add/<int:a>/<int:b>')
    def add(a, b):
        return jsonify({'resultat': a + b})

    @app.route('/mul/<int:a>/<int:b>')
    def mul(a, b):
        return jsonify({'resultat': a * b})

    @app.route('/puissance/<int:a>/<int:b>')
    def puissance(a, b):
        return jsonify({'resultat': a ** b})

    print("Calculatrice prête: /add/5/3, /mul/4/5, /puissance/2/8")


# =============================================================================
# EXERCICE 24.4 - TEMPLATE DE BASE
# =============================================================================
def exercice_24_4():
    """
    Solution de l'exercice 24.4
    Template de base HTML.
    """
    template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block titre %}Mon Site{% endblock %}</title>
    <style>
        nav { background: #333; padding: 1rem; }
        nav a { color: white; margin-right: 1rem; text-decoration: none; }
        main { padding: 2rem; }
        footer { background: #eee; padding: 1rem; text-align: center; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Accueil</a>
        <a href="/apropos">À propos</a>
        <a href="/contact">Contact</a>
    </nav>
    <main>
        {% block contenu %}{% endblock %}
    </main>
    <footer>
        &copy; 2024 Mon Site
    </footer>
</body>
</html>"""
    print("Template base.html créé:")
    print(template)


# =============================================================================
# EXERCICE 24.5 - TEMPLATE AVEC VARIABLES
# =============================================================================
def exercice_24_5():
    """
    Solution de l'exercice 24.5
    Template avec variables.
    """
    from flask import Flask, render_template_string

    app = Flask(__name__)

    template = """
{% extends "base.html" %}

{% block contenu %}
    <h1>Profil Utilisateur</h1>
    <ul>
        <li><strong>Nom:</strong> {{ user.nom }}</li>
        <li><strong>Âge:</strong> {{ user.age }} ans</li>
        <li><strong>Ville:</strong> {{ user.ville }}</li>
    </ul>
{% endblock %}
"""

    user = {"nom": "Alice", "age": 30, "ville": "Paris"}

    @app.route('/')
    def profil():
        return render_template_string(template, user=user)

    print("Template avec variables créé.")


# =============================================================================
# EXERCICE 24.6 - BOUCLE DANS TEMPLATE
# =============================================================================
def exercice_24_6():
    """
    Solution de l'exercice 24.6
    Tableau de produits.
    """
    from flask import Flask, render_template_string

    app = Flask(__name__)

    template = """
<h1>Catalogue Produits</h1>
<table border="1">
    <thead>
        <tr>
            <th>Nom</th>
            <th>Prix</th>
        </tr>
    </thead>
    <tbody>
    {% for produit in produits %}
        <tr>
            <td>{{ produit.nom }}</td>
            <td>{{ produit.prix }} €</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
"""

    produits = [
        {"nom": "Ordinateur", "prix": 999},
        {"nom": "Souris", "prix": 29},
        {"nom": "Clavier", "prix": 79}
    ]

    @app.route('/')
    def catalogue():
        return render_template_string(template, produits=produits)

    print("Template avec boucle créé.")


# =============================================================================
# EXERCICE 24.7 - FORMULAIRE SIMPLE
# =============================================================================
def exercice_24_7():
    """
    Solution de l'exercice 24.7
    Formulaire de contact.
    """
    form_html = """
<form method="POST" action="/contact">
    <div>
        <label for="nom">Nom:</label>
        <input type="text" id="nom" name="nom" required>
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>
    <div>
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>
    <button type="submit">Envoyer</button>
</form>
"""
    print("Formulaire créé:")
    print(form_html)


# =============================================================================
# EXERCICE 24.8 - PREMIÈRE API FASTAPI
# =============================================================================
def exercice_24_8():
    """
    Solution de l'exercice 24.8
    Première API FastAPI.
    """
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def lire_racine():
        return {"message": "Bienvenue sur l'API"}

    @app.get("/ping")
    def ping():
        return {"message": "pong"}

    print("API FastAPI créée. Lancez avec: uv run uvicorn app:app --reload")


# =============================================================================
# EXERCICE 24.9 - MODÈLE PYDANTIC
# =============================================================================
def exercice_24_9():
    """
    Solution de l'exercice 24.9
    Modèle Pydantic avec validation.
    """
    from pydantic import BaseModel, EmailStr, Field

    class Personne(BaseModel):
        nom: str
        age: int = Field(gt=0, lt=150)
        email: EmailStr

    # Test
    try:
        p = Personne(nom="Alice", age=30, email="alice@example.com")
        print(f"✓ Personne créée: {p}")
    except Exception as e:
        print(f"✗ Erreur de validation: {e}")


# =============================================================================
# EXERCICE 24.10 - CRUD COMPLET
# =============================================================================
def exercice_24_10():
    """
    Solution de l'exercice 24.10
    CRUD complet pour todos.
    """
    from fastapi import FastAPI
    from pydantic import BaseModel
    from typing import Optional, List

    app = FastAPI()

    class Todo(BaseModel):
        titre: str
        complet: bool = False

    todos = []

    @app.get("/todos", response_model=List[dict])
    def liste_todos():
        return [{"id": i, "titre": t.titre, "complet": t.complet} for i, t in enumerate(todos)]

    @app.post("/todos", response_model=dict)
    def creer_todo(todo: Todo):
        todos.append(todo)
        return {"id": len(todos) - 1, "titre": todo.titre, "complet": todo.complet}

    print("CRUD Todos créé.")


# =============================================================================
# EXERCICE 24.11 - API REST PRODUITS
# =============================================================================
def exercice_24_11():
    """
    Solution de l'exercice 24.11
    API catalogue de produits.
    """
    from fastapi import FastAPI
    from pydantic import BaseModel
    from typing import List, Optional

    app = FastAPI()

    class Produit(BaseModel):
        nom: str
        prix: float
        stock: int

    produits = []

    @app.get("/produits", response_model=List[dict])
    def liste_produits():
        return [{"id": i, **p.dict()} for i, p in enumerate(produits)]

    @app.post("/produits", response_model=dict)
    def creer_produit(produit: Produit):
        produits.append(produit)
        return {"id": len(produits) - 1, **produit.dict()}

    @app.get("/produits/{id}", response_model=dict)
    def lire_produit(id: int):
        if id < len(produits):
            return {"id": id, **produits[id].dict()}
        return {"error": "Produit non trouvé"}

    print("API Produits créée.")


# =============================================================================
# EXERCICE 24.12 - AUTHENTIFICATION SIMPLE
# =============================================================================
def exercice_24_12():
    """
    Solution de l'exercice 24.12
    Route protégée avec token.
    """
    from fastapi import Depends, FastAPI
    from fastapi.security import OAuth2PasswordBearer

    app = FastAPI()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @app.get("/protected")
    def route_protegee(token: str = Depends(oauth2_scheme)):
        return {"utilisateur": "Alice", "token": token}

    @app.post("/token")
    def token_dummy():
        return {"access_token": "fake-token"}

    print("Route protégée créée. Token requis.")


# =============================================================================
# EXERCICE 24.13 - TEMPLATE HÉRITÉ
# =============================================================================
def exercice_24_13():
    """
    Solution de l'exercice 24.13
    Structure de templates avec héritage.
    """
    base_html = """<!DOCTYPE html>
<html>
<head><title>{% block titre %}Mon Site{% endblock %}</title></head>
<body>
    <nav>Accueil | À propos | Contact</nav>
    <main>{% block contenu %}{% endblock %}</main>
</body>
</html>"""

    index_html = """{% extends "base.html" %}
{% block titre %}Accueil{% endblock %}
{% block contenu %}<h1>Bienvenue!</h1>{% endblock %}"""

    about_html = """{% extends "base.html" %}
{% block titre %}À propos{% endblock %}
{% block contenu %}<h1>À propos de nous</h1>{% endblock %}"""

    print("Templates créés: base.html, index.html, about.html")


# =============================================================================
# EXERCICE 24.14 - API AVEC BASE DE DONNÉES
# =============================================================================
def exercice_24_14():
    """
    Solution de l'exercice 24.14
    API avec SQLAlchemy.
    """
    from fastapi import FastAPI, Depends, HTTPException
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, Session
    from pydantic import BaseModel
    from typing import List

    DATABASE_URL = "sqlite:///./livres.db"

    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, bind=engine)
    Base = declarative_base()

    class Livre(Base):
        __tablename__ = "livres"
        id = Column(Integer, primary_key=True, index=True)
        titre = Column(String, index=True)
        auteur = Column(String)
        annee = Column(Integer)

    Base.metadata.create_all(bind=engine)

    app = FastAPI()

    class LivreCreate(BaseModel):
        titre: str
        auteur: str
        annee: int

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.post("/livres/", response_model=dict)
    def creer_livre(livre: LivreCreate, db: Session = Depends(get_db)):
        db_livre = Livre(**livre.dict())
        db.add(db_livre)
        db.commit()
        db.refresh(db_livre)
        return {"id": db_livre.id, **livre.dict()}

    @app.get("/livres/", response_model=List[dict])
    def liste_livres(db: Session = Depends(get_db)):
        return [{"id": l.id, "titre": l.titre, "auteur": l.auteur, "annee": l.annee} for l in db.query(Livre).all()]

    print("API Livres avec BDD créée.")


# =============================================================================
# EXERCICE 24.15 - PROJET: BLOG COMPLET
# =============================================================================
def exercice_24_15():
    """
    Solution de l'exercice 24.15
    Mini-blog avec Flask.
    """
    from flask import Flask, render_template_string, request, redirect, url_for

    app = Flask(__name__)

    base_html = """
<!DOCTYPE html>
<html>
<head>
    <title>{% block titre %}Mon Blog{% endblock %}</title>
    <style>
        body { font-family: Arial; margin: 2rem; }
        article { border: 1px solid #ddd; padding: 1rem; margin: 1rem 0; }
        nav a { margin-right: 1rem; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Accueil</a>
        <a href="/nouveau">Nouvel Article</a>
    </nav>
    {% block contenu %}{% endblock %}
</body>
</html>
"""

    articles = []

    @app.route('/')
    def liste():
        return render_template_string("""
{% extends "base.html" %}
{% block contenu %}
    <h1>Articles</h1>
    {% for article in articles %}
        <article>
            <h2>{{ article.titre }}</h2>
            <p>{{ article.contenu }}</p>
            <small>{{ article.date }}</small>
        </article>
    {% endfor %}
{% endblock %}
""", articles=articles)

    @app.route('/nouveau', methods=['GET', 'POST'])
    def nouveau():
        if request.method == 'POST':
            titre = request.form['titre']
            contenu = from flask import request
            from datetime import datetime
            articles.append({
                'titre': titre,
                'contenu': contenu,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M')
            })
            return redirect(url_for('liste'))
        return render_template_string("""
{% extends "base.html" %}
{% block contenu %}
    <h1>Nouvel Article</h1>
    <form method="POST">
        <input name="titre" placeholder="Titre" required><br><br>
        <textarea name="contenu" placeholder="Contenu" rows="5" required></textarea><br><br>
        <button type="submit">Publier</button>
    </form>
{% endblock %}
""")

    print("Blog créé. Lancez l'application et accédez à /nouveau.")
