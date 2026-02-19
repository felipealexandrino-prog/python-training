def metade(num):
    return num / 2

def dobro(num):
    return num * 2

def porc(num):
    return num * 1.1

def dim(num):
    return num * 0.9


def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".",",")