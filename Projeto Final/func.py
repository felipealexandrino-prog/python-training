from time import sleep

# Função de título
def titulo(msg):
    tam = len(msg)
    print("-"*tam)
    print(f"\033[36m{msg}\033[0m".center(tam))
    print("-"*tam)

# Criar arquivo se não existir
def criar_arquivo(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        print(f"\033[31mArquivo {nome} não encontrado, criando um...\033[0m")
        a = open(nome, "wt+")
        a.close()
    else:
        print(f"\033[32mArquivo já foi encontrado!\033[0m")

# Cadastrar usuário
def cadastrar_usuario():
    a = open("cadastro.txt", "at")
    nom = input("\033[37mNome: \033[0m")
    ida = int(input("\033[37mIdade: \033[0m"))
    a.write(f"{nom};{ida}\n") 
    a.close()
    
    if ida >= 18:
        print(f"\033[32m{nom} cadastrado com sucesso!\033[0m")
    else:
        print(f"\033[31m{nom} cadastrado (menor de idade)\033[0m")

# Listar usuários
def listar_usuarios():
    a = open("cadastro.txt", "rt")
    listas = a.readlines()
    a.close()
    cont = 1
    for c in listas:
        print(f"\033[33mDADOS {cont}\033[0m")
        print(f"\033[37m{c.strip()}\033[0m".replace(";", "|"))
        sleep(0.8)
        cont += 1

# Menu principal
def menu():
    titulo("Menu Principal")
    print("1 - \033[34mCadastrar usuário\033[0m")
    print("2 - \033[34mListar usuários\033[0m")
    print("3 - \033[31mSair\033[0m")
    
    try:
        opcao = input("\n\033[33mEscolha uma opção: \033[0m")
        if opcao == "1":
            titulo("\033[32mCADASTRAR USUÁRIOS\033[0m")
            cadastrar_usuario()
        elif opcao == "2":
            titulo("\033[32mUSUÁRIOS CADASTRADOS\033[0m")
            listar_usuarios()
        elif opcao == "3":
            print("\033[31mSaindo do sistema...\033[0m")
            return 1
        else:
            print("\033[31mOpção inválida! Tente novamente.\033[0m")
    except Exception as erro:
        print(f"\033[31mErro {erro}! Tente novamente.\033[0m")

