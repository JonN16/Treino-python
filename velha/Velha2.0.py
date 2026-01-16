import tkinter as tk
import random

janela = tk.Tk()
janela.title("Jogo da Velha")

matriz = [["", "", ""],
          ["", "", ""],
          ["", "", ""]]

numero = random.randint(1, 2)

tamanho = 300

canvas = tk.Canvas(janela, width=tamanho, height=tamanho, bg="white")
canvas.pack()

def CriaX(x, y):
    canvas.create_line(x+10, y+10, x + 90, y + 90, width=3)
    canvas.create_line(x+10, y+ 90, x + 90, y+10, width=3)

def CriaO(x, y):
    canvas.create_oval(x + 10, y + 10, x + 90, y + 90, width=3)

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


def clickMouse(event):
    global numero

    linha = event.y // 100
    coluna = event.x // 100

    if linha >= 3 or coluna >= 3:
        return

    if matriz[linha][coluna] != "":
        return

    letra = "X" if numero == 1 else "O"
    matriz[linha][coluna] = letra

    x = coluna * 100
    y = linha * 100

    if letra == "X":
        CriaX(x, y)
    else:
        CriaO(x, y)

    if ganhador(matriz):
        print(f"{letra} ganhou")
        canvas.unbind("<Button-1>")  
        return

    numero = 2 if numero == 1 else 1


canvas.create_line(tamanho/3, 0, tamanho/3, tamanho)
canvas.create_line((tamanho/3)*2, 0, (tamanho/3)*2, tamanho)
canvas.create_line(0, tamanho/3, tamanho, tamanho/3)
canvas.create_line(0, (tamanho/3)*2, tamanho, (tamanho/3)*2)

canvas.bind("<Button-1>", clickMouse)

janela.mainloop()
