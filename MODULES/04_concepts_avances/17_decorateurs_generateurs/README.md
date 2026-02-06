# Chapitre 17: Decorateurs et Generateurs

## Decorateurs
```python
def decorateur(func):
    def wrapper(*args, **kwargs):
        # Avant
        resultat = func(*args, **kwargs)
        # Apres
        return resultat
    return wrapper

@decorateur
def ma_fonction():
    pass
```

## Generateurs
```python
def generator():
    for i in range(10):
        yield i

for x in generator():
    print(x)
```

## Yield From
```python
def parent():
    yield from enfant()
```
