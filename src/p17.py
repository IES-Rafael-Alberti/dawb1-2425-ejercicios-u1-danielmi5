#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido

name = input("Introduce tu nombre: ")
num = int(input("Introduce un número: "))
contador = 0
while (contador<num):
    print(name)
    contador += 1