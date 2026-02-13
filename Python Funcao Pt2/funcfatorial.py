b = int(input("Digite o valor que quer do fatorial: "))

def fatorial(a=1):
    resultado = 1
    for cont in range(a, 0, -1):
        resultado *= cont
    return resultado

f1 = fatorial(4)
f2 = fatorial (3)
f3 = fatorial(7)
print(f"Os fatoriais são {f1}, {f2}, {f3}")