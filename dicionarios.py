dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
dadoadd = str(input("Digite um dado para adicionar ao dicionário: "))
valoradd = str(input("Digite o valor desse dado: "))
dados[dadoadd] = valoradd
dados["nome"] = str(input("Digite o nome: "))
print(f"O {dados['nome']} tem {dados['idade']} anos")
dad



for um,dois in dados.items():
    print(f"{um}: {dois}")