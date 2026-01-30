from datetime import datetime
cad = dict()
cad["Nome"] = str(input("Nome: "))
Nascimento = int(input("Ano de Nascimento: "))
cad["Carteira"] = int(input("Carteira de trabalho (0 não tem): "))
cad["Idade"] = datetime.now().year - Nascimento
if cad["Carteira"] == 0:
    for ex, ex2 in cad.items():        
        print(f"{ex} -> {ex2}")
    print(f"Obrigado por usar o app!")
if cad["Carteira"] != 0:
    cad["Contratação"] = int(input("Ano da Contratação:"))
    cad["Salário"] = int(input("Salário: R$ "))
    cad["Aposentadoria"] = (cad["Contratação"] + 35) - Nascimento
    print(f"-+"*20)
    print(f"CARTEIRA DIGITAL DO TRABALHO\n")    
    for a,b in cad.items():
        print(f"{a} -> {b}")
    print(f"-+"*20)    
        
            