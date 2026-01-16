import json

def Create(caminho, conteudo):
    with open(caminho, 'w') as f:
        json.dump(conteudo, f, indent=4)

def read(caminho):
    with open(caminho, 'r') as f:
        return json.load(f)

def Delete(x):
    arquivo = x
    Json = read(arquivo)

    print("\n--- DELETAR USUÁRIO ---")

    if "usuarios" not in Json or len(Json["usuarios"]) == 0:
        print("Não há usuários para deletar.")
        return

    while True:
        print("\nUsuários disponíveis:")
        for u in Json["usuarios"]:
            print(f"- {u['nome']}")

        escolha = input("\nQual usuário você quer deletar: ")

        usuario_encontrado = None
        for u in Json["usuarios"]:
            if u["nome"] == escolha:
                usuario_encontrado = u
                break

        if usuario_encontrado is not None:
            break
        else:
            print("❌ Usuário não encontrado")

    confirm = input(f"Tem certeza que deseja deletar {usuario_encontrado['nome']}? (s/n): ")
    if confirm.lower() == 's':
        Json["usuarios"].remove(usuario_encontrado)
        Create(arquivo, Json)
        print(f"✅ Usuário {usuario_encontrado['nome']} deletado com sucesso!")
    else:
        print("Operação cancelada.")

def CriarUsuario(x):
    arquivo = x

    Json = read(arquivo)

    if "usuarios" not in Json:
        Json["usuarios"] = []

    usuarios = Json["usuarios"]

    id = len(usuarios) + 1
    nome = input("nome do usuario: ")
    idade = int(input("idade do usuario: "))
    CPF = input("CPF do usuario: ")

    usuario = {
        "id": id,
        "nome": nome,
        "idade": idade,
        "CPF": CPF
    }

    usuarios.append(usuario)

    Create(arquivo,Json)
    print("✅ Usuário criado com sucesso!")

def Update(x):
    arquivo = x
    Json = read(arquivo)

    while True:
        print("\nUsuários disponíveis:")
        for u in Json["usuarios"]:
            print(f"- {u['nome']}")

        escolha = input("\nQual usuário você quer modificar: ")

        usuario_encontrado = None

        for u in Json["usuarios"]:
            if u["nome"] == escolha:
                usuario_encontrado = u
                break

        if usuario_encontrado is not None:
            break
        else:
            print("❌ Usuário não encontrado")

    while True:
        print("\nCampos disponíveis:")
        for campo in usuario_encontrado:
            print(f"- {campo}")

        respostaFinal = input("\nVocê quer modificar qual campo: ")

        if respostaFinal in usuario_encontrado:
            break
        else:
            print("❌ Campo inválido")

    novo_valor = input(f"Novo valor para {respostaFinal}: ")

    usuario_encontrado[respostaFinal] = novo_valor

    Create(arquivo, Json)
    print("✅ Usuário atualizado com sucesso!")

def main():
    arquivo = "CRUD(JSON)/documento.JSON"
    
    while True:
        print("\n--- MENU ---")
        print("1. Ler usuários")
        print("2. Criar usuário")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            print(read(arquivo))
        elif opcao == "2":
            CriarUsuario(arquivo)
        elif opcao == "3":
            Update(arquivo)
        elif opcao == "4":
            Delete(arquivo)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida")

if __name__ == "__main__":
    main()