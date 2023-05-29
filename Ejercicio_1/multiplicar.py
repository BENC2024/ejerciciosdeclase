#tabla de multiplicar del numero ingresado

x = 0
num = int(input("\nIngrese un valor entero: "))
rest = 0

if num >= 0:
    print ("\nla tabla del {}\n".format(num))
    while x <= 10:
        print("{} * {} = {}".format(num,x,rest))
        rest = num + rest # Toma el numero anterior para volver a sumar
        x = x + 1
else:
    print ("\nSolo numeros positivos")
print("")