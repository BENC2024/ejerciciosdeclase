
try:
    mega = float(input("\ningrese los datos en megabyte: "))

    print("\nEl resultado en bits es: {}".format(int(mega*1024*1024*8)))
    print("El resultado en bytes es: {}".format(int(mega*1024*1024)))
    print("El resultado en kilobytes es: {}".format(int(mega*1024)))
    print("El resultado en gigabytes es: {}\n".format(mega/1024))
except:
    print("\nEl dato ingresado es erroneo\n")