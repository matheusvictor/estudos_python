def jogar():
    print()

    perdeu = False
    acertou = False
    palavra_secreta = 'PYTHON'

    while not acertou and not perdeu:

        palpite = input('Qual seu palpite?: ').strip().upper()

        for letra in palavra_secreta:
            if letra == palpite:
                print(letra)

        print('Fim de jogo')
