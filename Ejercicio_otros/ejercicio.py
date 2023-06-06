'''
Analisis
necesito los valores para calcular el IMC, en este caso son la altura y el peso
despues se procede a hacer el calculo del indice, para ello se aplica la formula
IMC = masa/altura^2 con valores positivos y masa y altura reales
analisis de masas y alturas reales
despues se hace una comparacion mediante una tabla de valores estandarizados
debajo del peso, peso normal, sobrepeso, obesidad 1, 2, 3 y asi conocer su condicion

criterios
<18.5 esta por debajo del peso
entre 18.5 y 24.4 peso saludable
entre 25 y 29.9 sobrepeso
entre 30 y 34.9 obesidad I
entre 35 y 39.9 obesidad II
>40 obesidad III

utilizando numeros decimales

EL IMC no es el mismo para niños que para adultos

'''

try:
    mayor = input("\nLa persona es mayor de edad? si/no: ")

    if mayor == 'si':

        altura = float(input("\nIngrese su altura en metros: "))
        masa = float(input("\nIngrese su masa en kilogramos: "))

        if masa > 0 and altura > 0:

            if altura < 3.0:
                IMC = masa/(altura**2)
                print("\nTu indice es. IMC={},".format(IMC))
                
                if IMC < 18.5:
                    print("Por lo tanto esta por debajo del peso saludable\n")
                elif IMC >= 18.5 and IMC<24.9999999999:
                    print("Por lo tanto esta en el peso saludable\n")
                elif IMC >= 25 and IMC<29.99999999999:
                    print("Por lo tanto esta en sobrepeso\n")
                elif IMC >= 30 and IMC<34.99999999999:
                    print("Por lo tanto esta en obesidad tipo I\n")
                elif IMC >= 35 and IMC<39.99999999999:
                    print("Por lo tanto esta en obesidad tipo II\n")
                elif IMC > 40:
                    print("Por lo tanto esta en obesidad tipo III\n")
            else:
                print("\nSolo se admiten valores de alturas menores a 3 y en metros\n")

        else:
            print("\nNo se admiten valores negativos o cero\n")

    elif mayor == 'no':
        print("\nPara los menores de edad, se utiliza una tabla de percentiles")
        print("La cual permite saber la salud y el IMC del menor.\n")
    else:
        print("\nSolo se admite si o no\n")

except:
    print("\nError ingresando datos\n")
