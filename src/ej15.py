#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

#Hecho suponiendo que es tras un año
dinero = float(input("Introduce el dinero depositado: "))

cantidad1 = round(dinero*1.04 , 2) 
cantidad2 = round(cantidad1*1.04 , 2)
cantidad3 = round(cantidad2*1.04 , 2)

print("Cantidad de ahorros tras: Primer año: " +str(cantidad1)+ ", segundo año: "+str(cantidad2)+", tercer año: " +str(cantidad3))
