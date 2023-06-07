'''
Usando la función anterior, escribir una función que imprima los primeros m números
tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m
números perfectos).
'''

def definir_perfectos(num):
    suma = 0
    perfecto = []
    a = 2 # Contador de numeros
    while a <= num:
        for i in range(1,a,1):
            if a%i == 0:
                suma = suma + i
        if suma == a:
            perfecto.append(a)
        a = a+1
        suma = 0
    return perfecto

try:
    m = int(input("\nIngrese un numero: "))

    if m > 0:
        resultado = definir_perfectos(m)

        if len(resultado) == 0:
            print("\nNo hay numeros perfectos hasta el {}\n".format(m))
        else:
            print("\nLos numeros perfectos del 1 al {} son: {}\n".format(m,resultado))

    else:
        print("\nNo se admiten numeros negativos o cero\n")
except:
    print("\nHas escrito un dato erroneo\n")



'''
def definir_perfectos(num):
    suma = 0
    perfecto = []
    perf = 1 # Contador de numeros
    i = 1
    while perf <= num:
        while perf > i:
            if perf%i == 0:
                suma = suma + i
            i += 1
        if suma == perf:
            perfecto.append(perf)
        perf = perf+1
        i = 1
        suma = 0
    return perfecto'''