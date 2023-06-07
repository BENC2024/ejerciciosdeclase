'''
Realiza un programa que muestre los numeros impares desde un numero
predeterminado hasta otro numero predeterminado
'''

try:
    a = int(input("\nIngrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("")

    if a > 0 and b > 0:
        if a < b:
            if a%2 == 1:
                if b%2 == 1:
                    for i in range(a,b+1,2):
                        print(i)
                else:
                    for i in range(a,b,2):
                        print(i)
            else:
                if b%2 == 1:
                    for i in range(a+1,b+1,2):
                        print(i)
                else:
                    for i in range(a+1,b,2):
                        print(i)
        elif a > b:
            if a%2 == 1:
                if b%2 == 1:
                    for i in range(b,a+1,2):
                        print(i)
                else:
                    for i in range(b+1,a+1,2):
                        print(i)
            else:
                if b%2 == 1:
                    for i in range(b,a,2):
                        print(i)
                else:
                    for i in range(b+1,a,2):
                        print(i)
        else:
            print("Ambos numeros son iguales")
        print("")

    else:
        print("\nSolo numeros enteros positivos\n")
except:
    print("\nSolo se admiten numeros\n")