
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