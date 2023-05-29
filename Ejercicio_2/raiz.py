#Raiz

try:
	num = float(input("\nIngrese un numero: "))
	resul = (num)**(1/2)
	if num >= 0:
		print("\nLa raiz de {} es {:.3f}\n".format(num,resul))
	else:
		print("\nSolo se calculan raices con numero positivos")
		print("Pero con valor complejo, La raiz de {} es {:.3f}j\n".format(num,resul.imag))
except:
    print("\nError en los datos\n")