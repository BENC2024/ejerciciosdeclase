a = float(input("\nIngrese el primer numero: ")) 
b = float(input("Ingrese el segundo numero: ")) 
c = float(input("Ingrese el tercer numero: ")) 

if a > b:
    if a > c:        
        print("\nEl numero mayor es {}\n".format(a))
    else:        
        print("\nEl numero mayor es {}\n".format(c))

elif b > c:
    print("\nEl numero mayor es {}\n".format(b))
elif b < c:    
    print("\nEl numero mayor es {}\n".format(c))

else:
    print("\nTodos los numeros son iguales\n")
