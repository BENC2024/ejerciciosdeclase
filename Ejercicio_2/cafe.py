'''
Tatiana tiene  ganas  de salir  con su amiga Paola a tomar un cafe  pero ella  sabe
que si va al  centro comercial Campanario deberá pagar transporte ida y regreso  y los
cafes de ambas, pero  si va a Terraplaza se ahorra el transporte,  pero  tambien debe
tener encuenta que  el  cafe  en Terraplaza es 2 veces mas costoso que en
campanario el cual  tiene un costo de 4000 y tambien cuenta con  20000 el  tranporte
seria en bus por un valor  de 1600  el  programa le debe decir a Tatiana cual seria la
mejor opcion que debe tomar
'''

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
