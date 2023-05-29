
try:
    nombre = input("\nIngrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    if edad > 18:
        print("\nTu, {}, puedes entrar\n".format(nombre))
    elif edad < 18:
        print("\nTu, {}, no puedes entrar\n".format(nombre))
    else:
        print("\nPor favor muestra identificacion\n")
except:
    print("\nError ingresando datos\n")