'''
Realiza un programa que  me calcule el  área  del  circulo, 
la  cual el usuario ingresa el  valor del  radio
'''

import math #Se utiliza para importar una libreria 

try:
    radio = float(input("\nIngrese el radio del circulo: "))
    area_circulo = math.pi*(radio**2)

    print("el area del circulo es {:.4f}".format(area_circulo))
except:
    print("\nEl dato ingresado no es valido\n")