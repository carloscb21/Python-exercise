#  Ejercicio 6 de la Hoja 3

#https://es.wikipedia.org/wiki/Ecuación_diofántica

"""
Se llama ecuación diofántica a cualquier ecuación algebraica, generalmente de varias variables,
planteada sobre el conjunto de los números enteros Z o los números naturales N.

x + y = n.
"""
def diofantic (n) :
    x = 0
    while x <= n :
        y = 0
        while y <= n :
            if x + y == n :
                print(x, " + ", y, " = ", n)
            y += 1
        x += 1


def diofantic2 (n) :
    x = 0
    while x <= n :
        y = n - x
        print(x, " + ", y, " = ", n)
        x += 1

#Ecuación diofantica en una lista
def diofantic3 (n) :
    x = 0
    t = []
    while x <= n :
        y = n - x
        t = t + [(x,y)]
        x += 1
    return t
