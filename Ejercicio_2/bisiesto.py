#Bisiesto
'''
Utiliza una Estructura selectiva para averiguar si un
año leído de teclado es o no bisiesto
'''

try:
    anio = int(input("\nIngrese el año para saber si es un año bisiesto: "))
    if anio > 0:
        if anio >= 1582:
            if anio % 4 == 0 and anio % 100 != 0 and anio % 400 != 0:
                    print("\nEl año {} es un año bisiesto\n".format(anio))
            else:
                print("\nEl año {} no es un año bisiesto\n".format(anio))
        else:
            print("\nNo se admiten años menores a 1582\n")
    else:
        print("\nNo se admiten numero negativos\n")
except:
    print("\nEl dato ingresado es invalido\n")