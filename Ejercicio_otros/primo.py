
try:
    num = int(input("\nIngrese el numero para conocer si es primo: "))
    i = 1
    cont = 0
    while num>=i:
        if num%i == 0:
            cont += 1
        if cont > 2:
            break
        i += 1
    if cont == 2:
        print(f"\nEl numero {num} es un numero primo\n")
    else:
        print(f"\nEl numero {num} no es un numero primo\n")

except:
    print("\nHas ingresado un dato erroneo\n")