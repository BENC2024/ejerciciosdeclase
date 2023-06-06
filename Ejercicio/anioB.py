def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Solicitar al usuario que ingrese un año
anio = int(input("Ingrese un año: "))

# Comprobar si el año es bisiesto
if es_bisiesto(anio):
    print(anio, "es un año bisiesto.")
else:
    print(anio, "no es un año bisiesto.")