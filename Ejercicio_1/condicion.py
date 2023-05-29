
try:
    x = float(input("\nx: "))
    y = float(input("y: "))

    if x > y:
        print("x es mayor que y")
    elif x < y:
        print("x es menor que y")
    else:
        print("x es igual que y")
except:
    print("\nEl dato no es valido\n")
