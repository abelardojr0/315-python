carro = {
    "Marca": "Ford",
    "Modelo": "Ka",
    "Ano": 2020,
    "Cor": "Cinza"
}

if "Cor" in carro:
    carro["Cor"] = "Preto"
else:
    del carro["Ano"]


print(carro)