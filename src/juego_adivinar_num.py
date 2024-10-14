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
  while num_dificultad.isdigit() == False:
      num_dificultad = input("ERROR: Debe introducir un número (1, 2 o 3): ").strip()
      while num_dificultad.isdigit() == True:
        if int(num_dificultad) >= 1 and int(num_dificultad) <=3:
          return int(num_dificultad) 
        else:
          num_dificultad = input("ERROR: Número equivocado (1, 2 o 3): ").strip()
          if num_dificultad.isdigit() == True and int(num_dificultad) >= 1 and int(num_dificultad) <=3:
            return int(num_dificultad)
  while num_dificultad.isdigit() == True:
    if int(num_dificultad) >= 1 and int(num_dificultad) <=3:
      return int(num_dificultad) 
    else:
      num_dificultad = input("ERROR: Introduce un número dentro del rango (1, 2 o 3): ").strip()
      if num_dificultad.isdigit() == True and int(num_dificultad) >= 1 and int(num_dificultad) <=3:
        return int(num_dificultad)    
    while num_dificultad.isdigit() == False:
      num_dificultad = input("ERROR: Debe introducir un número (1, 2 o 3): ").strip()
      
  return num_dificultad
  
def comprobar_entero_num(num):
  while num.isdigit() == False:
      num = input("ERROR: Debe introducir un número (1-100): ").replace(" ","")
      while num.isdigit() == True:
        if int(num) >= 1 and int(num) <=100:
          return int(num) 
        else:
          num = input("ERROR: Introduce un número dentro del rango (1-100): ").replace(" ","")
          if num.isdigit() == True and int(num) >= 1 and int(num) <=100:
            return int(num)
  while num.isdigit() == True:
    if int(num) >= 1 and int(num) <=100:
      return int(num) 
    else:
      num = input("ERROR: Introduce un número dentro del rango (1-100): ").replace(" ","")
      if num.isdigit() == True and int(num) >= 1 and int(num) <=100:
        return int(num)    
    while num.isdigit() == False:
      num = input("ERROR: Debe introducir un número (1-100): ").replace(" ","")
        
  

def comprobar_num (num, random, intentos):
  while (num != random and intentos > 0):
    if num > random:
      if num < random + 10:
        print ("No, el número es menor (🔥🔥)")
      else: 
        print ("No, el número es menor (🧊🧊)")
    if num < random:
      if num > random - 10:
        print ("No, el número es mayor (🔥🔥)")
      else: 
        print ("No, el número es mayor (🧊🧊)")
    if intentos > 1:
      print("Te quedan", intentos , "intentos: ", end="")
    else:
      print("Te queda", intentos , "intento: ", end="")
    intentos -= 1
    num = (input()).replace(" ","")
    num = comprobar_entero_num (num)
  
  return num
  
  
def main():
  print("Juego adivinar número (1-100)")
  print("🔥: El número esta a menos de 10 números   ||   🧊: El número esta a más de 10 números "  )
  print("""Dificultad:
  1: Fácil (10 Intentos)
  2: Normal (5 intentos)
  3: Imposible (1 intento)""")
  numDif = (input("Elige dificultad: ")).strip()
  num_dificultad = comprobar_entero_dificultad(numDif)
  intento = dificultad(num_dificultad)
  num = introduce_num ("Adivina el número: ").replace(" ","")
  num = comprobar_entero_num (num)
  random = numRandom()
  
  if comprobar_num (num,random,intento) == random :
    print ("Has acertado, enhorabuena!!!")
  else:
    print ("Has fallado 😂😂😂")
    print ("El número era:" , random)
    
if __name__ == "__main__":
  main()