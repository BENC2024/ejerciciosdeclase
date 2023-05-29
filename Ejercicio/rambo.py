'''

Datos
¿Rambo sigue recibiendo dinero despues de 14 meses?
2100000 mensuales durante 14 meses
500000 mensuales
2300000 ingresos al año
-8200000 a pagar al año
-840000 de arriendo mensual
-60000 de administracion mensual
-450000 de comida mensual
-120000 de transporte mensual
-180000 de servicios mensual
-140000 de ropa y zapatos mensual

Quiere comprar un auto de 18000000

En meses primera parte
500000 mensuales
191666.666 ingresos al mes
-683333.333 a pagar al mes
-840000 de arriendo mensual
-60000 de administracion mensual
-450000 de comida mensual
-120000 de transporte mensual
-180000 de servicios mensual
-140000 de ropa y zapatos mensual

Total
-1781666.666 al mes
-21380000 al año
-24943333.338 durante 14 meses

Recibe durante 14 meses 2100000 al mes pero despues deja de recibir
Pero dando en total 25200000 año + 4200000 en dos meses

En ese año recibe 3820000

'''

ingresoInicial = 2100000 #Mensuales
clasesParticulares = 500000 #Mensuales
ingresoEmpresa = 2300000/12 #Mensuales
pago = 8200000/12 #Mensuales gasto
arriendo = 840000 #Mensuales gasto
administracion = 60000 #Mensuales gasto
productos = 450000 #Mensuales gasto
transporte = 120000 #Mensuales gasto
servicios = 180000 #Mensuales gasto
vestir = 140000 #Mensuales gasto

automovil = 18000000 #Costo del auto

ingreso = ingresoInicial+clasesParticulares+ingresoEmpresa
gasto = pago+arriendo+administracion+productos+transporte+servicios+vestir

totalMensual = ingreso - gasto
totalAnual = totalMensual*12

anios = automovil/totalAnual
meses = anios*12

print("\nEl ingreso corresponde a {:.3f} de pesos".format(ingreso))
print("Los gastos corresponden a {:.3f} de pesos".format(gasto))
print("\nEl total que le queda a Rambo mensualmente es {:.3f} de pesos".format(totalMensual))
print("El total que le queda a Rambo anualmente es {:.3f} de pesos".format(totalAnual))

print("\nEl automovil lo pagara en los proximos {:.3f} meses".format(meses))
print("El automovil lo pagara en los proximos {:.3f} anios\n".format(anios))
