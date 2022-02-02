from time import sleep


def contador():
    print('-=' * 30)
    print('Realizando contagem de 1 até 10 de 1 em 1...')
    for numero in range(1, 11):
        print(numero, end=' ')
        sleep(0.2)
    print('FIM')
    print('-=' * 30)
    print('Realizando contagem de 10 até 0 de 2 em 2...')
    for numero in range(10, -1, -2):
        print(numero, end=' ')
        sleep(0.2)
    print('FIM')

    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        print('Não há contagem a ser feita com passo zero!')
    elif passo < 0:
        passo *= -1
    if passo > 0:
        if inicio == fim:
            print('Não há intervalo a ser considerado!')
        else:
            print('-=' * 30)
            print(f'Realizando contagem de {inicio} até {fim} de {passo} em {passo}...')
            if fim > inicio:
                for numero in range(inicio, fim + 1, passo):
                    print(numero, end=' ')
                    sleep(0.2)
                print('FIM')
            elif fim < inicio:
                for numero in range(inicio, fim - 1, -passo):
                    print(numero, end=' ')
                    sleep(0.2)
                print('FIM')


contador()
