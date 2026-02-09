cont = 0
while cont < 2:
    mens = str(input("Qual a mensagem: "))
    def mensagem(msg):
        tam = len(msg) + 4
        print(f"~" *tam) 
        print(f"{msg}".center(tam))
        print(f"~" *tam)
    mensagem(mens)
    cont += 1    
