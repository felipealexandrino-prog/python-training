def fatorial(num, show=True):
    """
    Função que calcula fatorial de um número!
    """
    resultado = 1
    for cont in range(num, 0, -1):
        if show:
            print(f"{cont}", end='')
            if cont != 1:
                print(f" X ",end="")
            else:
                print(f" = ",end="")    
                
        resultado *= cont
    return resultado

r1 = fatorial(5,show=True)
print(f"\n{r1}")