'''
Analisis

Se necesita conocer los estudiantes que tienen diferentes pesos y clasificarlos
por lo tanto necesito como datos de entrada
numero de estudiantes y sus pesos para clasificarlos

'''

try:
    estud = int(input("\nIngrese el numero de estudiantes: "))
    dato = 0
    peso_1 = 0
    peso_2 = 0
    peso_3 = 0
    peso_4 = 0
    print("")
    i=1

    for i in range(1,estud+1,1):
        dato = float(input("Ingrese peso(kg) del estudiante {}: ".format(i)))
        if dato > 0 and dato < 40:
            peso_1 += 1
        elif dato <= 50:
            peso_2 += 1
        elif dato < 60:
            peso_3 += 1
        elif dato >= 60:
            peso_4 += 1
        else:
            print("\nNo se admiten numeros negativos o cero")
            peso_1 = 0
            peso_2 = 0
            peso_3 = 0
            peso_4 = 0
            break

    if peso_1 > 0 or peso_2 > 0 or peso_3 > 0 or peso_4 > 0:
        print("\nLa cantidad de estudiantes con peso menor a 40 kg es: {}".format(peso_1))
        print("La cantidad de estudiantes con peso entre 40 a 50 kg es: {}".format(peso_2))
        print("La cantidad de estudiantes con peso mayor a 50 y menor a 60 es: {}".format(peso_3))
        print("La cantidad de estudiantes con peso mayor e igual a 60 es: {}\n".format(peso_4))

except:
    print("\nError en los datos\n")
