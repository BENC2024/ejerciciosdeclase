#Central

try:
	a = float(input("\nIngrese primer numero: "))
	b = float(input("Ingrese segundo numero: "))
	c = float(input("Ingrese tercer numero: "))

	if a == b and b == c:
		print("\nTodos los numeros son iguales\n")

	elif a > b:
		if a > c:
			if b > c:
				print("\nEl numero central es: {}\n".format(b))
			elif c > b:
				print("\nEl numero central es: {}\n".format(c))
			else:
				print("\nNo se puede saber el numero central\n")
		elif c > a:
			print("\nEl numero central es: {}\n".format(a))
		else:
			print("\nNo se puede saber el numero central\n")

	elif b > a:
		if b > c:
			if a > c:
				print("\nEl numero central es: {}\n".format(a))
			elif c > a:
				print("\nEl numero central es: {}\n".format(c))
			else:
				print("\nNo se puede saber el numero central\n")
		elif c > b:
			print("\nEl numero central es: {}\n".format(b))
		else:
			print("\nNo se puede saber el numero central\n")

	else:
		print("\nNo se puede saber el numero central\n")
except:
	print("\nError ingresando datos\n")