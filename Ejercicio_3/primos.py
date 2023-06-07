'''
Escribir una aplicación que reciba un número natural e imprima todos los números
primos que hay hasta ese número.
'''
try:
    num = int(input("\nIngrese un numero: "))
    contDiv = 1 #Contador de divisiones para saber si es o no numero primo
    primo = []

    if num == 1:
        print("\nEl numero 1 no es un valor valido\n")
    else:
        for valor in range(2,num+1,1):
            for aux in range(2,valor+1,1):
                if valor%aux == 0 and contDiv == 1:
                    primo.append(valor)
                    contDiv = contDiv+1
                else:
                    if contDiv > 1:
                        primo.remove(valor) #Remover el numero que se ingreso y no es primo
                        break # Puedo usar .pop para eliminar elemento en esa posicion
            contDiv = 1

    print("\nLos numeros de que hay del 2 al {} son: {}\n".format(num,primo))
except:
    print("\nEl dato ingresado no es valido\n")