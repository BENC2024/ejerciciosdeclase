'''
Escribir una función que devuelva la suma de todos los divisores de un número n, sin
incluirlo.
'''

try:
    def definir_suma(num):
        divisores = []
        suma = 0
        for i in range(1,num,1):
            if num%i == 0:
                divisores.append(i)
                suma = suma+i
        return suma,divisores
    
    n = int(input("\nIngrese un numero: "))
    
    if n == 1:
        print("\nLos divisores de {} son: 1 ya que no se incluye".format(n))
        print("La suma de estos divisores es 1\n")
    else:
        resultado, lista = definir_suma(n)

        print("\nLos divisores de {} son: {}".format(n,lista))
        print("La suma de estos divisores es {}\n".format(resultado))
except:
    print("\nHas ingresado un dato erroneo\n")