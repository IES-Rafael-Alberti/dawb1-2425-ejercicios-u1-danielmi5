#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

email = input("Introduce un email (example@name.ej): ")
posicion = email.find("@")
emailNew = email.replace(email[posicion+1:len(email)], "ceu.es")
print (emailNew)
