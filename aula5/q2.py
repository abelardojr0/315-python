def semaforo (cor:str):
    if cor == "vermelho":
        return "Pare!"
    elif cor == "amarelo":
        return "Atenção!"
    elif cor == "verde":
        return "Siga!"
    else:
        return "Error!"


while True:
    escolha_da_cor = str(input("Digite uma cor do semáforo: "))
    resposta = semaforo(escolha_da_cor)

    if resposta != "Error!":
        print(resposta)
        break
    else:
        print(resposta)

