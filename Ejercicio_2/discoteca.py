'''
Elabora un programa para una discoteca que necesita controlar el acceso a las
personas la  cual pida el nombre a una persona y su edad, en caso  que  sea  mayor
de  18  lo deje ingresar, si es  menor  de edad debe  mostrar un  mensaje diciendole
que no puede ingresar y si  tiene 18 años  debera  preguntar por su  identificación
'''
try:
    nombre = input("\nIngrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    if edad > 18:
        print("\nTu, {}, puedes entrar\n".format(nombre))
    elif edad < 18:
        print("\nTu, {}, no puedes entrar\n".format(nombre))
    else:
        print("\nPor favor {} muestra identificacion\n".format(nombre))
except:
    print("\nError ingresando datos\n")