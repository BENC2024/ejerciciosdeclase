
try:
    nota = float(input("\nIngrese valor numerico: "))
    letra = "" 
    if nota < 60:
        letra = 'F'
    elif nota < 70:
        letra = 'D'
    elif nota < 80:
        letra = 'C'
    elif nota < 90:
        letra = 'B'
    else:
        letra = 'A'

    print("\nSu calificacion es: "+letra+"\n")
except:
    print("\nError en los datos\n")