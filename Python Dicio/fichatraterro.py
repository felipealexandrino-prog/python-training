ficha = dict()
dados = list()
media = 0
print(f"Seja Bem-Vindo")

while True:
    ficha.clear()
    ficha["Nome"] = str(input("Digite seu nome:"))    
    try:
        
        ficha["Idade"] = int(input("Digite sua idade: "))
        media += ficha["Idade"]
    except ValueError:
        
        print("Resposta Inválida! Use somente Números")
        continue    
    dados.append(ficha.copy())
    resp = str(input("Deseja Continuar [S/N]"))
    if resp in "Ss":
        continue
    else:
        break
tamanho = len(dados)
for a,b in enumerate(dados):
    print(f"{a+1} -> {b}")    
print(f"{tamanho} Pessoas foram cadastradas!")
mediafin = media / tamanho
print(f"A média das idades foi de {mediafin} anos")
if ficha["Idade"] > mediafin:
    print("*" * 10)
    print("Pessoas acima da média de idade")
    for c in dados:
        if c["Idade"] > mediafin:
            print(c["Nome"], "->", c["Idade"])
    print("*" * 10)
    