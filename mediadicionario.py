dados = dict()
dados["nome"] = str(input("Digite seu nome: "))
dados["media"] = float(input("Digite sua média: "))
if dados["media"] >= 6:
    dados["situ"] = "Aprovado"
elif 6 >= dados["media"] >= 4.5:
    dados["situ"] = "Recuperação"
else:
    dados["situ"] = "Reprovado"
print(f"*-*"*15)    
for ex,ex2 in dados.items():
    print(f"{ex} - > {ex2}")
print(f"*-*" *15)            
