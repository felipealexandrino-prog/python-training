from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1  
    print(f"Contagem de {i} até {f} de {p} em {p}")
    cont = i
     
    if i < f:
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.4)
            cont += p
        print("FIM")
    else:
        while cont >= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.4)
            cont -= p
        print("FIM")
contador(1,10,1)
contador(10,0,2)
print(f"AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)