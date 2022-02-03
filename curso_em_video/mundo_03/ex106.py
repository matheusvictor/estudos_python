from time import sleep

cores = (
    '\033[m',  # 0 - sem cores
    '\033[0;30;41m',  # 1 - vermelho
    '\033[0;30;42m',  # 2 - verde
    '\033[0;30;43m',  # 3 - amarelo
    '\033[0;30;44m',  # 4 - azul
    '\033[0;30;45m',  # 5 - roxo
    '\033[7;40m'  # 6 - branco
)


def ajuda(comand):
    titulo(f'Acessando o manual do comando \'{comand}\'', cor=4)
    print(cores[6], end='')
    help(comand)
    print(cores[6], end='')
    sleep(2)


def titulo(txt, cor=0):
    tamanho_titulo = len(txt)
    print(cores[cor], end='')
    print('~' * tamanho_titulo)
    print(txt)
    print('~' * tamanho_titulo)
    print(cores[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2)
    comando = str(input(f'{cores[3]}Função ou Biblioteca >> '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', cor=1)
