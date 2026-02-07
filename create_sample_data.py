#!/usr/bin/env python3
"""
Script pour créer les données example pour tous les projets.
Génère des fichiers de données réalistes pour chaque domaine.
"""

import json
import csv
from pathlib import Path
from datetime import datetime, timedelta
import random


def create_sample_files():
    """Crée les fichiers example pour tous les projets."""
    base_path = Path(__file__).parent / "PROJETS"
    
    print("\n=== Création des données example ===\n")
    
    created = 0
    
    for module_dir in sorted(base_path.iterdir()):
        if not module_dir.is_dir():
            continue
        
        for project_dir in sorted(module_dir.iterdir()):
            if not project_dir.is_dir():
                continue
            
            sample_dir = project_dir / "data" / "sample"
            sample_dir.mkdir(parents=True, exist_ok=True)
            
            module_name = module_dir.name
            project_name = project_dir.name
            
            # Créer les fichiers selon le type de projet
            files = create_module_samples(module_name, project_name, sample_dir)
            
            if files:
                for f in files:
                    print(f"  ✅ {project_name}/{f}")
                created += len(files)
    
    print(f"\n=== {created} fichiers créés ===\n")


def create_module_samples(module_name: str, project_name: str, output_dir: Path) -> list[str]:
    """Crée les fichiers pour un module spécifique."""
    files = []
    
    if "web_scraping" in module_name or "automation" in module_name:
        # RSS feeds, config files
        if "aggregateur" in project_name or "rss" in project_name.lower():
            files.extend(create_rss_sample(output_dir))
        files.extend(create_json_config(output_dir))
        
    elif "data_science" in module_name or "visualisation" in module_name:
        # CSV data files
        files.extend(create_csv_samples(output_dir, module_name))
        
    elif "web_dev" in module_name:
        # JSON data
        files.extend(create_api_samples(output_dir))
        
    elif "machine_learning" in module_name or "deep_learning" in module_name:
        # CSV pour ML
        files.extend(create_ml_samples(output_dir))
        
    elif "robustesse" in module_name:
        # Various file formats
        files.extend(create_file_samples(output_dir))
        
    else:
        # Default JSON
        files.extend(create_json_config(output_dir))
    
    return files


def create_rss_sample(output_dir: Path) -> list[str]:
    """Crée des exemples de flux RSS."""
    files = []
    
    # RSS Le Monde style
    rss_lemonde = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Le Monde - Technologie</title>
    <link>https://www.lemonde.fr/technologie/</link>
    <description>Actualités technologie du Monde</description>
    <language>fr</language>
    <lastBuildDate>Sat, 07 Feb 2026 10:30:00 +0000</lastBuildDate>
    
    <item>
      <title>Intelligence Artificielle : Les avancées de 2026</title>
      <link>https://www.lemonde.fr/technologie/article/2026/02/07/ia-avancees</link>
      <description>L'intelligence artificielle continue de transformer notre quotidien avec des innovations majeures...</description>
      <pubDate>Sat, 07 Feb 2026 09:00:00 +0000</pubDate>
      <guid isPermaLink="false">lemonde-tech-20260207-001</guid>
      <category>Technologie</category>
    </item>
    
    <item>
      <title>Python 3.14 : Nouvelles fonctionnalités</title>
      <link>https://www.lemonde.fr/technologie/article/2026/02/07/python-3-14</link>
      <description>La nouvelle version de Python apporte des performances améliorées...</description>
      <pubDate>Fri, 06 Feb 2026 14:30:00 +0000</pubDate>
      <guid isPermaLink="false">lemonde-tech-20260206-002</guid>
      <category>Programmation</category>
    </item>
    
    <item>
      <title>Crypto : Le Bitcoin dépasse les 100 000 euros</title>
      <link>https://www.lemonde.fr/economie/article/2026/02/07/bitcoin-100000</link>
      <description>La cryptomonnaie atteint de nouveaux sommets...</description>
      <pubDate>Fri, 06 Feb 2026 11:00:00 +0000</pubDate>
      <guid isPermaLink="false">lemonde-eco-20260206-003</guid>
      <category>Economie</category>
    </item>
  </channel>
