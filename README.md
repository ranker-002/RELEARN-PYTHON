# Python Mastery - De Débutant à Expert en Intelligence Artificielle

## Bienvenue dans votre parcours d'apprentissage Python

Ce projet est conçu pour vous accompagner d'un niveau débutant jusqu'à une expertise solide en Python, en passant par tous les concepts essentiels et en culminant avec une spécialisation en Intelligence Artificielle.

---

## 🗺️ Structure du Parcours

### Phase 1: Fondations (Chapitres 1-4)
*Comprendre les bases du langage*

| Chapitre | Titre | Objectif |
|----------|-------|----------|
| 01 | Premiers Pas | Installer Python, configurer VS Code, écrire votre premier script |
| 02 | Variables & Types | Manipuler les types de données fondamentaux |
| 03 | Opérateurs | Effectuer des calculs et comparisons |
| 04 | Contrôle de Flux | Prendre des décisions dans votre code |

### Phase 2: Structures de Données (Chapitres 5-7)
*Organiser et manipuler des collections*

| Chapitre | Titre | Objectif |
|----------|-------|----------|
| 05 | Boucles | Répéter des actions efficacement |
| 06 | Listes & Tuples | Stocker des séquences ordonnées |
| 07 | Dictionnaires & Sets | Utiliser des associations clé-valeur |

### Phase 3: Fonctions & Modularité (Chapitres 8-10)
*Écrire du code réutilisable et organisé*

| Chapitre | Titre | Objectif |
|----------|-------|----------|
| 08 | Fonctions | Créer des blocs de code réutilisables |
| 09 | Arguments Avancés | Maîtriser les paramètres flexibles |
| 10 | Modules & Packages | Organiser et importer du code |

### Phase 4: Programmation Orientée Objet (Chapitres 11-13)
*Modéliser des objets du monde réel*

| Chapitre | Titre | Objectif |
|----------|-------|----------|
| 11 | Classes & Objets | Définir vos propres types de données |
| 12 | Héritage & Polymorphisme | Créer des relations entre classes |
| 13 | Propriétés & Méthodes Spéciales | Person le comportement des objets |

### Phase 5: Gestion des Erreurs & Fichiers (Chapitres 14-16)
*Manipuler les entrées/sorties robustement*

| Chapitre | Titre | Objectif |
|----------|-------|----------|
| 14 | Exceptions | Gérer les erreurs gracieusement |
| 15 | Fichiers I/O | Lire et écrire des fichiers |
| 16 | Serialisation | Stocker et partager des données |

### Phase 6: Concepts Avancés (Chapitres 17-19)
*Techniques expertes*

| Chapitre | Titre | Objectif |
|----------|-------|----------|
| 17 | Décorateurs & Générateurs | Patterns avancés |
| 18 | Programmation Concurrente | Paralléliser les tâches |
| 19 | Type Hinting | Annotations de types |

### Phase 7: Domaines Spécialisés (Chapitres 20-26)
*Applications professionnelles*

| Chapitre | Domaine | Contenu |
|----------|---------|---------|
| 20 | Automation | Selenium, APIs, emails |
| 21 | Web Scraping | BeautifulSoup, Scrapy |
| 22 | Data Science | NumPy, Pandas |
| 23 | Visualisation | Matplotlib, Seaborn |
| 24 | Web Dev | Flask, FastAPI |
| 25 | Machine Learning | Scikit-learn |
| 26 | Deep Learning | PyTorch |

---

## 🚀 Démarrage Rapide

### 1. Installation

```bash
# Cloner ou télécharger le projet
cd PYTHON_MASTRY

# Lancer l'installation des dépendances
./install.sh

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows
```

### 2. Configuration VS Code

1. Ouvrir le dossier dans VS Code
2. Installer l'extension "Python" (Microsoft)
3. Sélectionner l'interpréteur: `venv/bin/python`
4. Installer les extensions recommandées:
   - Pylance
   - Jupyter
   - AutoDocstring

### 3. Commencer le Parcours

```bash
# Ouvrir le premier chapitre
cd CHAPITRES/01_premiers_pas
cat README.md

# Lire les exercices
cat exercices.py

# Pratiquer dans le dossier EXERCICES/projets/
```

---

## 📚 Structure des Chapitres

Chaque chapitre suit cette structure:

```
CHAPITRE_XX/
├── README.md              # Théorie + exemples
├── exercices.py           # Énoncés vierges
├── solutions.py           # Corrections commentées
├── exemples/              # Scripts supplémentaires
└── verification.py       # Tests optionnels
```

---

## 📊 Suivi de Progression

Editez le fichier `progres_apprentissage.md` pour suivre votre avancement:

```markdown
## Votre Progression

### Phase 1: Fondations
- [x] Chapitre 1: Premiers Pas
- [ ] Chapitre 2: Variables & Types
- [ ] Chapitre 3: Opérateurs
- [ ] Chapitre 4: Contrôle de Flux
```

---

## 🎯 Projets par Niveau

### Débutant
- Calculatrice interactive
- Convertisseur de devises
- Générateur de mots de passe

### Amateur
- Todo list CLI
- Gestionnaire de contacts
- Analyseur de texte

### Intermédiaire
- Jeu RPG textuel
- Système de blog avec sauvegardes
- Parser de configuration

### Avancé
- API REST complète
- Bot Discord
- Scraper intelligent

### Expert
- Dashboard Data Science
- Système de recommandation
- Classification d'images IA

---

## 📦 Dépendances par Phase

```bash
# Phase 1-4: Core
pip install numpy pandas matplotlib

# Phase 5-6: Avancé
pip install pytest black flake8 mypy

# Phase 7: Spécialisations
pip install requests beautifulsoup4 selenium
pip install scikit-learn torch torchvision
pip install flask fastapi uvicorn openpyxl pillow
```

---

## 📖 Conventions de Code

### Nommage
- **Variables/Fonctions**: `snake_case` (ex: `calculate_total`, `user_name`)
- **Classes**: `PascalCase` (ex: `BankAccount`, `GamePlayer`)
- **Constantes**: `UPPER_SNAKE_CASE` (ex: `MAX_CONNECTIONS`)

### Commentaires
- Comments en **français** acceptés
- Docstrings pour toutes les fonctions publiques
- Expliquer le "pourquoi", pas le "quoi"

### Style
- Suivre PEP 8
- Longueur de ligne max: 88 caractères (Black)
- Type hints recommandés à partir du Chapitre 19

---

## 🆘 Aide et Ressources

### Si vous êtes bloqué

1. Relire la section "Points Clés à Retenir" du chapitre
2. Examiner les exemples dans `exemples/`
3. Consulter la solution dans `solutions/`
4. Utiliser `verification.py` pour valider votre code

### Ressources Externes
- [Documentation Python](https://docs.python.org/fr/3/)
- [Real Python](https://realpython.com/)
- [Stack Overflow](https://stackoverflow.com/)

---

## 📝 Licence

Ce projet est fait pour l'apprentissage personnel. Partagez-le librement !

---

**Bonne chance dans votre apprentissage Python ! 🐍