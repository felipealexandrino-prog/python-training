print(f"{' MEGA SENA ':=^40}")
num = []
cont = 1
from random import randint
quant = int(input("Quantos jogos você quer que eu sorteie? "))
while True:
    for c in range(0, 6):
        num.append(randint(1, 60))
    print(f"JOGO {cont} {sorted(num)} ")   
    cont += 1
    num.clear() 
    if cont > quant:
        break
    