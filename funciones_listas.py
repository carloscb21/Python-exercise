import random


from math import *


#Booleano de número primo
def isPrime (n) :
    i = 2
    while i*i <= n and n % i != 0 :
        i += 1
    return i*i > n


#El siguiente número primo apartir de n
def nextPrime (n) :
    t = n + 1
    while not isPrime (t) :
        t = t + 1
    return t

#El siguiente número primo apartir contando si n es primo
def nextPrime2 (n) :
    while not isPrime (n) :
        n = n + 1
    return n

#Los n primeros primos
def primes (n) :
    primes = []
    i = 1
    prime = 2   # 2 is the first prime number
    while i <= n :
        primes += [prime]
        i = i + 1
        prime = nextPrime2 (prime + 1)   # primo i-esimo
    return primes


#cambiamos los numeros de la lista por numeros aleatorios
def aleatorio (t) :
    i = 0
    n = len (t)
    while i <= n - 1 :
        t[i] = random.randint(0, 9)
        i += 1
    return t


#media y desviacion de una lista de datos 
def estadistica (t) :
    i = 0
    n = len (t)
    suma = 0.0
    suma_cuadrados = 0.0
    while i <= n - 1 :
        suma = suma + t[i]
        suma_cuadrados = suma_cuadrados + t[i] * t[i]
        i += 1
    media = suma / n
    varianza = (1.0 / n) * suma_cuadrados - (1.0 / (n ** 2)) * (suma ** 2)
    desviacion_tipica = sqrt(varianza)
    return media, desviacion_tipica


#Calcular la cantidad de los números cuyo logaritmo en base 2 sea menor que otro número dado log > 0.
def logaritmos (t, log) :
    i = 0
    n = len (t)
    cont = 0
    while i <= n - 1 :
        if (log10(t[i]) / log10(2)) < log :
            cont += 1
        i += 1
    return cont


#Boleano de si la lista esta ordenada o no
def sorted (t) :
    i = 0
    n = len (t)
    while i < n - 1 and t[i] <= t[i + 1] :
        i += 1
    return i >= n - 1


#ver si el número es potencia de dos
def es_potencia_dos (n) :
    if n == 0 :
        return False
    else :
        while n % 2 == 0 :
                    n = n / 2
        return n == 1

"""
https://es.wikipedia.org/wiki/Palíndromo

Ver si es palindroma la lista
"""
def palindroma (t) :
    longitud = len (t)
    inicio = 0
    final = longitud - 1
    posicion = inicio
    while posicion <= final and t[posicion] == t[final - posicion]:
              posicion = posicion + 1
    return posicion >= final

#Sumas parciales de la lista
def sumas_parciales (t) :
    i = 0
    n = len (t)
    acum = 0
    s = t
    while i <= n - 1 :
        acum = acum + t[i]
        s[i] = acum
        i += 1
    return s

#Booleano si es cuadrado el numero o no
def es_cuadrado (n) :
    raiz = round ( sqrt (n) )
    return raiz * raiz == n 



