#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
fecha2 = "hola"
print("Día: " , end="")
for i in fecha:
     if i in range(4,10) == "/" :
        print ("  Mes: ", end="")
        

     else:
        print (i, end="")    

