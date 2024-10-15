#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

###El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
###Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10

num = int(input("Introduce un número: "))
incremento = int(input("Introduce un incremento: "))
while incremento < 0:
    incremento = input("ERROR || Introduce el incremento (>0): ")
totalSerie= int(input("Introduce un total de la serie: "))
while totalSerie < 0:
    totalSerie = input("ERROR || Introduce el total de la serie (>0): ")

print("SERIE => ", end="")
if (num < 0):
    while num <= totalSerie:
        if num > (totalSerie - incremento) and num<=totalSerie:
            print(str(num))
            num += incremento
        else: 
            print(str(num) + "..", end="")
            num += incremento


else:
    while num <= totalSerie:
        if num > (totalSerie - incremento) and num<=totalSerie:
            print(str(num))
            num += incremento
        else: 
            print(str(num) + "-", end="")
            num += incremento
