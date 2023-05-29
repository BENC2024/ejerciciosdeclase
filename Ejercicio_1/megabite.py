
try:
    mega = float(input("ingrese los datos en megabyte: "))

    print("el resultado en bits es: {}".format(int(mega*1024*1024*8)))
    print("el resultado en bytes es: {}".format(int(mega*1024*1024)))
    print("el resultado en kilobytes es: {}".format(int(mega*1024)))
    print("el resultado en gigabytes es: {}".format(mega/1024))
except:
    print("\nEl dato ingresado es erroneo\n")