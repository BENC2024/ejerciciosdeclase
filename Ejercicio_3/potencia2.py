
try:
    numero = int(input("\nIngrese un numero: "))

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

    if numero > 0:
        if es_potencia_de_dos(numero) == True:
            print("\nEl numero {} es potencia de 2\n".format(numero))
        elif es_potencia_de_dos(numero) == False:
            print("\nEl numero {} no es potencia de 2\n".format(numero))
    else:
        print("\nSolo se admiten numeros mayores a cero\n")
except:
    print("\nSolo se admiten numero y no letras\n")