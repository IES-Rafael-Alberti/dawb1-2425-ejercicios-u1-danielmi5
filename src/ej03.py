ancho = 17
alto = 12.0
print ("Los datos son: ancho=17 y alto 12.0")
print ("""Estas son las operaciones:
       1. ancho / 2 
       2. ancho // 2
       3. alto / 3
       4. 1 + 2 * 5
Intenta adivinarlas""")
intento1 = float(input("Primera operación: "))
tipo1 = (input("Tipo operación 1: "))

intento2 = int(input("Segunda operación: "))
tipo2 = (input("Tipo operación 2: "))

intento3 = float(input("Tercera operación: "))
tipo3 = (input("Tipo operación 3: "))
intento4 = int(input("Cuarta operación: "))
tipo4 = (input("Tipo operación 4: "))


resultado1 = ancho/2
resultado2 = ancho//2
resultado3 = alto/3
resultado4 = 1 + 2 * 5

print("Resultados:")

if (intento1 == resultado1):
  print("1: Bien!!!")
else :
  print ("1: MAL")
if (intento2 == resultado2):
  print("2: Bien!!!")
else :
  print ("2: MAL")
if (intento3 == resultado3):
  print("3: Bien!!!")
else :
  print ("3: MAL")
if (intento4 == resultado4):
  print("4: Bien!!!")
else :
  print ("4: MAL")

print("Tipos:")

if (tipo1 in str(type(resultado1))):
  print("1: Bien!!!")
else :
  print ("1: MAL")
if (tipo2 in str(type(resultado2))):
  print("2: Bien!!!")
else :
  print ("2: MAL")
if (tipo3 in str(type(resultado3))):
  print("3: Bien!!!")
else :
  print ("3: MAL")
if (tipo4 in str(type(resultado4))):
  print("4: Bien!!!")
else :
  print ("4: MAL")
