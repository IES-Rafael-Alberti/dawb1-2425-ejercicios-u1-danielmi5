#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

lista= input("Introduce la lista de la compra entre comas: ")
listaVertical = lista.replace(", ", "\n")
print (listaVertical)