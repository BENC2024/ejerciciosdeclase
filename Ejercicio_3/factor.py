'''
Escribir una aplicación que reciba un número entero k 
e imprima su descomposición en factores primos.
'''

try:
    num = int(input("\nIngrese un numero entero positivo mayor a 1: "))
    numero = num
    factor = ""
    divisores = []
    primo = 2

    if num > 1:
        for i in range(1,num,1):
            if num%i == 0:
                divisores.append(i)
        while num >= 2:
            if num%primo == 0:
                while num%primo == 0:
                    num = num/primo
                factor = factor+str(primo)+", "
            else:
                primo += 1
        factor = factor.removesuffix(", ") #elimina la ultima coma y la almacena
        print(f"\nLos divisores de {numero} son: {divisores}")
        print("\nLos factores primos de {} son: {}\n".format(numero,factor))
    else:
        print("\nSolo enteros positivos mayores que 1\n")
except:
    print("\nHas ingresado un dato erroneo\n")