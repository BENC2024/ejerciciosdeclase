
texto = input("\nIngrese un texto: \n")
vocales = [0,0,0,0,0] #[a,e,i,o,u]
suma = 0

for t in texto:
    if t == 'a' or t == 'a'.upper():
        vocales[0] = vocales[0] + 1
    elif t == 'e' or t == 'e'.upper():
        vocales[1] = vocales[1] + 1
    elif t == 'i' or t == 'i'.upper():
        vocales[2] = vocales[2] + 1
    elif t == 'o' or t == 'o'.upper():
        vocales[3] = vocales[3] + 1
    elif t == 'u' or t == 'u'.upper():
        vocales[4] = vocales[4] + 1

for i in vocales:
    suma = suma + i #Vocales[i]

print("\nVocales: ")
print("'a'=",vocales[0],end=", ")
print("'e'=",vocales[1],end=", ")
print("'i'=",vocales[2],end=", ")
print("'o'=",vocales[3],end=", ")
print("'u'=",vocales[4])
print("En total hay {} vocales\n".format(suma))