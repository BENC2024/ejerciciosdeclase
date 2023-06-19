#Suma de fraccionarios
'''
Variables de entrada: a,b,c,d,e,f
variables de salida: m,n
condicion: denominadores diferentes de cero
Utilizar el minimo comun multiplo
mostrar todo el proceso en pantalla
'''
import time

try:
    a = int(input("\nIngrese el primer numerador: "))
    b = int(input("Ingrese el primer denominador: "))
    c = int(input("Ingrese el segundo numerador: "))
    d = int(input("Ingrese el segundo denominador: "))
    e = int(input("Ingrese el tercer numerador: "))
    f = int(input("Ingrese el tercer denominador: "))
    m = 0
    n = 1

    u,v,w = a,c,e #numeradores
    x,y,z = b,d,f #denominadores

    print(f"\nFracciones a sumar: {a}/{b} + {c}/{d} + {e}/{f}\n")
    time.sleep(3)

    if b != 0 and d != 0 and f !=0:
        if b < 0:
            x = -b
        if d < 0:
            y = -d
        if f < 0:
            z = -f

        divisores = [x,y,z]
        listaPrimo = []
        primo = 2
        aux = 0
        
        print("Se aplica el minimo comun multiplo a los denominadores\n")
        time.sleep(3)

        while divisores != [1,1,1]:
            #Esto es para ver el minimo comun multiplo
            aux = 0

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
        time.sleep(3)

        print("\nSe hace la multiplicacion de los factor primos\n")
        time.sleep(3)
        fac = ""
        for j in range(len(listaPrimo)-1,-1,-1): #Empieza del ancho de la lista hasta cero
            fac = str(listaPrimo[j]) + " * " + fac
            n = n*listaPrimo[j]
        fac = fac.removesuffix(" * ")
        fac = fac + " = " + str(n)
        print(fac)
        time.sleep(3)

        x,y,z = int(n/b),int(n/d),int(n/f) #Los nuevos denominadores
        u,v,w = int(a*(n/b)),int(c*(n/d)),int(e*(n/f)) #los nuevos numeradores
        
        m = u + v + w #Suma de numeradores

        print(f"\nLa multiplicacion en las fracciones seria: {u}/{n} + {v}/{n} + {w}/{n}")
        time.sleep(3)
        print(f"\nEl resultado es igual a: {m}/{n}")
        time.sleep(3)

        simpl = 2
        print("\nSe busca si se puede simplificar")
        time.sleep(3)
        s,t = m,n
        if s < 0:
            s = -m

        while simpl <= s and simpl <= t:
            if s%simpl == 0 and t%simpl == 0:
                s = int(s/simpl)
                t = int(t/simpl)
                if m < 0:
                    print("-"+str(s)+"/"+str(t))
                else:
                    print(str(s)+"/"+str(t))
                time.sleep(3)
            else:
                simpl += 1
        
        if m < 0:
            m = -s
        else:
            m = s
        n = t

        if n == 1:
            print(f"\nEl resultado final es igual a: {m}\n")
        else:
            print(f"\nEl resultado final es igual a: {m}/{n}\n")

    else:
        print("No se admiten divisiones por cero\n")

except:
    print("\nHa ocurrido error de ejecucion\n")