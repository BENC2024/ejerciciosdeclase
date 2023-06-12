'''
De acuerdo con la tabla realice un programa que convierta una unidad a otra unidad,
por  ejemplo  si el usuario ingresa 1 MB el  sistema  deberá  arrojar  el siguiente
resultado
1MB son:
8388608 Bits
1048576 Bytes
1024 Kb
0.000976563 GB
'''

try:
    mega = float(input("\ningrese los datos en megabyte: "))

    if mega >= 0:
        print("\nEl resultado en bits es: {}".format(mega*1024*1024*8))
        print("El resultado en bytes es: {}".format(mega*1024*1024))
        print("El resultado en kilobytes es: {}".format(mega*1024))
        print("El resultado en gigabytes es: {}\n".format(mega/1024))
    else:
        print("\nNo se admiten numeros menores a cero\n")
except:
    print("\nEl dato ingresado es erroneo\n")