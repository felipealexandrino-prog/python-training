listabom = ['massa', 'top', 'incrivel', 'excelente', 'show de bola', 'bom', 'fantastico']
listaruim = ['ruim', 'pessimo', 'horrivel', 'terrivel', 'lixo', 'muito ruim', 'decepcionante']

print("Seja Bem-Vindo a conversa com IA!")

while True:
    perg = input("Me fale como foi seu dia! ").lower()

    achou_bom = False
    achou_ruim = False

    for palavra in listabom:
        if palavra in perg:
            achou_bom = True

    for palavra in listaruim:
        if palavra in perg:
            achou_ruim = True

    if achou_bom and achou_ruim:
        print("Entendo que seu dia teve altos e baixos! Espero que os próximos dias sejam melhores!")
    elif achou_bom:
        print("Fico feliz que seu dia tenha sido bom! Que continue assim!")
    elif achou_ruim:
        print("Sinto muito que seu dia tenha sido ruim! Espero que amanhã seja melhor!")
    else:
        print("Obrigado por compartilhar como foi seu dia! Me conte mais se quiser!")
