# Chapitre 19 : Web Scraping

## Pourquoi Extraire des Données du Web ?

Le web est une immense base de données informelle. Des millions de pages contiennent des informations utiles : prix de produits, infos météorologiques, résultats sportifs, articles de presse... Mais ces données ne sont généralement pas disponibles sous forme de fichiers CSV ou JSON directement exploitables.

**Le web scraping**, c'est extraire ces données en programmant un "robot" qui visite les pages web pour nous, lit leur contenu, et le transforme en données structurées.

Imaginez que vous vouliez comparer les prix d'un même produit sur 50 boutiques en ligne. Le faire manuellement prendrait des jours. Un script de web scraping le fait en quelques secondes.

Python offre plusieurs outils pour cela, des plus simples aux plus puissants.

---

## Les Bases : `urllib.request`

La bibliothèque standard de Python permet de faire des requêtes HTTP basiques.

```python
from urllib.request import urlopen

# Faire une requête GET simple
reponse = urlopen("https://www.example.com")
contenu = reponse.read()
print(contenu.decode("utf-8"))  # Le HTML de la page

# Lire les headers
print(reponse.headers)
reponse.close()
```

---

## `requests` : La Méthode Simple (Recommandée)

La bibliothèque `requests` est bien plus simple et lisible que `urllib`. Il faut souvent l'installer (`pip install requests`).

```python
import requests

# Requête GET simple
reponse = requests.get("https://www.example.com")
print(reponse.status_code)      # 200 = OK
print(reponse.text)             # Contenu HTML
print(reponse.json())           # Si c'est du JSON

# Headers personnalisés
headers = {
    "User-Agent": "MonBot/1.0",
    "Accept": "application/json"
}
reponse = requests.get("https://api.example.com/data", headers=headers)

# Requête avec paramètres
params = {
    "q": "python tutorial",
    "lang": "fr",
    "num": 10
}
reponse = requests.get("https://www.google.com/search", params=params)

# Autres méthodes
reponse = requests.post("https://api.example.com/submit", data={"key": "value"})
reponse = requests.put("https://api.example.com/update", json={"status": "done"})
reponse = requests.delete("https://api.example.com/resource")
```

---

## Parser le HTML : `BeautifulSoup`

Une fois qu'on a le HTML, il faut l'analyser pour trouver les données. `BeautifulSoup` est l'outil de référence pour ça.

```python
from bs4 import BeautifulSoup
import requests

# Récupérer une page
reponse = requests.get("https://www.example.com")
html = reponse.text

# Parser avec BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Trouver tous les éléments d'un type
tous_les_paragraphes = soup.find_all("p")
print(f"Trouvés {len(tous_les_paragraphes)} paragraphes")

# Trouver le premier
premier_p = soup.find("p")
print(premier_p.text)

# Rechercher par classe
articles = soup.find_all("div", class_="article")
print(f"Trouvés {len(articles)} articles")

# Rechercher par ID
titre_principal = soup.find(id="main-title")
print(titre_principal.text)

# Rechercher avec attributs
liens = soup.find_all("a", href=True)  # Tous les liens
for lien in liens:
    print(lien["href"])  # L'URL du lien
    print(lien.text)     # Le texte du lien
```

### Naviguer dans l'Arbre HTML

```python
soup = BeautifulSoup("<html><body><div><p>Premier</p><p>Second</p></div></body></html>")

# Accéder aux enfants
div = soup.find("div")
print(div.children)           # Tous les enfants directs
print(div.contents)           # Liste des enfants

# Rechercher en descendant
soup.find("div").find("p")    # Trouver un <p> dans un <div>

# Rechercher en remontant
paragraphe = soup.find("p")
print(paragraphe.parent)      # Le parent
print(paragraphe.parents)     # Tous les parents (itérateur)

# Rechercher par fratrie (éléments suivants)
paragraphe = soup.find("p")
print(paragraphe.next_sibling)    # Frère suivant
print(paragraphe.previous_sibling)  # Frère précédent
```

### Sélecteurs CSS (Plus Puissant)

```python
soup = BeautifulSoup(html, "html.parser")

# Sélection par sélecteur CSS
tous_les_paragraphes = soup.select("p")
articles = soup.select(".article")           # Par classe
id_unique = soup.select("#main-content")   # Par ID
liens = soup.select("div.article a")        # Liens dans div avec classe article
premier = soup.select_one("p")              # Un seul élément

# Sélecteurs avancés
soup.select("div > p")          # <p> enfants directs de <div>
soup.select("p:first-child")    # Premier enfant de type <p>
soup.select("a[href*='example']")  # Liens contenant "example"
```

---

## Exemple Complet : Scraper une Page de News

