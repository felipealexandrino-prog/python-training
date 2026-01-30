ficha = dict()
gols = list()
ficha["Nome"] = str((input(f"Nome do Jogador: ")))
ficha["Partidas"] = int(input(f"Quantas Partidas {ficha['Nome']} jogou: "))
cont = 1
for a in range(0,ficha["Partidas"]):
    gols.append(int(input(f"Quantos Gols {ficha['Nome']} fez na Partida {cont} ->  ")))
    cont += 1
print(f"="*20)
ficha["Total"] = sum(gols)
ficha["GOLS"] = gols   
print(f"{ficha}") 
print(f"="*20)
for a,b in ficha.items():
    print(f"O campo {a} tem o valor {b}")
print(f"O jogador {ficha['Nome']} jogou {ficha['Partidas']} partidas.")
for i, g in enumerate(ficha["GOLS"]):
    print(f"→ Na partida {i + 1}, fez {g} gols.")

print(f"Total de gols: {ficha['Total']}")

    