</rss>'''
    
    path = output_dir / "le_monde_tech.xml"
    path.write_text(rss_lemonde, encoding='utf-8')
    files.append("le_monde_tech.xml")
    
    # RSS GitHub Blog
    rss_github = '''<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>GitHub Blog</title>
  <subtitle>News, ideas, and perspective from GitHub.</subtitle>
  <link href="https://github.blog/" rel="alternate"/>
  <link href="https://github.blog/feed/" rel="self"/>
  <id>https://github.blog/</id>
  <updated>2026-02-07T10:30:00Z</updated>
  
  <entry>
    <title>GitHub Actions: Nouvelles fonctionnalités CI/CD</title>
    <link href="https://github.blog/2026-02-07-actions-update"/>
    <id>tag:github.com,2008:entry/12345</id>
    <published>2026-02-07T09:00:00Z</published>
    <updated>2026-02-07T09:00:00Z</updated>
    <summary>GitHub améliore ses workflows CI/CD avec de nouvelles fonctionnalités...</summary>
  </entry>
  
  <entry>
    <title>Copilot: 50% des développeurs l'utilisent</title>
    <link href="https://github.blog/2026-02-06-copilot-stats"/>
    <id>tag:github.com,2008:entry/12344</id>
    <published>2026-02-06T14:00:00Z</published>
    <updated>2026-02-06T14:00:00Z</updated>
    <summary>Plus de la moitié des développeurs utilisent désormais Copilot...</summary>
  </entry>
