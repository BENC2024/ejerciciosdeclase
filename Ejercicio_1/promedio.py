
'''
Suma de 3 numeros ingresados por  teclado  y calcular el promedio
'''

try:
    a = float(input("\nIngrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    c = float(input("Ingrese el tercer numero: "))

    print("\nEl promedio de los numero {}, {} y {} es: {:.3f}".format(a,b,c,(a+b+c)/3))
except:
    print("\nEl dato ingresado no es valido\n")