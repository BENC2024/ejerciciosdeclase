'''
Al programa anterior debe modificarlo y agregarle que al final  muestre el numero
acumulado y la cantidad de numeros ingresados por el usuario
'''

try:
    x = 1
    suma = 0
    print("\nEl ciclo termina cuando ingrese un cero.\n")
    cont = 0

    while x != 0:
        x = float(input("Ingrese un numero: "))
        suma = suma + x
        cont += 1

    print("\nLos numeros ingresados fueron {}".format(cont-1))
    print("El suma de los numeros ingresados es {}\n".format(suma))
except:
    print("\nHas ingresado un dato erroneo\n")