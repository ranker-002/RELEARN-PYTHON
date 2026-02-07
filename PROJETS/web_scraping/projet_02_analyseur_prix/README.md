# Projet 2 : Analyseur de Prix

Créez un système d'analyse et de comparaison de prix qui récupère les tarifs de plusieurs sites e-commerce et vous aide à trouver les meilleures offres.

---

## Introduction : Qu'est-ce qu'un Analyseur de Prix ?

Un analyseur de prix est un outil qui :
- **Surveille** les prix sur plusieurs sites marchands
- **Compare** les tarifs pour trouver les meilleures offres
- **Alerte** lorsque le prix d'un produit descend sous un seuil
- **Historise** les variations de prix pour identifier les tendances

**Exemples d'utilisation réelle :**
- **Keepa** : Suivi des prix Amazon
- **CamelCamelCamel** : Historique des prix Amazon
- **Honey** : Coupons et comparateur automatique

**Architecture du système :**
```
┌─────────────────────────────────────────────────────────┐
│              ANALYSEUR DE PRIX                          │
├─────────────────────────────────────────────────────────┤
│  SOURCES:           │  FONCTIONNALITÉS:                 │
│  - Amazon          │  ✓ Scraping multi-sites           │
│  - Cdiscount       │  ✓ Comparaison de prix            │
│  - Fnac           │  ✓ Alertes seuil de prix          │
│  - Rue du Commerce │  ✓ Historique et graphiques       │
│                    │  ✓ Export CSV/JSON                │
└─────────────────────────────────────────────────────────┘
```

---

## Prérequis

- **Module 5 requis** : [Web Scraping](../../05_domaines_specifies/21_web_scraping/README_MODULE.md)
- Compétences nécessaires :
  - Requêtes HTTP avec `requests` et `BeautifulSoup`
  - Parsing HTML avec `bs4`
  - Manipulation de dates avec `datetime`
  - Structures de données avancées

---

## Structure du Projet

```
projet_02_analyseur_prix/
├── src/
│   ├── main.py              # Point d'entrée CLI
│   ├── models/
│   │   ├── produit.py       # Classe Produit
│   │   └── prix.py          # Classe Prix
│   ├── services/
│   │   ├── scraper.py       # Scraping des sites
│   │   ├── comparator.py    # Comparaison de prix
│   │   ├── alerter.py       # Gestion des alertes
│   │   └── history.py       # Historique des prix
│   └── utils/
│       ├── config.py        # Configuration
│       ├── date_utils.py    # Formatage de dates
│       └── formatter.py     # Formatage des prix
├── tests/
│   ├── test_scraper.py
│   ├── test_comparator.py
│   └── test_main.py
├── data/
│   ├── sample/              # Données exemples
│   │   ├── subscriptions.json
│   │   └── produits_suivis.json
│   └── history/            # Historique des prix
├── README.md
└── requirements.txt
```

---

## Fonctionnalités

### 1. Scraping Multi-Sites

Les sites e-commerce utilisent différentes structures HTML :

```python
from bs4 import BeautifulSoup
import requests

class PriceScraper:
    SITES = {
        'amazon': {
            'selecteur_titre': '#productTitle',
            'selecteur_prix': '.a-price .a-offscreen',
            'selecteur_dispo': '#availability span',
        },
        'cdiscount': {
            'selecteur_titre': '.fpProdName',
            'selecteur_prix': '.fpPrice.price',
            'selecteur_dispo': '.fpStock',
        },
    }
    
    def scraper_produit(self, url: str) -> dict:
        response = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        site = self.detecter_site(url)
        config = self.SITES[site]
        
        return {
            'titre': soup.select_one(config['selecteur_titre']).text.strip(),
            'prix': self.extraire_prix(soup, config['selecteur_prix']),
            'disponible': self.verifier_disponibilite(soup, config['selecteur_dispo']),
            'url': url,
            'site': site,
        }
```

### 2. Comparaison de Prix

```python
class PriceComparator:
    def comparer(self, produits: list[dict]) -> list[dict]:
        resultats = []
        for produit in produits:
            if produit['prix'] is None:
                continue
            resultats.append({
                'titre': produit['titre'][:50],
                'prix_min': min(p['prix'] for p in [produit] if p['prix']),
                'prix_max': max(p['prix'] for p in [produit] if p['prix']),
                'moyenne': sum(p['prix'] for p in [produit] if p['prix']) / len([produit]),
                'site': produit['site'],
                'url': produit['url'],
            })
        return sorted(resultats, key=lambda x: x['prix_min'])
```

### 3. Alertes de Prix

```python
class PriceAlerter:
    def __init__(self, seuil_default: float = 0.1):
        self.seuils = {}
        self.seuil_default = seuil_default
    
    def ajouter_seuil(self, produit_id: str, seuil: float):
        self.seuils[produit_id] = seuil
    
    def verifier(self, produit: dict) -> list[str]:
        alertes = []
        seuil = self.seuils.get(produit['id'], produit['prix'] * (1 - self.seuil_default))
        if produit['prix'] <= seuil:
            alertes.append(f"🚨 {produit['titre'][:30]}... est à {produit['prix']}€ (seuil: {seuil}€)")
        return alertes
```

### 4. Interface CLI Interactive

```
╔══════════════════════════════════════════════════╗
║            ANALYSEUR DE PRIX                    ║
╠══════════════════════════════════════════════════╣
║  1. Scanner un produit     2. Lister produits  ║
║  3. Comparer prix          4. Définir alerte    ║
║  5. Historique             6. Exporter          ║
║  7. Quitter                                      ║
╚══════════════════════════════════════════════════╝
```

