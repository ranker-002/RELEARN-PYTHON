# Chapitre 4 : Le Contrôle de Flux - Prendre des Décisions

## Introduction : Le if, c'est quoi ?

Parfois, ton programme doit choisir entre plusieurs chemins. "SI il pleut, je prends mon parapluie. SINON, je vais me promener."

Les instructions conditionnelles permettent à ton code de prendre des décisions !

---

## 1. La structure if (si)

```python
# SI une condition est vraie, ALORS on fait quelque chose
age = 20

if age >= 18:
    print("Tu es majeur !")
    print("Tu peux voter.")
```

**ATTENTION à l'indentation !** En Python, les espaces au début de la ligne sont OBLIGATOIRES. Ils disent quelle partie du code est "dedans" le if.

```python
# AVEC indentation (correct)
if age >= 18:
    print("Majeur")  # Cette ligne est DANS le if

# SANS indentation (ERREUR !)
if age >= 18:
print("Majeur")  # ERREUR ! Python ne sait pas si c'est dans le if
```

---

## 2. Le if...else (si...sinon)

```python
age = 15

if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")
```

---

## 3. Le if...elif...else (si...sinon si...sinon)

```python
note = 15

if note >= 16:
    print("Très bien !")
elif note >= 14:
    print("Bien !")
elif note >= 12:
    print("Assez bien")
else:
    print("À améliorer")
```

---

## 4. Les Conditions Composées

```python
age = 25
avec_argent = True

# ET
if age >= 18 and avec_argent:
    print("Tu peux entrer")

# OU
if age < 18 or avec_argent == False:
    print("Tu ne peux pas entrer")

# NON
if not avec_argent:
    print("Tu n'as pas d'argent")

# Combinaison complexe
if (age >= 18 and avec_argent) or (age >= 16 and avec_parent):
    print("Accès autorisé")
```

---

## 5. Conditions Imbriquées

On peut mettre des conditions dans d'autres conditions :

```python
age = 20
inscrit = True

if inscrit:
    if age >= 18:
        print("Accès autorisé - adulte")
    else:
        print("Accès autorisé - mineur avec inscription")
else:
    print("Inscription requise")
```

### Alternative avec Logique

```python
# Même logique, plus lisible
if not inscrit:
    print("Inscription requise")
elif age >= 18:
    print("Accès autorisé - adulte")
else:
    print("Accès autorisé - mineur avec inscription")
```

---

## 6. Pass et Ellipsis

Quand tu dois créer une structure vide (temporairement) :

```python
# Pass - ne fait rien, permet de garder la structure
if age >= 18:
    pass  # TODO: implémenter plus tard
else:
    print("Accès refusé")

# Ellipsis (...) - même usage, surtout pour les classes
if age >= 18:
    ...  # À implémenter
```

---

## 7. Conditions avec Booléens Directement

```python
est_actif = True

# PAS besoin de == True
if est_actif:
    print("Le compte est actif")

# Équivalent mais redondant
if est_actif == True:  # Inutile !
    print("Le compte est actif")

# Vérifier si vide/non vide
nom = "Alice"
if nom:  # True car non vide
    print(f"Bonjour {nom}")

liste = []
if not liste:  # True car vide
    print("La liste est vide")

# Vérifier si None
valeur = None
if valeur is None:
    print("Pas de valeur")

# Combiné
if nom and valeur:
    print("Les deux sont définis")
```

---

## 8. L'Instruction Match/Case (Python 3.10+)

Le pattern matching est une alternative élégante aux elif multiples.

### Syntaxe de Base

```python
match status_code:
    case 200:
        print("Succès")
    case 404:
        print("Page non trouvée")
    case 500:
        print("Erreur serveur")
    case _:
        print(f"Code inconnu: {status_code}")
```

### Avec Variables

```python
commande = input("Entrez une commande : ")

match commande.split():
    case ["quit"]:
        print("Au revoir !")
    case ["help"]:
        print("Aide disponible...")
    case ["load", nom_fichier]:
        print(f"Chargement de {nom_fichier}...")
    case ["save", nom_fichier]:
        print(f"Sauvegarde dans {nom_fichier}...")
    case _:
        print("Commande inconnue")
```

### Comparaison If vs Match

```python
# Avec if/elif (verbeux)
jour = "lundi"
if jour == "lundi":
    print("Début de semaine")
elif jour == "samedi" or jour == "dimanche":
    print("Weekend !")
else:
    print("Milieu de semaine")

# Avec match/case (plus lisible)
match jour:
    case "lundi":
        print("Début de semaine")
    case "samedi" | "dimanche":  # OU avec |
        print("Weekend !")
    case _:
        print("Milieu de semaine")
```

---

## 9. Exemples Pratiques Complets

### Exemple 1 : Calculateur d'Impôts

```python
revenu = float(input("Revenu annuel : "))

if revenu <= 10000:
    impot = 0
    print("Non imposable")
elif revenu <= 30000:
    impot = (revenu - 10000) * 0.11
    print(f"Tranche 11% : {impot:.2f}€")
elif revenu <= 50000:
    impot = 2200 + (revenu - 30000) * 0.30
    print(f"Tranche 30% : {impot:.2f}€")
else:
    impot = 8200 + (revenu - 50000) * 0.41
    print(f"Tranche 41% : {impot:.2f}€")

print(f"Taux effectif : {(impot/revenu)*100:.1f}%")
```

### Exemple 2 : Validation de Formulaire

