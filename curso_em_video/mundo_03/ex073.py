times_brasileirao_2021 = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Bragantino', 'Palmeiras', 'Corinthians',
                         'Internacional', 'Athletico-PR', 'Fluminense', 'Atlético-GO', 'América-MG', 'Cuiabá',
                         'São Paulo', 'Ceará', 'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
opcao = 1

while(opcao != 0):
    print('-=' * 30)
    print('[1] - Exibir os 5 primeiros colocados.\n'
          '[2] - Exibir os 4 últimos colocados.\n'
          '[3] - Exibir times em ordem alfabética.\n'
          '[4] - Colocação do time da Chapecoense.\n'
          '[0] - Encerrar o programa.')
    opcao = int(input('Digite uma das opções: '))
    print('-=' * 30)

    if(opcao < 0 or opcao > 4):
        print('Opção inválida! Tente novamente.', end=' ')
    elif(opcao == 0):
        print('Programa encerrado!')
        exit()
    elif(opcao == 1):
        print('Os 5 primeiros times colocados do Brasileirão 2021 são:')
        for posicao in range(0,5):
            print(f'{posicao+1}º - {times_brasileirao_2021[posicao]}')
    elif(opcao == 2):
        print('Os 4 últimos times colocados do Brasileirão 2021 são:')
        for posicao in range(16, 20):
            print(f'{posicao+1}º - {times_brasileirao_2021[posicao]}')
    elif(opcao == 3):
        print(f'{"Times listados em ordem alfabética:": ^60}')
        times_ordem_alfabetica = sorted(times_brasileirao_2021)
        for posicao in range(0, len(times_ordem_alfabetica)):
            print(times_ordem_alfabetica[posicao])
    else:
        print(f'O time da Chapecoense encontra-se da {times_brasileirao_2021.index("Chapecoense")+1}ª posição!')
