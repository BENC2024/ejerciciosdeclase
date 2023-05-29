
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
                    None
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
    numero = int(input("\nCuantos pares de numeros amigos desea: "))

    print("\nLos  numeros amigos que existen son: \n")
    definir_amigos(numero)
    ####
except:
    print("\nHa ocurrido un error")
print("")



'''
# Ni se como lo hice
No se como funciona, pero funciona
print(lista)
    for x in lista:
        print(x)
    print("")
'''