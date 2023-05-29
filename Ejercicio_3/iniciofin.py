
try:
    a = int(input("\nIngrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("")
    if a < b:
        for i in range(a,b+1,1):
            print(i)
    elif a > b:
        for i in range(b,a+1,1):
            print(i)
    else:
        print("\nAmbos numeros son iguales")
    print("")
except:
    print("\nSe ha ingresado un dato no valido\n")