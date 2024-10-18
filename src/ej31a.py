#Mostrar todos los divisores de un número

def comprobar_num(num: str) -> int:
  if num.isdigit() == True:
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir un número: ").replace(" ","")
      if num.isdigit() == True:
        return int(num)

def divisores_num(num: int):
  for i in range (1,num + 1):
    if num % i == 0:
      if i != num:
        print (i, end="-")
      else: 
        print(i)
      

def main():
  print ("Introduce un número:")
  num = input("").replace(" ","")
  num = comprobar_num(num)
  print ("Es divisible por: ", end="")
  divisores_num(num)
  

if __name__ == "__main__":
    main()