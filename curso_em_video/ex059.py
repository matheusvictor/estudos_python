# criando funções a ser utilizada pelo programa
def menu():
    print('*=' * 20,
          '\n[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior número\n'
          '[4] inserir novos números\n'
          '[5] encerrar o programa')

def soma(n1, n2):
    soma = n1 + n2
    return f'{"*=" * 20}\nA soma entre {n1} e {n2} é igual a {soma}.'

def multiplicacao(n1, n2):
    mult = n1 * n2
    return f'{"*=" * 20}\nO produto entre {n1} e {n2} é igual a {mult}.'

def maior_numero(n1, n2):
    if(n1 == n2):
        return 'Os número são iguais!'
    elif(n1 > n2):
        return f'{n1} é o maior número!'
    else:
        return f'{n2} é o maior número!'

continua = True

primeiro_numero = float(input('Insira o primeiro valor: '))
segundo_numero = float(input('Insira o segundo valor: '))

while(continua):
    menu()
    valida_opcao = True
    while(valida_opcao):
        opcao = int(input('Digite uma das opções acima: '))
        if(opcao < 1 or opcao > 5):
            print('Opção inválida! Tente novamente.', end=' ')
        else:
            valida_opcao = False

    if(opcao == 1):
        print(soma(primeiro_numero, segundo_numero))
    elif(opcao == 2):
        print((multiplicacao(primeiro_numero, segundo_numero)))
    elif(opcao == 3):
        print(maior_numero(primeiro_numero, segundo_numero))
    elif(opcao == 4):
        primeiro_numero = float(input('Insira o primeiro valor: '))
        segundo_numero = float(input('Insira o segundo valor: '))
    else:
        print('Programa encerrado!')
        exit()

