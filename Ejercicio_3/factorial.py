
try:
    fack = int(input("\nIngrese numero entero positivo: "))
    resul = fack
    i = 1
    if fack == 0:
        print("\nEl factorial de 0! es: 1\n")
    elif fack > 0:
        while i < fack:
            resul = resul*(fack-i)
            i += 1

        print("\nEl factorial de {}! es {}\n".format(fack,resul))
    else:
        print("\nSolo enteros positivos\n")
except:
    print("\nHas ingresado un dato erroneo\n")