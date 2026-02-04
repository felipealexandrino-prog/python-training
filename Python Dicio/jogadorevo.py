ficha = dict()
geral = list()

while True:
    nota = list()

    ficha["Nome"] = input("Digite seu nome: ")
    for c in range(3):
        nota.append(float(input(f"Nota {c+1}: ")))

    ficha["Nota"] = nota
    geral.append(ficha.copy())
    ficha.clear()

    resp = input("Deseja continuar [S/N] ").strip().upper()
    if resp != "S":
        break


for i, aluno in enumerate(geral):
    print(f"{i} -> {aluno['Nome']} -> {aluno['Nota']}")


while True:
    opc = int(input("Deseja ver a nota de qual aluno? (999 para sair) "))

    if opc == 999:
        break

    print(f"\nNotas de {geral[opc]['Nome']}")

    for i, nota in enumerate(geral[opc]['Nota']):
        print(f"Prova {i+1}: {nota}")
