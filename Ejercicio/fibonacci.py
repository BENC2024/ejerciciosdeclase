
#Escribir la serie fibonacci hasta un numero dado

try:
    num = int(input("\ningrese un numero para hallar la serie de fibonacci: "))
    valor = 1
    serie = [1]
    i = 0
    while num >= valor:
        serie.append(valor)
        valor = serie[i] + valor
        i+=1
    print("\nLa serie fibonacci es: {}\n".format(serie))

except:
    print("\nHa ocurrido un error\n")