
transporte = 1600
cafe = 4000
dinero = 20000

print("\ntransporte: {}".format(transporte))
print("cafe: {}".format(cafe))
print("Dinero que cuenta: {}".format(dinero))

costoT = 2*(cafe*2)
costoC = 2*transporte + cafe*2

#PARA CAMPANARIO
campanario = dinero - costoC

#PARA TERRAPLAZA
terraplaza = dinero - costoT

print("\nSi va a terraplaza el costo sera de ${} y le quedaria ${}".format(costoT,terraplaza))
print("Si va a campanario el costo sera de ${} y le quedaria ${}\n".format(costoC,campanario))

#LA QUE PRESENTE MENOR GASTO
if campanario > terraplaza:
    print("Entonces para Tatiana, la mejor opcion es ir a campanario.\n")
elif campanario < terraplaza:
    print("Entonces para Tatiana, la mejor opcion es ir a terraplaza.\n")
else:
    print("Entonces para Tatiana, ambas son buenas opciones.\n")
