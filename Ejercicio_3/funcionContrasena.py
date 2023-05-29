
nombre = input("\nIngrese su nombre: ")
contrasena = input("Ingrese su contrasena: ")
ingreso = ""

def cuenta(contra):
    if contra == contrasena:
        return True
    else:
        return False

while contrasena != ingreso:
    ingreso = input("\nIngrese su contrasena: ")
    if cuenta(ingreso) == True:
        print("\n¡Contrasena correcta {}!\n".format(nombre))
        break
    else:
        print("\n¡Contrasena incorrecta!")
