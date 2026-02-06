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

## 4. Les conditions composées

```python
age = 25
avec_argent = True

# ET
if age >= 18 and avec_argent:
    print("Tu peux entrer")

# OU
if age < 18 or avec_argent == False:
    print("Tu ne peux pas entrer")
```

---

## Erreurs courantes

```python
# ERREUR : = au lieu de ==
if age = 18:   # ERREUR !
    pass

# CORRECT
if age == 18:
    pass
```

---

## Exercices

1. Demande l'âge et dit si l'utilisateur est mineur, majeur ou senior (65+)
