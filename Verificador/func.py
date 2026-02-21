import urllib
from time import sleep
def verificar(url):
    try:
        urllib.request.urlopen(url)
    except:
        print(f"Verificando...",flush=True)
        sleep(0.8)
        print(f"\033[31mSite está fora do ar! Ou Problema na internet do Cliente!\033[0m")
        print(f"\033[34mEntre em contato com o suporte xxxxxxxxx\033[0m")
    else:
        print(f"Verificando...",flush=True)
        sleep(0.8)
        print(f"\033[32mSite está online!\033[0m")       
        
        
# Reset
RESET = "\033[0m"

# Cores básicas
PRETO   = "\033[30m"
VERMELHO = "\033[31m"
VERDE   = "\033[32m"
AMARELO = "\033[33m"
AZUL    = "\033[34m"
MAGENTA = "\033[35m"
CIANO   = "\033[36m"
BRANCO  = "\033[37m"
