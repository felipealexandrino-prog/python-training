maiornum = 0

def maior(*num):
    global maiornum
    print(f"Analisando os valores passados...")

    cont = len(num)

    for n in num:
        print(f"{n} ", end="")

    print(f"\nForam informados {cont} números ao todo!")

    for valor in num:
        if valor > maiornum:
            maiornum = valor

    print(f"O maior número informado é {maiornum}")

maior(5, 8, 1)
maior(10,5,3,8,-10)   
    
    

