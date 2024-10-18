#recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def main():
  precio_sin_IVA = float(input("Introduce un precio sin IVA:"))
  tipo_IVA = int(input("Introduce cuanto IVA: "))
  calcula_IVA(precio_sin_IVA, tipo_IVA)
  
if __name__ == "__main__":
  main()
  

def calcula_IVA(precio_sin_IVA, tipo_IVA):
  precio_con_IVA = (tipo_IVA/100 + 1)*precio_sin_IVA
  print ("El precio con IVA es:" ,precio_con_IVA)

  # return puesto para que funcione el test
  return precio_con_IVA
  
  
  