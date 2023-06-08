'''
Escribir un programa que contenga una contraseña inventada, que le pregunte al
usuario la contraseña, y no le permita continuar hasta que la haya ingresado
correctamente
'''

contrasena = input("\nIngrese su nueva contrasena: ")
ingreso = ""

while contrasena != ingreso:
    ingreso = input("\nIngrese su contrasena: ")
    if contrasena == ingreso:
        print("\n¡Contrasena correcta, bienvenido!\n")
    else:
        print("\n¡Contrasena incorrecta!")
