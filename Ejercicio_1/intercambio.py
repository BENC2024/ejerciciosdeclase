
try:
    a = int(input("\nIngrese primer numero: "))

    b = int(input("Ingrese segundo numero: "))

    print("\nEl valor anterior es a={} y b={}".format(a,b))

    c = a

    a = b

    b = c

    print("El valor actual es a={} y b={}".format(a,b))
except:
    print("\nEl valor ingresado es erroneo\n")
