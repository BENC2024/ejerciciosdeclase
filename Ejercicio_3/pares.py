'''
Realiza un programa que muestre los numeros pares desde un numero
predeterminado hasta otro numero predeterminado
'''

try:
    a = int(input("\nIngrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("")
    if a > 0 and b > 0:
        if a > b:
            for i in range(b,a+1):
                if i%2 == 0:
                    print(i)
        elif a < b:
            for j in range(a,b+1):
                if j%2 == 0:
                    print(j)
        else:
            print("\nAmbos numeros son iguales")
        print("")

    else:
        print("\nSolo se permiten numeros positivos\n")
except:
    print("\nSe ha ingresado un dato no valido\n")


'''
complicandome solo jsjs
    if a > 0 and b > 0:
        if a < b:
            if a%2 == 0:
                if b%2 == 0:
                    for i in range(a,b+1,2):
                        print(i)
                else:
                    for i in range(a,b,2):
                        print(i)
            else:
                if b%2 == 0:
                    for i in range(a+1,b+1,2):
                        print(i)
                else:
                    for i in range(a+1,b,2):
                        print(i)
        elif a > b:
            if a%2 == 0:
                if b%2 == 0:
                    for i in range(b,a+1,2):
                        print(i)
                else:
                    for i in range(b+1,a+1,2):
                        print(i)
            else:
                if b%2 == 0:
                    for i in range(b,a,2):
                        print(i)
                else:
                    for i in range(b+1,a,2):
                        print(i)
        else:
            print("\nAmbos numeros son iguales")
        print("")

    else:
        print("\nSolo numeros enteros positivos\n")
except:
    print("\nSe ha ingresado un dato no valido\n")
'''

