# pessoa = {
#     "nome": str(input("Digite seu nome: ")),
#     "idade": int(input("Digite sua idade: ")),
#     "cpf": str(input("Digite seu cpf: "))
# }

# if pessoa["idade"] >= 18:
#     pessoa["habilitação"] = True
# else:
#     pessoa["nome"] = "Joãozinho"

# print(pessoa)


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cpf = str(input("Digite seu cpf: "))

pessoa = {
    "nome": nome,
    "idade": idade,
    "cpf": cpf
}

if pessoa["idade"] >= 18:
    pessoa["habilitação"] = True
else:
    pessoa["nome"] = "Joãozinho"

print(pessoa)