#.strip() elimina los espacios de los lados |  .isdigit() Comprueba si la cadena es un digito, si es así lo pone True  | 
cadena = input("Introduce un entero: ").strip()
cadena = cadena.replace(" ", "\r")
print (cadena)
boo = cadena.isdigit()
print (boo)
if int(cadena)>0:
    

    if boo == False:
        while boo == False:
            cadena = input("ERROR, introduce un entero")
            boo = cadena.isdigit()


         
