#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


frase = input("Introduce una frase: ")
esarf = ""

for letra in frase:
    esarf = letra + esarf

print(esarf)