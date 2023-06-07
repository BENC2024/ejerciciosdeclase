'''
Elaboraremos un programa  que  convierta  un  numero binario
ingresado por teclado a numero  decimal, al final  deberá mostrar
cual es su equivalencia
'''

binario = int(input("\nIngrese numero binario: "))
div = binario
i = 0
decimal = 0

while div > 0:
    decimal = decimal + (div%10)*(2**i)
    div = int(div/10)
    i += 1

print("\n{} en numero decimal es {}\n".format(binario,decimal))

