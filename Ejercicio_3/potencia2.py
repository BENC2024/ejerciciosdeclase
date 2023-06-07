'''
Escribir una función 'es_potencia_de_dos' que reciba como parámetro un número
natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
también incluir una función que, dados dos números naturales pasados como
parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango
formado por esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar
la función es_potencia_de_dos, descrita en el punto anterior.Números perfectos y
números amigo
'''

try:
    def es_potencia_de_dos(num):
        exp = 0
        if num == 1:
            return True
        else:
            while 2**exp < num:
                exp = exp+1
                if 2**exp == num:
                    return True
                elif 2**exp > num:
                    return False
    
    numero = int(input("\nIngrese un numero: "))

    if numero > 0:
        if es_potencia_de_dos(numero) == True:
            print("\nEl numero {} es potencia de 2\n".format(numero))
        elif es_potencia_de_dos(numero) == False:
            print("\nEl numero {} no es potencia de 2\n".format(numero))
    else:
        print("\nSolo se admiten numeros mayores a cero\n")
except:
    print("\nSolo se admiten numero y no letras\n")