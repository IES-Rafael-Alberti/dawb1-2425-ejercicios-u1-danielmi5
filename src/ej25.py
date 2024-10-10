#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
if (len(fecha) == 10):
  print("Día: " + fecha[0:2] )
  print("Mes: " + fecha[3:5] )
  print("Año: " + fecha[6:10] )
else:
  if (len(fecha) == 8):
    print("Día: " + "0" + fecha[0] )
    print("Mes: " + "0" + fecha[2] )
    print("Año: " + fecha[4:8] )
  else:
    if (len(fecha) == 9 and "/" in fecha[1]):
      print("Día: " + "0" + fecha[0] )
      print("Mes: " + fecha[2:4] )
      print("Año: " + fecha[5:9] )
    else:
      print("Día: " + fecha[0:2] )
      print("Mes: " + "0" + fecha[3] )
      print("Año: " + fecha[5:9] )
       
    


