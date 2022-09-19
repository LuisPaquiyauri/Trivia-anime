#Mi trivia
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random
import time

iniciar_trivia = True  
intentos = 0  
jugador_turnos = []

print(GREEN+"¡Bienvenidos a mi trivia sobre animes!\n"+RESET)
time.sleep(1)
print(GREEN+"Pondremos a prueba tus conocimientos"+RESET)
time.sleep(1)

nombre=input(GREEN+"Ingresa tu nombre: "+RESET)
time.sleep(1)

print(GREEN+"\nHola", nombre,"deberás escribir la letra de la alternativa que consideres correcta luego presionar enter. En el caso de que tu respuesta sea correcta se te premiará con un número aleatorio entre 5 y 10, pero si fallas se te restará un número aleatorio del 1 al 5. Los puntajes son acumulativos, te deseo suerte!"+RESET)
time.sleep(1)

while iniciar_trivia==True:
  correcta=0
  incorrecta=0
  puntaje=random.randint(0,10)
  time.sleep(1)
  
  intentos+=1
  print("\nIntento número: ",intentos)
  input("Presione enter para continuar")
  print(CYAN+"Comenzarás con:",puntaje,"puntos"+RESET)
  
  for numero_carga in range(5,0,-1):
    print(numero_carga)
    time.sleep(1)

  #Pregunta 1
  print(YELLOW+"\n1) ¿Quién es el personaje principal de Boku no hero?"+RESET)
  lista1=[BLUE+"a) Deku","b) Meliodas","c) Naruto","d) Goku"+RESET]
  for element in lista1:
    print(element)
  
  respuesta_1=input(GREEN+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1=input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_1=="a":
    puntaje+=random.randint(5,10)
    correcta+=1
    print("Muy bien",nombre,"!")
  else:
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto",nombre,"!")
  time.sleep(1)
  print(MAGENTA+nombre,"llevas",puntaje,"puntos."+RESET)
  time.sleep(1)
  
  #Pregunta 2
  print(YELLOW+"\n2) ¿Cuál de estos animes pertenece al género Seinen?"+RESET)
  lista2=[BLUE+"a) Dragon Ball Super","b) Bleach","c) Overlord","d) Anohana"+RESET]
  for element in lista2:
    print(element)
  
  respuesta_2=input(GREEN+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_2 not in ("a","b","c","d","x"):
    respuesta_2=input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_2=="x":
    puntaje+=random.randint(1,5)
    incorrecta+=1
    print("Este es un mensaje secreto")
  elif respuesta_2=="a":
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto!", nombre, "Dragón ball es un anime de Shonen")
  elif respuesta_2=="b":
    puntaje+=random.randint(5,10)
    incorrecta+=1
    print("Incorrecto!", nombre, "Bleach es un anime de Shonen")
  elif respuesta_2=="c":
    puntaje-=random.randint(1,5)
    correcta+=1
    print("Muy bien", nombre,"!")
  else:
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto!", nombre, "Anohana es un anime de drama")
  time.sleep(1)
  print(MAGENTA+nombre,"hasta ahora tienes",puntaje,"puntos."+RESET)  
  time.sleep(1)  
  
  #Pregunta 3
  print(YELLOW+"\n3) ¿Cuál de estos animes pertenece al género Shounen?"+RESET)
  lista3=[BLUE+"a) Ao Ashi","b) Kanojo","c) Bakuten","d) One Piece"+RESET]
  for element in lista3:
    print(element)
  
  respuesta_3=input(GREEN+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3=input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_3=="d":
    puntaje+=random.randint(5,10)
    correcta+=1
    print("Muy bien",nombre,"!")
  else:
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto",nombre,"!")
  time.sleep(1)
  print(MAGENTA+nombre,"llevas",puntaje,"puntos."+RESET)  
  time.sleep(1)
  
  #Pregunta 4
  print(GREEN+"\nLa siguiente pregunta es la última", nombre,"si aciertas podrías hasta duplicar tu puntaje, ánimo!")
  input("Presione enter para continuar"+RESET)
  print(YELLOW+"\n4) ¿Cuál de los siguientes animes es de Mecha?"+RESET)
  lista4=[BLUE+"a) Darling in the FranXX","b) Oregairu","c) Made in Abyss","d) Karekano"+RESET]
  for element in lista4:
    print(element)
  
  respuesta_4=input(GREEN+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_4 not in ("a","b","c","d","x"):
    respuesta_4=input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_4=="a":
    print("Correcto!")
    puntaje=puntaje*2
    correcta+=1
  elif respuesta_4=="b":
    print("Incorrecto!")
    puntaje=puntaje+5  
    incorrecta+=1
  elif respuesta_4=="c":
    print("Incorrecto!")
    puntaje=puntaje-5
    incorrecta+=1
  else:
    print("Incorrecto!")
    puntaje=puntaje/2
    incorrecta+=1
  time.sleep(1)
  print(MAGENTA+nombre,"llevas",puntaje,"puntos."+RESET) 
  time.sleep(1)
  
  #Ruleta
  print(GREEN+"\nJugaremos la ruleta de puntaje final")
  numero_carga2=int(input("\n¿Cuántas veces quieres girar la ruleta? \n"+RESET))
  for ruleta in range(1,numero_carga2+1):
    e=random.randint(1,10)
    if ruleta==numero_carga2:
      print("Intento final, resultado: ",e)
      puntaje+=e
      time.sleep(1)
    else:
      print("Intento N°",ruleta,", resultado: ",e)
      time.sleep(1)
  time.sleep(1) 
    
  #Final
  print("\nCantidad de respuestas correctas: ",correcta)
  time.sleep(1)
  print("Cantidad de respuestas incorrectas: ",incorrecta)
  time.sleep(1)
  
  print(GREEN+"\nGracias",nombre,"por jugar mi trivia, alcanzaste",puntaje,"puntos."+RESET)
  
  jugador_turnos.append(puntaje)

  print(GREEN+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si": 
   print(GREEN+"\nSecuencia de puntaje por cada turno: "+RESET,jugador_turnos)
   print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False