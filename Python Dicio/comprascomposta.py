compras = list()
total = 0
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$ "))
    quant = int(input("Quantidade: "))
    prefi = preço * quant
    total += prefi
    compras.append([produto, preço, quant,prefi])
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in 'N':
        break

print("-" * 40)
print(f"{' LISTA DE COMPRAS ':^40}")
print("-" * 40)
print(f"{'Produto':<25}{'Preço':>7}{'Qtd':>5} {'Total':>8}")
for i, item in enumerate(compras):
    print(f"{item[0]:<24} {item[1]:>6} {item[2]:>4} {item[3]:>8.2f}")
maior_preco = 0
produto_maior = ""

for item in compras:
    if item[1] > maior_preco:
        maior_preco = item[1]
        produto_maior = item[0]

print(f"Produto mais caro: {produto_maior} (R$ {maior_preco:.2f})")

maior_total = 0
produto_total = ""
for item in compras:
    if item[3] > maior_total:
        maior_total = item[3]
        produto_total = item[0]
print(f"Produto com maior gasto total: {produto_total} (R$ {maior_total:.2f})")        

print("-" * 40)
print(f"{'Total a pagar':<30} R$ {total:>8.2f}")