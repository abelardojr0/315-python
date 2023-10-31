# RESOLUÇÃO 1:
# cor = str(input("Escolha uma cor do semáforo: ")).lower()

# if cor == "vermelho":
#     print("Pare!")
# elif cor == "amarelo":
#     print("Atenção!")
# elif cor == "verde":
#     print("Acelere!")
# else:
#     print("Cor inválida")


# RESOLUÇÃO 2:
# cor = str(input("Escolha uma cor do semáforo: ")).lower()

# match cor:
#     case "vermelho":
#         print("Pare!")
#     case "amarelo":
#         print("Atenção!")
#     case "verde":
#         print("Acelere!")
#     case _:
#         print("Cor inválida")


# RESOLUÇÃO 3:
cor = int(input("""
                Escolha uma cor do semáforo:
                1 - Vermelho
                2 - Amarelo
                3 - Verde
                 """))
match cor:
    case 1:
        print("Pare!")
    case 2:
        print("Atenção!")
    case 3:
        print("Acelere!")
    case _:
        print("Cor inválida")