'''
Elabore una minicalculadora que al ingresar 2 numeros 
me calcule el resultado de la suma, resta, producto, division,
exponenciacion, modulo de la division
'''

try:
    a = float(input("\nIngrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))

    print("\nNumeros dados {} y {}".format(a,b))
    print("La suma es: {}".format(a+b))
    print("La resta es: {}".format(a-b))
    print("La multiplicacion es: {}".format(a*b))
    if b == 0:
        print("No es posible la division por cero")
    else:
        print("La division es: {}".format(a/b))
    if a == 0 and b <= 0:
        print("No se puede hacer la operacion {}^{}".format(a,b))
    else:
        print("La exponenciacion es: {}".format(a**b))
    print("El modulo de la division es: {}\n".format(a%b))
    
except:
    print("\nNo se admite el dato ingresado\n")