```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scraper_articles(url):
    """Extraire les titres et résumés d'une page de news."""
    
    # Headers pour se faire passer pour un navigateur
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # Récupérer la page
    reponse = requests.get(url, headers=headers)
    
    if reponse.status_code != 200:
        print(f"Erreur: {reponse.status_code}")
        return
    
    # Parser le HTML
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    # Trouver les articles (adaptez selon le site !)
    articles = soup.find_all("article", class_="news-article")
    
    print(f"Trouvés {len(articles)} articles:\n")
    
    for i, article in enumerate(articles, 1):
        # Le titre
        titre = article.find("h2")
        titre_texte = titre.text.strip() if titre else "Sans titre"
        
        # La date
        date = article.find("time")
        date_texte = date.get("datetime") if date else "Date inconnue"
        
        # Le résumé
        resume = article.find("p", class_="summary")
        resume_texte = resume.text.strip()[:100] if resume else "Pas de résumé"
        
        # Le lien
        lien = article.find("a", href=True)
        url_complet = "https://site.com" + lien["href"] if lien else ""
        
        print(f"{i}. {titre_texte}")
        print(f"   Date: {date_texte}")
        print(f"   {resume_texte}...")
        print(f"   Lien: {url_complet}")
        print()

# Utilisation
# scraper_articles("https://www.example.com/news")
```

---

## `requests-html` : JavaScript et Sessions

Certaines pages utilisent JavaScript pour charger leurs données. `requests-html` peut exécuter du JavaScript.

```python
from requests_html import HTMLSession

session = HTMLSession()

# Charger une page (JavaScript exécuté)
reponse = session.get("https://www.example.com")
reponse.html.render(timeout=20)  # Exécute le JavaScript

# Maintenant le contenu généré par JS est disponible
print(reponse.html.find("div.dynamic-content", first=True).text)

session.close()
```

---

## Gestion des Erreurs

```python
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

try:
    reponse = requests.get("https://www.example.com", timeout=5)
    reponse.raise_for_status()  # Lève une erreur si 4xx ou 5xx
    print("Succès!")
    
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Erreur de connexion: {e}")
except requests.exceptions.Timeout as e:
    print(f"Timeout: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erreur générale: {e}")

# Vérifications avant de parser
if reponse.status_code == 200:
    contenu = reponse.text
else:
    print(f"Échec: {reponse.status_code}")
```

---

## Respecter le Web : Bonnes Pratiques

| Pratique | Pourquoi |
|----------|----------|
| `robots.txt` | Vérifiez si le site autorise le scraping |
| Délai entre requêtes (1-2s) | Ne surchargez pas le serveur |
| Headers User-Agent | Identifiez votre bot |
| Ne pas scraper en boucle | Utilisez des APIs quand disponibles |
| Limiter les requêtes | Ne téléchargez que le nécessaire |

---

## Stockage des Données Scrapées

```python
import json
import csv

# Sauvegarder en JSON
donnees = [
    {"titre": "Article 1", "url": "https://..."},
    {"titre": "Article 2", "url": "https://..."}
]

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, ensure_ascii=False, indent=2)

# Sauvegarder en CSV
with open("articles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["titre", "url"])
    writer.writeheader()
    writer.writerows(donnees)

# Lire ensuite
with open("articles.json", "r", encoding="utf-8") as f:
    donnees_lues = json.load(f)
```

---

## Résumé

| Module | Usage |
|--------|-------|
| `urllib.request` | Requêtes HTTP basiques (stdlib) |
| `requests` | Requêtes HTTP simples et puissantes |
| `BeautifulSoup` | Parser et naviguer dans le HTML |
| `requests-html` | Pages avec JavaScript |

---

## Erreurs Courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| `403 Forbidden` | Le site vous bloque | Changez le User-Agent |
| `429 Too Many Requests` | Trop de requêtes | Ajoutez des délais |
| `ConnectionError` | Pas d'accès réseau | Vérifiez la connexion |
| `AttributeError` | L'élément n'existe pas | Vérifiez le HTML avec le navigateur |
| `JSONDecodeError` | Ce n'est pas du JSON | Utilisez `.text` au lieu de `.json()` |

---

## Exercices Pratiques

1. **Scraper les titres d'un blog** : Extraire tous les titres d'articles d'un blog

2. **Tableau en CSV** : Parser un tableau HTML et le sauvegarder en CSV

3. **Suivre les liens** : Scraper une page, suivre les liens, et parser les pages liées

4. **Monitoring de prix** : Vérifier régulièrement le prix d'un produit et alerter les changements

5. **Aggregator de news** : Collecter des articles de plusieurs sources et les fusionner

---

## Chapitre Suivant

Vos données sont maintenant extraites et stockées. Passons au [Chapitre 21 : Data Science I](21_data_science/README.md) pour apprendre à analyser et visualiser ces données !
