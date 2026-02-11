from time import sleep
def funcmenor(*num):
    menornum = num[0]
    print(f"Analisando valores passados!")
    for c in num:
        print(f"{c} ", end ="", flush=True)
        sleep(0.3)
    quant = len(num)    
    print(f"Foram lidos {quant} números ao todo!")
    for valor in num:
        if valor < menornum:
            menornum = valor
    print(f"O menor número acima é {menornum}")            
    


funcmenor(8,3,2)
funcmenor(8, 3, 5, 1, 9)
