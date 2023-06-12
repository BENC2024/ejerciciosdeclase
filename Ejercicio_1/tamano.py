'''
Crea un programa que lea un valor  y  muestre en pantalla
la longitud de ese valor por ejemplo si el usuario ingresa
"Diego Fernando"  deberá decir  que ha ingresado  14
caracteres
'''

dato = input("\nIngrese el dato: ")

longi = 0 #Se utiliza para saber el tamaño de un caracter

for i in dato: # i es un caracter de la variable dato
    longi += 1

print("\nEl dato dado: {}, cuenta con {} caracteres\n".format(dato,longi))




#NONE : es un valor nulo, que no guarda nada

#amb = None

'''if amb:
    print("muestra algo")
else:
    print("no muestra nada")

for i in range(5):
    print(str(i))
'''