'''
Escribir un programa que contenga una contraseña inventada, que le pregunte al
usuario la contraseña, y no le permita continuar hasta que la haya ingresado
correctamente
'''

nombre = input("\nIngrese su nombre: ")
contrasena = input("Ingrese su contrasena: ")
ingreso = ""

while contrasena != ingreso:
    ingreso = input("\nIngrese su contrasena: ")
    if contrasena == ingreso:
        print("\n¡Contrasena correcta {}!\n".format(nombre))
    else:
        print("\n¡Contrasena incorrecta!")
