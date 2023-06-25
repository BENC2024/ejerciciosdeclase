'''
Usando la primera función, escribir una función que imprima las primeras m parejas
de números (a,b), tales que la suma de los divisores de a es igual a b y la suma de los
divisores de b es igual a a (es decir las primeras m parejas de números amigos).
Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de
ejecución.
'''


def definir_amigos(num):
    contAmigo = 1
    pares = []
    a = 2 #no se empieza con 1
    sumaA = 0  #suma de los divisores
    sumaB = 0

    while contAmigo <= num:
        while True:
            for i in range(1,a,1):
                if a%i == 0:
                    sumaA = sumaA+i
            b = sumaA
            for j in range(1,b,1):
                if b%j == 0:
                    sumaB = sumaB+j

            if a == sumaB and a != b: #Si se da el caso de que sea perfecto
                if a in pares:
                    pass #None -- no haga nada
                else:
                    print("({},{})".format(a,b)) #(f"(a)(b)")
                    pares.append(a), pares.append(b)
                    contAmigo += 1
                    a += 1
                    sumaA, sumaB = 0,0
                break
            else:
                sumaA, sumaB = 0,0
                a += 1

try:
    numero = int(input("\nCuantas parejas de numeros amigos desea: "))

    print("\nLas parejas de numeros amigos son: \n")
    definir_amigos(numero)
    ####
except:
    print("\nHa ocurrido un error")
print("")

'''
# Ni como lo hice
print(lista)
    for x in lista:
        print(x)
    print("")
'''