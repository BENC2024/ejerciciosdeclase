'''
Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).
'''

contrasena = input("\nIngrese su nueva contrasena: ")
ingreso = ""

def cuenta(contra):
    if contra == contrasena:
        return True
    else:
        return False

while contrasena != ingreso:
    ingreso = input("\nIngrese su contrasena: ")
    if cuenta(ingreso) == True:
        print("\n¡Contrasena correcta, bienvenido!\n")
        break
    else:
        print("\n¡Contrasena incorrecta!")
