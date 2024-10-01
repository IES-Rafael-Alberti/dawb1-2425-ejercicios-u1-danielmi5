#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
precioNoIVA = float(input("Escribe un precio: "))
iva = float(input("Introduce el IVA (1-100): "))
importe_IVA = (iva*precioNoIVA)/100
print("El precio final con IVA es : " , precioNoIVA+importe_IVA)