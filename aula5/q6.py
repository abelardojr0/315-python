divisivel_3_5 = lambda numero : "divisível" if numero % 3 == 0 and numero % 5 == 0 else "não é divisível"

numero = int(input(input("Digite um número: ")))
print(divisivel_3_5(numero))