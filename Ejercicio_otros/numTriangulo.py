
try:
    num = int(input("\nIngrese la cantidad de filas para el triangulo: "))
    i = 1
    imp = ""
    while 2*num >= i:
        imp = str(i)+" "+imp
        print(imp)
        i = i+2
    print("")
except:
    print("\nHa ocurrido un error\n")