from random import randint
from time import sleep
numeros = list()
def sortear():
    for c in range(0,5):
        numeros.append(randint(0,10))
    for d in numeros:
        print(f"{d} ", flush=True, end="")
        sleep(0.3)
    print(f" Foram os números escolhidos!")    
    
def somar():
    soma = 0
    print(f"Somando os valores pares de {numeros}")
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma dos números pares é de {soma}!")        
            


sortear()
somar()