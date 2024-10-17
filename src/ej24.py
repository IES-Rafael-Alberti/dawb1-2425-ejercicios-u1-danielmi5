#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = str(input("Introduce un precio con dos decimales: "))
posicion = precio.find(".")
posicion = precio.find(",")
print("Número de euros: " + precio[0:posicion])
print("Número de céntimos: " + precio[posicion+1:len(precio)])

