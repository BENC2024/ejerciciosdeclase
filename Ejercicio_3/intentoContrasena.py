'''
Modificar el programa anterior para que solamente permita una cantidad fija de
intentos.
'''

contrasena = input("\nIngrese su nueva contrasena: ")
ingreso = ""
intento = 5  #Suponiendo que tiene cinco intentos

while contrasena != ingreso:
    print("\n--------------------------------")
    ingreso = input("\nIngrese su contrasena: ")
    if contrasena == ingreso:
        print("\n¡Contrasena correcta, bienvenido!\n")
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
