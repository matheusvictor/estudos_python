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


dimensao_matriz = int(input('Digite a dimensão da matriz: '))
matriz_gerada = gerar_matriz(dimensao_matriz, dimensao_matriz)

imprime_matriz(matriz_gerada)
