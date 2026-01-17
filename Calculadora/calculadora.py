import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x450")

bloco_w = 75
bloco_h = 70
offset_y = 100

a = 0
l = 0

operadores = ['/', 'X', '-', '+']
op_i = 0
num = 1

escrita = tk.Label(
    janela,
    text="",
    anchor="e",
    font=("Arial", 24),
    bg="white"
)
escrita.place(x=20, y=20, width=260, height=60)

def calcular(x):
    numeros = []
    operadores = []
    numero = ""
    contagem = -1

    for i in x:
        if i.isdigit() or i == '.':
            numero += i
        else:
            numeros.append(numero)
            operadores.append(i)
            numero = ""

    if numero != "":
        numeros.append(numero)

    print(numeros, operadores)

    for j in numeros:
        if contagem == -1:
            numero1 = float(j)
            contagem += 1
            pass
        else:
            numero2 = float(j)
            if operadores[contagem] == "/":
                numero1 /= numero2
            elif operadores[contagem] == "X":
                numero1 *= numero2
            elif operadores[contagem] == "-":
                numero1 -= numero2
            elif operadores[contagem] == "+":
                numero1 += numero2
            contagem += 1

    escrita.config(text=f"{numero1:.3f}".rstrip('0').rstrip('.'))

def clicar(valor):
    atual = escrita.cget("text")

    if valor == 'C':
        escrita.config(text="")

    elif valor == '⌫':
        escrita.config(text=atual[:-1])

    elif valor == '=':
        calcular(escrita.cget("text")) 

    else:
        escrita.config(text=atual + str(valor))
        print(escrita.cget("text"))


for i in range(18):
    largura = bloco_w
    texto = ''

    if a == 0:
        texto = 'C' if l == 0 else '⌫'
        largura = bloco_w * 2
        pos_x = 0 if l == 0 else bloco_w * 2

    elif a == 4:
        extras = ['0', '.', '=']
        if l < 3:
            texto = extras[l]
        else:
            texto = operadores[op_i]
            op_i += 1
        pos_x = l * bloco_w

    else:
        if l < 3 and num <= 9:
            texto = num
            num += 1
        elif l == 3:
            texto = operadores[op_i]
            op_i += 1
        pos_x = l * bloco_w

    tk.Button(
        janela,
        text=texto,
         command=lambda v=texto: clicar(v)
    ).place(
        x=pos_x,
        y=(a * bloco_h) + offset_y,
        width=largura,
        height=bloco_h
    )

    if a == 0:
        l += 1
        if l > 1:
            l = 0
            a += 1
    else:
        l += 1
        if l > 3:
            l = 0
            a += 1

janela.mainloop()
