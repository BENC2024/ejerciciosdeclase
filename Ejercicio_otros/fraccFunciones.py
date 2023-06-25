#Suma de fraccionarios
'''
Variables de entrada: a,b,c,d,e,f
variables de salida: m,n
condicion: denominadores diferentes de cero
Utilizar el minimo comun multiplo
mostrar todo el proceso en pantalla
'''
import time

def mcm(x,y,z): #Funcion para el minimo comun multiplo
    divisores = [x,y,z]
    listaPrimo = []
    primo = 2
    aux = 0

    while divisores != [1,1,1]:
        aux = 0 #Esto es para ver el minimo comun multiplo y guardar en la lista
        for i in range(len(divisores)):
            if divisores[i]%primo == 0:
                if aux == 0:
                    for k in divisores:
                        print(k,end=" ")
                aux = 1
                divisores[i] = int(divisores[i]/primo)
        if aux == 0:
            primo += 1
        else:
            listaPrimo.append(primo)
            print("", end=" | ")
            print(primo)
            time.sleep(3)
            
    for k in divisores: #Para mostrar el 1,1,1
        print(k,end=" ")
    print("")
    return listaPrimo

def multiFactor(listaPrimo): #Funcion para la multiplicacion de los factores
    fac = ""
    n = 1
    for j in range(len(listaPrimo)-1,-1,-1): #Empieza del ancho de la lista hasta cero
        fac = str(listaPrimo[j]) + " * " + fac
        n = n*listaPrimo[j]
    fac = fac.removesuffix(" * ")
    fac = fac + " = " + str(n)
    return fac,n

def simplificacion(m,n): #Funcion para simplificar
    simpl = 2
    s,t = m,n
    if s < 0:
        s = -m
    while simpl <= s and simpl <= t:
        if s%simpl == 0 and t%simpl == 0:
            s = int(s/simpl)
            t = int(t/simpl)
            print("(",simpl,")",end=" -> ")
            if m < 0:
                print("-"+str(s)+"/"+str(t))
            else:
                print(str(s)+"/"+str(t))
            time.sleep(3)
        else:
            simpl += 1
    return s,t

try:
    a = int(input("\nIngrese el primer numerador: "))
    b = int(input("Ingrese el primer denominador: "))
    c = int(input("Ingrese el segundo numerador: "))
    d = int(input("Ingrese el segundo denominador: "))
    e = int(input("Ingrese el tercer numerador: "))
    f = int(input("Ingrese el tercer denominador: "))

    u,v,w = a,c,e #numeradores
    x,y,z = b,d,f #denominadores

    print(f"\nFracciones a sumar: {a}/{b} , {c}/{d} , {e}/{f}\n")
    time.sleep(3)

    if b != 0 and d != 0 and f !=0:
        if x == y and x == z and y == z: #Suma con denominadores iguales
            n = x
            if n < 0:
                u,v,w = -u,-v,-w
                n = -n
            m = u + v + w
            
            print(f"Las operaciones en las fracciones seria: {u}/{n} + {v}/{n} + {w}/{n}")
            time.sleep(3)
            print(f"\nEl resultado es igual a: {m}/{n}")
            time.sleep(3)
        else: #Suma con denominadores diferentes
            if b < 0:
                x = -b
            if d < 0:
                y = -d
            if f < 0:
                z = -f
                    
            print("Se aplica el minimo comun multiplo a los denominadores\n")
            time.sleep(3)
            listaPrimo = mcm(x,y,z)
            time.sleep(3)

            print("\nSe hace la multiplicacion de los factor primos\n")
            time.sleep(3)
            fac,n = multiFactor(listaPrimo)
            print(fac)
            time.sleep(3)

            u,v,w = int(a*(n/b)),int(c*(n/d)),int(e*(n/f)) #los nuevos numeradores
            x,y,z = n,n,n #Los nuevos denominadores
            
            m = u + v + w #Suma de numeradores

            print(f"\nLas operaciones en las fracciones seria: {u}/{n} + {v}/{n} + {w}/{n}")
            time.sleep(3)
            print(f"\nEl resultado es igual a: {m}/{n}")
            time.sleep(3)

        print("\nSe busca si se puede simplificar")
        time.sleep(3)
        s,t = simplificacion(m,n)
        
        #Valor simplificado del numerador si es positivo o negativo
        if m < 0:
            m = -s
        else:
            m = s
        n = t
        if n == 1 or m == 0:
            print(f"\nEl resultado final es igual a: {m}\n")
        else:
            print(f"\nEl resultado final es igual a: {m}/{n}\n")

    else:
        print("No se admiten divisiones por cero\n")

except:
    print("\nHa ocurrido error de ejecucion\n")