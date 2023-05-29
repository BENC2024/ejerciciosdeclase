#pico y placa

'''
lunes: 3 - 4
martes: 5 - 6
miercoles: 7 - 8
jueves: 9 - 0
viernes: 1 - 2
'''

pico = input("\nIngrese ultimo digito de su placa: ")

if len(pico) == 1:
	if pico == '1' or pico == '2':
		print("\nTu pico y placa es el viernes\n")
	elif pico == '3' or pico == '4':
		print("\nTu pico y placa es el lunes\n")
	elif pico == '5' or pico == '6':
		print("\nTu pico y placa es el martes\n")
	elif pico == '7' or pico == '8':
		print("\nTu pico y placa es el miercoles\n")
	elif pico == '9' or pico == '0':
		print("\nTu pico y placa es el jueves\n")
	else:
		print("\nSolo se admiten numeros y en el rango 0 a 9\n")
else:
	print("\nSolo se admiten un solo caracter\n")