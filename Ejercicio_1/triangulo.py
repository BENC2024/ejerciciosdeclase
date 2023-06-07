'''
Crea un programa que  permita calcular el área del triangulo
'''

try:
    base = float(input("\nIngrese la base(m): "))
    altura = float(input("Ingrese la altura(m): "))

    print("\nEl area del triangulo de base {} y altura {} en metros cuadrados es {}\n".format(base,altura,(base*altura/2)))
except:
    print("\nEl dato ingresado no es valido\n")