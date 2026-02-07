from random import randint
num1 = int(input("Digite um numero"))
num2 = int(input("Digite outro "))
def jogar_bola():
    print(randint(0,4))
def narrador(narrar):
    print(f"O jogo está {narrar}")    
    
print("Começou o jogo de futebol!")
jogar_bola()
print("Time adversário")
jogar_bola()
narrador(str(input("Como está o jogo?")))
narrador("Horrivel!")
def calc(num1,num2):
    s = num1 + num2
    print(s)


calc(num1,num2)    
    