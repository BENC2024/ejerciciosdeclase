
try:
    x = float(input("\nIngrese el primer numero: "))
    y = float(input("Ingrese el segundo numero: "))

    if x > y:
        print("\nEl primer numero es mayor {}\n".format(x))

    elif x < y:
        print("\nEl segundo numero es mayor {}\n".format(y))

    else:
        print("\nAmbos numeros son iguales\n")
except:
    print("\nError ingresando datos\n")