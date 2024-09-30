#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = str(input("Introduce un precio con dos decimales: "))
print("Número de euros: ", end="")
for i in precio:
     if i == "." or i == ",":
        print ("\n"+"Número de céntimos: ", end="")
     else:
        print (i, end="")    

