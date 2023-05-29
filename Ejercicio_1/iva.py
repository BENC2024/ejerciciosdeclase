
try:
    valor = int(input("\nIngrese el valor del producto: "))
    iva = float(valor*0.19)

    preg = input("\nEl producto tiene descuento? Y/N: ")

    if preg == "Y":
        descuento = int(input("\nIngrese porcentaje de descuento: "))
        producto_final = valor - (valor*descuento/100)
        print("\nEl valor del iva del producto es: {}".format(iva))
        print("El descuento del producto es de : {}".format(valor*descuento/100))
        print("El producto con descuento es de: {:.3f}".format(producto_final))
    elif preg == "N":
        print("el valor del iva del producto es: {:.3f}".format(iva))
        
    else:
        print("\nSolo se adimite 'Y' o 'N'\n")
except:
    print("\nHas ingresado un dato erroneo\n")
        