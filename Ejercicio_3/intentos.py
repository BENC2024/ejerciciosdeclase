
nombre = input("\nIngrese su nombre: ")
contrasena = input("Ingrese su contrasena: ")
ingreso = ""
intento = 5  #Suponiendo que tiene cinco intentos

while contrasena != ingreso:
    print("\n--------------------------------")
    ingreso = input("\nIngrese su contrasena: ")
    if contrasena == ingreso:
        print("\n¡Contrasena correcta {}!\n".format(nombre))
        break
    else:
        print("\n¡Contrasena incorrecta!")
        if intento <= 5 and intento > 1:
            print("¡Solo le quedan {} intentos".format(intento))
            intento -= 1
        elif intento == 1:
            print("¡Solo le quedan {} intento".format(intento))
            intento -= 1
        else:
            print("El sistema ha sido bloqueado\n")
            break
