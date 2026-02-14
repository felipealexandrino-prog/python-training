
def leiaInt(msg):
    ok = False
    num = 0
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print("Erro! Digite um número inteiro válido!")

            
    


#Prog Principal
num = leiaInt('Digite Um Número: ')
print(f"Você digitou o número {num}")