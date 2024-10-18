#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

precioConIVA = float(input("Introduce un precio con IVA: "))
precioSinIVA = precioConIVA / 1.10
pagadoIVA = precioConIVA - precioSinIVA
print ("IVA pagado: ", "{:.2f}".format(pagadoIVA))
print ("Importe sin IVA: ", "{:.2f}".format(precioSinIVA))