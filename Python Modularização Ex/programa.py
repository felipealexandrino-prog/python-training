import funcoes
valor = (float(input("Digite o Preço: R$ ")))
met = funcoes.metade(valor)
dob = funcoes.dobro(valor)
por = funcoes.porc(valor)
print(f"A metade de R$ {valor:.2f} é {met:.2f}")
print(f"O dobro de R$ {valor:.2f} é R$ {dob:.2f}")
print(f"Aumentando 10% de R$ {valor:.2f} fica  R$ {por:.2f}")