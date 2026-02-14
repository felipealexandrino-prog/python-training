perg1 = str(input("Qual o nome do jogador: "))
if perg1.strip() == "":
    perg1 = "Desconhecido"

try:
    perg2 = int(input("Quantos Gols ele Fez? "))
except ValueError:
    perg2 = 0
        

def ficha(a=" Desconhecido",b=0):
    print(f"O jogador {a} fez {b} gol(s) no campeonato")
    
    
ficha(perg1,perg2)