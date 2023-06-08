'''
Modificar el programa anterior para que después de cada intento agregue una pausa
cada vez mayor, utilizando la función sleep del módulo time.
'''

import time

contrasena = input("\nIngrese su nueva contrasena: ")
ingreso = ""
intento = 5
seg = 1

while contrasena != ingreso:
    print("\n--------------------------------")
    ingreso = input("\nIngrese su contrasena: ")
    seg += 1
    if contrasena == ingreso:
        print("\n¡Contrasena correcta, bienvenido!\n")
    else:
        print("\n¡Contrasena incorrecta!")
        if intento <= 5 and intento > 1:
            print("¡Solo le quedan {} intentos, esperar {} seg.".format(intento,seg))
            intento -= 1
        elif intento == 1:
            print("¡Solo le quedan {} intento, esperar {} seg.".format(intento,seg))
            intento -= 1
        else:
            print("El sistema ha sido bloqueado\n")
            break
        for i in range(0,seg,1):
                time.sleep(1)
                print(".")
