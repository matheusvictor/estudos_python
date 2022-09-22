def jogar():
    print('*' * 40)
    print('Boas-vindas ao jogo da forca!'.upper())
    print('*' * 40)

    perdeu = False
    acertou = False
    palavra_secreta = 'PYTHON'

    palavra_secreta_mascarada = ['_'] * len(palavra_secreta)
    print(f'\n{palavra_secreta_mascarada}')
    print(f'Dica: a palavra possui {contar_letras_palavra_secreta(palavra_secreta)} letra(s)!\n')

    while not acertou and not perdeu:

        palpite = input('Qual seu palpite?: ').strip().upper()

        index = 0
        letras_acertadas = list()

        for letra in palavra_secreta:
            if letra == palpite:
                letras_acertadas.append(letra)
                palavra_secreta_mascarada[index] = letra
                print(palavra_secreta_mascarada)
            index += 1
    print('Fim de jogo')


def gerar_palavra_secreta():
    # TODO
    pass


def transformar_palavra_em_minusculas():
    # TODO
    pass


def transformar_palavra_em_maiusculas():
    pass


def contar_letras_palavra_secreta(palavra):
    return len(palavra)
