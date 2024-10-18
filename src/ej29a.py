#Cálculo de un número aleatorio entre dos valores
import random
def numRandom(min,max):
    num = random.randrange(min,max) 
    return num
def comprobar_num(num):
    while num.isdigit() == False:
        num = input("ERROR: Debe introducir un número:").replace(" ","")
        if num.isdigit() == True:
            return int(num)
    while num.isdigit() == True:
        return int(num)

def main():
    min1 = input("El mínimo del numero aleatorio es: ")
    min2 = comprobar_num(min1)

    max1 = input("El máximo del numero aleatorio es: ")
    max2 = comprobar_num(max1)

    num_random = numRandom(min2,max2 + 1)
    print("El número es:",num_random)
if __name__ == "__main__":
    main()