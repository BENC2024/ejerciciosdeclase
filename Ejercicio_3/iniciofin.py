'''
Elabora un programa que muestre una lista de números la cual pida al usuario desde
que numero quiere y hasta que numero quiere mostrar por ejemplo si  ingresa  2  y 10
debería mostrar  2,3,4,5,6,7,8,9,10 o si  ingresa  2  y -10  debería mostrar
2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10
'''

try:
    a = int(input("\nIngrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("")
    if a < b:
        for i in range(a,b+1,1):
            print(i, end=", ")
        print("\n")
    elif a > b:
        for i in range(a,b-1,-1):
            print(i, end=", ")
        print("\n")
    else:
        print(f"\n{a}, Ambos numeros son iguales\n")
except:
    print("\nSe ha ingresado un dato no valido\n")