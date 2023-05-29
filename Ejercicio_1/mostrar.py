
try:
    nombre = str(input("\nIngrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    identificacion = int(input("Ingrese su identificacion: "))

    if edad >= 18:
        print("\nTu, {}, identificado con numero {} eres mayor de edad".format(nombre,identificacion))
    else:
        print("\nTu, {}, identificado con numero {} eres menor de edad".format(nombre,identificacion))
except:
    print("\nEl dato ingresado no es valido")
print("")