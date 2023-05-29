
try:
    a = int(input("\nIngrese un valor: "))
    n = 0
    print("\nLas secuencias potencia de 2 hasta {} son: ".format(a))
    while a >= (2**n):
        valor = 2**n
        print(valor,end=" ")
        n = n+1
    print("\n")
except:
    print("\nHas ingresado un dato erroneo\n")
