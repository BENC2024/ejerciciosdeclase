'''
Analisis:
Se desea obtener la nómina semanal —salario neto— de los empleados de una
empresa cuyo trabajo se paga por horas y del modo siguiente:
las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa
determinada que se debe introducir por teclado al igual que el número de horas y el
nombre del trabajador,
las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas
normales,
los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
sueldo <= 2.000, libre de impuestos,
las siguientes 220 euros al 20 por 100,
el resto, al 30 por 100.
'''
try:
    hora = 0
    nombre = ""
    nominaSemana = 0 #Nomina semanal
    nominaMensual = 0
    impuesto = 0
    nominaTotal = 0

    nombre = input("\nIngrese nombre del empleado: ")
    pago = float(input("Ingrese el pago(Euro) por hora: "))
    hora = float(input("Ingrese las horas de trabajo: "))
    
    if hora > 0 and pago > 0:
        if hora <= 35:
            nominaSemana = pago*hora

        elif hora > 35:
            horaExtra = (hora-35)*1.5 #Conocer las horas extra trabajadas
            pagoExtra = horaExtra*pago #Pago por esas horas extra trabajadas
            nominaSemana = pago*hora + pagoExtra

        nominaMensual = nominaSemana*4

        if nominaMensual <= 2000:
            impuesto = 0
            nominaTotal = nominaMensual
        elif nominaMensual <= 2220:
            impuesto = nominaMensual*0.2
            nominaTotal = nominaMensual - impuesto
        else:
            impuesto = nominaMensual*0.3
            nominaTotal = nominaMensual - impuesto

        print("\nEl empleado {} tiene los siguientes resultados: ".format(nombre))
        print("Su nomina semana es de {}".format(nominaSemana))
        print("Su nomina mensual es de {}".format(nominaMensual))
        print("Su impuesto a pagar es de {}".format(impuesto))
        print("Su nomina a pagar con impuestos es de {}\n".format(nominaTotal))
    else:
        print("\nNo se admiten datos negativos\n")
except:
    print("\nSe han ingresado datos no validos\n")
