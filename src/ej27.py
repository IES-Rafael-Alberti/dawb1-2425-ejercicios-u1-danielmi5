#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre = input ("Introduce el nombre del producto: ")
numero = (input("Introduce el número de unidades del producto: "))
numero2 = numero
precio = (input("Introduce el precio con decimales"))
precio = round(float(precio),2)


if len(numero2)==1:
    numero = ("00"+numero)
if len(numero2)==2:
    numero = ("0"+numero)

   


print(precio)