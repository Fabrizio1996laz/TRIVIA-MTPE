# En primer lugar, se muestra por pantalla un texto de bienvenida indicando que tipo de trivia realizar.
RED = '\033[31m'
RESET = '\033[39m'
GREEN = '\033[92m'
BLUE = '\033[94m'
print ("")
print("\033[31m BIENVENID@ A LA TRIVIA SOBRE HISTORIA DEL PERÚ".center(100))
print (""+ RESET)
# Se pinta las palabras con red y con reset finalizas el color de la palabra.
# El .center es para centrar la palabra.
print ("")
print ("Responde a continuación una serie de preguntas: ")
print ("Debes ingresar el número correspondiente, desde el 1 hasta el 4, de acuerdo a la alternativa.")
print ("Podrás responder la pregunta solo 2 veces, comencemos ")
print ("")
print ("¿Peruano, qué tanto sabes del Perú?".center(100))
print ("[1/3]".center(100))
print ("")

print ("¿Quién cantó por primera vez el Himno Nacional del Perú en setiembre de 1821?")
print ("(1). Rosa Merino ")
print ("(2). José de la Torre Ugarte ")
print ("(3). Rosa Mariño ")
print ("(4). Micaela Bastidas ")
print("\n\n\n\n\n")

numero = int (input("Ingresa nuevamente tu respuesta: "))
validador = 0
while validador < 2:
  if numero == 1:
    print("Tu respuesta es correcta fue Rosa Merino ")
    break
  elif numero == 2:
    print("Tu respuesta es incorrecta")
    validador +=1
  elif numero == 3:
    print("Tu respuesta es incorrecta")
    validador +=1
  elif numero == 4:
    print ("Tu respuesta es incorrecta") 
    validador +=1
  else:
    print("Elijiste una opción correcta incorrecta!")        
    validador +=1
  numero = int (input("Ingresa nuevamente tu respuesta: "))

if validador >1:
  print (" la respuesta correcta es la 1 su nombre es Rosa Merino")
print ("\n\n")
print ("\033[94m Continuamos ")
print (""+ RESET)
print ("[2/3]".center(100))
print ("")

print ("¿De qué nacionalidad era el libertador Don José de San Martín?")
print ("(1). Peruana ")
print ("(2). Boliviana ")
print ("(3). Argentina ")
print ("(4). Colombiana ")
print("\n\n\n\n\n")
numero_2 = int (input("Tu respuesta es: "))
validador_2 = 0
while validador_2 < 2:
    if numero_2 == 1:
      print("Tu respuesta es incorrecta ")
      validador_2 +=1
    elif numero_2 == 2:
      print("Tu respuesta es incorrecta")
      validador_2 +=1
    elif numero_2 == 3:
      print("Tu respuesta es correcta ,erá Argentino")
      break
    elif numero_2 == 4:
      print ("Tu respuesta es incorrecta") 
      validador_2 +=1
    else:
      print("Elijiste una opción correcta incorrecta!")        
      validador_2 +=1
    numero_2 = int (input("Ingresa nuevamente tu respuesta: "))

if validador_2 > 1:
    print (" la respuesta correcta es la 3 era Argentino")

print ("\n\n")
print ("\033[94m Continuamos ")
print (""+ RESET)

print ("[3/10]".center(100))
print ("")

print ("¿Cuáles son los símbolos patrios del Perú?")
print ("(1). La Escarapela, El Escudo y el Himno Nacional ")
print ("(2). El escudo, La Bandera del Perú y el Himno Nacional ")
print ("(3). La vicuña, la cornucopia y el árbol de la quina ")
print ("(4). La vicuña, la Bandera del Perú y la Escarapela ")
print("\n\n\n\n\n")

numero_3 = int (input("Tu respuesta es: "))
validador_3 = 0
while validador_3 < 2:
    if numero_3 == 1:
      print("Tu respuesta es incorrecta ")
      validador_3 +=1
    elif numero_3 == 2:
      print("Tu respuesta es incorrecta")
      validador_3 +=1
    elif numero_3 == 3:
      print("Tu respuesta es correcta ,erá Argentino")
      break
    elif numero_3 == 4:
      print ("Tu respuesta es incorrecta") 
      validador_3 +=1
    else:
      print("Elijiste una opción correcta incorrecta!")        
      validador_3 +=1
    numero_3 = int (input("Tu respuesta es: "))

if validador_3 > 1:
    print (" la respuesta correcta es la 3 era La vicuña, la Bandera del Perú y la Escarapela")

print ("\033[92m ESTA TRIVIA FINALIZÓ , HASTA PRONTO".center(100))
print (""+ RESET)