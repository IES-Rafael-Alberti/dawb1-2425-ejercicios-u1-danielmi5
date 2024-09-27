#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
precioNoIVA = float(input("Escribe un precio: "))
print ("""Tipos IVA:
1. IVA General: 21%
2. IVA Reducido: 10%.
3. IVA Superreducido: 4%.
4. Actividades exentas de IVA: No hay""")


eleccion = float(input("Escribe una opción: "))
while (eleccion<1 or eleccion>4):
  print ("Número equivocado, debe estar entre (1-4).")
  eleccion = float(input("Escribe otra opción: "))
  
if (eleccion == 1):
  IVA = 1.21
  print ("Precio con IVA: "+str(precioNoIVA*IVA))
if (eleccion == 2):
  IVA = 1.10
  print ("Precio con IVA: "+str(precioNoIVA*IVA))
if (eleccion == 3):
  IVA = 1.04
  print ("Precio con IVA: "+str(precioNoIVA*IVA))
if (eleccion == 4):
  IVA = 1
  print ("Precio con IVA: "+str(precioNoIVA*IVA))

