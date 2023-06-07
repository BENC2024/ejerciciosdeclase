'''
Elaborar un programa  que  convierta  un  numero decimal 
ingresado  por teclado a numero  binario, al final  deberá 
mostrar cual es su equivalencia
'''

try:
    numero = int(input("\nIngrese un valor: "))
    binario = ""

    if numero == 0:
        print("\nEl numero en binario es 0\n")
    else:
        while numero >= 1:
            binario = str(numero%2) + binario #Calculo el modulo y lo convierte en una cadena
            numero = int(numero/2) #Tambien puedo utilizar la parte entera //
        print("\nEl numero en binario es {}\n".format(binario))
except:
    print("\nEl dato ingresado no es admitido\n")