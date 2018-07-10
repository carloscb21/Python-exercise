#  Ejercicio 4 de la Hoja 3

#maximo comun divisor
def maxcd (a, b) :
    while a != b :
        if a > b :
            a = a - b
        else :
            b = b - a
    return a

#segunda version del maximo comun divisor
def maxcd2 (a, b) :
    while b > 0 :
        a, b = b, a % b
        print(a,b)
    return a

#simplicamos los valores apartir del maximo comun divisor
def simplificar (n, d) :
    m = maxcd (n, d)
    new_n = n / m
    new_d = d / m
    return new_n, new_d
