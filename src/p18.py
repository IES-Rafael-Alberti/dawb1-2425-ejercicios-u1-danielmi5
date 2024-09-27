#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("Introduce tu nombre completo: ")
contador = 0
contador = 0
while(contador<3):
    print (nombre.lower())
    contador += 1
contador = 0
while(contador<3):
    print (nombre.upper())
    contador += 1

