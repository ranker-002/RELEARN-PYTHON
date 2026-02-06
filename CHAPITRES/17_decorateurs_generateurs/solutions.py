# =============================================================================
# CHAPITRE 17: DECORATEURS GENERATEURS - SOLUTIONS
# =============================================================================

import time


def exercice_17_1():
    def timer(func):
        def w(*a, **k):
            t = time.time()
            r = func(*a, **k)
            print(f"{time.time()-t:.4f}s")
            return r
        return w
    
    @timer
    def f(): time.sleep(0.1); return "OK"
    
    print(f())


def exercice_17_2():
    def reps(n):
        def d(func):
            def w():
                for _ in range(n): func()
            return w
        return d
    
    @reps(3)
    def hi(): print("Hi")
    
    hi()


def exercice_17_3():
    def c(n):
        for i in range(n):
            yield i*i
    
    print(list(c(5)))


def exercice_17_4():
    def a(start=0):
        total=start
        while True:
            yield total
            total+=1
    
    print([next(a()) for _ in range(10)])


def exercice_17_5():
    def g1():
        for i in range(3): yield i
    
    def g2():
        yield from g1()
        yield from range(3,6)
    
    print(list(g2()))


def exercice_17_6():
    def memo(func):
        cache = {}
        def w(n):
            if n not in cache:
                cache[n] = func(n)
            return cache[n]
        return w
    
    @memo
    def fib(n):
        return 1 if n<2 else fib(n-1)+fib(n-2)
    
    print(fib(10))


def exercice_17_7():
    def p(lim):
        for n in range(2, lim+1):
            for d in range(2, int(n**0.5)+1):
                if n%d==0: break
            else: yield n
    
    print(list(p(30)))


def exercice_17_8():
    def val(types):
        def d(func):
            def w(*a):
                for x,t in zip(a,types):
                    if not isinstance(x,t):
                        raise TypeError()
                return func(*a)
            return w
        return d
    
    @val((int,int))
    def add(a,b): return a+b
    
    print(add(1,2))


def exercice_17_9():
    def comb(items,k):
        if k==0: yield []
        else:
            for i in range(len(items)):
                for r in comb(items[i+1:],k-1):
                    yield [items[i]]+r
    
    print(list(comb([1,2,3],2)))


def exercice_17_10():
    def final(cls):
        cls.final=True
        return cls
    
    @final
    class C: pass
    
    print(C.final)
