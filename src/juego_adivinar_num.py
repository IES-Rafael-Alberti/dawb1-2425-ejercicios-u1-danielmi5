import random
def numRandom():
  numAleatorio = random.randrange(1,100)
  return int(numAleatorio)

def introduce_num(msj: str):
  num = input(msj)
  return num

intentos = 0
def dificultad(num_dificultad):
  global intentos
  if num_dificultad == 1:
    intentos = 9
      
  elif num_dificultad == 2:
    intentos = 4
      
  elif num_dificultad == 3:
    intentos = 0
    
  return intentos
    
def comprobar_entero_dificultad (num_dificultad):
  if num_dificultad.isdigit() == False:
    while num_dificultad.isdigit() == False:
      print ("Valor errónea (1, 2 o 3)")
      num_dificultad = input("Elección: ")
  if num_dificultad.isdigit() == True:
    num_dificultad = int(num_dificultad)
  while num_dificultad <1 or num_dificultad >3:
      print ("Número equivocado (1, 2 o 3)")
      num_dificultad = int(input("Elección: "))
      
  return num_dificultad
  
def comprobar_entero_num(num):
  if num.isdigit() == False:
    while num.isdigit() == False:
      print ("**Valor erróneo**  Debe ser un número (1-100)")
      num = input("Elección: ")
  if num.isdigit() == True:
    num = int(num)
  while num <1 or num >= 100:
      print ("Número equivocado (1-100)")
      num = int(input("Elección: "))
  return num
      
  

def comprobar_num (num, random, intentos):
  while (num != random and intentos > 0):
    if num > random:
      print ("No, el número es menor")
    if num < random:
      print ("No, el número es mayor") 
    if intentos > 1:
      print("Te quedan", intentos , "intentos: ", end="")
    else:
      print("Te queda", intentos , "intento: ", end="")
    intentos -= 1
    num = (input())
    num = comprobar_entero_num (num)
  
  return num
  
  
def main():
  print("Juego adivinar número (1-100)")
  print("""Dificultad:
  1: Fácil (10 Intentos)
  2: Normal (5 intentos)
  3: Imposible (1 intento)""")
  numDif = (input("Elección: "))
  num_dificultad = comprobar_entero_dificultad(numDif)
  intento = dificultad(num_dificultad)
  num = introduce_num ("Adivina el número: ")
  num = comprobar_entero_num (num)
  random = numRandom()
  
  if comprobar_num (num,random,intento) == random :
    print ("Has acertado, enhorabuena!!!")
  else:
    print ("Has fallado 😂😂😂")
    
if __name__ == "__main__":
  main()