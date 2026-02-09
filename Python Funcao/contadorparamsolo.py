from time import sleep
def saltos(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1    
    print(f"\nContagem de {inicio} até {fim} de {passo} em {passo}")
    cont = inicio
    
    if inicio <= fim:
        while cont <= fim:
            print(f"{cont} ", end="", flush=True)
            cont += passo
            sleep(0.4)
    else:
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            cont -= passo
            sleep(0.4)
                



saltos(2,12,2)
saltos(20,10,4)
print(f"SUA VEZ!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
saltos(i,f,p)