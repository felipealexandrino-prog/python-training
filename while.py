n1 = int(input("Que numero deseja começar - > "))
while True:

    print("Menu de opções: \n1.Somar\n2.Multiplicar\n3.Sair \n")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        n2 = int(input("Que numero deseja somar: "))
        n3 = n1 + n2
        print(f"A soma entre {n1} e {n2} é igual a {n3}")
        n1 = n3
        print(f"O VALOR ATUAL É {n3}")
    elif opcao == 2:
        n2 = int(input("Que numero deseja multiplicar: "))
        n3 = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é igual a {n3}")
        n1 = n3
        print(f"O VALOR ATUAL É {n3}")
    elif opcao == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")        