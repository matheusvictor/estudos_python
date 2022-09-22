import data


def jogar():
    print('*' * 40)
    print('Boas-vindas ao jogo da forca!'.upper())
    print('*' * 40)

    acertou = False
    enforcou = False
    numero_erros = 0
    palavra_secreta = 'PYTHON'.strip().upper()
    palavra_secreta_mascarada = ['_'] * len(palavra_secreta)

    print(f'\n{palavra_secreta_mascarada}')
    print(f'Dica: a palavra possui {contar_letras_palavra_secreta(palavra_secreta)} letra(s)!\n')

    while not acertou and not enforcou:

        palpite = input('Qual seu palpite?: ').strip().upper()

        letras_acertadas = list()

        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == palpite:
                    letras_acertadas.append(letra)
                    palavra_secreta_mascarada[index] = palpite
                index += 1
        else:
            numero_erros += 1

        acertou = '_' not in palavra_secreta_mascarada
        enforcou = numero_erros == len(palavra_secreta)

    if acertou:
        print('Você ganhou'.upper())
    else:
        print('Você perdeu'.upper())
    print('Fim de jogo'.upper())


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
