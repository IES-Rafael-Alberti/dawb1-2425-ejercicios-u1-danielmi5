#  recibe un número y retorna una cadena de caracteres con el resultado de la función.

def main():
  return 0
  
if __name__ == "__main__":
  main()
  

def calcula_IVA(n):
  while (n<0):
    print("ERROR")
    n = int(input("Introduce n (entero positivo): "))

  resultado = (str((n*(n+1))/2))
  return resultado
  