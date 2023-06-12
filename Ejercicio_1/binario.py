'''
Elaborar un programa  que  convierta  un  numero decimal 
ingresado  por teclado a numero  binario, al final  deberá 
mostrar cual es su equivalencia
'''

try:
    numero = int(input("\nIngrese un valor a convertir a binario: "))
    num = numero
    binario = ""
    if numero == 0:
        print("\nEl numero {} en binario es 0\n".format(num))
    elif numero >= 0:
        while numero > 0:
            binario = str(numero%2) + binario #Calculo el modulo y lo convierte en una cadena
            numero = int(numero/2) #Tambien puedo utilizar la parte entera //
        print("\nEl numero {} en binario es {}\n".format(num,binario))
    else:
        print("\nSolo se admiten numeros mayores a cero\n")
except:
    print("\nEl dato ingresado no es admitido\n")