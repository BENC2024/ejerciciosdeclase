
texto = input("\nIngrese el texto:\n")
palabras = 0
caracter = 0

for i in texto:
    caracter += 1
    if i == ' ':
        palabras = palabras + 1
    else:
        if caracter==len(texto):
            palabras = palabras + 1
            

print(f"\n en total hay {palabras}\n")
