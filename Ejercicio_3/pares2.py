'''
Utiliza la forma matemática para calcular los numeros pares e impares imprimir la
secuencia de los  200 primeros numeros  pares partiendo desde 0
'''

x = 0

print("\nLos 200 primeros numeros pares son:")

while x <= 400:
    if x%2 == 0:
        print(x, end=(" "))
    x += 1
print("\n")