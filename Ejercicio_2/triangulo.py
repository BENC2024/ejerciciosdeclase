'''
Crea un Algoritmo que nos calcule el área de un triángulo conociendo sus lados
'''

#Hallar el area del triangulo segun sus lados

try:
    a = float(input("\nIngrese el primer lado: "))
    b = float(input("Ingrese el segundo lado: "))
    c = float(input("Ingrese el tercer lado: "))

    if a > 0 and b > 0 and c > 0:
        # formula de Heron

        s = (a + b + c) / 2 #El semiperimetro

        area = (s*(s-a)*(s-b)*(s-c))**(1/2)
        if area.imag == 0:
            print("\nEl area del triangulo segun sus lados es: {:.2f}\n".format(area))
        else:
            print("\nEl area del triangulo no puede ser calculada\n")
    else:
        print("\nSolo numeros positivos\n")
except:
    print("\nError en los datos\n")