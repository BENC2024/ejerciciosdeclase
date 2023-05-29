
try:
    num = float(input("\nIngrese numero: "))

    if num-int(num/1) > 0 or num-int(num/1) < 0: # num//1
        print("\n{} es un numero racional\n".format(num))
    else:
        print("\n{} es un numero entero\n".format(int(num)))
except:
    print("\nError ingresando datos\n")
