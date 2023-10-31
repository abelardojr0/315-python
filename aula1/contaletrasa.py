nome = str(input("Digite o seu nome: "))

contador = 0

for letra in nome:
    if letra.lower() == 'a':
        contador += 1
    
print(f"O nome {nome} possui {contador} letras 'a'")
