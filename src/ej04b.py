celsius = float(input("Escribe una temperatura en grados Celsius: "))
fahrenheit = (1.8*celsius) + 32
print("La temperatura en grados Farenheit es :" , "{:.2f}".format(fahrenheit) , "ºF" + "(" , "{:.2f}".format(celsius) , "ºC)")