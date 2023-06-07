#Cree un programa que muestre una lista los 10 primeros numeros pares

x = 2

while x <= 20: #Se ingresa la condicion a realizar la operacion
    print("{}".format(x))
    x = x+2 # acumuladores; contador; incremento; x+=1

x = 1
print("")
while x <= 20:
    if x%2 == 0:
        print("{}".format(x))
    x = x+1
print("")

x=2
while x<=20:
    print(x)
    x = x+2
