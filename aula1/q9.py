frase = str(input("Digite uma frase: "))
contador_de_vogal = 0
contador_de_consoante = 0

for letra in frase:
    if letra.lower() in "aeiouâáêéîíôóúã":
        contador_de_vogal += 1
    if letra.lower() in "bcdfghjkmlnpqrstvxywz":
        contador_de_consoante += 1


print(f"A frase digitada possui {contador_de_vogal} vogais ")
print(f"A frase digitada possui {contador_de_consoante} consoantes ")
