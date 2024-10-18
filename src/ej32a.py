#Calcular la serie de Fibonacci hasta un número dado

def comprobar_num(num: str) -> int:
  if num.isdigit() == True:
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir un número: ").replace(" ","")
      if num.isdigit() == True:
        return int(num)

def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    secuencia = fibonacci (num - 1) + fibonacci (num - 2)
    return secuencia

def main():
  print ("Introduce un número:")
  num = input("").replace(" ","")
  num = comprobar_num(num)
  print ("La secuencia de Fibonacci es: ",fibonacci(num))
  
  

if __name__ == "__main__":
    main()