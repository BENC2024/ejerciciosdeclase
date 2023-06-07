'''
Dada la siguiente secuencia, hallar la expresión matemática para  realizar el  calculo
de tal forma que el  usuario  pueda  ingresar un numero y  la  calcule la secuencia
hasta ese numero ingresado1 2 4 8 16 32 64 128 256 512 1024 2048 ......si el  usuario
ingresa 200 debe mostrar la  secuencia  así,  1 2 4 8 16 32 64 128
'''

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
