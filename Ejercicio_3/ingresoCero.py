'''
Realice un programa que acumule todo numero  ingresado  por  el  usuario, el
programa  deberá  finalizar cuando el  usuario ingrese el numero 0,  el  programa  al
final  debe mostrar cual  es el numero acumulado

'''
try:
    x = 1
    suma = 0
    print("\nEl ciclo termina cuando ingrese un cero.\n")

    while x != 0:
        x = float(input("Ingrese un numero: "))
        suma = suma + x

    print("\nEl suma de los numeros ingresados es {}\n".format(suma))
except:
    print("\nHas ingresado un dato erroneo\n")