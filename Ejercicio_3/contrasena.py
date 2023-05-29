
nombre = input("\nIngrese su nombre: ")
contrasena = input("Ingrese su contrasena: ")
ingreso = ""

while contrasena != ingreso:
    ingreso = input("\nIngrese su contrasena: ")
    if contrasena == ingreso:
        print("\n¡Contrasena correcta {}!\n".format(nombre))
    else:
        print("\n¡Contrasena incorrecta!")
