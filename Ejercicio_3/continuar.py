'''
Realiza un programa que imprima una secuencia de numeros de uno en uno desde el
que el usuario desee, el programa debe pedirle al usuario después de que imprima un
numero en pantalla le pregunte si desea continuar o no mostrando en pantalla
'''

try:
    i = "si"
    while i == "si" or i != "no":
        if i == "si":
            a = int(input("\nIngrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            print("")
            if a < b:
                for i in range(a,b+1,1):
                    print(i)
            elif a > b:
                for i in range(b,a+1,1):
                    print(i)
            else:
                print("\nAmbos numeros son iguales\n")

        i = input("\nDesea continuar? si/no?: ")
        if i == "no":
            print("\nGracias por participar.\n")
            break
        elif i == "si":
            print("\nSe procede a continuar")
        else:
            print("\nSolo se acepta 'si' o 'no'")
except:
    print("\nHas ingresado un dato erroneo\n")