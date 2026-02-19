def metade(num=0, formato=False):
    resultado = num / 2
    if formato:
        return moeda(resultado)
    else:
        return resultado

   


def dobro(num=0, formato=False):
    resultado = num * 2
    if formato:
        return moeda(resultado)
    else:
        return resultado


def aumentar(num=0, porcentagem=0, formato=False):
    resultado = num + (num * porcentagem / 100)
    if formato:
        return moeda(resultado)
    else:
        return resultado


def diminuir(num=0, porcentagem=0, formato=False):
    resultado = num - (num * porcentagem / 100)
    if formato:
        return moeda(resultado)
    else:
        return resultado

def resumo(num=0,aum=1,des=1,formato = False):
    print("-"*20)
    print(f"  Resumo Do Valor   ".center(1))
    print("-"*20)
    if formato == True:
        print(f"Preço Analisado: {moeda(num)}")
        print(f"Dobro do Preço: {dobro(num,True)} ")
        print(f"Metade do Preço: {metade(num,True)}")
        print(f"Aumentando {aum}% : {aumentar(num,aum,True)}")
        print(f"Diminuindo {des}%: {diminuir(num,des,True)} ")
    else:
        print(f"Preço Analisado: {moeda(num)}")
        print(f"Dobro do Preço: {dobro(num)} ")
        print(f"Metade do Preço: {metade(num)}")
        print(f"Aumentando {aum}% : {aumentar(num)}")
        print(f"Diminuindo {des}%: {diminuir(num)} ")
        

def moeda(num=0, simbolo="R$"):
    return f"{simbolo}{num:.2f}".replace(".", ",")        