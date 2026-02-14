ficha = dict()

def notas(*num,sit=False):
    """
    Função para calcular média
    """
    maior = 0
    menor = 10
    media = 0
    ficha["Total"] = len(num)
    for c in num:
        if c > maior:
            maior = c
    for d in num:
        if d < menor:
            menor = d         
    ficha["Maior"] = maior
    ficha["Menor"] = menor
    for e in num:
        media += e
    ficha["Média"] = media / ficha["Total"]
    if sit:
        if ficha["Média"] < 6:
            ficha["Situação"] = "Péssima"
        elif ficha["Média"] >= 6:
            ficha["Situação"] = "Passou"    
    return ficha    
    
    
    
    
    







#Prog Principal
resp = notas(8.5,2.5,1.5,7.5,10,sit=True)
print(resp)