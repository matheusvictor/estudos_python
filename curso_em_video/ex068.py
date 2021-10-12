from random import randint
vitorias = 0

while(True):
    numero_usuario = int(input('Digite um número entre 0 e 10: '))

    if(numero_usuario < 0 or numero_usuario > 10):
        print('Número inválido. Tente novamente!', end=' ')
    else:
        numero_computador = randint(0, 10)
        soma_numeros = numero_usuario + numero_computador

        opcao = int(input('Digite sua [0] para escolher Par ou [1] para escolher Ímpar: '))

        while (opcao < 0 or opcao > 1):
            opcao = int(input('Opção inválida. Tente novamente: '))

        print('=-' * 40)
        print(f'Você escolheu {numero_usuario} e o computador escolheu {numero_computador}.')

        #se a soma der par e a escolha do usuário tiver sido par:
        if(soma_numeros % 2 == 0 and opcao == 0):
            vitorias += 1
            print('VOCÊ GANHOU!')
        # se a soma der ímpar e a escolha do usuário tiver sido ímpar:
        elif(soma_numeros % 2 != 0 and opcao == 1):
            vitorias += 1
            print('VOCÊ GANHOU!')
        else:
            print('VOCÊ PERDEU!')
            break
        print('=-' * 40)
print('=-' * 40)
print(f'Número de vitórias consecutivas: {vitorias}.')
