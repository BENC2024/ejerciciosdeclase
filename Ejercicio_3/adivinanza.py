'''
Utilizando la función randrange del módulo random, escribir un programa que obtenga
un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
sin son menores o mayores que el número a adivinar, hasta que el usuario ingrese el
número correcto
'''

import random

try:
    numero = 0
    print("\n¡Adivinar el numero!\n")
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa otro numero: "))

    if a == b:
        print("\nAmbos numeros son iguales, no se puede jugar\n")
    else:
        if a > b:
            numAletorio = random.randint(b,a)
        elif a < b:
            numAletorio = random.randint(a,b)
        print("\n¡¡Numero aleatorio generado!!")    

        while numAletorio != numero:
            print("\n--------------------------------")
            numero = int(input("\nIngresa un numero entre {} y {}: ".format(a,b)))
            if a<=numero<=b or b<=numero<=a:
                if numero > numAletorio:
                    print("El numero ingresado es menor, sigue intentando!!")
                elif numero < numAletorio:
                    print("El numero ingresado es mayor, sigue intentando!!")
                else:
                    print("\n¡¡¡EL NUMERO {} ES EL CORRECTO: [{}] !!!\n".format(numero,numAletorio))
            else:
                print("\nEl numero ingresado esta fuera de rango entre {} y {}".format(a,b))
except:
    print("\n¡¡Has ingresado un dato erroneo, no se puede continuar!!\n")
