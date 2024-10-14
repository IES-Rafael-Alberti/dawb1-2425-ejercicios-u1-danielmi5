#Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, (mas adelante veremos como detectar los fallos usando try y except)
def pedir_num():
    contador = 0
    suma = 0
    num = input("Introduce un número:").replace(" ","")
    while num != "fin":
        if num.isdigit()==True:
            suma += int(num)
            contador +=1
            num = input("Introduce un número o 'fin':").replace(" ","")
        else:
            num = input("Valor erróneo, introduce un numero o 'fin': ").replace(" ","")
        num = num.lower()

        
    return suma, contador
    
def main():
    suma, contador = pedir_num()

    print("La suma es:",suma)
    print("La cantidad de números es:",contador)
    print("La media es:",suma/contador)
if __name__ == "__main__":
    main()