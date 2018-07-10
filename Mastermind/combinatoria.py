import random
def factorial(n):
   if (n==0):
      return 1
   else:
      return n*factorial(n-1)
    
def permutaciones_k(listaElementos,k):
   if (k==0):
      yield []
   else:
      for i in range(len(listaElementos)):
         for permuta in permutaciones_k(listaElementos[:i]+listaElementos[(i+1):],k-1):
            yield [listaElementos[i]]+permuta
            
def permutacion_random(listaElementos):
# permutaciones(listaElementos)=permutaciones_k(listaElementos,len(listaElementos))
   cantidadPermutaciones=factorial(len(listaElementos))
   indice=random.randrange(0,cantidadPermutaciones)
   i=0
   for permuta in permutaciones_k(listaElementos,len(listaElementos)):
      if (i==indice):
         return permuta
      i=i+1
      
def permutaciones_random(listaElementos,k):
   nuevaListaElementos=permutacion_random(listaElementos)
   for permuta in permutaciones_k(nuevaListaElementos,k):
      yield permuta
