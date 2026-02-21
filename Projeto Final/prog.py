import func
arq = 'cadastro.txt'
func.criar_arquivo(arq)
valid = 0
while valid != 1:
    valid = func.menu()
    