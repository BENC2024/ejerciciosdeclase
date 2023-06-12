'''
Cree un algoritmo  que  permita intercambiar el valor 
de una variable a=3, b=2 deberá quedar a=2 y b=3
'''

try:
    a = input("\nIngrese primer numero: ")

    b = input("Ingrese segundo numero: ")

    print("\nEl valor anterior es a={} y b={}".format(a,b))

    c = a

    a = b

    b = c

    print("El valor actual es a={} y b={}".format(a,b))
except:
    print("\nEl valor ingresado es erroneo\n")
