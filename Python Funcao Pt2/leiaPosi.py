def leiaPositivo(msg):
    while True:
        try:
            num = int(input(msg))
            if num <= 0:
                print(f"Só aceitamos números positivos!")
                continue
            else:
                ok = True
                return num
        except ValueError:
            print(f"Só aceitamos números positivos!")
            continue

        
                




#Prog Princ
n = leiaPositivo("Digite um número inteiro positivo: ")
print(f"Você digitou {n}")