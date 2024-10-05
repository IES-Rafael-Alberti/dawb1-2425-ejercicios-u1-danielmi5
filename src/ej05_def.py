#recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def main():
  num = float(input("Introduce un precio sin IVA:"))
  tipo = int(input("Introduce cuanto IVA: "))
  return num, tipo
  
if __name__ == "__main__":
  main()
  

def calcula_IVA():
  precio_sin_IVA, tipo_IVA = main()
  precio_con_IVA = (tipo_IVA/100 + 1)*precio_sin_IVA
  print ("El precio con IVA es: ",precio_con_IVA)
  
  
  