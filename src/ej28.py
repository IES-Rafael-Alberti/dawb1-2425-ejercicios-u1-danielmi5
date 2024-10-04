# Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.
###El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
###Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".

num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce otro número entero: "))
menor = 0 ; mayor = 0

if num1 == num2:
    print ("Los números no pueden ser iguales")
elif num1>num2:
    menor = num2
    mayor = num1
    longitud = mayor - menor
    print("El número menor es el ",menor," y entre ellos ellos existen ",longitud," números enteros")
else:
    menor = num1
    mayor = num2
    longitud = mayor - menor
    print("El número menor es el ",menor," y entre ellos ellos existen ",longitud," números enteros")






         


















