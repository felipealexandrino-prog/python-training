def potencia(a,b,show=False):
    """
    Função pra calcular potencia
    se show for true mostra processo
    """
    cont = b
    resultado = 1
    for d in range(b):
        if show:
            print(f"{a}",end="")
            if d == b - 1:
                print(" = ", end="")
            else:
                print(" x ", end="")
                
            
        resultado *= a
    return resultado


print(f"{potencia(2,5,show=True)}")