
try:
    x = float(input("\nIngrese primer numero: "))
    y = float(input("Ingrese segungo numero: "))
    z = float(input("Ingrese tercer numero: "))

    print("\nLos numeros ingresados son: {}, {}, {}".format(x,y,z))

    if x == y and y == z:
        print("Los numeros ingresados son iguales")
    else:
        if x > y:
            if x > z:
                if y > z:
                    print("Los numeros en orden son {}, {}, {}".format(x,y,z))
                else: # y < z
                    print("Los numeros en orden son {}, {}, {}".format(x,z,y))
            else: # x <= z
                if y > x:
                    print("Los numeros en orden son {}, {}, {}".format(z,y,x))
                else:
                    print("Los numeros en orden son {}, {}, {}".format(z,x,y))
        
        else: # y > x
            if y > z:
                if x > z:
                    print("Los numeros en orden son {}, {}, {}".format(y,x,z))
                else: # x < z
                    print("Los numeros en orden son {}, {}, {}".format(y,z,x))
            else: # y < z
                if y > x:
                    print("Los numeros en orden son {}, {}, {}".format(z,y,x))
                else:
                    print("Los numeros en orden son {}, {}, {}".format(z,x,y))
    print("")
except:
    print("\nError ingresando datos\n")