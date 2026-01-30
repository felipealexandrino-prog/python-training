from random import randint
from operator import itemgetter
from time import sleep
geral ={"Jogador 1" : randint(1,6),
        "Jogador 2" :  randint(1,6),
        "Jogador 3" : randint(1,6)
        }
ranking = sorted(geral.items(),key=itemgetter(1), reverse=True)
for ex, ex2 in geral.items():
    sleep(2)
    print(f"{ex} tirou {ex2} no Dado")
    print(f"....................")
cont = 1    
for a,b in ranking:
    print(f"{cont}.Lugar {a} -> {b} Pontos")
    cont += 1
vencedor = ranking[0][0]
print(f"{vencedor} foi o campeão!")        
