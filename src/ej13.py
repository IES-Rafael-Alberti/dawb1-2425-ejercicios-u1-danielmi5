#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

n = int(input("Introduce un número : "))
m = int(input("Introduce otro número : "))

while (m==0):
    print ("No se puede dividir por 0")
    m = int(input("Introduce otro número : "))

c  = n//m
r = n%m

print ("la división de " + str(n) +  " entre " + str(m) + " da un cociente " + str(c) + " y un resto " + str(r) + " , donde " + str(n) + " y " + str(m) + " son los números introducidos por el usuario, y " + str(c) + " y " + str(r) + " son el cociente y el resto de la división entera respectivamente.")





#"la división de " + str(n) +  " entre " + str(m) + " da un cociente " + str(c) + " y un resto " str(r) " , donde " + str(n) + " y " + str(m) + " son los números introducidos por el usuario, y " + str(c) + " y " + str(r) + " son el cociente y el resto de la división entera respectivamente."