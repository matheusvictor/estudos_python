from random import randrange

import unidecode


def jogar():
    print('*' * 80)
    print('Boas-vindas ao jogo da forca!'.upper())
    print('*' * 80)

    acertou = False
    enforcou = False
    numero_erros = 0
    quantidade_dicas_disponiveis = 3  # TODO: implementar funcionalidade de dicas

    palavra_secreta = gerar_palavra_secreta()
    palavra_secreta_mascarada = ['_' for letra in palavra_secreta]  # compreensão de lista

    palpites_errados = list()
    palpites_corretos = list()
    quantidade_palpites_dados = 0
    while not acertou and not enforcou:

        print(f'\n{palavra_secreta_mascarada}')

        palpite = input('Qual seu palpite?: ').strip().upper()

        if palpite in palavra_secreta:
            if palpite in palpites_corretos:
                print(f'Você já usou {palpite} como palpite!')
            else:
                index = 0
                for letra in palavra_secreta:
                    if palpite == letra:
                        quantidade_palpites_dados += 1
                        palpites_corretos.append(letra)
                        palavra_secreta_mascarada[index] = palpite
                    index += 1
        else:
            if palpite in palpites_errados:
                print(f'Você já usou {palpite} como palpite!')
            else:
                numero_erros += 1
                quantidade_palpites_dados += 1
                palpites_errados.append(palpite)
                print(f'Você ainda possui {len(palavra_secreta) - numero_erros} chances!')

        acertou = '_' not in palavra_secreta_mascarada
        enforcou = numero_erros == len(palavra_secreta)

    if acertou:
        print('*' * 80)
        print('Você ganhou!'.upper())
        print(f'Para acertar a palavra secreta, você utilizou {quantidade_palpites_dados} '
              f'palpites (desconsiderando palpites repetidos)')
    else:
        print('*' * 80)
        print('Você perdeu!'.upper())

    print('*' * 80)
    print('Fim de jogo!'.upper())
    print('*' * 80)


def gerar_palavra_secreta():
    arquivo = open(file='./data/banco_de_palavras.txt', mode='r', encoding='utf-8')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())

    arquivo.close()

    indice_randomico_palavra = randrange(start=0, stop=len(palavras))

    return unidecode.unidecode(palavras[indice_randomico_palavra])


def cadastrar_nova_palavra():
    arquivo = open(file='./data/banco_de_palavras.txt', mode='a', encoding='utf-8')
    nova_palavra = input('Digite uma nova palavra para cadastrar na base de dados: ')

    try:
        arquivo.write(nova_palavra)
        print('Nova palavra salva com sucesso!')
    except:
        print('Erro ao tentar gravar palavra na base de dados...')
    arquivo.close()
