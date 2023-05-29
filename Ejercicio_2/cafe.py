
transporte = 1600
cafe = 4000
dinero = 20000

print("\ntransporte: {}".format(transporte))
print("cafe: {}".format(cafe))
print("Dinero que cuenta: {}".format(dinero))

#PARA CAMPANARIO
campanario = dinero - 2*transporte - cafe*2

#PARA TERRAPLAZA
terraplaza = dinero - 2*(cafe*2)

print("\nSi va a terraplaza le queda {} y a campanario queda {},".format(terraplaza,campanario))
print("Entonces para Tatiana, la mejor opcion es campanario.\n")
