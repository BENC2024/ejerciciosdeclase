'''
Elaboraremos un programa  que  convierta  un  numero binario
ingresado por teclado a numero  decimal, al final  deberá mostrar
cual es su equivalencia
'''

try:
    binario = int(input("\nIngrese numero binario a convertir: "))
    b = binario
    i = 0
    decimal = 0

    if binario >= 0:
        while binario > 0:
            if binario%10 <= 1:
                decimal = decimal + (binario%10)*(2**i)
                binario = int(binario/10)
                i += 1
            else:
                break

        if binario == 0:
            print("\n{} en numero decimal es {}\n".format(b,decimal))
        else:
            print("\nSolo se admiten numeros en binario\n")
    else:
        print("\nNo se admite signo negativo\n")

except:
    print("\nHas ingresado un dato erroneo\n")