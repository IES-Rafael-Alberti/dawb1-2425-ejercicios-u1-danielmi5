#Realiza un programa en Python que solicite un nombre y una edad.

###Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
###El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".

nombre = input("Introduce un nombre: ")
nombre = nombre.replace(" ", "")
if nombre == "":
    nombre = "Desconocido"
edad = int(input ("Itroduce un número: "))
while (edad<0 or edad>125):
    edad = input("ERROR  ||  Introduce un número entre 0 y 125: ")

rango = 125 - edad

print("Te llamas ",nombre," y tienes ",edad," años, te quedan aún", rango ,"años por cumplir")


