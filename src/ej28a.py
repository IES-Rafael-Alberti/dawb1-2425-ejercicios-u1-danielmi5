#Calcular el área de un triángulo a partir de tres lados
import math

def calcular_area(a: float, b: float, c: float) -> float:

    sp = (a+b+c) /2
    area = math.sqrt(sp *(sp-a)*(sp-b)*(sp-c))
    
    return area

def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]
    
    pos_punto = valor.find(".")
    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[pos_punto + 1:]

    return valor.isdigit()


def introduce_numero(msj: str) -> float:
    valor = input(msj).strip().replace(",",".")

    while comprobar_float (valor) == False:
        print("\n**ERROR** Numero invalido!")
        valor = input(msj).strip().replace(",",".")
    return float(valor)

def comprobar_triangulo_valido(a,b,c):
    return (a+b >c) and (a+c >b) and (b+c > a)

def main():
    print("Dame los 3 lados.. ")
    ladoA = introduce_numero("Lado1:")
    ladoB = introduce_numero("Lado2:")
    ladoC = introduce_numero("Lado3:")
    if comprobar_triangulo_valido (ladoA,ladoB,ladoC):
        area = calcular_area(ladoA,ladoB,ladoC)
        print("El area del triangulo con lados ({:.2f},{:.2f},{:.2f})".format(ladoA,ladoB,ladoC,area),"es: ", area)
    else:
        print ("El triangulo con lados ({:.2f},{:.2f},{:.2f}) no es valido!".format(ladoA,ladoB,ladoC))

if __name__ == "__main__":
    main()