# =============================================================================
# CHAPITRE 21: WEB SCRAPING - SOLUTIONS
# =============================================================================

import requests
from bs4 import BeautifulSoup
import json
import csv


def exercice_21_1():
    """Faire une requête HTTP simple."""
    try:
        reponse = requests.get("https://httpbin.org/get", timeout=5)
        print(f"Status: {reponse.status_code}")
        print(f"URL: {reponse.url}")
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_2():
    """Utiliser des headers personnalisés."""
    headers = {
        "User-Agent": "MonBot/1.0",
        "Accept": "application/json"
    }
    
    try:
        reponse = requests.get("https://httpbin.org/headers", headers=headers, timeout=5)
        print(reponse.json())
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_3():
    """Parser du HTML simple."""
    html = """
    <html>
        <body>
            <h1>Titre Principal</h1>
            <p>Premier paragraphe</p>
            <p>Deuxième paragraphe</p>
            <a href="https://example.com">Lien</a>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, "html.parser")
    
    titre = soup.find("h1")
    if titre:
        print(f"Titre: {titre.get_text()}")
    
    paragraphes = soup.find_all("p")
    print(f"Paragraphes: {len(paragraphes)}")
    for p in paragraphes:
        print(f"  - {p.get_text()}")


def exercice_21_4():
    """Rechercher par classe CSS."""
    html = """
    <div class="article">
        <h2 class="title">Article 1</h2>
        <p class="content">Contenu de l'article 1</p>
    </div>
    <div class="article">
        <h2 class="title">Article 2</h2>
        <p class="content">Contenu de l'article 2</p>
    </div>
    """
    
    soup = BeautifulSoup(html, "html.parser")
    
    articles = soup.find_all("div", class_="article")
    print(f"Articles trouvés: {len(articles)}")
    
    for i, article in enumerate(articles, 1):
        titre = article.find("h2", class_="title")
        contenu = article.find("p", class_="content")
        if titre and contenu:
            print(f"{i}. {titre.get_text()}: {contenu.get_text()}")


def exercice_21_5():
    """Extraire tous les liens d'une page."""
    html = """
    <html>
        <body>
            <a href="https://site.com/page1">Page 1</a>
            <a href="https://site.com/page2">Page 2</a>
            <a href="https://autre.com">Autre site</a>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, "html.parser")
    
    liens = soup.find_all("a", href=True)
    print(f"Liens trouvés: {len(liens)}")
    
    for lien in liens:
        print(f"  Texte: {lien.get_text()}")
        print(f"  URL: {lien['href']}")


def exercice_21_6():
    """Utiliser les sélecteurs CSS."""
    html = """
    <div id="main">
        <div class="container">
            <p class="text">Premier</p>
            <p class="text">Deuxième</p>
        </div>
        <span class="info">Info</span>
    </div>
    """
    
    soup = BeautifulSoup(html, "html.parser")
    
    main = soup.select_one("#main")
    if main:
        print(f"Main content: {len(main.get_text())} chars")
    
    texts = soup.select(".text")
    print(f"Textes: {len(texts)}")
    for t in texts:
        print(f"  - {t.get_text()}")


def exercice_21_7():
    """Gérer les erreurs de requête."""
    urls = [
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://inexistant.xyz",
    ]
    
    for url in urls:
        try:
            reponse = requests.get(url, timeout=5)
            print(f"{url}: {reponse.status_code}")
        except Exception as e:
            print(f"{url}: ERREUR - {type(e).__name__}")


def exercice_21_8():
    """Utiliser des paramètres de requête."""
    params = {
        "page": 2,
        "limit": 5,
        "sort": "date"
    }
    
    try:
        reponse = requests.get("https://httpbin.org/get", params=params, timeout=5)
        data = reponse.json()
        print(f"URL: {data['args']}")
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_9():
    """Récupérer et parser du JSON."""
    try:
        reponse = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        data = reponse.json()
        
        print(f"Titre: {data['title']}")
        print(f"Corps: {data['body']}")
        print(f"ID: {data['id']}")
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_10():
    """Faire plusieurs requêtes."""
    ids = [1, 2, 3]
    
    for id_ in ids:
        try:
            reponse = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_}", timeout=5)
            data = reponse.json()
            print(f"{id_}: {data['title']}")
        except Exception as e:
            print(f"Erreur pour {id_}: {e}")


def exercice_21_11():
    """Sauvegarder des données en JSON."""
    try:
        reponse = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
        posts = reponse.json()[:5]
        
        with open("posts.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        
        print(f"Sauvegardé {len(posts)} posts dans posts.json")
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_12():
    """Sauvegarder des données en CSV."""
    try:
        reponse = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
        users = reponse.json()[:3]
        
        with open("users.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "email", "city"])
            writer.writeheader()
            for user in users:
                writer.writerow({
                    "id": user["id"],
                    "name": user["name"],
                    "email": user["email"],
                    "city": user["address"]["city"]
                })
        
        print("Utilisateurs sauvegardés dans users.csv")
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_13():
    """Parser un tableau HTML et sauvegarder en CSV."""
    html = """
    <table>
        <tr>
            <th>Nom</th>
            <th>Age</th>
            <th>Ville</th>
        </tr>
        <tr>
            <td>Alice</td>
            <td>25</td>
            <td>Paris</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>30</td>
            <td>Lyon</td>
        </tr>
        <tr>
            <td>Charlie</td>
            <td>35</td>
            <td>Marseille</td>
        </tr>
    </table>
    """
    
    soup = BeautifulSoup(html, "html.parser")
    
    rows = soup.find_all("tr")
    
    with open("tableau.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        for row in rows:
            cells = row.find_all(["td", "th"])
            if cells:
                writer.writerow([cell.get_text() for cell in cells])
    
    print("Tableau sauvegardé dans tableau.csv")


def exercice_21_14():
    """Utiliser un User-Agent réaliste."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
    }
    
    try:
        reponse = requests.get("https://httpbin.org/headers", headers=headers, timeout=5)
        data = reponse.json()
        print("Headers envoyés:")
        for key, value in data["headers"].items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"Erreur: {e}")


def exercice_21_15():
    """Scraper une page de données structurées."""
    html = """
    <div class="products">
        <div class="product" data-id="1">
            <h3>Ordinateur Portable</h3>
            <span class="price">999.99 €</span>
            <span class="category">Informatique</span>
        </div>
        <div class="product" data-id="2">
            <h3>Smartphone</h3>
            <span class="price">599.99 €</span>
            <span class="category">Téléphonie</span>
        </div>
        <div class="product" data-id="3">
            <h3>Casque Audio</h3>
            <span class="price">149.99 €</span>
            <span class="category">Audio</span>
        </div>
    </div>
    """
    
    soup = BeautifulSoup(html, "html.parser")
    
    produits = []
    
    for product in soup.find_all("div", class_="product"):
        nom = product.find("h3")
        prix = product.find("span", class_="price")
        categorie = product.find("span", class_="category")
        id_ = product.get("data-id")
        
        if nom and prix and categorie:
            produits.append({
                "id": id_,
                "nom": nom.get_text(),
                "prix": prix.get_text(),
                "categorie": categorie.get_text()
            })
    
    print(f"Produits trouvés: {len(produits)}")
    for p in produits:
        print(f"  - {p['nom']}: {p['prix']} ({p['categorie']})")


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 21: WEB SCRAPING - SOLUTIONS")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Solution 21.{i} ---")
        try:
            eval(f"exercice_21_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
