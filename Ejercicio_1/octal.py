#Binario, octal, hexadecimal

'''
Realiza un  programa que  convierta un  numero  decimal
a binario, octal y hexadecimal, al final  deberá mostrar 
cual es su resultado
'''

try:
    numero = int(input("\nIngrese un numero entero: "))
    binario = ""
    octal = ""
    hexadecimal = ""

    if numero == 0:
        print("\nEl numero en binario es 0")
    else:
        aux = numero #Para binario
        while aux >= 1:
            binario = str(aux%2) + binario #Calculo el modulo y lo convierte en una cadena
            aux = int(aux/2) #Tambien puedo utilizar la parte entera //
        
        aux = numero #Para octal
        while aux >= 1:
            octal = str(aux%8) + octal #Calculo el modulo y lo convierte en una cadena
            aux = int(aux/8) #Tambien puedo utilizar la parte entera //
    
        aux = numero #Para hexadecimal
        while aux >= 1:
            if aux % 16 < 10:
                hexadecimal = str(aux%16) + hexadecimal
                aux = int(aux/16)
            elif aux % 16 == 10:
                hexadecimal = 'A' + hexadecimal
                aux = int(aux/16)
            elif aux % 16 == 11:
                hexadecimal = 'B' + hexadecimal
                aux = int(aux/16)
            elif aux % 16 == 12:
                hexadecimal = 'C' + hexadecimal
                aux = int(aux/16)
            elif aux % 16 == 13:
                hexadecimal = 'D' + hexadecimal
                aux = int(aux/16)
            elif aux % 16 == 14:
                hexadecimal = 'E' + hexadecimal
                aux = int(aux/16)
            elif aux % 16 == 15:
                hexadecimal = 'F' + hexadecimal
                aux = int(aux/16)

    print("\nEl numero en binario es {}".format(binario))
    print("El numero en octal es {}".format(octal))
    print("El numero en hexadecimal es {}".format(hexadecimal))
except:
    print("\nEl dato ingresado no es valido")
print("")