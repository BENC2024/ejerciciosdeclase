#pico y placa

'''
lunes: 3 - 4
martes: 5 - 6
miercoles: 7 - 8
jueves: 9 - 0
viernes: 1 - 2
'''

pico = input("\nIngrese su placa (Ejm: abc123): ")
numero = ['3','4','5','6','7','8','9','0','1','2']
dias = ["lunes","martes","miercoles","jueves","viernes"]

if len(pico) == 6:
	if pico[5] in numero:
		digito = pico[5]
		print("\nTu vehiculo es un carro")
	else:
		digito = pico[4]
		print("\nTu vehiculo es una moto")
	
	print("El vehiculo tiene pico y placa el",end=(" "))
	if digito == numero[0] or digito == numero[1]:   #puedo usar ('3' or '4') esto para el viernes
		print(f"{dias[0]}\n")
	elif digito == numero[2] or digito == numero[3]: # ('5' or '6') esto para el lunes
		print(f"{dias[1]}\n")
	elif digito == numero[4] or digito == numero[5]: # ('7' or '8') esto para el martes
		print(f"{dias[2]}\n")
	elif digito == numero[6] or digito == numero[7]: # ('9' or '0') esto para el miercoles
		print(f"{dias[3]}\n")
	elif digito == numero[8] or digito == numero[9]: # ('1' or '2') esto para el jueves
		print(f"{dias[4]}\n")

else:
	print("\nEl dato ingresado es erroneo\n")
