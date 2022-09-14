#COLORES
BLACK = '\033[30m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[39m'

#Variables
iniciar_trivia = True #variable true o false del inicio del juego
intentos = 0 #variable para los intentos
# Bienvenida al juego
print (GREEN+"Bienvenido a mi trivia sobre la selección peruana de fútbol ")
# Indicamos las reglas al usuario
print("\n INSTRUCCIONES: \n")
print("1) Comienzas con puntaje cero (0) \n")
print("2) Por cada respuesta correcta se suma 4 puntos \n")
print("3) Por cada respuesta incorrecta se resta dos\n")
print("4) Se asignará un puntaje aleatorio, el cual será sumado en caso de ser correcta la respuesta o restado en caso de ser incorrecta la respuesta")
print ("Pongamos a prueba tus conocimientos \n"+RESET)

# Instrucciones sobre cómo jugar:
print ("Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
import time

print("Cuál es tú nombre: \n")
nombre = input()
time.sleep(1.2)
print("\n¡Bienvenido ",nombre,"!"," \nComenzaremos la TRIVIA DEL HINCHA PERUANO \n")
#CICLO DEL JUEGO
while iniciar_trivia == True:
  #RANDOM
  import random
  intentos+=1
  puntaje=0

  print("\nIntento número: ",intentos)
  input("Presiona Enter para comenzar\n")

  # Pregunta 1
  print (CYAN+"1) ¿Cuál fue el último mundial en el que participó la selección peruana?\n")
  print ("a) Sudáfrica 2010")
  print ("b) España 1982")
  print ("c) Rusia 2018")
  print ("d) Catar 2022"+RESET)
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ").lower()
  # Verificamos que el usuario haya seleccionado una de las alternativas, de lo contrario la pregunta se repite
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta\n").lower()
  bonus = random.randint(0,3)
  #Calificamos la respuesta del usuario
  if respuesta_1 == "c":
    print("¡Bien",nombre,"!")
    puntaje = puntaje + 4 + bonus
    print("Obteniendo bonus 3,2,1...")
    time.sleep(1.5)
    print("Tu bonus es: ",bonus)
  else:
    print("Incorrecto")
    puntaje = puntaje -2 - bonus
  print(YELLOW+"Puntaje actual: ",puntaje,"\n"+RESET)
  time.sleep(2)
  # Pregunta 2
  print (CYAN+"2) ¿Quién marcó el último gol de la selección peruana en un mundial?\n")
  print("a) Jefferson Farfán")
  print("b) Paolo Guerrero")
  print("c) André Carrillo")
  print("d) Cristian Cueva"+RESET)
  #Almacenamos la respuesta 2
  respuesta_2 = input("\nTu respuesta: ").lower()
  # Verificamos que el usuario haya seleccionado una de las alternativas, de lo contrario la pregunta se repite
  while respuesta_2 not in ("a","b","c","d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta\n").lower()
  bonus2 = random.randint(0,3)
  #Calificamos la respuesta 2
  if respuesta_2 == "b":
    print("¡Correcto",nombre,"!")
    puntaje = puntaje + 4 + bonus2
    print("Obteniendo bonus 3,2,1...")
    time.sleep(1.5)
    print("Tu bonus es: ",bonus2)
  else:
    print("Incorrecto")
    puntaje = puntaje -2 - bonus2
  print(YELLOW+"Puntaje actual: ",puntaje,"\n"+RESET)
  time.sleep(2)
  # Pregunta 3
  print (CYAN+"3) ¿Cuál número de camiseta utilizó C. Cueva en el último mundial?\n")
  print("a) #8")
  print("b) #11")
  print("c) #10")
  print("d) #19"+RESET)
  #Almacenamos la respuesta 3
  respuesta_3 = input("\nTu respuesta: ").lower()
  # Verificamos que el usuario haya seleccionado una de las alternativas, de lo contrario la pregunta se repite
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta\n").lower()
  bonus3 = random.randint(0,3)
  #Calificamos la respuesta 3
  if respuesta_3 == "a":
    print("¡Muy bien",nombre,"!")
    puntaje = puntaje + 4 + bonus3
    print("Obteniendo bonus 3,2,1...")
    time.sleep(1.5)
    print("Tu bonus es: ",bonus3)
  else:
    print("Incorrecto")
    puntaje = puntaje -2 -bonus3
  print(YELLOW+"Puntaje actual: ",puntaje,"\n"+RESET)
  time.sleep(2)
  # Pregunta 4
  print (CYAN+"4) ¿Cuál fue el último cambio en el partido Francia vs Perú en Rusia2018?\n")
  print("a) Paolo Guerrero por Jefferson Farfán")
  print("b) Gianluca Lapadula por Paolo Guerrero")
  print("c) Paolo Guerrero por André Carrillo")
  print("d) Ruidiaz por Cristian Cueva"+RESET)
  #Almacenamos la respuesta 4
  respuesta_4 = input("\nTu respuesta: ").lower()
  # Verificamos que el usuario haya seleccionado una de las alternativas, de lo contrario la pregunta se repite
  while respuesta_4 not in ("a","b","c","d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta\n").lower()
  bonus4 = random.randint(0,3)
  #Calificamos la respuesta 4
  if respuesta_4 == "d":
    print("¡Correcto",nombre,"!")
    puntaje = puntaje + 4 + bonus4
    print("Obteniendo bonus 3,2,1...")
    time.sleep(1.5)
    print("Tu bonus es: ",bonus4)
  else:
    print("Incorrecto")
    puntaje = puntaje -2 -bonus4
  print(YELLOW+"Puntaje actual: ",puntaje,"\n"+RESET)
  time.sleep(2)
  # Pregunta 5
  print (CYAN+"5) ¿Cuál es el segundo apellido del Oreja Flores?\n")
  print("a) Perales")
  print("b) Peña")
  print("c) Peralta")
  print("d) Gonzales"+RESET)
  #Almacenamos la respuesta 5
  respuesta_5 = input("\nTu respuesta: ").lower()
  # Verificamos que el usuario haya seleccionado una de las alternativas, de lo contrario la pregunta se repite
  while respuesta_5 not in ("a","b","c","d"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta\n").lower()
  bonus5 = random.randint(0,3)
  #Calificamos la respuesta 5
  if respuesta_5 == "c":
    print("¡Genial",nombre,"!")
    puntaje = puntaje + 4 + bonus5
    print("Obteniendo bonus 3,2,1...")
    time.sleep(1.5)
    print("Tu bonus es: ",bonus5)
  else:
    print("Incorrecto")
    puntaje = puntaje -2 -bonus5
  print(YELLOW+"Puntaje actual: ",puntaje,"\n"+RESET)
  #Calificamos el juego del usuario
  print("Obteniendo calificación en 3,2,1...\n")
  time.sleep(3)
  if puntaje >15 and puntaje < 20:
    print(GREEN+"\nObtuviste ",puntaje," puntos, ¡Felicitaciones, eres un buen hincha de la selección",nombre,"!\n"+RESET)
    print("Número de intentos:",intentos)
  elif puntaje > 19:
    print(GREEN+"\nObtuviste ",puntaje," puntos, ¡Extraordinario, realmente eres un fiel hincha de la selección",nombre,"!\n"+RESET)
    print("Número de intentos:",intentos)
  else:
    print(GREEN+"\nObtuviste",puntaje,", ¡De seguro eres hincha de resultados",nombre,"!\n"+RESET)
    print("Número de intentos:",intentos)

  #Preguntamos si desea volver a jugar
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  #Validamos lo ingresado por el usuario
  if repetir_trivia != "si":
    print(YELLOW+"\n¡Esperamos que la hayas pasado bien ",nombre," vuelve cuando quieras!"+RESET)
    iniciar_trivia=False