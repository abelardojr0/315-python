nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7 and media >= 0:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Média inválida, digite notas entre 0 e 10")