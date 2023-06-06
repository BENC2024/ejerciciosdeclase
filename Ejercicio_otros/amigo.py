def obtener_divisores(num):
    divisores = []
    for i in range(1, num // 2 + 1):  # Optimización: Limitamos el rango hasta la mitad de num
        if num % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(num1, num2):
    div_num1 = obtener_divisores(num1)
    div_num2 = obtener_divisores(num2)
    return sum(div_num1) == num2 and sum(div_num2) == num1

def imprimir_parejas_amigas(m):
    pares_encontrados = 0
    num1 = 1

    while pares_encontrados < m:
        num2 = num1 + 1
        while True:
            if son_amigos(num1, num2):
                print(f"({num1}, {num2})")
                pares_encontrados += 1
                break
            num2 += 1
        num1 += 1

m = int(input("Ingrese la cantidad de parejas de números amigos que desea encontrar: "))
imprimir_parejas_amigas(m)
