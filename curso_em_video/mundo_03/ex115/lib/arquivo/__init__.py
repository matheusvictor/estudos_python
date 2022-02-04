from time import sleep
from curso_em_video.mundo_03.ex115.lib.interface import *


def arquivoExiste(nome_arquivo='repositorio.txt'):
    try:
        print('Localizando arquivo...')
        sleep(2)
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        entrada = input('Arquivo não encontrado!\nDeseja criar o arquivo agora? [S/N] >> ')[0].strip()
        if entrada in 'Ss':
            print(f'Criando arquivo "{nome_arquivo}"...')
            criarArquivo(nome_arquivo)
        else:
            print(cor_texto('Criação de arquivo cancelada pelo usuário!', 1))
            return False
    else:
        print(cor_texto(f'Arquivo "{nome_arquivo}" encontrado!', 2))
        return True


def criarArquivo(nome_arquivo='repositorio.txt'):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print(cor_texto('Houve um erro na criação do arquivo!', 1))
        return False
    else:
        sleep(1)
        print(cor_texto(f'Arquivo "{nome_arquivo}" criado com sucesso!', 2))
        return True


def lerArquivo(nome_arquivo='repositorio.txt'):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except FileNotFoundError:
        print(cor_texto('Arquivo não encontrado!', 1))
        entrada = input('Deseja criar o arquivo agora? [S/N] >> ')[0].strip()
        if entrada in 'Ss':
            print(f'Criando arquivo "{nome_arquivo}"...')
            criarArquivo(nome_arquivo)
        else:
            print(cor_texto('Criação de arquivo cancelada pelo usuário!', 1))
    else:
        cabecalho('Pessoas cadastradas')
        print(arquivo.readlines())
