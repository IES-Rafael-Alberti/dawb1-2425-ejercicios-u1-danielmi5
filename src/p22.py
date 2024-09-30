#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Introduce una frase: ")
vocal = str(input("Introduce una vocal: "))

while (vocal != "a" and vocal !="e" and vocal!="i" and vocal!="o" and vocal!="u"):
    print ("No has introducido una vocal")
    vocal = input("Introduce una vocal: ")
    

print (frase+str(vocal.upper()))