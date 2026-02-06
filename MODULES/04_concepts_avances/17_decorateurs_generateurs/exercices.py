# =============================================================================
# CHAPITRE 17: DECORATEURS GENERATEURS - EXERCICES
# =============================================================================

# =============================================================================
# EXERCICE 17.1 - DECORATEUR SIMPLE
# =============================================================================
def exercice_17_1():
    """Decorateur qui mesure le temps."""
    import time
    
    def timer(func):
        def wrapper(*args, **kwargs):
            debut = time.time()
            resultat = func(*args, **kwargs)
            print(f"Temps: {time.time() - debut:.4f}s")
            return resultat
        return wrapper
    
    @timer
    def lente():
        time.sleep(0.1)
        return "Fini"
    
    print(lente())


# =============================================================================
# EXERCICE 17.2 - DECORATEUR AVEC ARGUMENTS
# =============================================================================
def exercice_17_2():
    """Decorateur avec repetitions."""
    def repetitions(n):
        def decorateur(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func(*args, **kwargs)
            return wrapper
        return decorateur
    
    @repetitions(3)
    def dire_bonjour():
        print("Bonjour!")
    
    dire_bonjour()


# =============================================================================
# EXERCICE 17.3 - GENERATOR SIMPLE
# =============================================================================
def exercice_17_3():
    """Generator de carres."""
    def carres(n):
        for i in range(n):
            yield i ** 2
    
    for c in carres(5):
        print(c)


# =============================================================================
# EXERCICE 17.4 - GENERATOR PUISSANCE
# =============================================================================
def exercice_17_4():
    """Generator avec accumulateur."""
    def accumulateur(depart=0):
        total = start = 1
        while True:
            yield total
            total += start
            start += 1
    
    for i, v in enumerate(accumulateur()):
        if i >= 10:
            break
        print(v)


# =============================================================================
# EXERCICE 17.5 - YIELD FROM
# =============================================================================
def exercice_17_5():
    """Generator compose."""
    def gen1():
        for i in range(3):
            yield i
    
    def gen2():
        yield from gen1()
        yield from range(3, 6)
    
    print(list(gen2()))


# =============================================================================
# EXERCICE 17.6 - DECORATEUR CACHE
# =============================================================================
def exercice_17_6():
    """Decorateur avec memoisation."""
    def cache(func):
        memo = {}
        def wrapper(n):
            if n not in memo:
                memo[n] = func(n)
            return memo[n]
        return wrapper
    
    @cache
    def factorielle(n):
        print(f"Calcul {n}")
        return 1 if n <= 1 else n * factorielle(n - 1)
    
    print(fact(5))
    print(fact(5))  # Pas de recalcul


# =============================================================================
# EXERCICE 17.7 - GENERATOR DE NOMBRES PREMIERS
# =============================================================================
def exercice_17_7():
    """Generator de nombres premiers."""
    def premiers(limite):
        for n in range(2, limite + 1):
            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    break
            else:
                yield n
    
    print(list(premiers(30)))


# =============================================================================
# EXERCICE 17.8 - DECORATEUR VALIDATION
# =============================================================================
def exercice_17_8():
    """Decorateur de validation."""
    def valider(types):
        def decorateur(func):
            def wrapper(*args):
                for arg, expected in zip(args, types):
                    if not isinstance(arg, expected):
                        raise TypeError(f"{arg} doit etre {expected}")
                return func(*args)
            return wrapper
        return decorateur
    
    @valider((int, int))
    def addition(a, b):
        return a + b
    
    print(addition(5, 3))


# =============================================================================
# EXERCICE 17.9 - GENERATOR DE COMBINAISONS
# =============================================================================
def exercice_17_9():
    """Generator de combinaisons."""
    def combinaisons(items, k):
        if k == 0:
            yield []
        else:
            for i in range(len(items)):
                for reste in combinaisons(items[i + 1:], k - 1):
                    yield [items[i]] + reste
    
    print(list(combinaisons([1, 2, 3], 2)))


# =============================================================================
# EXERCICE 17.10 - DECORATEUR CLASS
# =============================================================================
def exercice_17_10():
    """Decorateur de classe."""
    def classe_final(cls):
        cls.final = True
        return cls
    
    @classe_final
    class MaClasse:
        pass
    
    print(MaClasse.final)


if __name__ == "__main__":
    print("Chapitre 17: Decorateurs et Generateurs")
