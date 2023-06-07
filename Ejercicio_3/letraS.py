'''
El usuario ingresa por teclado una oración por ejemplo 'Las cuentas claras y el
chocolate espeso' el programa debe permitir buscar la  letra que el usuario quiere
buscar y contar cuantas letras hay; Ejemplo: letra a buscar 's'; 'Las cuentas claras y
el chocolate espeso' posee 4 letras 's'
'''

texto = input("\nIngrese un texto: ")

abc = input("\nListo, Cual caracter que quiere buscar: ")
x = 0

for i in texto:
    if i == abc or i == abc.upper(): #upper se utiliza para convertir a mayusculas
        x = x+1

if len(abc) == 1: #len es el ancho del caracter
    if x > 1:
        print("\nHay {} letras '{}'\n".format(x,abc))
    elif x == 1:
        print("\nHay {} letra '{}'\n".format(x,abc))
    else:
        print("\nNo se encontro ese caracter '{}'\n".format(abc))
else:
    print("\nSolo se admite una sola caracter\n")
