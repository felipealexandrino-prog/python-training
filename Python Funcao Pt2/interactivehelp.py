from time import sleep
# Lista de cores ANSI
c = [
    "\033[m",          # 0 - Reset / Padrão
    "\033[30;42m",     # 1 - Fundo verde (título principal)
    "\033[30;44m",     # 2 - Fundo azul (entrada)
    "\033[7;40m"       # 3 - Fundo cinza/preto invertido (help)
]


def titulo(msg, cor=0):
    """
    Função para criar um título colorido
    """
    tam = len(msg) + 4
    sleep(0.3)
    print(c[cor], end="")         # Aplica a cor
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end="")           # Reseta a cor


def ajuda(com):
    """
    Função que mostra o help colorido
    """
    titulo(f"Acessando manual do comando '{com}'", 2)
    print(f"....",flush=True)
    sleep(0.8)
    print(c[3], end="")           # Cor do help
    help(com)
    print(c[0], end="")           # Reset


# =======================
# PROGRAMA PRINCIPAL
# =======================

while True:

    titulo("Sistema De Ajuda PyHelp", 1)

    comando = input("Função ou Biblioteca (FIM para sair) -> ")

    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

titulo("Finalizando Interactive Help...", 1)

