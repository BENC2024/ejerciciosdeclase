'''
Escribir una función 'es_potencia_de_dos' que reciba como parámetro un número
natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
también incluir una función que, dados dos números naturales pasados como
parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango
formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar
la función es_potencia_de_dos, descrita en el punto anterior.Números perfectos y
números amigo
'''

def es_potencia_de_dos(num):
    exp = 0
    while (2**exp) <= num:
        if (2**exp) == num:
            potencia = True
        else:
            potencia = False
        exp = exp + 1
    return potencia
    
def suma_potencia(num1,num2):
    suma = 0
    msj = ""
    for i in range(num1,num2+1,1):
        if es_potencia_de_dos(i) == True:  #Utilizando la funcion es_potencia_2
            msj = msj + str(i) + "+"
            suma = suma + i
    msj = msj.removesuffix("+") #Me remueve el ultimo caracter de final, sufijo
    msj = msj + " = " + str(suma)
    return msj

try:
     
    numero = int(input("\nIngrese el numero: "))

    if numero > 0:
        if es_potencia_de_dos(numero) == True:
            print("\nEl numero {} es potencia de 2".format(numero))
        elif es_potencia_de_dos(numero) == False:
            print("\nEl numero {} no es potencia de 2".format(numero))
    else:
        print("\nSolo se permiten numeros naturales (mayores a cero)")
    
    print("\nSuma de potencias de 2 (dos numeros mayores que cero):")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    if num1 > 0 and num2 > 0:
        print(f"\nLa suma de las potencias de 2 entre {num1} y {num2} es:")
        if num1 <= num2:
            print(suma_potencia(num1,num2))
        elif num1 > num2:
            print(suma_potencia(num2,num1))
        print("")
    else:
        print("\nSolo se permiten numeros naturales (mayores a cero)\n")

except:
    print("\nHa ocurrido un error en la ejecucion\n")