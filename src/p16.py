#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
PRECIOPAN = 3.39 ;  descuento = PRECIOPAN * 0.6
precioPanNoDia = PRECIOPAN - descuento
numPanNoDia = int(input("Introduce el número de barras vendidas que no son del día: "))
precioTotal = numPanNoDia * precioPanNoDia

print ("Precio habitual: "+str(PRECIOPAN))
print ("Precio con descuento para barras no del día: "+str(round(precioPanNoDia, 2)))
print ("Precio total para barras no del día:  "+str(round(precioTotal, 2)))
