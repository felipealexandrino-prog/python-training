from random import randint
from time import sleep
from operator import itemgetter
ficha = {"Jogador 1" : randint(1,6),
         "Jogador 2": randint (1,6),
         "Jogador 3": randint (1,6),
         "Jogador 4": randint (1,6)
}
ranking = dict()
for ex,ex2 in ficha.items():
    print(f"{ex} tirou {ex2} no dado!")
    print(f".......")
    sleep(3)
ranking = sorted(ficha.items(), key=itemgetter(1), reverse=True)
cont = 1
for a,b in ranking:
    print(f"{cont}. Lugar {a} -> {b}")
    cont +=1

       
