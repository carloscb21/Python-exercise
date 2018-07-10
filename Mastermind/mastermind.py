import combinatoria
import random
import sys


def suerte(n): #para los muertos y heridos 2, se cogen dos numeros de la lista para su permutacion
   l = []
   i = random.randint(0,3)
   while i < len(n) -1:
      l.append(n[i])
      if len(l)==2:
         return l

    
def numeros_posibles(): #lista de numeros de la combinacion
    lista_numeros = [0,1,2,3,4,5,6,7,8,9]
    return lista_numeros

def generar_combinacion():  #combinacion de numeros para el usuario, para que no se repita el numero
    llamada = numeros_posibles()
    lista_combinacion = [0]
    posible = 4
    i = 0
    while i < posible:
        posicion_random = random.randint(0, 9)
        j = 0
        while j < len(lista_combinacion)-1:
            if posicion_random == lista_combinacion[i-1]:
                posicion_random = random.randint(0, 9)
            j = j + 1
        lista_combinacion.append(llamada[posicion_random])
        i = i + 1
    del lista_combinacion[0]
    return lista_combinacion

def generar_combinacion2(): #Comprueba que la lista de las posibles combinaciones es valido
    lista_combinacion1 = generar_combinacion()
    guardar_combinacion = lista_combinacion1
    i = 0
    while i < len(lista_combinacion1):
        j = i - 1
        while j >= 0:
            if lista_combinacion1[i] == lista_combinacion1[j]:
                lista_combinacion1 = generar_combinacion()
                j = j + 1
            j = j - 1
        i = i + 1
    return lista_combinacion1

def impresion_combinacion():
    combinacion_final = 0
    k = 0
    while k < 4:
        combinacion_final = combinacion_final + lista_combinacion1[k]* (10**k)
        k = k + 1
    return combinacion_final


#muertos acierto
#heridos acierto sin posicion
def game():

    combinatoria = generar_combinacion2()
    
    lista_descartes = []
    r = 0
    combinacion_final2 = 0
    while r < len(lista_descartes):
       j = 0
       while j < len(lista_descartes):
          combinacion_final2 = combinacion_final2 + lista_descartes[i][j]* (10**j)
          j = j + 1
          lista_descartes[i] = combinacion_final2
       r = r +1
    auxiliar2 = False
    combinacion_final = 0
    combinatoria2 = combinatoria
    while auxiliar2 == False:
       
       k = 0       #pasa a un numero entero
       while k < 4:
           combinacion_final = combinacion_final + combinatoria[k]* (10**k)
           k = k + 1
        
       
       #print ("lista_descartes: "+str(lista_descartes))
       print ("Lista de numeros de la posible combinacion: " + str(numeros_posibles()))
       print ("Numero de elementos: " + str(4))
       print ("Propuesta: " + str(combinacion_final))    
       muertos = input("numero de muertos: ")
       heridos = input("numero de heridos: ")  

       
       auxiliar = False
       while auxiliar == False: #Nos aseguramos que el numero de muertos+heridos este en el rango correcto
          if int(muertos) + int(heridos) > 4:
             print ("se ha equivocado en el su declaracion, reponda de nuevo a la pregunta")
             muertos = input("numero de muertos: ")
             heridos = input("numero de heridos: ")
          else:

             auxiliar = True
       print(" ")
            
       if int(muertos) == 4 or() :
          return "Se acabo" 
       else:
            #lista_descartes.append(combinatoria)
            propuesta_muertos = int(muertos)
            propuesta_heridos = int(heridos)
            propuesta_muertosmasheridos = propuesta_muertos + propuesta_heridos 
            combinatoria3 = generar_combinacion2()
           
            lista_descartes.append(combinatoria2)
            lista_descartes[0] = combinatoria
            prueba = False
            if int(heridos) == 4 or (propuesta_muertosmasheridos == 4): #si los heridos y muertos 4
                combinatoria4 = random.shuffle(combinatoria2)
                t = 0
                #random.shuffle(combinatoria2)
                while t < len(lista_descartes):
                   if (combinatoria4 == lista_descartes[t]):
                      prueba = True
                   if prueba == True:
                      random.shuffle(combinatoria4)
                      t = t - t - 1
                   prueba = False
                   t = t + 1
            elif propuesta_muertosmasheridos == 3: #heridos y muertos 3 
                #if int(muertos) == 0 or int(muertos) == 1:
                i = 0
                combinatoria3 = generar_combinacion2()
                while i < propuesta_muertosmasheridos:
                   if (combinatoria3[i] != combinatoria2[i]) and (combinatoria3 != lista_descartes[i]):
                      lista_descartes.append(combinatoria3)
                      combinatoria3 = generar_combinacion2()
                      #print (combinatoria3)
                      i = - 1
                   i = i + 1
            elif propuesta_muertosmasheridos == 2:
               obtencion = suerte(combinatoria)
               a = obtencion[0]
               b = obtencion[1]
               combinatoria = generar_combinacion2()
               i = 0
               while i < len(combinatoria)-1:
                  if combinatoria[i] != a:
                     j = 0
                     if combinatoria[j] == b:
                        combinatoria = combinatoria
                     if combinatoria[j] != b:
                        if j == 3 and suerte[j] != 4:
                           lista_descartes.append(combinatoria)
                           combinatoria = generar_combinacion2()
                           j = j - 4
                        j = j +1
                  if combinatoria[i] == a:
                     combinatoria = combinatoria
                  i = i + 1
                        
            else:
               if (propuesta_muertosmasheridos == 1) or (propuesta_muertosmasheridos == 0): #heridos y muertos 0 o 1
                  lista_descartes.append(combinatoria)
                  combinatoria = generar_combinacion2()
            combinacion_final = 0

