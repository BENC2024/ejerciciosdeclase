
'''
Elabora un programa que le pida al usuario una base y un
exponente, posteriormente mostrar el  resultado  al usuario
'''

try:
    base = float(input("\ningrese la base: "))
    exponente = float(input("ingrese el exponente: "))

    if base == 0 and exponente <= 0:
        print("\nNo se puede hacer la operacion")
    else:
        print("\nla base {} y el exponente {} da como resultado: {}\n".format(base,exponente,base**exponente))
except:
    print("\nHas ingresado dato erroneo\n")