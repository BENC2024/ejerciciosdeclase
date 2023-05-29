
try:
    x = float(input("\nIngrese el primer numero: "))
    y = float(input("Ingrese el segundo numero: "))
    z = float(input("Ingrese el tercer numero: "))

    result = (x+y+z)/3

    print("\nEl numero promedio de {}, {} y {} es {:.3f}\n".format(x,y,z,result))
except:
    print("\nError en los datos\n")