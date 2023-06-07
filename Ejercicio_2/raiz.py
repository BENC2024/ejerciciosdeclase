#Raiz

'''
Calcular la raíz cuadrada de un número y escribir su resultado. Considerando el caso
en que el número sea negativo
'''

try:
	num = float(input("\nIngrese un numero: "))
	if num >= 0:
		resul = (num)**(1/2)
		print("\nLa raiz de {} es {:.3f}\n".format(num,resul))
	else:
		print("\nSolo se calculan raices con numero positivos")
		resul = (num)**(1/2)
		print("Pero con valor complejo, La raiz de {} es {:.3f}j\n".format(num,resul.imag))
except:
    print("\nError en los datos\n")