'''
Calcule el  valor  del  IVA 19% y el descuento
de un producto ingresado por teclado
'''

try:
    valor = float(input("\nIngrese el valor del producto: "))
    iva = float(valor*0.19)

    descuento = float(input("\nIngrese porcentaje de descuento: "))
    if valor >= 0 and iva >= 0 and descuento >= 0:
        producto_final = valor - (valor*descuento/100)

        print("\nEl valor del iva del producto es: {}".format(iva))
        print("El descuento del producto es de : {}".format(valor*descuento/100))
        print("El producto con descuento es de: {:.3f}".format(producto_final))
    else:
        print("\nSolo se admiten numeros mayores a cero\n")

except:
    print("\nHas ingresado un dato erroneo\n")
        