# Chapitre 23 : Web Development avec Flask et FastAPI

## Introduction : Pourquoi Créer des Applications Web ?

Le web est le moyen le plus courant d'accéder aux applications. Python offre deux frameworks puissants pour créer des APIs et applications web :

- **Flask** : Simple, léger, parfait pour les débutants et les petites applications
- **FastAPI** : Moderne, rapide, avec validation automatique des données

---

## 1. Flask : Les Bases

### Installation

```bash
uv sync --extra web
```

### Première Application Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bonjour, monde!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

Lancer avec :
```bash
uv run python app.py
```

### Routes et Paramètres

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur mon site!'

@app.route('/utilisateurs/<nom>')
def saluer(nom):
    return f'Bonjour {nom}!'

@app.route('/calcul/<operation>/<int:a>/<int:b>')
def calculer(operation, a, b):
    resultats = {
        'add': a + b,
        'sub': a - b,
        'mul': a * b,
        'div': a / b if b != 0 else 'Erreur'
    }
    return jsonify({'resultat': resultats.get(operation, 'Opération invalide')})
```

---

## 2. Templates Jinja2

### Structure de Templates

```
templates/
├── base.html
├── index.html
└── utilisateur.html
```

### Template de Base (base.html)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block titre %}Mon Site{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Accueil</a>
        <a href="/utilisateurs">Utilisateurs</a>
    </nav>
    
    <main>
        {% block contenu %}{% endblock %}
    </main>
</body>
</html>
```

### Template Héritant

```html
{% extends "base.html" %}

{% block titre %}Page d'Accueil{% endblock %}

{% block contenu %}
    <h1>Bienvenue!</h1>
    <p>Vous êtes sur mon site.</p>
{% endblock %}
```

### Variables et Boucles

```python
@app.route('/utilisateurs')
def utilisateurs():
    users = [
        {'id': 1, 'nom': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'nom': 'Bob', 'email': 'bob@example.com'},
    ]
    return render_template('utilisateurs.html', utilisateurs=users)
```

```html
<h1>Liste des Utilisateurs</h1>
<ul>
{% for user in utilisateurs %}
    <li>{{ user.nom }} - {{ user.email }}</li>
{% endfor %}
</ul>
```

---

## 3. Formulaires et Validation

### Formulaire Simple

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']
        # Traiter les données...
        return redirect(url_for('merci'))
    return render_template('contact.html')
```

```html
<form method="POST">
    <label for="nom">Nom:</label>
    <input type="text" id="nom" name="nom" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    
    <button type="submit">Envoyer</button>
</form>
```

---

## 4. FastAPI : Moderne et Performant

### Installation

```bash
uv sync --extra web
```

### Première API FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Mon API")

# Modèle de données
class Utilisateur(BaseModel):
    nom: str
    email: str
    age: Optional[int] = None

# Données en mémoire
utilisateurs = []

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur mon API!"}

@app.get("/utilisateurs")
def liste_utilisateurs():
    return utilisateurs

@app.post("/utilisateurs")
def creer_utilisateur(user: Utilisateur):
    utilisateurs.append(user)
    return {"message": "Utilisateur créé", "utilisateur": user}

@app.get("/utilisateurs/{user_id}")
def lire_utilisateur(user_id: int):
    if user_id < len(utilisateurs):
        return utilisateurs[user_id]
    return {"error": "Utilisateur non trouvé"}
```

Lancer avec :
```bash
uv run uvicorn app:app --reload
```

Documentation automatique : http://localhost:8000/docs

---

## 5. Modèles Pydantic

### Validation Automatique

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI()

class Produit(BaseModel):
    nom: str
    prix: float = Field(gt=0, description="Prix doit être positif")
    description: Optional[str] = None
    disponible: bool = True

class Commande(BaseModel):
    produits: List[Produit]
    email: EmailStr
    adresse: str

@app.post("/commandes")
def passer_commande(commande: Commande):
    total = sum(p.prix for p in commande.produits)
    return {
        "message": "Commande reçue",
        "total": total,
        "nombre_produits": len(commande.produits)
    }
```

---

## 6. Templates avec FastAPI

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/utilisateurs/{user_id}")
def lire_utilisateur(request: Request, user_id: int):
    user = {"id": user_id, "nom": "Alice", "email": "alice@example.com"}
    return templates.TemplateResponse("utilisateur.html", {"request": request, "user": user})
```

---

## 7. Base de Données avec SQLAlchemy

### Configuration

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./ma_base.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)
```

### CRUD Complet

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Dépendance pour la session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/utilisateurs/", response_model=dict)
def creer_utilisateur(user: UtilisateurCreate, db: Session = Depends(get_db)):
    db_user = db.query(Utilisateur).filter(Utilisateur.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email déjà enregistré")
    db_user = Utilisateur(nom=user.nom, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "nom": db_user.nom, "email": db_user.email}

@app.get("/utilisateurs/", response_model=List[dict])
def lire_utilisateurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(Utilisateur).offset(skip).limit(limit).all()
    return [{"id": u.id, "nom": u.nom, "email": u.email} for u in users]
```

---

## 8. Authentification Basique

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/profil")
def lire_profil(token: str = Depends(oauth2_scheme)):
    # Vérifier le token ici...
    return {"utilisateur": "Alice", "token": token}
```

---

## 9. Déploiement

### Avec Gunicorn

```bash
gunicorn -k uvicorn.workers.UvicornWorker app:app -b 0.0.0.0:8000
```

### Avec Docker

```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 10. Erreurs Courantes

### 1. Oublier `app.run()`

```python
# MAUVAIS
@app.route('/')
def home():
    return 'Hello'

# CORRECT
if __name__ == '__main__':
    app.run(debug=True)
```

### 2. Mauvaise organisation des routes

```python
# MAUVAIS - tout dans un fichier
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return 'Hello'

# CORRECT - une route par fonction
@app.route('/')
def index():
    return 'Hello'
```

---

## 11. Résumé

| Concept | Flask | FastAPI |
|---------|-------|---------|
| Routing | `@app.route()` | `@app.get()` |
| Templates | Jinja2 intégré | Jinja2 (install séparé) |
| Validation | Manuelle | Automatique (Pydantic) |
| Documentation | Non | Automatique (Swagger) |
| Performance | Bonne | Très bonne |

---

## Prochain Chapitre

Tu as maintenant les bases du web development ! Passons au **chapitre 25 : Machine Learning** pour apprendre à créer des modèles prédictifs.

---

*Félicitations ! Tu peux maintenant créer des applications web complètes! 🕸️*
