def dame_entero():
    cadena = input("Introduce un entero: ")
    return cadena

def comprobar_entero(cadena):
    cadena.strip()
    valor = dame_entero()
    boo = valor.isdigit()
    if boo == False:
        while boo == False:
            valor = input("ERROR, introduce un entero").strip()
            boo = valor.isdigit()

    return valor
       
def hola(x):
    assert x>0, "Hola, numero equivocado"






def main():
    valor = dame_entero()
    print("Has introducido el número: {valor}")

if __name__ == "__main__":
    main()