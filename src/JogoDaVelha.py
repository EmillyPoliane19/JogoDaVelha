espaco = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def exibirTabuleiro():
    tabela = (
        " " + espaco[0] + " | " + espaco[1] + " | " + espaco[2] +
        "\n-----------\n" +
        " " + espaco[3] + " | " + espaco[4] + " | " + espaco[5] +
        "\n-----------\n" +
        " " + espaco[6] + " | " + espaco[7] + " | " + espaco[8]
    )
    print(tabela)

def verificaPosicao(posicao):
    return espaco[posicao-1] not in ["X","O"]

def verificaVencedor(jogador):
    if espaco[0] == espaco[1] == espaco[2] == jogador:
        return True
    elif espaco[3] == espaco[4] == espaco[5] == jogador:
        return True
    elif espaco[6] == espaco[7] == espaco[8] == jogador:
        return True
    elif espaco[0] == espaco[3] == espaco[6] == jogador:
        return True
    elif espaco[1] == espaco[4] == espaco[7] == jogador:
        return True
    elif espaco[2] == espaco[5] == espaco[8] == jogador:
        return True
    elif espaco[0] == espaco[4] == espaco[8] == jogador:
        return True
    elif espaco[2] == espaco[4] == espaco[6] == jogador:
        return True
    else:
        return False

cont = 1
while True:
    jogadorAtual = "X" if cont % 2 != 0 else "O"
    exibirTabuleiro()
    print(f"Jogador {jogadorAtual}, é sua vez.")

    escolha = int(input("Digite a posição que você deseja:"))

    if verificaPosicao(escolha):
        espaco[escolha-1] = jogadorAtual
    else:
        print("Posicao está ocupada. Tente novamente.")
        continue
    if verificaVencedor(jogadorAtual):
        exibirTabuleiro()
        print("Parabés você venceu.")
        break

    if cont == 9:
        exibirTabuleiro()
        print("Deu velha! Não houve vencedores")
        break

    cont += 1
