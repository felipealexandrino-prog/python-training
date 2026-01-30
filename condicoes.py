ida = int(input("Digite sua idade: "))
if ida >= 18:
    print(f"Você é maior de idade.")
elif ida < 18:
    print(f"Você é menor de idade.")    
    
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Aprovado")
elif media >= 5 and media < 7:
    print(f"Recuperação")
elif media < 5:
    print(f"Reprovado")        