---

## Modèle de Données

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum


class Disponibilite(Enum):
    DISPONIBLE = "disponible"
    INDISPONIBLE = "indisponible"
    Rupture = "rupture"
    PRECOMMANDE = "precommande"


@dataclass
class Prix:
    montant: float
    devise: str = "EUR"
    date_collecte: datetime = None
    url_source: str = ""
    site: str = ""
    
    def __post_init__(self):
        if self.date_collecte is None:
            self.date_collecte = datetime.now()
    
    def formater(self) -> str:
        return f"{self.montant:.2f} {self.devise}"


@dataclass
class Produit:
    id: str
    nom: str
    url: str
    categorie: str = ""
    prix_actuel: Optional[Prix] = None
    prix_historique: list[Prix] = None
    seuil_alerte: Optional[float] = None
    disponible: Disponibilite = Disponibilite.DISPONIBLE
    
    def __post_init__(self):
        if self.prix_historique is None:
            self.prix_historique = []
    
    def ajouter_prix(self, prix: Prix):
        self.prix_actuel = prix
        self.prix_historique.append(prix)
    
    @property
    def variation_pourcentage(self) -> Optional[float]:
        if len(self.prix_historique) < 2:
            return None
        premier = self.prix_historique[0].montant
        dernier = self.prix_historique[-1].montant
        return ((dernier - premier) / premier) * 100
    
    def est_alerte(self) -> bool:
        if self.prix_actuel is None or self.seuil_alerte is None:
            return False
        return self.prix_actuel.montant <= self.seuil_alerte
```

---

## Indications Progressives

### Niveau 1 - Découverte

**Objectif:** Scraper un produit simple

```python
import requests
from bs4 import BeautifulSoup


class BasicScraper:
    def scraper(self, url: str) -> dict:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        titre = soup.find('h1').text.strip()
        prix = soup.find('span', class_='price').text.strip()
        
        return {'titre': titre, 'prix': prix}
```

**Indice:** Utilisez `print(soup.prettify())` pour voir la structure HTML

---

### Niveau 2 - Approfondissement

**Objectif:** Gestion multi-sites et erreurs robustes

```python
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


class RobustScraper:
    SITES = {
        'amazon': {'prix': '.a-price .a-offscreen'},
        'cdiscount': {'prix': '.fpPrice'},
    }
    
    def scraper(self, url: str) -> dict:
        try:
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
        except RequestException as e:
            print(f"Erreur: {e}")
            return None
        
        site = 'amazon' if 'amazon' in url else 'cdiscount'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        prix_elem = soup.select_one(self.SITES[site]['prix'])
        prix = float(prix_elem.text.replace('€', '').replace(',', '.').strip()) if prix_elem else None
        
        return {'url': url, 'prix': prix, 'site': site}
```

---

### Niveau 3 - Expert

**Objectif:** Application CLI complète avec historique et alertes

```python
class PriceAnalyzerApp:
    def __init__(self):
        self.produits = []
        self.scraper = RobustScraper()
        self.alerter = PriceAlerter()
        self.history = PriceHistory()
    
    def scanner(self, url: str) -> dict:
        resultat = self.scraper.scraper(url)
        if resultat:
            self.history.sauvegarder(resultat)
        return resultat
    
    def comparer(self, urls: list[str]) -> list[dict]:
        produits = []
        for url in urls:
            if p := self.scraper.scraper(url):
                produits.append(p)
        return sorted(produits, key=lambda x: x.get('prix', float('inf')))
    
    def definir_alerte(self, url: str, seuil: float):
        self.alerter.ajouter(url, seuil)
```

---

## Configuration

Créez `data/produits_suivis.json` :

```json
{
  "produits": [
    {
      "id": "prod_001",
      "nom": "iPhone 15 Pro",
      "url": "https://www.amazon.fr/dp/B0CHX8K5ZV",
      "categorie": "Smartphone",
      "seuil_alerte": 900.0
    },
    {
      "id": "prod_002",
      "nom": "MacBook Air M3",
      "url": "https://www.cdiscount.com/p-5467890.html",
      "categorie": "Ordinateur",
      "seuil_alerte": 1100.0
    }
  ],
  "alertes": {
    "email": "votre@email.com",
    "notification": true
  }
}
```

---

## Critères de Validation

- [ ] Scraping Amazon et Cdiscount
- [ ] Conversion prix string vers float
- [ ] Comparaison multi-produits
- [ ] Système d'alertes seuil
- [ ] Historique des prix
- [ ] Export CSV des comparaisons
- [ ] Type hints et docstrings

---

## Pièges Courants

### 1. User-Agent
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

### 2. Prix formatés différemment
```python
prix = prix_elem.text.replace('€', '').replace(',', '.').replace(' ', '').strip()
prix = float(prix) if prix else None
```

### 3. Site en maintenance
```python
if response.status_code == 503:
    print("Site temporairement indisponible")
    return None
```

---

## Installation et Utilisation

```bash
uv sync --extra web-scraping
python src/main.py
pytest tests/ -v
python verification.py
```

---

## Ressources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)
- [CSS Selectors](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Selectors)

**Sites de test :**
- Amazon : https://www.amazon.fr/
- Cdiscount : https://www.cdiscount.com/

---

## Objectifs d'Apprentissage

- Parser des pages HTML complexes
- Gérer différents formats de données
- Implémenter un système de notification
- Stocker et analyser des séries temporelles
- Créer une CLI interactive avec argparse
- Manipuler des fichiers JSON et CSV

---

*Durée estimée : 10-15 heures | Difficulté : Avancé*

---

[Retour au module](../README_PROJETS.md)
