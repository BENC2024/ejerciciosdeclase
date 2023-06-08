'''
Elabore un  programa me muestre en  pantalla el  tipo de  dato 
que el usuario ha ingresado, por  ejemplo si  ingresa Juan el
deberá decir que es texto, en caso  que ingrese 2018 deberá decir que es  entero
'''
dato = ""
try:
    dato = float(input("\nIngrese su dato: "))
    print("\nEl dato es un numero entero")
    print(type(dato))
except:
    print(f"\nEl dato es un texto")
    print(type(dato))
print("")


'''
aux = 0

for i in dato:
    if i=='0'or i=='1'or i=='2'or i=='3'or i=='4'or i=='5'or i=='6'or i=='7'or i=='8'or i=='9':
        aux = 1
    else:
        aux = 0
        break

if aux == 1:
    print ("\nEl dato es un numero real\n")
else:
    print ("\nEl dato es un caracter\n")
'''

'''
if dato.isnumeric():
    print ("La variable es un numero")
else:
    print ("La variable es una cadena")
'''

'''
if type(dato) == str
    print ("\nEl dato es un caracter\n")
else
    print ("\nEl dato es un numero real\n")
'''
