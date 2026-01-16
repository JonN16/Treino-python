import tkinter as tk
import json as js
import time

arquivo = "CRUD(JSON)/documento.JSON"

janela = tk.Tk()
janela.title("Jogo da Velha")

label = tk.Label(janela, text="Bem vindo area de controle de usuarios o que gostaria de fazer")
label.pack()

def apagar():
    for widget in janela.winfo_children():
        widget.destroy()

def Create(caminho, conteudo):
    with open(caminho, 'w') as f:
        js.dump(conteudo, f, indent=4)

def read(caminho):
    with open(caminho, 'r') as f:
        return js.load(f)
    
def Delete(caminho):
    apagar()
    Json = read(caminho)

    tk.Label(janela, text="Deletar Usuario").pack()

    if "usuarios" not in Json or len(Json["usuarios"]) == 0:
        tk.Label(janela, text="Não há usuarios para deletar").pack()
        return

    tk.Label(janela, text="Usuarios disponiveis").pack()
    for u in Json["usuarios"]:
        tk.Label(janela, text=f"- {u['nome']}").pack()

    tk.Label(janela, text="Qual usuario voce quer deletar: ").pack()
    escolha = tk.Entry(janela)
    escolha.pack()

    def confirmar():
        usuario_encontrado = None
        for u in Json["usuarios"]:
            if u["nome"] == escolha.get():
                usuario_encontrado = u
                break

        if usuario_encontrado is None:
            tk.Label(janela, text="❌ Usuario nao encontrado").pack()
            return

        tk.Label(janela, text=f"Tem certeza que deseja deletar {usuario_encontrado['nome']}? (s/n)").pack()
        confirm = tk.Entry(janela)
        confirm.pack()

        def deletar():
            if confirm.get().lower() == 's':
                Json["usuarios"].remove(usuario_encontrado)
                Create(caminho, Json)
                tk.Label(janela, text=f"✅ Usuario {usuario_encontrado['nome']} deletado com sucesso!").pack()
            else:
                tk.Label(janela, text="Operacao cancelada.").pack()

        tk.Button(janela, text="Confirmar", command=deletar).pack()

    tk.Button(janela, text="Buscar usuario", command=confirmar).pack()

def Update(x):
    arquivo = x
    Json = read(arquivo)

    apagar()

    tk.Label(janela, text="--- MODIFICAR USUÁRIO ---").pack()

    for u in Json["usuarios"]:
        tk.Label(janela, text=f"- {u['nome']}").pack()

    tk.Label(janela, text="Qual usuário você quer modificar:").pack()
    escolha = tk.Entry(janela)
    escolha.pack()

    def escolher_usuario():
        usuario_encontrado = None

        for u in Json["usuarios"]:
            if u["nome"] == escolha.get():
                usuario_encontrado = u
                break

        if usuario_encontrado is None:
            tk.Label(janela, text="❌ Usuário não encontrado").pack()
            return

        tk.Label(janela, text="Campos disponíveis:").pack()
        for campo in usuario_encontrado:
            tk.Label(janela, text=f"- {campo}").pack()

        tk.Label(janela, text="Qual campo deseja modificar:").pack()
        respostaFinal = tk.Entry(janela)
        respostaFinal.pack()

        tk.Label(janela, text="Novo valor:").pack()
        novo_valor = tk.Entry(janela)
        novo_valor.pack()

        def salvar():
            campo = respostaFinal.get()

            if campo not in usuario_encontrado:
                tk.Label(janela, text="❌ Campo não encontrado").pack()
                return

            usuario_encontrado[campo] = novo_valor.get()
            Create(arquivo, Json)
            tk.Label(janela, text="✅ Usuário modificado com sucesso!").pack()

        tk.Button(janela, text="Salvar", command=salvar).pack()

    tk.Button(janela, text="Continuar", command=escolher_usuario).pack()


def CriarUsuario(x):
    apagar()
    arquivo = x

    Json = read(arquivo)

    if "usuarios" not in Json:
        Json["usuarios"] = []

    usuarios = Json["usuarios"]

    id = len(usuarios) + 1
    campos = ["nome", "idade", "CPF"]
    entradas = {}

    for campo in campos:
        tk.Label(janela, text=f"{campo.capitalize()}:").pack()
        entry = tk.Entry(janela)
        entry.pack()
        entradas[campo] = entry

    def salvar_usuario():
        usuario = {
            "id": id,
            "nome": entradas["nome"].get(),
            "idade": int(entradas["idade"].get()),
            "CPF": entradas["CPF"].get()
        }

        usuarios.append(usuario)

        Create(arquivo, Json)
        tk.Label(janela, text="✅ Usuário criado com sucesso!").pack()


    tk.Button(janela, text="Salvar Usuário", command=salvar_usuario).pack()

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=lambda: Delete(arquivo),
    font=("Arial", 12),
    bg="green",
    fg="white"
)
botao.pack()

botaoUpdate = tk.Button(
    janela,
    text="Modificar Usuario",
    command=lambda: Update(arquivo),
    font=("Arial", 12),
    bg="blue",
    fg="white"
)
botaoUpdate.pack()

botaoCreate = tk.Button(
    janela,
    text="Criar Usuario",
    command=lambda: CriarUsuario(arquivo),
    font=("Arial", 12),
    bg="orange",
    fg="white"
)
botaoCreate.pack()

janela.mainloop()
