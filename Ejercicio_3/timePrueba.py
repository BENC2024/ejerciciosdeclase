import time

print('ejecucion inmediata')

for letra in '¡hola, mundo!':
    time.sleep(1)  # espera 2 segundos entre cada print()
    print(letra)

d = []
b = [2,2,3,4]
c = [4,2,3]
 
d.append(b)
d.append(c)
 
print(d)
