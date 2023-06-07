'''
Elabora un programa que lea 3 números por  teclado y me los muestre  organizado de
mayor a menor por ejemplo si ingreso 53, 10 Y 24 deberá mostrar, "los números
ingresados  son  53, 10 Y 24 y organizados de forma descendente son  53, 24, 10
'''

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