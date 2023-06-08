'''
Escribir una aplicación que reciba un número entero k 
e imprima su descomposición en factores primos.
'''

try:
    num = int(input("\nIngrese un numero entero positivo: "))
    numero = num
    factor = ""
    primo = 2

    if num > 1:
        while num >= 2:
            if num%primo == 0:
                while num%primo == 0:
                    num = num/primo
                factor = factor+str(primo)+", "
            else:
                primo += 1
        factor = factor.removesuffix(", ") #elimina la ultima coma y la almacena
        print("\nLos factores primos de {} son: {}\n".format(numero,factor))
    else:
        print("\nSolo enteros positivos mayores que 1\n")
except:
    print("\nHas ingresado un dato erroneo\n")