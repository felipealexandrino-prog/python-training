import funcoes
valor = (float(input("Digite o Preço: R$ ")))
met = funcoes.metade(valor)
dob = funcoes.dobro(valor)
por = funcoes.porc(valor)
print(f"A metade de  {funcoes.moeda(valor)} é {funcoes.moeda(met)}")
print(f"O dobro de  {funcoes.moeda(valor)} é {funcoes.moeda(dob)}")
print(f"Aumentando 10% de  {funcoes.moeda(valor)} fica   {funcoes.moeda(por):}")