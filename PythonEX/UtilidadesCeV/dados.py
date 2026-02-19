from UtilidadesCeV import calculos
def leiaDinheiro(msg):
    while True:
        valor = input(msg)
        valor = valor.replace(',', '.')
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print("Erro! Digite um valor monetário válido.")
    