#Escribir un programa que determine si un número es primo
import math
def comprobar_num(num: str) -> int:
  if num.isdigit() == True:
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir un número: ").replace(" ","")
      if num.isdigit() == True:
        return int(num)

def comprobar_primo(num: int):
  if num < 2:
    print ("No es primo")
  elif num == 2:
    print ("Es primo")  
  elif num != 2 and num % 2 == 0:
    print ("No es primo")
  else:
    terminar = False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
      if num % i == 0:
        print ("No es primo")
        terminar = True
        break
    if terminar == False:
      print ("Es primo")
    else:
      pass 
      
    
  
def main():
  print ("Introduce un número:")
  num = input("").replace(" ","")
  num = comprobar_num(num)
  num = comprobar_primo(num)

if __name__ == "__main__":
    main()