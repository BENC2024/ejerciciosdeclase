
try:
    num = int(input("\nIngrese un numero entero positivo: "))
    numero = num
    factor = "1"
    primo = 2

    if num > 1:
        while num >= 2:
            if num%primo == 0:
                while num%primo == 0:
                    num = num/primo
                factor = factor+","+str(primo)
            else:
                primo += 1
        print("\nLos numeros factores de {} son: {}\n".format(numero,factor))
    else:
        print("\nSolo enteros positivos mayores que 1\n")
except:
    print("\nHas ingresado un dato erroneo\n")