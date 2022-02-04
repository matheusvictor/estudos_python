from curso_em_video.mundo_03.ex115.lib.interface import *

while True:
    reposta = menu()
    if reposta == 1:
        cabecalho('Opção 1')
    elif reposta == 2:
        cabecalho('Opção 2')
    elif reposta == 3:
        cabecalho('Saindo do sistema', cor=2)
        break
    else:
        opcaoInvalida()
