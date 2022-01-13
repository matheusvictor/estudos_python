while(True):
    numero = int(input('Digite um número inteiro para ver sua tabuada. Para sair, digite qualquer número negativo: '))

    if (numero < 0):
        print('Programa encerrado!')
        break

    print('-' * 12)
    for contador in range(1,11):
        print(f'{numero} x {contador:2} = {numero*contador}')
        #:2 considera como se todo número tivesse 2 dígitos
    print('-' * 12)


