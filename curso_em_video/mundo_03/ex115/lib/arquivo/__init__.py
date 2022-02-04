from time import sleep
from curso_em_video.mundo_03.ex115.lib.interface import *


def arquivoExiste(nome_arquivo='repositorio.txt'):
    try:
        print('Localizando arquivo de dados...')
        sleep(1)
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print(cor_texto('Arquivo não encontrado!', 1))
        entrada = input('Deseja criar o arquivo agora? [S/N] >> ')[0].strip()
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
        if contador_linhas_arquivo() > 0:
            print(arquivo.read())
        else:
            print(cor_texto('Não contém registros no arquivo!', 1))


def contador_linhas_arquivo(nome_arquivo='repositorio.txt'):
    with open(nome_arquivo) as arquivo:
        qtd_linhas = 0
        for linha in arquivo:
            qtd_linhas += 1
    return qtd_linhas


def cadastrar_pessoa(nome_arquivo='repositorio.txt', nome='<desconhecido>', idade=0):
    try:
        arquivo = open(nome_arquivo, 'at')
    except:
        print(cor_texto('Houve um erro ao tentar abrir o arquivo!', 1))
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print(cor_texto('Houve um erro ao inserir os dados no arquivo!', 1))
        else:
            print(cor_texto(f'Registro de {nome} realizado com sucesso!', 2))
        finally:
            arquivo.close()
