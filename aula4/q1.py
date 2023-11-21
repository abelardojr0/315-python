def calcular_imc(p,a):
  return p / a **2

lista_de_usuarios = []

for i in range(1,5):
  nome = str(input(f"Digite o {i} nome: "))
  peso = float(input(f"Digite o {i}º peso: "))
  altura = float(input(f"Digite a {i}ª altura: "))
  imc = calcular_imc(peso, altura)
  lista_de_usuarios.append({
    "name": nome,
    "weight": peso,
    "height": altura,
    "imc": imc
    })

for item in lista_de_usuarios:
  print(f"""
      Nome: {item["name"]}
      Altura: {item["height"]}
      Peso: {item["weight"]}
      IMC: {item["imc"]:.2f}
""")