</feed>'''
    
    path = output_dir / "github_blog.xml"
    path.write_text(rss_github, encoding='utf-8')
    files.append("github_blog.xml")
    
    return files


def create_json_config(output_dir: Path) -> list[str]:
    """Crée des fichiers de configuration JSON."""
    files = []
    
    # Subscriptions
    subscriptions = {
        "abonnements": [
            {
                "nom": "Le Monde - Technologie",
                "url": "https://example.com/tech.xml",
                "categorie": "technologie"
            },
            {
                "nom": "GitHub Blog",
                "url": "https://example.com/github.xml",
                "categorie": "programmation"
            },
            {
                "nom": "Science & Vie",
                "url": "https://example.com/science.xml",
                "categorie": "science"
            }
        ],
        "filtres": {
            "mots_cles_inclure": [],
            "mots_cles_exclure": ["publicité", "sponsorisé", "abonnement"]
        },
        "preferences": {
            "articles_par_page": 10,
            "langue": ["fr", "en"],
            "cache_duree_heures": 1
        }
    }
    
    path = output_dir / "subscriptions.json"
    path.write_text(json.dumps(subscriptions, indent=2, ensure_ascii=False), encoding='utf-8')
    files.append("subscriptions.json")
    
    return files


def create_csv_samples(output_dir: Path, module_name: str) -> list[str]:
    """Crée des fichiers CSV pour data science."""
    files = []
    
    # Titanic style dataset ( Machine Learning classic)
    titanic_path = output_dir / "titanic_sample.csv"
    with open(titanic_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'])
        
        passengers = [
            [1, 0, 3, 'Braund, Mr. Owen Harris', 'male', 22, 1, 0, 7.25, 'S'],
            [2, 1, 1, 'Cumings, Mrs. John Bradley', 'female', 38, 1, 0, 71.28, 'C'],
            [3, 1, 3, 'Heikkinen, Miss. Laina', 'female', 26, 0, 0, 7.92, 'S'],
            [4, 1, 1, 'Futrelle, Mrs. Jacques Heath', 'female', 35, 1, 0, 53.10, 'S'],
            [5, 0, 3, 'Allen, Mr. William Henry', 'male', 35, 0, 0, 8.05, 'S'],
            [6, 0, 3, 'Moran, Mr. James', 'male', None, 0, 0, 8.46, 'Q'],
            [7, 0, 1, 'McCarthy, Mr. Timothy J', 'male', 54, 0, 0, 51.86, 'S'],
            [8, 1, 3, 'Palsson, Master. Gosta Leonard', 'male', 2, 3, 1, 21.08, 'S'],
            [9, 1, 1, 'Johnson, Mrs. Oscar W', 'female', 27, 0, 2, 11.13, 'S'],
            [10, 1, 2, 'Nasser, Mrs. Nicholas', 'female', 14, 1, 0, 30.07, 'C'],
        ]
        writer.writerows(passengers)
    files.append("titanic_sample.csv")
    
    # Housing prices
    housing_path = output_dir / "housing_sample.csv"
    with open(housing_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Id', 'MSSubClass', 'LotArea', 'YearBuilt', 'GarageCars', 'GarageArea', 'GrLivArea', 'TotalBsmtSF', 'SalePrice'])
        
        houses = [
            [1, 60, 8450, 2003, 2, 548, 856, 856, 208500],
            [2, 20, 9600, 1976, 2, 420, 1262, 1262, 181500],
            [3, 60, 11250, 2001, 2, 608, 920, 920, 223500],
            [4, 70, 9550, 1915, 2, 540, 961, 0, 140000],
            [5, 60, 14260, 2000, 2, 572, 1140, 1140, 250000],
            [6, 50, 14115, 1993, 2, 440, 1077, 1077, 143000],
            [7, 20, 10084, 2004, 2, 484, 1256, 1256, 307000],
            [8, 60, 10382, 2006, 2, 504, 1106, 1106, 200000],
            [9, 50, 6120, 1962, 1, 264, 729, 0, 129000],
            [10, 190, 11645, 2007, 3, 850, 1750, 1750, 345000],
        ]
        writer.writerows(houses)
    files.append("housing_sample.csv")
    
    return files


def create_api_samples(output_dir: Path) -> list[str]:
    """Crée des fichiers JSON pour API."""
    files = []
    
    # Users API sample
    users = {
        "users": [
            {
                "id": 1,
                "nom": "Dupont",
                "prenom": "Jean",
                "email": "jean.dupont@email.com",
                "role": "admin",
                "actif": True
            },
            {
                "id": 2,
                "nom": "Martin",
                "prenom": "Marie",
                "email": "marie.martin@email.com",
                "role": "utilisateur",
                "actif": True
            },
            {
                "id": 3,
                "nom": "Bernard",
                "prenom": "Pierre",
                "email": "pierre.bernard@email.com",
                "role": "utilisateur",
                "actif": False
            }
        ]
    }
    
    path = output_dir / "users_sample.json"
    path.write_text(json.dumps(users, indent=2, ensure_ascii=False), encoding='utf-8')
    files.append("users_sample.json")
    
    # Products sample
    products = {
        "produits": [
            {"id": 1, "nom": "Ordinateur portable", "prix": 999.99, "stock": 50},
            {"id": 2, "nom": "Souris sans fil", "prix": 29.99, "stock": 200},
            {"id": 3, "nom": "Clavier mécanique", "prix": 89.99, "stock": 75},
            {"id": 4, "nom": "Écran 27 pouces", "prix": 349.99, "stock": 30},
            {"id": 5, "nom": "Casque audio", "prix": 149.99, "stock": 100},
        ]
    }
    
    path = output_dir / "products_sample.json"
    path.write_text(json.dumps(products, indent=2, ensure_ascii=False), encoding='utf-8')
    files.append("products_sample.json")
    
    return files


def create_ml_samples(output_dir: Path) -> list[str]:
    """Crée des fichiers pour machine learning."""
    files = []
    
    # Iris dataset style
    iris_path = output_dir / "iris_sample.csv"
    with open(iris_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
        
        iris_data = [
            [5.1, 3.5, 1.4, 0.2, 'setosa'],
            [4.9, 3.0, 1.4, 0.2, 'setosa'],
            [4.7, 3.2, 1.3, 0.2, 'setosa'],
            [7.0, 3.2, 4.7, 1.4, 'versicolor'],
            [6.4, 3.2, 4.5, 1.5, 'versicolor'],
            [6.9, 3.1, 4.9, 1.5, 'versicolor'],
            [6.3, 3.3, 6.0, 2.5, 'virginica'],
            [5.8, 2.7, 5.1, 1.9, 'virginica'],
            [7.1, 3.0, 5.9, 2.1, 'virginica'],
            [6.3, 2.9, 5.6, 1.8, 'virginica'],
        ]
        writer.writerows(iris_data)
    files.append("iris_sample.csv")
    
    # Prices prediction
    prices_path = output_dir / "prices_sample.csv"
    with open(prices_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['surface', 'chambres', 'age', 'localisation', 'prix'])
        
        data = [
            [50, 2, 10, 1, 150000],
            [70, 3, 5, 1, 210000],
            [90, 4, 2, 2, 320000],
            [45, 1, 20, 1, 90000],
            [120, 5, 1, 2, 450000],
            [60, 2, 15, 1, 130000],
            [80, 3, 8, 2, 280000],
            [100, 4, 3, 1, 350000],
        ]
        writer.writerows(data)
    files.append("prices_sample.csv")
    
    return files


def create_file_samples(output_dir: Path) -> list[str]:
    """Crée des fichiers pour robustesse fichiers."""
    files = []
    
    # contacts JSON
    contacts = {
        "contacts": [
            {"nom": "Dupont", "prenom": "Jean", "tel": "0612345678", "email": "jean@email.com"},
            {"nom": "Martin", "prenom": "Marie", "tel": "0698765432", "email": "marie@email.com"},
        ]
    }
    
    path = output_dir / "contacts_sample.json"
    path.write_text(json.dumps(contacts, indent=2, ensure_ascii=False), encoding='utf-8')
    files.append("contacts_sample.json")
    
    # contacts CSV
    csv_path = output_dir / "contacts_sample.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['nom', 'prenom', 'tel', 'email'])
        writer.writerow(['Dupont', 'Jean', '0612345678', 'jean@email.com'])
        writer.writerow(['Martin', 'Marie', '0698765432', 'marie@email.com'])
    files.append("contacts_sample.csv")
    
    # Text file
    text_path = output_dir / "sample_text.txt"
    text_path.write_text("""Ceci est un fichier texte d'exemple.
Il contient plusieurs lignes de texte.
Chaque ligne peut contenir des informations différentes.
Le but est de tester la lecture de fichiers texte.""", encoding='utf-8')
    files.append("sample_text.txt")
    
    return files


if __name__ == "__main__":
    create_sample_files()
