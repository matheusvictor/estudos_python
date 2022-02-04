from time import sleep
from curso_em_video.mundo_03.ex115.lib.arquivo import *
from curso_em_video.mundo_03.ex115.lib.interface import *

arquivoExiste()

while True:
    reposta = menu()
    if reposta == 1:
        lerArquivo()
    elif reposta == 2:
        if arquivoExiste():
            cabecalho('novo cadastro')
            nome = str(input('Nome: '))
            idade = leiaInt(f'Idade de {nome}:')
            cadastrar_pessoa(nome=nome, idade=idade)
    elif reposta == 3:
        cabecalho('Saindo do sistema', cor=2)
        break
    else:
        opcaoInvalida()
    sleep(1)
