#NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.

def main():
  cadena = convertir_temp()
  print(cadena)
  
if __name__ == "__main__":
  main()
  

def convertir_temp(farenheit):
  farenheit = float(input("Introduce una temperatura en grados farenheit:"))
  celsius = (farenheit-32)/1.8
  cadena = ("{:.2f}".format(celsius) + " °C" + " (""{:.2f}".format(farenheit)+ " °F)")
  return cadena
  
  