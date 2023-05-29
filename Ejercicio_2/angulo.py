
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