```python
email = input("Email : ")
mot_de_passe = input("Mot de passe : ")
confirmation = input("Confirmer : ")

erreurs = []

if not email:
    erreurs.append("Email requis")
elif "@" not in email:
    erreurs.append("Email invalide")

if not mot_de_passe:
    erreurs.append("Mot de passe requis")
elif len(mot_de_passe) < 8:
    erreurs.append("Mot de passe trop court (min 8 caractères)")

if mot_de_passe != confirmation:
    erreurs.append("Les mots de passe ne correspondent pas")

if erreurs:
    print("\n❌ Erreurs :")
    for erreur in erreurs:
        print(f"  - {erreur}")
else:
    print("\n✅ Compte créé avec succès !")
```

### Exemple 3 : Système de Recommandation

```python
temperature = 22
meteo = "ensoleillé"

if meteo == "ensoleillé":
    if temperature > 25:
        print("☀️ Parfait pour la plage !")
    elif temperature > 15:
        print("🚴 Idéal pour du vélo")
    else:
        print("🧥 Ensoleillé mais frais, prends un pull")
elif meteo == "pluvieux":
    if temperature < 10:
        print("🌧️ Reste au chaud avec un bon film")
    else:
        print("☂️ Prends un parapluie pour sortir")
elif meteo == "nuageux":
    print("🌤️ Bon pour une balade en forêt")
else:
    print("🤷 Vérifie la météo avant de sortir")
```

---

## Erreurs Courantes

```python
# ERREUR : = au lieu de ==
if age = 18:   # ERREUR !
    pass

# CORRECT
if age == 18:
    pass
```

---

## Exercices Pratiques

### Exercice 1 : Catégorie d'Âge
Demande l'âge et affiche :
- "Enfant" si < 13
- "Adolescent" si entre 13 et 17
- "Adulte" si entre 18 et 64
- "Senior" si ≥ 65

### Exercice 2 : Calculateur de Réduction
Un magasin offre des réductions :
- < 18 ans : -20%
- 18-25 ans (étudiants) : -15%
- > 65 ans : -25%
- Autres : pas de réduction

Demande l'âge et le statut étudiant (oui/non), puis calcule le prix final.

### Exercice 3 : Validation de Connexion
Crée un système qui demande :
- Nom d'utilisateur
- Mot de passe

Vérifie :
- Si les champs sont vides
- Si le mot de passe a au moins 8 caractères
- Si le mot de passe contient au moins un chiffre

Affiche les erreurs ou "Connexion réussie".

### Exercice 4 : Jeu Plus ou Moins
L'ordinateur choisit un nombre entre 1 et 100.
Le joueur propose un nombre.
Indique si c'est "Trop grand", "Trop petit" ou "Gagné !".

### Exercice 5 : Calculatrice avec Menu
Affiche un menu :
1. Addition
2. Soustraction
3. Multiplication
4. Division
5. Quitter

Demande deux nombres et effectue l'opération choisie.
Gère la division par zéro.

### Exercice 6 : Jour de la Semaine
Demande un numéro de jour (1-7) et affiche :
- "Weekend" pour samedi/dimanche
- "Début de semaine" pour lundi
- "Milieu de semaine" pour mardi-jeudi
- "Bientôt le weekend" pour vendredi

Utilise les conditions imbriquées.

### Exercice 7 : Convertisseur de Température
Demande une température et l'unité (C/F/K).
Convertis dans les autres unités et affiche :
- "Glace" si < 0°C
- "Froid" si 0-15°C
- "Tempéré" si 15-25°C
- "Chaud" si > 25°C

### Exercice 8 : Système de Notes
Demande une note entre 0 et 20.
Affiche :
- "Excellent" si ≥ 16
- "Très bien" si 14-15
- "Bien" si 12-13
- "Passable" si 10-11
- "Insuffisant" si < 10

Ajoute une mention "Félicitations" si ≥ 18.

### Exercice 9 : Année Bissextile
Demande une année et détermine si elle est bissextile.
Règle : bissextile si divisible par 4, sauf si divisible par 100 (sauf si divisible par 400).

### Exercice 10 : Permission d'Entrée
Crée un système de contrôle d'accès avec :
- Vérification d'âge
- Vérification d'identité (nom sur liste)
- Vérification de billet (si payant)
- Horaire (si événement limité dans le temps)

Affiche "Entrée autorisée" ou la raison du refus.

---

## Bonnes Pratiques

### 1. Ordre des Conditions
```python
# Du plus spécifique au plus général
if note == 20:
    print("Perfect !")
elif note >= 16:
    print("Très bien")
elif note >= 10:
    print("Passable")
else:
    print("À revoir")
```

### 2. Éviter les Conditions Inutiles
```python
# ❌ Redondant
if condition == True:
    pass

# ✅ Correct
if condition:
    pass
```

### 3. Garder le Code Lisible
```python
# ❌ Trop imbriqué
if a:
    if b:
        if c:
            print("ok")

# ✅ Aplatir quand possible
if a and b and c:
    print("ok")
```

---

## Résumé

| Structure | Syntaxe | Usage |
|-----------|---------|-------|
| If simple | `if cond:` | Une condition |
| If/else | `if cond: ... else:` | Deux choix |
| If/elif/else | `if/elif/else` | Plusieurs choix |
| Match/Case | `match var: case val:` | Pattern matching |
| Pass | `pass` | Structure vide |

---

## Prochain Chapitre

Tu sais maintenant prendre des décisions dans ton code ! Le prochain chapitre sur les **boucles** te permettra de répéter des actions automatiquement.
