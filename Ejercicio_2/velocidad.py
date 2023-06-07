#Velocidad

'''
Construye un programa que Si distancia es mayor que 20 y
menos que 35, leer un valor para tiempo y calcular la 
Velocidad si   Distancia = Velocidad * Tiempo
'''

try:
	distancia = float(input("\nIngrese la distancia en mts(entre 20 y 35): "))

	if distancia > 0 and distancia > 20 and distancia < 35:
		
		tiempo = float(input("Ingrese tiempo en seg: "))
		if tiempo > 0:
			velocidad = distancia/tiempo
			print("\nLa velocidad del vehiculo es: {} m/s\n".format(velocidad))
		else:
			print("\nEl tiempo ingresado no es valido")

	else:
		print("\nLa distancia ingresada no es valida\n")
except:
	print("\nError ingresando datos\n")