num1 = (int(input("Largura (M) : ")))
num2 = (int(input("Comprimento (M): ")))
def linha():
    print("-"*15)
def area(larg, comp):
    res = larg * comp
    print(f"A área de um terrendo de {num1}x{num2} é de {res}m quadrados!")
linha()
print(f"CONTROLE DE TERRENO")
linha()
area(num1,num2)
linha()