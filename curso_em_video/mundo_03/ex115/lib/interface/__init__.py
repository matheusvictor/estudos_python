def cor_texto(texto, cod_cor=0):
    """
    Style                      Text          Background
    =========================================================
    0 (sem estilo)              30              40      (branco)
    1 (negrito)                 31              41      (vermelho)
    4 (sublinhado)              32              42      (verde)
    7 (inverter cores)          33              43      (amarelo)
                                34              44      (azul)
                                35              45      (roxo)
                                36              46      (ciano)
                                37              47      (cinza)
    """
    lista_cores = (
        '\033[m',  # 0 - sem cores
        '\033[0;31m',  # 1 - vermelho
        '\033[0;32m',  # 2 - verde
        '\033[0;33m',  # 3 - amarelo
        '\033[0;34m',  # 4 - azul
        '\033[0;35m',  # 5 - roxo
        '\033[7;40m'  # 6 - branco
    )
    fecha_cor = '\033[m'

    return f'{lista_cores[cod_cor]}{texto}{fecha_cor}'


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(texto, caixa_alta=True, cor=0):
    print(linha())
    cor_texto(texto, cor)
    if caixa_alta:
        print(cor_texto(texto.center(42).upper(), cor))
    else:
        print(cor_texto(texto.center(42), cor))
    print(linha())


def lista_opcoes():
    lista = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
    return lista


def menu():
    cabecalho('menu principal')
    for pos, item in enumerate(lista_opcoes()):
        print(f'{cor_texto(texto=pos + 1, cod_cor=3)} - {cor_texto(texto=item, cod_cor=4)}')
    print(linha())
    opcao = leiaInt(f'Digite uma opção:')
    return opcao


def leiaInt(msg):
    isNotANumber = True
    while isNotANumber:
        try:
            msg = int(input(f'{msg} '))
        except (ValueError, TypeError):
            print(f'{cor_texto(texto="Erro! Digite um número inteiro válido!", cod_cor=1)}')
            continue
        except KeyboardInterrupt:
            mensagem_interrupcao = f'{cor_texto(texto="Entrada de dados interrompida pelo usuário!", cod_cor=1)}'
            return f'\n{mensagem_interrupcao}'
            break
        else:
            isNotANumber = False
            return msg


def opcaoInvalida(msg='Erro! Digite uma opção válida!'):
    print(cor_texto(msg, cod_cor=1))
