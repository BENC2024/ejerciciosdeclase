
try:
    x = int(input("\nIngrese un numero: "))

    if x%2 == 0:
        print("\nEl numero {} es un numero par\n".format(x))
    else:
        print("\nEl numero {} es un numero impar\n".format(x))
except:
    print("\nError en los datos\n")