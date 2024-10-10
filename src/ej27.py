#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre = input ("Introduce el nombre del producto: ") ; numero = (input("Introduce el número de unidades del producto: ")) ; precio = float(input("Introduce el precio: "))
costeTotal = int(numero)*precio
precio = str(round(float(precio),2))
posicion = (precio.find("."))
valor0 = "0"; longitudEnteros = 6  - posicion ; longitudDecimales = len(precio) - posicion - 1

print(nombre, end="--")
if longitudDecimales == 1:
    print(valor0*longitudEnteros+ precio + "0", end="--")
else:
    print(valor0*longitudEnteros+ precio, end="--")
    
longitudNumUnidades = len(numero)
if (longitudNumUnidades == 2):
    print("0"+numero, end="--")
else:
    if(longitudNumUnidades == 1):
        print("00"+numero, end ="--")
    else: 
        print(numero[:3], end= "--")
        
posicion = (str(costeTotal).find("."))
longitudDecimales = len(str(costeTotal)) - posicion -1
longitudEnteros = 8 - posicion
        
if longitudDecimales == 1:
    print(valor0*longitudEnteros + str(costeTotal) + "0")
else:
    print(valor0*longitudEnteros + str(costeTotal))
    
print("nombre--precio--unidades--costeTotal")


        


    


    




