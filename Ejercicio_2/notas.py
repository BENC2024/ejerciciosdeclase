'''
El sistema de calificación americano (de Estados Unidos) se suele calcular de
acuerdo al siguiente cuadro: (Utilizando esta información, escribir un algoritmo que
acepte una calificación numérica del estudiante (0-100), convierta esta calificación a
su equivalente en letra y visualice la calificación correspondiente en letra)
Grado numérico Grado en letra
Grado mayor o igual a 90    A
Menor de 90 pero mayor o igual a 80  B
Menor de 80 pero mayor o igual a 70  C
Menor de 70 pero mayor o igual a 69  D
Menor de 69        F
'''

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