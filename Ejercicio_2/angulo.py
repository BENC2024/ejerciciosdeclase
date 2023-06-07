'''
Un ángulo se considera agudo si es menor de 90 grados, obtuso si es mayor de 90
grados y recto si es igual a 90 grados. Utilizando esta información, escribir un
algoritmo que acepte un ángulo en grados y visualice el tipo de ángulo
correspondiente a los grados introducidos
'''

try:
    angulo = float(input("\nIngrese angulo: "))

    if angulo >= 0:
        if angulo < 90:
            print("\nEl angulo de",angulo,"grados es un angulo agudo\n")
        elif angulo == 90:
            print("\nEl angulo de",angulo,"grados es un angulo recto\n")
        else:
            print("\nEl angulo de",angulo,"grados es un angulo obtuso\n")
    else:
        print("\nNo se admiten angulos negativos\n")
except:
    print("\nHas ingresado un dato erroneo\n")