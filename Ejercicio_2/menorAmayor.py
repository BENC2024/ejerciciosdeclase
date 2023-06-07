'''
Elabora un programa que me muestre en pantalla de forma ordenada de menor a
mayor dos números ingresados por teclado, por ejemplo si ingreso 5 Y 4 deberá
mostrar, "los números ingresados  son  5 y 4 y organizados  son  4, 5"
'''

try:
    x = float(input("\nIngrese primer numero: "))
    y = float(input("Ingrese segungo numero: "))

    print("\nLos numeros ingresados son {}, {}".format(x,y))

    if x > y:
        print("\nEl orden es {}, {}\n".format(y,x))
    elif x < y:
        print("\nEl orden es {}, {}]\n".format(x,y))
    else:
        print("\nAmbos numeros son iguales\n")
except:
    print("\nError ingresando datos\n")