import random
import time

def ganhador(matriz):
    n = len(matriz)

    for linha in matriz:
        if linha.count("X") == n:
            return "X"
        if linha.count("O") == n:
            return "O"

    for c in range(n):
        coluna = [matriz[i][c] for i in range(n)]
        if coluna.count("X") == n:
            return "X"
        if coluna.count("O") == n:
            return "O"

    diag1 = [matriz[i][i] for i in range(n)]
    diag2 = [matriz[i][n - 1 - i] for i in range(n)]

    if diag1.count("X") == n or diag2.count("X") == n:
        return "X"
    if diag1.count("O") == n or diag2.count("O") == n:
        return "O"

    return None


def Jogada(matriz, letra):
    while True:
        linha = int(input("linha (0 a 2): "))
        coluna = int(input("coluna (0 a 2): "))
        if 0 <= linha < 3 and 0 <= coluna < 3 and matriz[linha][coluna] == "":
            matriz[linha][coluna] = letra
            break
        print("posição inválida ou ocupada")
    return matriz


def dashboard(matriz):
    for i in range(3):
        for j in range(3):
            print(matriz[i][j] if matriz[i][j] != "" else " ", end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("---------")


def JogoDaVelha():
    print("começando o jogo da velha:")
    time.sleep(1)

    numero = random.randint(1, 2)
    matriz = [["", "", ""], ["", "", ""], ["", "", ""]]
    jogadas = 0

    while True:
        letra = "X" if numero == 1 else "O"

        dashboard(matriz)
        print(f"\njogador {numero}, onde você colocará seu {letra}?")

        Jogada(matriz, letra)
        jogadas += 1

        vencedor = ganhador(matriz)
        if vencedor:
            dashboard(matriz)
            print(f"\nJogador {vencedor} ganhou!")
            break

        if jogadas == 9:
            dashboard(matriz)
            print("\nEmpate")
            break

        numero = 2 if numero == 1 else 1


JogoDaVelha()
