from random import choice
import os

vitorias_jogador = 0
vitorias_maquina = 0

def escolha_jogador():
    while True:
        escolha = str(input("Digite sua escolha: Pedra, Papel ou Tesoura:")).lower().strip()
        if escolha in ["pedra", "papel", "tesoura", "sair"]:
            return escolha
        else:
             print("Escolha inválida")

def escolha_maquina():
    lista = ["pedra", "papel", "tesoura"]
    escolha = choice(lista)
    return escolha

def checar_vencedor(usuario,computador):
    global vitorias_maquina
    global vitorias_jogador
    if usuario == computador:
        return "Empate"
    elif (usuario == "pedra" and computador == "tesoura") or (usuario == "tesoura" and computador=="papel") or (usuario == "papel" and computador== "pedra"):
        vitorias_jogador += 1
        return "Você Ganhou"
    else:
        vitorias_maquina +=1
        return "Você Perdeu"

def mostrar_vitorioso():
    if vitorias_jogador > vitorias_maquina:
            return(f"Você venceu no placar geral de {vitorias_jogador} a {vitorias_maquina} ")
    elif vitorias_maquina > vitorias_jogador:
            return(f"Você perdeu no placar geral de {vitorias_maquina} a {vitorias_jogador} ")
    else:
            return(f"O jogo terminou empatado de {vitorias_jogador} a {vitorias_maquina}")

def mostrar_placar_atual():
    return f"""
    Placar Atual:
    Jogador {vitorias_jogador} x {vitorias_maquina} Máquina
"""

while True:
    maquina = escolha_maquina()
    jogador = escolha_jogador()
    if jogador == "sair":
        print(mostrar_vitorioso())
        break
    os.system("cls")
    print(checar_vencedor(usuario=jogador, computador=maquina))
    print(mostrar_placar_atual())