# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

n = int(input("Introduce n: "))

while (n<0):
    print("ERROR")
    n = int(input("Introduce n (entero positivo): "))

print ("La suma es: " ,int((n*(n+1))/2))