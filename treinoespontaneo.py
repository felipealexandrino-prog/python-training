cont = 0
while cont == 0:
    resp = int(input("Em quem voce votou Lula(1) Bolsonaro(2) Nulo(3) ->"))
    if resp == 1:
        print(f"Você votou no Lula {resp} e ele foi eleito")
        cont += 1
    elif resp == 2:
        print(f"Voce votou no Bolsonaro {resp} e ele NAO foi eleito")
        cont += 1
    elif resp == 3:
        print(f"Voce votou nulo")
        cont += 1
    else:
        print(f"Formato nao aceito, tente novamente!")
        cont == 0        
print(f"ATÉ 2026!")
    

