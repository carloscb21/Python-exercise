import combinatoria

class Chequeo(object):
   def __init__(self,muertos,heridos,k):
      self.muertos = muertos
      self.heridos = heridos
      self.k = k

   #muestra las posibles combinaciones
   def getChequeoOrdenador(combina1,combina2,k):# Metodo estatico. Llamada: Chequeo.getChequeoOrdenador(combina1,combina2,k)
   
   #Checkear el numero de muertos y el numero de heridos    
   def getChequeoHumano(combina,k): # Metodo estatico. Llamada: Chequeo.getChequeoHumano(combina,k)   

   #Comrpueba si el checeo humano es correo
   def esChequeoCompatible(self):
      
      
   def __eq__(self,objeto):
   def __ne__(self,objeto):
   def __str__(self):
      
class Jugada(object):
   def __init__(self,combinacion,chequeo,k):
      self.combinacion=combinacion
      self.chequeo=chequeo
      self.k=k
   def __str__(self):
       

class ListaJugadas(object):
   def __init__(self,iterador,k):
      self.listaJugadas=[]
      self.iterador=iterador
      self.k=k
   def appendJugada(self,objeto):
   def esJugadaCompatible(self,objeto):
   def generarCombinacion(self):
      siguienteCombinacion=next(self.iterador)
      auxiliar=Jugada(siguienteCombinacion,Chequeo(0,0,self.k),self.k)
      while (not self.esJugadaCompatible(auxiliar)):
         try:
             print("DESCARTE",siguienteCombinacion)
             siguienteCombinacion=next(self.iterador)
             auxiliar=Jugada(siguienteCombi7nacion,Chequeo(0,0,self.k),self.k)
         except StopIteration:
             print("ERROR: Las respuestas son inconsistentes")
             return None
      return siguienteCombinacion
   def generarJugada(self,combina):
      ''' Obtiene el chequeohumano de la permutacion "combina", comprueba su validez, inserta
          la jugada obtenida en la lista y genera una nueva permutacion. '''
      Checkeo.getChequeoHumano();
   def __str__(self):

def main():
   listaColores=["blanco","gris","marron","negro","rojo","verde"]
   k=4
   print("Lista de colores: ",listaColores)
   print("Numero de elementos: ",k)
   iterador=combinatoria.permutaciones_random(listaColores,k)
   combina=next(iterador)
   nuevaJugada=Jugada(combina,Chequeo(0,0,k),k)
   lista=ListaJugadas(iterador,k)
   while ((nuevaJugada.combinacion!=None) and ((nuevaJugada.chequeo.muertos!=k) or (nuevaJugada.chequeo.muertos==-1))):#-1 cuando se quiera salir del juego
      nuevaJugada=lista.generarJugada(nuevaJugada.combinacion)
   print("El juego ha terminado")
if __name__=="__main__":
   main()

