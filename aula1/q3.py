letra = str(input("""
                  Digite uma letra:
                  F - Feminino
                  M - Masculino
                   """)).upper().strip()

if len(letra) == 1:
    match letra:
        case "F":
            print("Sexo Feminino")
        case "M":
            print("Sexo Masculino")
        case _:
            print("Sexo inválido")
else:
    print("Digite apenas uma letra")

