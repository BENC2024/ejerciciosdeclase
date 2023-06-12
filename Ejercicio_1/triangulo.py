'''
Crea un programa que  permita calcular el área del triangulo
'''

try:
    base = float(input("\nIngrese la base: "))
    altura = float(input("Ingrese la altura: "))

    if base >= 0 and altura >= 0:
        print("\nEl area del triangulo de base {} y altura {} en metros cuadrados es {}\n".format(base,altura,(base*altura/2)))
    else:
        print("\nNo se admiten numeros negativos\n")
except:
    print("\nEl dato ingresado no es valido\n")