def gerar_matriz(n_linhas, n_colunas):
    matriz = []  # lista vazia

    for x in range(n_linhas):
        linha = []  # lista vazia, que será zerada toda vez que o laço voltar
        for y in range(n_colunas):
            valor = int(input(f'Digite o valor para {x, y}: '))
            linha.append(valor)
        matriz.append(linha)

    return matriz


def imprime_matriz(matriz):
    print('*=' * 10)
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            print(f'[{matriz[x][y]:^3}]', end='')
        print()
    print('*=' * 10)


def soma_pares_digitados(matriz):
    soma_pares = 0
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if matriz[x][y] % 2 == 0:
                soma_pares += matriz[x][y]
    print(f'A soma dos valores pares digitados é igual a {soma_pares}')


def soma_terceira_coluna(matriz):
    soma = 0
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if y == 2:
                soma += matriz[x][y]

    print(f'A soma dos valores da terceira coluna é igual a {soma}')


def maior_valor_segunda_linha(matriz):
    maior = 0
    for x in range(len(matriz)):
        for y in range(len(matriz)):
            if x == 1:
                if matriz[x][y] > maior:
                    maior = matriz[x][y]

    print(f'O maior valor da segunda linha é {maior}')


dimensao_matriz = int(input('Digite a dimensão da matriz: '))
matriz_gerada = gerar_matriz(dimensao_matriz, dimensao_matriz)

imprime_matriz(matriz_gerada)
soma_pares_digitados(matriz_gerada)
soma_terceira_coluna(matriz_gerada)
maior_valor_segunda_linha(matriz_gerada)
