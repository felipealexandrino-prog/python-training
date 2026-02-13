from datetime import datetime
agora = datetime.now()
ano_atual = agora.year
dia = agora.day
mes = agora.month
def voto(a):
    ida = ano_atual - a
    if ida < 16:
        return f"Com {ida} anos = Não Pode Votar!"
    elif ida <= 17 and ida >= 16 or ida > 65:
        return f"Com {ida} anos = Voto Opcional"
    elif ida >= 18 and ida<=65:
        return f"Com {ida} anos = Voto Obrigatório"
    
    
nasc = int(input("Em que ano você nasceu?"))
print(f"{voto(nasc)}")
